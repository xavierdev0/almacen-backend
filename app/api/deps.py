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





def require_permission(required_permission: str) -> Callable:
    """
    Fábrica que crea una dependencia de FastAPI para verificar si el usuario
    activo tiene un permiso específico. (CON PRINTS PARA DEBUG)
    """
    async def _permission_check(
        current_user: Annotated[Usuario, Depends(get_current_active_user)]
    ):
        """Dependencia interna que realiza la verificación."""
        print(f"\n--- DEBUG [require_permission] para '{required_permission}' ---") 
        print(f"--- DEBUG Usuario: ID={current_user.id}, Username='{current_user.username}'") 

        user_permissions: Set[str] = set()
        if not current_user.roles:
             print(f"--- WARNING Usuario ID={current_user.id} no tiene roles asignados.") 
        else:
            print(f"--- DEBUG Roles encontrados: {[r.nombre for r in current_user.roles]}") 
            for role in current_user.roles:
                print(f"--- DEBUG Procesando Rol: ID={role.id}, Nombre='{role.nombre}'") 
                if hasattr(role, 'permisos') and role.permisos is not None:
                    print(f"--- DEBUG  Rol '{role.nombre}' - Atributo 'permisos' existe y no es None. Intentando iterar...") 
                    perm_count_in_role = 0
                    try:
                        for permission in role.permisos:
                            if hasattr(permission, 'nombre_accion') and hasattr(permission, 'nombre_recurso'):
                                permission_str = f"{permission.nombre_accion}:{permission.nombre_recurso}"
                                user_permissions.add(permission_str)
                                perm_count_in_role += 1
                                # print(f"    Añadido permiso: {permission_str}") # Descomentar si es necesario ver cada uno
                            else:
                                print(f"    ERROR: Objeto permiso inválido o atributos faltantes en Rol ID={role.id}: {permission}") 
                        print(f"--- DEBUG  Rol '{role.nombre}' - Se añadieron {perm_count_in_role} permisos al set.") 
                    except Exception as iter_exc:
                        print(f"--- ERROR CRÍTICO al iterar role.permisos para Rol ID={role.id}: {iter_exc}") 

                else:
                    print(f"--- ERROR CRÍTICO: La relación 'permisos' NO está cargada o es None para el Rol ID={role.id} ('{role.nombre}') del usuario ID={current_user.id}.") # <-- PRINT (era error)

        print(f"--- DEBUG Set final de permisos agregados: {user_permissions}") 


        if required_permission not in user_permissions:
            print( 
                f"--- ACCESS DENIED para Usuario ID={current_user.id}. "
                f"Req: '{required_permission}'. Found: {user_permissions}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permiso insuficiente: Se requiere '{required_permission}'."
            )
        else:
            print( 
                f"--- ACCESS GRANTED para Usuario ID={current_user.id}. "
                f"Req: '{required_permission}'. Found in {user_permissions}."
            )

    return _permission_check