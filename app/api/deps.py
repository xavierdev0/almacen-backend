# app/api/deps.py
from typing import Annotated, Optional, Callable, Set
from fastapi import Depends, HTTPException, status, Request
from sqlmodel import Session, select # <--- Asegúrate de importar select
from sqlalchemy.orm import selectinload # <--- Importar selectinload
from jose import JWTError
import logging
# Ya no necesitamos importar UUID aquí si no se usa directamente

from app.core.database import get_db
from app.core.security import oauth2_scheme, decode_access_token
# Importar modelos necesarios
from app.models import Usuario, Rol, Permiso
# Importar repositorio (aunque ahora haremos la consulta aquí)
from app.repositories import usuario_repository

logger = logging.getLogger(__name__)

def auth_exception(detail: str = "Credenciales de autenticación inválidas") -> HTTPException:
    """
    Helper para generar la excepción estándar de autenticación 401.
    """
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )

async def get_current_user(
    # request: Request, # 'request' no se usa actualmente, se puede quitar si no hay planes para usar IP/headers aquí
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_scheme)]
) -> Usuario:
    """
    Obtiene el usuario actual desde el JWT, verifica su existencia en la DB
    y carga eager sus roles asociados.

    Args:
        db: Sesión de base de datos inyectada por FastAPI.
        token: Token JWT extraído del header Authorization por FastAPI.

    Returns:
        El objeto Usuario con sus roles cargados.

    Raises:
        HTTPException 401: Para cualquier fallo de autenticación (token inválido,
                           usuario no encontrado, error de formato, etc.).
    """
    try:
        subject_str = decode_access_token(token)

        if not subject_str:
            # Quitar IP de log si no se usa 'request'
            logger.warning(f"Token inválido o claims incompletos: {token[:10]}...")
            raise auth_exception("Token inválido o expirado")

        try:
            user_id = int(subject_str)
        except ValueError:
            logger.error(f"Subject del token no es un entero válido: {subject_str}")
            raise auth_exception("Identificador de usuario inválido en el token")

        statement = (
            select(Usuario)
            .where(Usuario.id == user_id)
            .options(
                selectinload(Usuario.roles).selectinload(Rol.permisos)
            )
        )
        user = db.exec(statement).first()

        if not user:
            logger.error(f"Usuario del token no encontrado: ID {user_id}")
            raise auth_exception("Usuario asociado al token no encontrado.")

        logger.debug(f"Usuario autenticado: ID={user.id}, Username='{user.username}'")
        if user.roles:
            perm_count = sum(len(r.permisos) if r.permisos else 0 for r in user.roles)
            logger.debug(f"Carga Eager: Usuario ID={user.id} tiene {len(user.roles)} roles y un total de {perm_count} permisos asociados cargados.")
        else:
            logger.debug(f"Carga Eager: Usuario ID={user.id} no tiene roles asignados.")

        return user

    except JWTError as e:
        logger.error(f"Error decodificando token JWT: {str(e)}")
        raise auth_exception("Error en el token JWT.")
    # ValueError ya se captura arriba al convertir user_id
    except HTTPException as http_exc: # Relanzar excepciones HTTP directamente
        raise http_exc
    except Exception as e:
        logger.critical(f"Error inesperado en get_current_user: {str(e)}", exc_info=True)
        raise auth_exception("Error interno durante la autenticación.")


def get_current_active_user(
    current_user: Annotated[Usuario, Depends(get_current_user)]
) -> Usuario:
    """
    Verifica que el usuario obtenido de get_current_user esté activo.

    Args:
        current_user: El usuario obtenido de la dependencia get_current_user.

    Returns:
        El objeto Usuario si está activo.

    Raises:
        HTTPException 403: Si el usuario no está activo.
    """
    if not current_user.esta_activo:
        logger.warning(f"Intento de acceso de usuario inactivo: ID={current_user.id}, Username='{current_user.username}'")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cuenta de usuario deshabilitada."
        )
    return current_user




ADMIN_ROLE_NAME = "Administrador" 
def require_admin_role(
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """
    Dependencia placeholder que verifica si el usuario activo tiene el rol 'Administrador'.
    NOTA: Esto debería reemplazarse más adelante con una verificación basada en permisos.
    Asume que current_user (de get_current_active_user -> get_current_user)
    ya tiene la relación 'roles' cargada.

    Args:
        current_user: El usuario activo obtenido de get_current_active_user.

    Raises:
        HTTPException 403: Si el usuario no tiene el rol de Administrador.
                           O si el usuario no tiene roles asignados.
    """
    # Gracias a la carga eager en get_current_user, no debería haber lazy loading aquí.
    if not current_user.roles:
         logger.warning(f"Usuario ID {current_user.id} ('{current_user.username}') no tiene roles asignados al verificar acceso admin.")
         # Lanzar 403 porque sin roles, no puede ser admin.
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acción no permitida. Roles no definidos para el usuario."
        )

    has_admin_role = any(role.nombre == ADMIN_ROLE_NAME for role in current_user.roles)

    if not has_admin_role:
        logger.warning(f"Intento de acceso admin no autorizado por Usuario ID: {current_user.id} ('{current_user.username}'). Roles: {[r.nombre for r in current_user.roles]}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requiere rol de Administrador para realizar esta acción."
        )
    # Si tiene el rol, simplemente permite continuar (no devuelve nada)
    logger.debug(f"Acceso admin permitido para Usuario ID: {current_user.id} ('{current_user.username}')")


def require_permission(required_permission: str) -> Callable:
    """
    Fábrica que crea una dependencia de FastAPI para verificar si el usuario
    activo tiene un permiso específico.

    El permiso debe estar en formato 'accion:recurso'.

    Ejemplo de uso en un endpoint:
        @router.get("/ruta", dependencies=[Depends(require_permission("leer:recurso"))])

    Args:
        required_permission: El string del permiso requerido (ej: "crear:proforma").

    Returns:
        Una función de dependencia callable para FastAPI.
    """
    async def _permission_check(
        current_user: Annotated[Usuario, Depends(get_current_active_user)]
    ):
        """
        Función de dependencia interna que realiza la verificación.
        Es llamada por FastAPI para cada solicitud al endpoint protegido.
        """
        user_permissions: Set[str] = set()
        if current_user.roles:
            for role in current_user.roles:
                # Verificar si los permisos del rol están cargados (deberían estarlo por selectinload)
                if role.permisos is not None:
                    for permission in role.permisos:
                        permission_str = f"{permission.nombre_accion}:{permission.nombre_recurso}"
                        user_permissions.add(permission_str)
                else:
                    # Esto indicaría un problema con la carga eager o la relación
                    logger.warning(f"Permisos no cargados para el rol ID={role.id} ('{role.nombre}') "
                                   f"del usuario ID={current_user.id}. Verifique la carga eager en get_current_user.")


        logger.debug(f"Permisos agregados para Usuario ID={current_user.id}: {user_permissions}")

        # Verificar si el permiso requerido está en el conjunto de permisos del usuario
        if required_permission not in user_permissions:
            logger.warning(
                f"Acceso denegado para Usuario ID={current_user.id} ('{current_user.username}'). "
                f"Permiso requerido: '{required_permission}'. Permisos del usuario: {user_permissions}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permiso insuficiente: Se requiere '{required_permission}'."
            )
        else:
            logger.debug(
                f"Acceso permitido para Usuario ID={current_user.id} ('{current_user.username}'). "
                f"Permiso requerido '{required_permission}' encontrado."
            )
            # Si el permiso existe, la dependencia pasa sin hacer nada más.

    # La fábrica devuelve la función interna que FastAPI usará como dependencia
    return _permission_check
