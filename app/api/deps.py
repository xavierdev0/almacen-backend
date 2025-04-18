# app/api/deps.py
from typing import Annotated, Optional
from fastapi import Depends, HTTPException, status, Request
from sqlmodel import Session
from jose import JWTError
import logging
from uuid import UUID

from app.core.database import get_db
from app.core.security import oauth2_scheme, decode_access_token
from app.models.user_models import Usuario
from app.repositories import usuario_repository

logger = logging.getLogger(__name__)

def auth_exception(detail: str = "Credenciales de autenticación inválidas") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )

async def get_current_user(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_scheme)]
) -> Usuario:
    """
    Obtiene el usuario actual desde el JWT y verifica su existencia en la DB.
    
    Args:
        token: JWT extraído del header Authorization
        db: Sesión de base de datos
        
    Raises:
        HTTPException 401: Para cualquier fallo de autenticación
    """
    try:

        subject_str = decode_access_token(token) 

        if not subject_str:
            logger.warning(f"Token inválido o claims incompletos: {token[:10]}... (IP: {request.client.host})")
            # Puedes usar un mensaje más específico si quieres diferenciar de otros errores 401
            raise auth_exception("Token inválido o expirado")
            
        try:
            user_id = int(subject_str)
        except ValueError:
            # Si no se puede convertir a entero, el token es inválido para nuestro sistema
            logger.error(f"Subject del token no es un entero válido: {subject_str}")
            raise auth_exception("Identificador de usuario inválido en el token")
        # Buscar usuario
        user = usuario_repository.get_usuario(db, user_id)
        if not user:
            logger.error(f"Usuario del token no encontrado: ID {user_id}")
            raise auth_exception()
            
        logger.debug(f"Usuario autenticado: {user.id}")
        return user
        
    except JWTError as e:
        logger.error(f"Error decodificando token: {str(e)}")
        raise auth_exception()
    except ValueError as e:
        logger.error(f"Formato de ID inválido en token: {str(e)}")
        raise auth_exception()
    except Exception as e:
        logger.critical(f"Error inesperado en autenticación: {str(e)}")
        raise auth_exception("Error interno de autenticación")

def get_current_active_user(
    current_user: Annotated[Usuario, Depends(get_current_user)]
) -> Usuario:
    """Verifica que el usuario esté activo."""
    if not current_user.esta_activo:
        logger.warning(f"Intento de acceso de usuario inactivo: {current_user.id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cuenta deshabilitada"
        )
    return current_user

# Ejemplo de dependencia para roles
# def require_admin(user: Usuario = Depends(get_current_active_user)) -> Usuario:
#     if not user.es_admin:
#         logger.warning(f"Intento de acceso admin no autorizado: {user.id}")
#         raise HTTPException(status.HTTP_403_FORBIDDEN, "Acceso restringido")
#     return user