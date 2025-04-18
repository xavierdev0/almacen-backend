# app/services/usuario_service.py
import logging
from sqlmodel import Session
from fastapi import HTTPException, status
from typing import Optional, Union
from uuid import UUID
import re

from app.models.user_models import Usuario
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioUpdatePassword
from app.repositories import usuario_repository
from app.core.security import get_password_hash, verify_password
from app.core.config import settings

logger = logging.getLogger(__name__)

# --- Helpers ---
def _sanitize_email(email: str) -> str:
    """Normaliza emails a minúsculas y remueve espacios."""
    return email.strip().lower()

def _sanitize_username(username: str) -> str:
    """Normaliza username y valida formato."""
    sanitized = username.strip().lower()
    if not re.match(r"^[a-z0-9_]+$", sanitized):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username solo puede contener letras, números y guiones bajos"
        )
    return sanitized

# --- Creación ---
def create_new_user(db: Session, user_in: UsuarioCreate) -> Usuario:
    """Crea un nuevo usuario con validación avanzada."""
    try:
        # Sanitización
        email = _sanitize_email(user_in.email)
        username = _sanitize_username(user_in.username)
        
        logger.info(f"Creando usuario: {username[:3]}***")  # Log seguro
        
        # Verificar duplicados
        if usuario_repository.get_usuario_by_email(db, email):
            logger.warning(f"Email ya registrado: {email[:5]}***")
            raise HTTPException(status_code=400, detail="Email ya registrado")

        if usuario_repository.get_usuario_by_username(db, username):
            logger.warning(f"Username ya registrado: {username[:3]}***")
            raise HTTPException(status_code=400, detail="Username no disponible")

        # Validar fortaleza de contraseña
        #if settings.ENFORCE_PASSWORD_POLICY:
        #    if len(user_in.password) < 12:
        #        raise HTTPException(
        #            status_code=400,
        #            detail="La contraseña debe tener al menos 12 caracteres"
        #        )

        # Crear usuario
        hashed_password = get_password_hash(user_in.password)
        user_data_dict = user_in.model_dump(exclude={"password", "email", "username"})
        db_user = Usuario(
            email=email,                          # Pasar email sanitizado
            username=username,                    # Pasar username sanitizado
            contrasena_hash=hashed_password,
            esta_activo=True,
            **user_data_dict                      # Pasar el *resto* de los datos (ej: nombre_completo)
        )

        created_user = usuario_repository.create_usuario(db, db_user)
        logger.info(f"Usuario {created_user.id} creado")
        return created_user

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creando usuario: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Error interno al crear el usuario"
        )

# --- Actualización de Perfil ---
def update_user_profile(db: Session, *, current_user: Usuario, user_in: UsuarioUpdate) -> Usuario:
    """Actualiza perfil con sanitización."""
    try:
        update_data = user_in.model_dump(exclude_unset=True)
        
        # Sanitizar email si se actualiza
        if "email" in update_data:
            new_email = _sanitize_email(update_data["email"])
            if new_email != current_user.email:
                existing = usuario_repository.get_usuario_by_email(db, new_email)
                if existing:
                    raise HTTPException(400, "Email ya en uso")
                update_data["email"] = new_email

        # Sanitizar username si se permite actualizar
        if "username" in update_data:
            new_username = _sanitize_username(update_data["username"])
            if new_username != current_user.username:
                existing = usuario_repository.get_usuario_by_username(db, new_username)
                if existing:
                    raise HTTPException(400, "Username no disponible")
                update_data["username"] = new_username

        updated_user = usuario_repository.update_usuario(
            db, 
            db_user=current_user, 
            update_data=update_data
        )
        logger.info(f"Usuario {updated_user.id} actualizado")
        return updated_user

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error actualizando perfil: {str(e)}")
        raise HTTPException(500, "Error interno al actualizar")

# --- Actualización de Contraseña ---
def update_user_password(
    db: Session, 
    *, 
    current_user: Usuario, 
    password_in: UsuarioUpdatePassword
) -> Usuario:
    """Cambia contraseña con validación de política."""
    try:
        # Verificar contraseña actual
        if not verify_password(password_in.old_password, current_user.contrasena_hash):
            raise HTTPException(400, "Contraseña actual incorrecta")

        # Validar nueva contraseña
        #if settings.ENFORCE_PASSWORD_POLICY:
        #    if len(password_in.new_password) < 12:
        #        raise HTTPException(400, "La contraseña debe tener al menos 12 caracteres")

        # Actualizar
        new_hash = get_password_hash(password_in.new_password)
        return usuario_repository.update_usuario(
            db,
            db_user=current_user,
            update_data={"contrasena_hash": new_hash}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error cambiando contraseña: {str(e)}")
        raise HTTPException(500, "Error interno al actualizar contraseña")

# --- Lectura ---
def get_user_info(db: Session, user_id: Optional[int]) -> Usuario:
    """Obtiene usuario por ID/UUID."""
    try:
        user = usuario_repository.get_usuario(db, user_id)
        if not user:
            logger.warning(f"Usuario {user_id} no encontrado")
            raise HTTPException(404, "Usuario no encontrado")
        return user
    except Exception as e:
        logger.error(f"Error obteniendo usuario: {str(e)}")
        raise HTTPException(500, "Error interno al recuperar usuario")