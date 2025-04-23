# app/services/service_service.py
import logging
from typing import Optional, Sequence, Dict, Any

from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError # Para capturar errores del repo

# Importar Repositorio, Modelo y Schemas
from app.repositories import service_repository
from app.models.service_models import ServicioDefinicion
from app.schemas.service_schema import ServicioDefinicionCreate, ServicioDefinicionUpdate

logger = logging.getLogger(__name__)

# =======================================
#  Servicios para ServicioDefinicion
# =======================================

def create_servicio_service(db: Session, *, servicio_in: ServicioDefinicionCreate) -> ServicioDefinicion:
    """
    Crea una nueva definición de servicio, validando nombre único.
    """
    logger.info(f"Servicio: Intentando crear ServicioDefinicion: Nombre='{servicio_in.nombre}'")

    # Validar Nombre único ANTES de intentar crear
    existing_by_name = service_repository.get_servicio_by_nombre(db, nombre=servicio_in.nombre)
    if existing_by_name:
        logger.warning(f"Conflicto: Nombre '{servicio_in.nombre}' ya existe para ServicioDefinicion.")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe una definición de servicio con el nombre '{servicio_in.nombre}'."
        )
    try:
        servicio_data = ServicioDefinicion.model_validate(servicio_in)
        new_servicio = service_repository.create_servicio(db=db, servicio_data=servicio_data)
        return new_servicio
    except IntegrityError: # Por si acaso (ej: futura constraint UNIQUE)
        db.rollback()
        logger.error(f"Error de Integridad (inesperado) al crear ServicioDefinicion '{servicio_in.nombre}'.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al crear ServicioDefinicion: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear definición de servicio.")

def get_servicio_by_id_service(db: Session, *, servicio_id: int) -> ServicioDefinicion:
    """
    Obtiene una definición de servicio por su ID.
    """
    logger.debug(f"Servicio: Buscando ServicioDefinicion ID: {servicio_id}")
    servicio = service_repository.get_servicio_by_id(db=db, servicio_id=servicio_id)
    if not servicio:
        logger.warning(f"Servicio: ServicioDefinicion ID {servicio_id} no encontrado.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Definición de servicio con ID {servicio_id} no encontrada.")
    return servicio

def list_servicios_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[ServicioDefinicion]:
    """
    Lista las definiciones de servicios.
    """
    logger.debug(f"Servicio: Listando definiciones de servicios, skip={skip}, limit={limit}")
    try:
        return service_repository.list_servicios(db=db, skip=skip, limit=limit)
    except Exception as e:
        logger.error(f"Error inesperado en servicio al listar ServicioDefinicion: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar definiciones de servicios.")

def update_servicio_service(db: Session, *, servicio_id: int, servicio_in: ServicioDefinicionUpdate) -> ServicioDefinicion:
    """
    Actualiza una definición de servicio, validando nombre único si cambia.
    """
    logger.info(f"Servicio: Intentando actualizar ServicioDefinicion ID: {servicio_id}")
    db_servicio = get_servicio_by_id_service(db=db, servicio_id=servicio_id) # Maneja 404

    update_data = servicio_in.model_dump(exclude_unset=True)
    if not update_data:
        logger.warning(f"Servicio: No se proporcionaron datos para actualizar ServicioDefinicion ID {servicio_id}.")
        return db_servicio # Devolver sin cambios

    # Validar conflicto de nombre si se intenta cambiar
    new_nombre = update_data.get("nombre")
    if new_nombre is not None and new_nombre != db_servicio.nombre:
        existing_by_name = service_repository.get_servicio_by_nombre(db, nombre=new_nombre)
        # Si existe OTRO servicio con ese nombre
        if existing_by_name and existing_by_name.id != servicio_id:
            logger.warning(f"Conflicto al actualizar: Nuevo nombre '{new_nombre}' ya pertenece a servicio ID {existing_by_name.id}.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Ya existe otra definición de servicio con el nombre '{new_nombre}'."
            )

    try:
        return service_repository.update_servicio(db=db, db_servicio=db_servicio, update_data=update_data)
    except IntegrityError: # Por si acaso (ej: futura constraint UNIQUE)
        db.rollback()
        logger.error(f"Error de Integridad (inesperado) al actualizar ServicioDefinicion ID {servicio_id}.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar la actualización.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al actualizar ServicioDefinicion ID {servicio_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar definición de servicio.")

def delete_servicio_service(db: Session, *, servicio_id: int) -> ServicioDefinicion:
    """
    Elimina una definición de servicio.
    """
    logger.warning(f"Servicio: Intentando eliminar ServicioDefinicion ID: {servicio_id}")
    db_servicio = get_servicio_by_id_service(db=db, servicio_id=servicio_id) # Maneja 404
    try:
        deleted_servicio = service_repository.delete_servicio(db=db, servicio_id=servicio_id)
        return deleted_servicio # type: ignore
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de Integridad al eliminar ServicioDefinicion ID {servicio_id}. Probablemente referenciado por Fórmulas o Líneas de Proforma: {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"No se puede eliminar la definición de servicio ID {servicio_id} porque está en uso (ej: en fórmulas o proformas existentes)."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al eliminar ServicioDefinicion ID {servicio_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar definición de servicio.")