# app/api/v1/endpoints/usuarios.py
import logging
from typing import List, Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response
from sqlmodel import Session

from app.core.database import get_db
# Importar dependencias necesarias
from app.api.deps import get_db, get_current_active_user, require_permission # Cambiar require_admin_role por require_permission
from app.models import Usuario
from app.services import usuario_service
from app.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioRead,
    UsuarioUpdate,
    UsuarioUpdatePassword
)
from app.schemas.rol_permiso_schema import RolRead

router = APIRouter(prefix="/usuarios", tags=["Usuarios"]) # O "Users"
logger = logging.getLogger(__name__)

# --- Creación de Usuario ---
@router.post(
    "", # Ruta base del router de usuarios (ej: /api/v1/usuarios)
    response_model=UsuarioRead, # Devuelve el usuario creado con sus roles
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo usuario",
    dependencies=[Depends(require_permission("crear:usuario"))], # <--- PERMISO ESPECÍFICO
    responses={
        400: {"description": "Datos inválidos"},
        404: {"description": "Uno o más IDs de rol no existen"},
        403: {"description": "Permiso insuficiente"} 
    }
)
def create_user(
    *,
    db: Annotated[Session, Depends(get_db)],
    user_in: UsuarioCreate
):
    """
    Crea un nuevo usuario en el sistema especificando sus datos y roles iniciales.

    - **Requiere permiso:** `crear:usuario`.
    - Permite asignar roles mediante la lista `rol_ids`.
    """
    # Log indicando la acción protegida
    logger.info(f"[Permiso: crear:usuario] Solicitud para crear usuario: {user_in.username}")
    try:
        new_user = usuario_service.create_new_user(db=db, user_in=user_in)
        return new_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado al crear usuario '{user_in.username}': {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el usuario."
        )


# --- Endpoints /me (Solo requieren usuario activo, sin permiso específico) ---
@router.get(
    "/me",
    response_model=UsuarioRead,
    summary="Obtener datos del usuario autenticado"
    # No requiere permiso específico más allá de estar autenticado y activo
)
def read_users_me(
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Obtiene los datos del usuario autenticado (incluyendo sus roles)."""
    logger.info(f"Solicitud de datos para usuario ID: {current_user.id}")
    return current_user

@router.patch(
    "/me",
    response_model=UsuarioRead,
    summary="Actualizar perfil del usuario autenticado"
    # No requiere permiso específico
)
def update_self(
    *,
    db: Annotated[Session, Depends(get_db)],
    update_data: UsuarioUpdate,
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Permite al usuario autenticado actualizar su propio perfil."""
    logger.info(f"Actualizando perfil propio para usuario ID: {current_user.id}")
    try:
        updated_user = usuario_service.update_user_profile(
            db=db, current_user=current_user, user_in=update_data
        )
        return updated_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error actualizando perfil propio (ID: {current_user.id}): {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al actualizar el perfil.")

@router.put(
    "/me/password",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Cambiar contraseña del usuario autenticado"
    # No requiere permiso específico
)
def update_password(
    *,
    db: Annotated[Session, Depends(get_db)],
    password_data: UsuarioUpdatePassword,
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Endpoint para que el usuario autenticado cambie su propia contraseña."""
    logger.info(f"Solicitando cambio de contraseña para usuario ID: {current_user.id}")
    try:
        usuario_service.update_user_password(db=db, current_user=current_user, password_in=password_data)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error cambiando contraseña propia (ID: {current_user.id}): {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al actualizar contraseña.")




# --- Endpoints Admin sobre Usuarios Específicos ---

@router.get(
    "/{user_id}",
    response_model=UsuarioRead,
    summary="Obtener usuario por ID", # Ya no necesita (Admin) aquí
    # Aplicar permiso específico
    dependencies=[Depends(require_permission("leer:usuario"))], # <--- PERMISO ESPECÍFICO
    responses={404: {"description": "Usuario no encontrado"},
               403: {"description": "Permiso insuficiente"}}
)
def get_user(
    *,
    db: Annotated[Session, Depends(get_db)],
    user_id: int = Path(..., description="ID del usuario a obtener", gt=0)
):
    """
    Obtiene información de cualquier usuario por su ID.
    - **Requiere permiso:** `leer:usuario`.
    """
    logger.info(f"[Permiso: leer:usuario] Solicitud para obtener usuario ID: {user_id}")
    try:
        user = usuario_service.get_user_info(db=db, user_id=user_id)
        return user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error obteniendo usuario ID {user_id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al recuperar usuario.")


@router.post(
    "/{user_id}/roles/{rol_id}",
    response_model=UsuarioRead,
    status_code=status.HTTP_200_OK,
    summary="Asignar un Rol a un Usuario",
    # Aplicar permiso específico
    dependencies=[Depends(require_permission("asignar:rol_usuario"))], # <--- PERMISO ESPECÍFICO
    responses={
        404: {"description": "Usuario o Rol no encontrado"},
        403: {"description": "Permiso insuficiente"}
    }
)
def assign_role_to_user_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    user_id: int = Path(..., description="ID del usuario al que asignar el rol", gt=0),
    rol_id: int = Path(..., description="ID del rol a asignar", gt=0)
):
    """
    Asigna un rol específico a un usuario específico.
    - **Requiere permiso:** `asignar:rol_usuario`.
    """
    logger.info(f"[Permiso: asignar:rol_usuario] Solicitud para asignar rol ID={rol_id} a usuario ID={user_id}")
    try:
        updated_user = usuario_service.assign_role_to_user_service(
            db=db, user_id=user_id, rol_id=rol_id
        )
        return updated_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado asignando rol ID={rol_id} a usuario ID={user_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor.")


@router.delete(
    "/{user_id}/roles/{rol_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Quitar un Rol de un Usuario",
    # Aplicar permiso específico
    dependencies=[Depends(require_permission("remover:rol_usuario"))], # <--- PERMISO ESPECÍFICO
    responses={
        404: {"description": "Usuario o Rol no encontrado"},
        403: {"description": "Permiso insuficiente"}
    }
)
def remove_role_from_user_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    user_id: int = Path(..., description="ID del usuario del que quitar el rol", gt=0),
    rol_id: int = Path(..., description="ID del rol a quitar", gt=0)
):
    """
    Quita la asignación de un rol específico a un usuario específico.
    - **Requiere permiso:** `remover:rol_usuario`.
    """
    logger.info(f"[Permiso: remover:rol_usuario] Solicitud para quitar rol ID={rol_id} de usuario ID={user_id}")
    try:
        usuario_service.remove_role_from_user_service(
            db=db, user_id=user_id, rol_id=rol_id
        )
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado quitando rol ID={rol_id} de usuario ID={user_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor.")
