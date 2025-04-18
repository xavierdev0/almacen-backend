# app/api/v1/endpoints/usuarios.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Annotated
import logging
from uuid import UUID

from app.core.database import get_db
from app.services import usuario_service
from app.schemas.usuario_schema import (
    UsuarioCreate, 
    UsuarioRead, 
    UsuarioUpdate, 
    UsuarioUpdatePassword
)
from app.api.deps import get_current_active_user
from app.models.user_models import Usuario

router = APIRouter(tags=["users"])
logger = logging.getLogger(__name__)

# --- Creación de Usuario ---
@router.post(
    "", 
    response_model=UsuarioRead, 
    status_code=status.HTTP_201_CREATED,
    summary="Crear nuevo usuario"
)
def create_user(
    db: Annotated[Session, Depends(get_db)],
    user_in: UsuarioCreate
):
    """Endpoint público para registro de nuevos usuarios."""
    try:
        logger.info(f"Creando usuario: {user_in.username[:3]}***")
        return usuario_service.create_new_user(db, user_in)
    except Exception as e:
        logger.error(f"Error creando usuario: {str(e)}", exc_info=True)
        raise

# --- Usuario Actual ---
@router.get(
    "/me",
    response_model=UsuarioRead,
    summary="Obtener datos del usuario autenticado"
)
def read_users_me(
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Obtiene los datos del usuario autenticado."""
    logger.info(f"Solicitud de datos para usuario ID: {current_user.id}")
    return current_user

# --- Actualización de Perfil ---
@router.patch(
    "/me",
    response_model=UsuarioRead,
    summary="Actualizar perfil del usuario"
)
def update_self(
    db: Annotated[Session, Depends(get_db)],
    update_data: UsuarioUpdate,
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Permite actualizar información del perfil."""
    try:
        logger.info(f"Actualizando usuario ID: {current_user.id}")
        return usuario_service.update_user_profile(
                                                    db=db,
                                                    current_user=current_user,
                                                    user_in=update_data # Match the parameter name 'user_in' in the service function definition
                                                )
    except Exception as e:
        logger.error(f"Error actualizando perfil: {str(e)}")
        raise HTTPException(500, "Error interno al actualizar")

# --- Actualización de Contraseña ---
@router.put(
    "/me/password",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Cambiar contraseña"
)
def update_password(
    db: Annotated[Session, Depends(get_db)],
    password_data: UsuarioUpdatePassword,
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Endpoint para cambio de contraseña."""
    try:
        logger.info(f"Cambiando contraseña usuario ID: {current_user.id}")
        usuario_service.update_user_password(db=db, current_user=current_user, password_in=password_data)
    except Exception as e:
        logger.error(f"Error cambiando contraseña: {str(e)}")
        raise HTTPException(500, "Error interno al actualizar contraseña")

# --- Endpoints Admin (Ejemplo) ---
@router.get(
    "/{user_id}",
    response_model=UsuarioRead,
    summary="Obtener usuario por ID (Admin)",
    dependencies=[Depends(get_current_active_user)]  # + dependencia de rol
)
def get_user(
    db: Annotated[Session, Depends(get_db)],
    user_id: int
):
    """Endpoint administrativo para obtener cualquier usuario."""
    try:
        return usuario_service.get_user_info(db, user_id)
    except Exception as e:
        logger.error(f"Error obteniendo usuario {user_id}: {str(e)}")
        raise HTTPException(500, "Error interno al recuperar usuario")