# app/services/auth_service.py
from sqlmodel import Session
from typing import Optional
from fastapi import HTTPException, status
import logging

from app.models.usuario_model import Usuario
from app.repositories import usuario_repository
from app.core.security import verify_password

logger = logging.getLogger(__name__)

class AuthException(HTTPException):
    """Excepción base para errores de autenticación."""
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )

def authenticate_user(db: Session, username: str, password: str) -> Usuario:
    """
    Autentica un usuario y devuelve el objeto Usuario.
    
    Args:
        db: Sesión de base de datos
        username: Nombre de usuario o email
        password: Contraseña en texto plano

    Raises:
        AuthException: Para todos los casos de fallo de autenticación

    Ejemplo:
        >>> authenticate_user(db, "johndoe", "secret")
        <Usuario: johndoe>
    """
    # Sanitización básica de inputs
    username = username.strip().lower()
    if not username or not password:
        logger.warning("Intento de autenticación con credenciales vacías")
        raise AuthException("Credenciales incompletas")

    # Buscar por username o email
    user = usuario_repository.get_usuario_by_username(db, username)
    if not user:
        user = usuario_repository.get_usuario_by_email(db, username)
    
    error_detail = "Credenciales inválidas"
    if not user:
        logger.warning(f"Intento de login con usuario inexistente: {username}")
        raise AuthException(error_detail)
    
    if not user.esta_activo:
        logger.warning(f"Intento de login en cuenta inactiva: {user.username}")
        raise AuthException("Cuenta deshabilitada")
    
    if not verify_password(password, user.contrasena_hash):
        logger.warning(f"Contraseña incorrecta para usuario: {user.username}")
        raise AuthException(error_detail)
    
    logger.info(f"Login exitoso: {user.username}")
    return user