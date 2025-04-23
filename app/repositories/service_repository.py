# app/repositories/service_repository.py
import logging
from typing import Optional, Sequence, Dict, Any

from sqlmodel import Session, select, SQLModel
from sqlalchemy.exc import IntegrityError

# Importar Modelo
from app.models.service_models import ServicioDefinicion

logger = logging.getLogger(__name__)

# =======================================
# Repositorio para ServicioDefinicion
# =======================================

def get_servicio_by_id(db: Session, *, servicio_id: int) -> Optional[ServicioDefinicion]:
    """Obtiene una definición de servicio por su ID."""
    try:
        return db.get(ServicioDefinicion, servicio_id)
    except Exception as e:
        logger.error(f"Error obteniendo ServicioDefinicion ID {servicio_id}: {e}", exc_info=True)
        raise

def get_servicio_by_nombre(db: Session, *, nombre: str) -> Optional[ServicioDefinicion]:
    """Obtiene una definición de servicio por su nombre (asumiendo unicidad)."""
    # Nota: La BD no tiene constraint UNIQUE para nombre, pero la lógica de negocio podría requerirla.
    try:
        statement = select(ServicioDefinicion).where(ServicioDefinicion.nombre == nombre)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo ServicioDefinicion nombre '{nombre}': {e}", exc_info=True)
        raise

def list_servicios(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[ServicioDefinicion]:
    """Lista las definiciones de servicios."""
    try:
        statement = select(ServicioDefinicion).offset(skip).limit(limit).order_by(ServicioDefinicion.id)
        return db.exec(statement).all()
    except Exception as e:
        logger.error(f"Error listando ServicioDefinicion: {e}", exc_info=True)
        raise

def create_servicio(db: Session, *, servicio_data: ServicioDefinicion) -> ServicioDefinicion:
    """Crea una nueva definición de servicio."""
    db_servicio = servicio_data
    try:
        db.add(db_servicio)
        db.commit()
        db.refresh(db_servicio)
        logger.info(f"ServicioDefinicion creado: ID={db_servicio.id}, Nombre='{db_servicio.nombre}'")
        return db_servicio
    except IntegrityError as e: # Podría ocurrir si se añade UNIQUE(nombre) en el futuro
        db.rollback()
        logger.warning(f"Error de integridad al crear ServicioDefinicion Nombre '{db_servicio.nombre}': {e}")
        raise e # Relanzar para que el servicio maneje (ej: 409 si nombre debe ser único)
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado creando ServicioDefinicion '{db_servicio.nombre}': {e}", exc_info=True)
        raise

def update_servicio(db: Session, *, db_servicio: ServicioDefinicion, update_data: Dict[str, Any]) -> ServicioDefinicion:
    """Actualiza una definición de servicio."""
    try:
        if not update_data: return db_servicio # Nada que actualizar
        db_servicio.sqlmodel_update(update_data)
        db.add(db_servicio)
        db.commit()
        db.refresh(db_servicio)
        logger.info(f"ServicioDefinicion actualizado: ID={db_servicio.id}")
        return db_servicio
    except IntegrityError as e: # Si se hace UNIQUE(nombre) y se intenta duplicar
        db.rollback()
        logger.warning(f"Error de integridad al actualizar ServicioDefinicion ID {db_servicio.id}: {e}")
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado actualizando ServicioDefinicion ID {db_servicio.id}: {e}", exc_info=True)
        raise

def delete_servicio(db: Session, *, servicio_id: int) -> Optional[ServicioDefinicion]:
    """Elimina una definición de servicio."""
    try:
        db_servicio = db.get(ServicioDefinicion, servicio_id)
        if not db_servicio: return None
        logger.warning(f"Intentando eliminar ServicioDefinicion: ID={servicio_id}, Nombre='{db_servicio.nombre}'")
        db.delete(db_servicio)
        db.commit()
        logger.warning(f"ServicioDefinicion eliminado: ID={servicio_id}")
        return db_servicio
    except IntegrityError as e: # Fallará si está referenciado por Formula o LineaProformaServicio (ON DELETE RESTRICT)
        db.rollback()
        logger.error(f"Error de integridad al eliminar ServicioDefinicion ID {servicio_id}. Probablemente referenciado: {e}")
        raise e # Relanzar para que el servicio maneje (409)
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado eliminando ServicioDefinicion ID {servicio_id}: {e}", exc_info=True)
        raise