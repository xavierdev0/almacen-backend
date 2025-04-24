# app/api/deps.py
from typing import Annotated, Optional, Callable, Set, Union
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
            role_names_str = ', '.join([r.nombre for r in user.roles])
            logger.debug(f"*** EAGER LOAD CHECK Usuario ID={user.id}: Roles cargados=[{role_names_str}], Permisos totales cargados={perm_count} ***")
            for r in user.roles:
                if r.permisos is None:
                    logger.warning(f"*** EAGER LOAD CHECK: Rol '{r.nombre}' (ID={r.id}) tiene 'permisos' como None! ***")
                elif len(r.permisos) == 0:
                     logger.debug(f"*** EAGER LOAD CHECK: Rol '{r.nombre}' (ID={r.id}) tiene lista 'permisos' vacía. ***")

        else:
            logger.debug(f"*** EAGER LOAD CHECK Usuario ID={user.id}: No tiene roles asignados. ***")

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





def require_permission(required_permissions: Union[str, Set[str]]) -> Callable:
    """
    Fábrica que crea una dependencia de FastAPI para verificar si el usuario
    activo tiene un permiso específico O al menos uno de un conjunto de permisos.

    Args:
        required_permissions: Un string con el permiso requerido (ej: "leer:cliente")
                              o un set/list de strings con los permisos requeridos
                              (ej: {"actualizar:proforma_propia", "actualizar:proforma_global"}).

    Returns:
        Una función de dependencia asíncrona para usar con FastAPI (`Depends`).
    """
    # Convertir a set si se recibe un solo string para manejo uniforme
    if isinstance(required_permissions, str):
        permission_set = {required_permissions}
        req_perm_repr = f"'{required_permissions}'" # Para logging
    elif isinstance(required_permissions, (set, list)):
        permission_set = set(required_permissions)
        req_perm_repr = f"uno de {permission_set}" # Para logging
    else:
        # Error de configuración si no es string ni set/list
        raise TypeError("required_permissions debe ser un string o un set/list de strings")

    if not permission_set:
         raise ValueError("El conjunto de permisos requeridos no puede estar vacío.")


    async def _permission_check(
        current_user: Annotated[Usuario, Depends(get_current_active_user)]
    ):
        """Dependencia interna que realiza la verificación."""
        # 1. Obtener todos los permisos únicos del usuario (como antes)
        user_permissions: Set[str] = set()
        if current_user.roles:
            for role in current_user.roles:
                # Verificar que la relación 'permisos' fue cargada (por get_current_user)
                if role.permisos is None:
                     logger.error(f"ERROR CRÍTICO: La relación 'permisos' NO está cargada para el Rol ID={role.id} ('{role.nombre}') del usuario ID={current_user.id}. Asegurar selectinload(Usuario.roles).selectinload(Rol.permisos) en get_current_user.") # noqa
                     # Lanzar error 500 porque es un fallo de configuración/carga de datos
                     raise HTTPException(status_code=500, detail="Error interno verificando permisos [LoadFail]")
                for permission in role.permisos:
                    if permission.nombre_accion and permission.nombre_recurso:
                        user_permissions.add(f"{permission.nombre_accion}:{permission.nombre_recurso}")

        # 2. Verificar si el usuario tiene AL MENOS UNO de los permisos requeridos
        #    Usamos la intersección de conjuntos: si la intersección NO está vacía,
        #    significa que el usuario tiene al menos uno de los permisos requeridos.
        has_permission = bool(permission_set.intersection(user_permissions))

        # 3. Lanzar excepción 403 si NO tiene ninguno de los permisos requeridos
        if not has_permission:
            logger.warning(
                f"Acceso DENEGADO para Usuario ID={current_user.id}. "
                f"Requiere: {req_perm_repr}. Posee: {user_permissions}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permiso insuficiente: Se requiere {req_perm_repr}."
            )
        else:
            # Opcional: Log de acceso permitido
            logger.debug(
                 f"Acceso PERMITIDO para Usuario ID={current_user.id}. "
                 f"Req: {req_perm_repr}. Posee: {user_permissions}."
             )
        # Si tiene el permiso (o uno de ellos), la dependencia simplemente termina
        # y FastAPI continúa con la ejecución del endpoint.

    return _permission_check