# app/api/v1/endpoints/servicios.py
import logging
from typing import List, Optional, Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response
from sqlmodel import Session

# Importar dependencias, servicios y schemas necesarios
from app.api.deps import get_db, require_permission
from app.services import service_service # Cambiado a service_service
from app.schemas.service_schema import (
    ServicioDefinicionCreate, ServicioDefinicionUpdate, ServicioDefinicionRead
)

logger = logging.getLogger(__name__)

# --- Router Principal para Servicios ---
# Podríamos tener más endpoints relacionados a servicios aquí en el futuro (ej: Fórmulas)
router = APIRouter(
    prefix="/servicios", # Prefijo base para todos los endpoints relacionados a servicios
    tags=["Servicios"],  # Etiqueta para agrupar en la documentación OpenAPI
    responses={
        404: {"description": "Recurso de servicio no encontrado"},
        403: {"description": "Permiso insuficiente"},
        409: {"description": "Conflicto de datos (ej: nombre duplicado, dependencia)"}
    }
)

# --- Endpoints específicos para Definiciones de Servicio ---

@router.post(
    "/definiciones", # Ruta: POST /api/v1/servicios/definiciones
    response_model=ServicioDefinicionRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva Definición de Servicio",
    # Asumiendo permiso 'gestionar:servicio_definicion'
    dependencies=[Depends(require_permission("gestionar:servicio_definicion"))]
)
def create_new_servicio_definicion(
    *, # Forzar kwargs
    db: Annotated[Session, Depends(get_db)],
    servicio_in: ServicioDefinicionCreate # Cuerpo de la solicitud
):
    """
    Crea una nueva definición para un tipo de servicio ofrecido.

    Requiere permiso: `gestionar:servicio_definicion`.
    """
    logger.info(f"[Permiso: gestionar:servicio_definicion] Crear ServicioDefinicion: {servicio_in.nombre}")
    # El servicio maneja la validación de nombre único y errores
    return service_service.create_servicio_service(db=db, servicio_in=servicio_in)

@router.get(
    "/definiciones", # Ruta: GET /api/v1/servicios/definiciones
    response_model=List[ServicioDefinicionRead],
    summary="Listar Definiciones de Servicio",
    # Asumiendo permiso 'leer:servicio_definicion'
    dependencies=[Depends(require_permission("leer:servicio_definicion"))]
)
def list_all_servicio_definiciones(
    # Parámetros de Query primero
    skip: int = Query(0, ge=0, description="Número de definiciones a saltar"),
    limit: int = Query(100, ge=1, le=200, description="Número máximo de definiciones a devolver"),
    *, # Separador
    db: Annotated[Session, Depends(get_db)]
):
    """
    Obtiene una lista paginada de todas las definiciones de servicios disponibles.

    Requiere permiso: `leer:servicio_definicion`.
    """
    logger.debug(f"[Permiso: leer:servicio_definicion] Listar ServicioDefinicion")
    return service_service.list_servicios_service(db=db, skip=skip, limit=limit)

@router.get(
    "/definiciones/{servicio_id}", # Ruta: GET /api/v1/servicios/definiciones/{id}
    response_model=ServicioDefinicionRead,
    summary="Obtener Definición de Servicio por ID",
    dependencies=[Depends(require_permission("leer:servicio_definicion"))]
)
def get_single_servicio_definicion(
    # Parámetro de Path primero
    servicio_id: int = Path(..., description="ID de la definición de servicio a obtener", gt=0),
    *, # Separador
    db: Annotated[Session, Depends(get_db)]
):
    """
    Obtiene los detalles de una definición de servicio específica por su ID.

    Requiere permiso: `leer:servicio_definicion`.
    """
    logger.debug(f"[Permiso: leer:servicio_definicion] Obtener ServicioDefinicion ID: {servicio_id}")
    # El servicio maneja el error 404 si no se encuentra
    return service_service.get_servicio_by_id_service(db=db, servicio_id=servicio_id)

@router.put(
    "/definiciones/{servicio_id}", # Ruta: PUT /api/v1/servicios/definiciones/{id}
    response_model=ServicioDefinicionRead,
    summary="Actualizar Definición de Servicio",
    dependencies=[Depends(require_permission("gestionar:servicio_definicion"))]
)
def update_existing_servicio_definicion(
    # Path param primero
    servicio_id: int = Path(..., description="ID de la definición de servicio a actualizar", gt=0),
    *, # Separador
    db: Annotated[Session, Depends(get_db)],
    servicio_in: ServicioDefinicionUpdate # Cuerpo con los campos a actualizar
):
    """
    Actualiza la información de una definición de servicio existente.
    Solo los campos proporcionados en el cuerpo de la solicitud serán actualizados.

    Requiere permiso: `gestionar:servicio_definicion`.
    """
    logger.info(f"[Permiso: gestionar:servicio_definicion] Actualizar ServicioDefinicion ID: {servicio_id}")
    # El servicio maneja 404, conflicto de nombre (409) y actualización
    return service_service.update_servicio_service(db=db, servicio_id=servicio_id, servicio_in=servicio_in)

@router.delete(
    "/definiciones/{servicio_id}", # Ruta: DELETE /api/v1/servicios/definiciones/{id}
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar Definición de Servicio",
    dependencies=[Depends(require_permission("gestionar:servicio_definicion"))]
)
def delete_existing_servicio_definicion(
    # Path param primero
    servicio_id: int = Path(..., description="ID de la definición de servicio a eliminar", gt=0),
    *, # Separador
    db: Annotated[Session, Depends(get_db)]
):
    """
    Elimina una definición de servicio existente.
    Falla si el servicio está referenciado en Fórmulas o Proformas.

    Requiere permiso: `gestionar:servicio_definicion`.
    """
    logger.warning(f"[Permiso: gestionar:servicio_definicion] Eliminar ServicioDefinicion ID: {servicio_id}")
    # El servicio maneja 404 y conflicto de integridad (409)
    service_service.delete_servicio_service(db=db, servicio_id=servicio_id)
    # Si el servicio no lanzó excepción, la eliminación fue exitosa
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Aquí se podrían añadir endpoints para Fórmulas en el futuro (ej: POST /definiciones/{id}/formulas)