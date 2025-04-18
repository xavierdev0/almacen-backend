# app/api/v1/endpoints/permisos.py

import logging
from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response # Añadir Response
from sqlmodel import Session

from app.core.database import get_db
# Importar dependencias necesarias
from app.api.deps import get_db, require_permission # Quitar get_current_active_user si no se usa, quitar require_admin_role
# from app.models import Usuario # Ya no se necesita aquí si no se inyecta current_user
# Importar servicios y schemas
from app.services import permiso_service
from app.schemas.rol_permiso_schema import (
    PermisoCreate, PermisoUpdate, PermisoRead
)

logger = logging.getLogger(__name__)

# Aplicar la dependencia de seguridad a nivel de router
router = APIRouter(
    prefix="/permisos",
    tags=["Roles y Permisos (Admin)"], # Mismo tag para agrupar en Swagger
)

@router.post(
    "",
    response_model=PermisoRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo Permiso"
)
def create_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_in: PermisoCreate
):
    """
    Endpoint para crear un nuevo permiso en el sistema.
    (Requiere rol Administrador).
    """
    logger.info(f"Solicitud para crear permiso: {permiso_in.nombre_accion}:{permiso_in.nombre_recurso}")
    permiso = permiso_service.create_new_permiso(db=db, permiso_in=permiso_in)
    return permiso

@router.get(
    "",
    response_model=List[PermisoRead],
    summary="Listar Permisos"
)
def list_permisos(
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0, description="Número de permisos a saltar"),
    limit: int = Query(100, ge=1, le=500, description="Número máximo de permisos a devolver") # Aumentado limite para permisos
):
    """
    Endpoint para listar permisos con paginación.
    (Requiere rol Administrador).
    """
    logger.debug(f"Solicitud para listar permisos, skip={skip}, limit={limit}")
    permisos = permiso_service.get_all_permisos(db=db, skip=skip, limit=limit)
    return permisos

@router.get(
    "/{permiso_id}",
    response_model=PermisoRead,
    summary="Obtener un Permiso por ID",
    responses={404: {"description": "Permiso no encontrado"}}
)
def get_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a obtener", gt=0)
):
    """
    Endpoint para obtener detalles de un permiso específico.
    (Requiere rol Administrador).
    """
    logger.debug(f"Solicitud para obtener permiso ID: {permiso_id}")
    permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id)
    return permiso

@router.put(
    "/{permiso_id}",
    response_model=PermisoRead,
    summary="Actualizar un Permiso",
    responses={404: {"description": "Permiso no encontrado"},
               409: {"description": "Conflicto, acción/recurso ya existe"}}
)
def update_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a actualizar", gt=0),
    permiso_in: PermisoUpdate
):
    """
    Endpoint para actualizar un permiso existente.
    (Requiere rol Administrador).
    """
    logger.info(f"Solicitud para actualizar permiso ID: {permiso_id}")
    updated_permiso = permiso_service.update_existing_permiso(
        db=db, permiso_id=permiso_id, permiso_in=permiso_in
    )
    return updated_permiso

@router.delete(
    "/{permiso_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un Permiso",
    responses={404: {"description": "Permiso no encontrado"}}
     # No añadimos 409 aquí porque confiamos en ON DELETE CASCADE por ahora
)
def delete_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a eliminar", gt=0)
):
    """
    Endpoint para eliminar un permiso existente.
    Las asociaciones con roles se eliminan en cascada (DB).
    (Requiere rol Administrador).
    """
    logger.info(f"Solicitud para eliminar permiso ID: {permiso_id}")
    permiso_service.delete_existing_permiso(db=db, permiso_id=permiso_id)
    return None # O return Response(status_code=status.HTTP_204_NO_CONTENT)
@router.post(
    "", # Ruta: POST /api/v1/permisos
    response_model=PermisoRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo Permiso",
    # Añadir dependencia de permiso específico
    dependencies=[Depends(require_permission("gestionar:permiso"))] # <--- NUEVA DEPENDENCIA
)
def create_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_in: PermisoCreate
):
    """
    Crea un nuevo permiso en el sistema.
    Requiere permiso 'gestionar:permiso'.
    """
    logger.info(f"[Permiso: gestionar:permiso] Solicitud para crear permiso: {permiso_in.nombre_accion}:{permiso_in.nombre_recurso}")
    # El servicio maneja la lógica y posible 409 por duplicado
    permiso = permiso_service.create_new_permiso(db=db, permiso_in=permiso_in)
    return permiso

@router.get(
    "", # Ruta: GET /api/v1/permisos
    response_model=List[PermisoRead],
    summary="Listar Permisos",
    dependencies=[Depends(require_permission("leer:permiso"))] # <--- NUEVA DEPENDENCIA
)
def list_permisos(
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500)
):
    """
    Lista permisos con paginación.
    Requiere permiso 'leer:permiso'.
    """
    logger.debug(f"[Permiso: leer:permiso] Solicitud para listar permisos, skip={skip}, limit={limit}")
    permisos = permiso_service.get_all_permisos(db=db, skip=skip, limit=limit)
    return permisos

@router.get(
    "/{permiso_id}", # Ruta: GET /api/v1/permisos/{permiso_id}
    response_model=PermisoRead,
    summary="Obtener un Permiso por ID",
    dependencies=[Depends(require_permission("leer:permiso"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Permiso no encontrado"}}
)
def get_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a obtener", gt=0)
):
    """
    Obtiene detalles de un permiso específico.
    Requiere permiso 'leer:permiso'.
    """
    logger.debug(f"[Permiso: leer:permiso] Solicitud para obtener permiso ID: {permiso_id}")
    # El servicio maneja el 404
    permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id)
    return permiso

@router.put(
    "/{permiso_id}", # Ruta: PUT /api/v1/permisos/{permiso_id}
    response_model=PermisoRead,
    summary="Actualizar un Permiso",
    dependencies=[Depends(require_permission("gestionar:permiso"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Permiso no encontrado"},
               409: {"description": "Conflicto, acción/recurso ya existe"}}
)
def update_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a actualizar", gt=0),
    permiso_in: PermisoUpdate
):
    """
    Actualiza un permiso existente.
    Requiere permiso 'gestionar:permiso'.
    """
    logger.info(f"[Permiso: gestionar:permiso] Solicitud para actualizar permiso ID: {permiso_id}")
    # El servicio maneja 404, 409 y lógica
    updated_permiso = permiso_service.update_existing_permiso(
        db=db, permiso_id=permiso_id, permiso_in=permiso_in
    )
    return updated_permiso

@router.delete(
    "/{permiso_id}", # Ruta: DELETE /api/v1/permisos/{permiso_id}
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un Permiso",
    dependencies=[Depends(require_permission("gestionar:permiso"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Permiso no encontrado"}}
     # 409 no aplica por ON DELETE CASCADE
)
def delete_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a eliminar", gt=0)
):
    """
    Elimina un permiso existente. Las asociaciones con roles se eliminan en cascada.
    Requiere permiso 'gestionar:permiso'.
    """
    logger.info(f"[Permiso: gestionar:permiso] Solicitud para eliminar permiso ID: {permiso_id}")
    # El servicio maneja 404
    permiso_service.delete_existing_permiso(db=db, permiso_id=permiso_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)