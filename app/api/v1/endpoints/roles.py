# app/api/v1/endpoints/roles.py

import logging
from typing import List, Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response
from sqlmodel import Session

from app.core.database import get_db
# Importar dependencias necesarias
from app.api.deps import get_db, get_current_active_user, require_permission #QUITAMOS require_admin_role, AÑADIMOS require_permission
from app.models import Usuario, Rol
from app.services import rol_service
from app.schemas.rol_permiso_schema import (
    RolCreate, RolUpdate, RolRead, RolReadWithPermissions, PermisoRead
)

logger = logging.getLogger(__name__)

# Aplicar la dependencia de seguridad a nivel de router
# Todas las rutas en este archivo requerirán el rol de admin
router = APIRouter(
    prefix="/roles",
    tags=["Roles y Permisos"],
)

@router.post(
    "",
    response_model=RolRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo Rol",
    # Añadir dependencia de permiso específico
    dependencies=[Depends(require_permission("crear:rol"))] # <--- NUEVA DEPENDENCIA
)
def create_rol(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_in: RolCreate,
    dependencies=[Depends(require_permission("crear:rol"))] # <<<--- AÑADIR ESTA LÍNEA

):
    """Crea un nuevo rol en el sistema. Requiere permiso 'crear:rol'."""
    logger.info(f"[Permiso: crear:rol] Solicitud para crear rol: {rol_in.nombre}")
    rol = rol_service.create_new_rol(db=db, rol_in=rol_in)
    return rol

@router.get(
    "",
    response_model=List[RolRead],
    summary="Listar Roles",
    dependencies=[Depends(require_permission("leer:rol"))] # <--- NUEVA DEPENDENCIA
)
def list_roles(
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200)
):
    """Lista roles con paginación. Requiere permiso 'leer:rol'."""
    logger.debug(f"[Permiso: leer:rol] Solicitud para listar roles, skip={skip}, limit={limit}")
    roles = rol_service.get_all_roles(db=db, skip=skip, limit=limit)
    return roles

@router.get(
    "/{rol_id}",
    response_model=RolReadWithPermissions,
    summary="Obtener un Rol por ID (con permisos)",
    dependencies=[Depends(require_permission("leer:rol"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Rol no encontrado"}}
)
def get_rol(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol a obtener", gt=0)
    
):
    """Obtiene detalles de un rol específico, incluyendo sus permisos. Requiere permiso 'leer:rol'."""
    logger.debug(f"[Permiso: leer:rol] Solicitud para obtener rol ID: {rol_id}")
    rol = rol_service.get_rol_by_id(db=db, rol_id=rol_id, include_permissions=True)
    return rol


@router.put(
    "/{rol_id}",
    response_model=RolRead,
    summary="Actualizar un Rol",
    dependencies=[Depends(require_permission("actualizar:rol"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Rol no encontrado"},
               409: {"description": "Conflicto, nombre ya existe"}}
)
def update_rol(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol a actualizar", gt=0),
    rol_in: RolUpdate
):
    """Actualiza un rol existente. Requiere permiso 'actualizar:rol'."""
    logger.info(f"[Permiso: actualizar:rol] Solicitud para actualizar rol ID: {rol_id}")
    updated_rol = rol_service.update_existing_rol(db=db, rol_id=rol_id, rol_in=rol_in)
    return updated_rol

@router.delete(
    "/{rol_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un Rol",
    dependencies=[Depends(require_permission("eliminar:rol"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Rol no encontrado"},
               409: {"description": "Conflicto, rol asignado a usuarios"}}
)
def delete_rol(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol a eliminar", gt=0)
):
    """Elimina un rol existente. Falla si está asignado a usuarios. Requiere permiso 'eliminar:rol'."""
    logger.info(f"[Permiso: eliminar:rol] Solicitud para eliminar rol ID: {rol_id}")
    rol_service.delete_existing_rol(db=db, rol_id=rol_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- Endpoints para Asociación Rol-Permiso (Ahora con permisos específicos) ---

@router.post(
    "/{rol_id}/permisos/{permiso_id}",
    response_model=RolReadWithPermissions,
    status_code=status.HTTP_200_OK,
    summary="Asignar un Permiso a un Rol",
    dependencies=[Depends(require_permission("asignar:permiso_rol"))], 
    responses={
        404: {"description": "Rol o Permiso no encontrado"},
        409: {"description": "Conflicto, el permiso ya está asignado a este rol"}
    }
)
def assign_permission_to_role_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol al que asignar el permiso", gt=0),
    permiso_id: int = Path(..., description="ID del permiso a asignar", gt=0)
):
    """Asigna un permiso específico a un rol específico. Requiere permiso 'asignar:permiso_rol'."""
    logger.info(f"[Permiso: asignar:permiso_rol] Solicitud para asignar permiso ID={permiso_id} a rol ID={rol_id}")
    try:
        updated_rol = rol_service.add_permission_to_role(
            db=db, rol_id=rol_id, permiso_id=permiso_id
        )
        return updated_rol
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado asignando permiso ID={permiso_id} a rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor.")


@router.delete(
    "/{rol_id}/permisos/{permiso_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Quitar un Permiso de un Rol",
    dependencies=[Depends(require_permission("remover:permiso_rol"))], 
    responses={
        404: {"description": "Rol o Permiso no encontrado, o Permiso no asignado a este Rol"}
    }
)
def remove_permission_from_role_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol del que quitar el permiso", gt=0),
    permiso_id: int = Path(..., description="ID del permiso a quitar", gt=0)
):
    """Quita la asignación de un permiso específico a un rol específico. Requiere permiso 'remover:permiso_rol'."""
    logger.info(f"[Permiso: remover:permiso_rol] Solicitud para quitar permiso ID={permiso_id} de rol ID={rol_id}")
    try:
        rol_service.remove_permission_from_role(
            db=db, rol_id=rol_id, permiso_id=permiso_id
        )
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado quitando permiso ID={permiso_id} de rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor.")
