# app/services/auth_service.py

from sqlmodel import Session
from fastapi import HTTPException, status
import logging

from app.models.user_models import Usuario
from app.repositories import usuario_repository
from app.core.security import verify_password

logger = logging.getLogger(__name__)

# =====================
#  Excepción Personalizada
# =====================

class AuthException(HTTPException):
    """
    Excepción personalizada para errores específicos de autenticación.

    Hereda de HTTPException, estableciendo automáticamente el código de estado
    401 (Unauthorized) y la cabecera 'WWW-Authenticate' requerida.

    Args:
        detail: Mensaje de error detallado que se enviará al cliente.
    """
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"} # Estándar para autenticación Bearer
        )

# =====================
#  Lógica de Autenticación
# =====================

def authenticate_user(db: Session, username: str, password: str) -> Usuario:
    """
    Autentica un usuario por nombre de usuario/email y contraseña.

    Verifica la existencia del usuario (buscando por username o email),
    si la cuenta está activa y si la contraseña proporcionada coincide
    con el hash almacenado.

    Args:
        db: La sesión de base de datos activa.
        username: El nombre de usuario o correo electrónico del usuario.
                  Se normaliza a minúsculas y se eliminan espacios.
        password: La contraseña en texto plano proporcionada por el usuario.

    Returns:
        El objeto Usuario completo si la autenticación es exitosa.

    Raises:
        AuthException: Si las credenciales están incompletas, el usuario no existe,
                       la cuenta está inactiva o la contraseña es incorrecta.

    Example:
        >>> user = authenticate_user(db, " testuser@example.com ", "password123")
        >>> print(user.username)
        testuser
    """
    # Sanitización básica de inputs
    username = username.strip().lower()
    if not username or not password:
        logger.warning("Intento de autenticación con credenciales vacías")
        raise AuthException("Credenciales incompletas")

    # Buscar por username o email usando el repositorio
    user = usuario_repository.get_usuario_by_username(db, username)
    if not user:
        # Si no se encontró por username, intentar por email
        user = usuario_repository.get_usuario_by_email(db, username)

    # Mensaje genérico para no revelar si el usuario existe o no
    error_detail = "Credenciales inválidas"
    if not user:
        logger.warning(f"Intento de login con usuario inexistente: {username}")
        raise AuthException(error_detail)

    # Verificar si la cuenta está activa
    if not user.esta_activo:
        logger.warning(f"Intento de login en cuenta inactiva: {user.username}")
        raise AuthException("Cuenta deshabilitada")

    # Verificar la contraseña
    if not verify_password(password, user.contrasena_hash):
        logger.warning(f"Contraseña incorrecta para usuario: {user.username}")
        raise AuthException(error_detail)

    # Autenticación exitosa
    logger.info(f"Login exitoso: {user.username}")
    return user