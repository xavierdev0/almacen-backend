# app/repositories/permiso_repository.py

import logging
from typing import Optional, Sequence, Union, Dict, Any

from sqlmodel import Session, select, SQLModel
from sqlalchemy.exc import IntegrityError # Para capturar errores de duplicados
from fastapi import HTTPException, status

# Importamos los modelos y schemas necesarios
from app.models import Permiso
from app.schemas.rol_permiso_schema import PermisoCreate, PermisoUpdate

logger = logging.getLogger(__name__)

def get_permiso(db: Session, permiso_id: int) -> Optional[Permiso]:
    """Obtiene un permiso por su ID."""
    try:
        return db.get(Permiso, permiso_id)
    except Exception as e:
        logger.error(f"Error obteniendo permiso ID {permiso_id}: {e}", exc_info=True)
        raise

def get_permiso_by_accion_recurso(
    db: Session, *, nombre_accion: str, nombre_recurso: str
) -> Optional[Permiso]:
    """Obtiene un permiso por su combinación única de acción y recurso."""
    try:
        statement = select(Permiso).where(
            Permiso.nombre_accion == nombre_accion,
            Permiso.nombre_recurso == nombre_recurso
        )
        return db.exec(statement).first()
    except Exception as e:
        logger.error(
            f"Error obteniendo permiso por accion='{nombre_accion}', recurso='{nombre_recurso}': {e}",
            exc_info=True
        )
        raise

def list_permisos(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Permiso]:
    """Lista todos los permisos con paginación."""
    try:
        statement = select(Permiso).offset(skip).limit(limit)
        return db.exec(statement).all()
    except Exception as e:
        logger.error(f"Error listando permisos: {e}", exc_info=True)
        raise

def create_permiso(db: Session, *, permiso_in: PermisoCreate) -> Permiso:
    """Crea un nuevo permiso."""
    try:
        # Crear instancia del modelo desde el schema
        db_permiso = Permiso.model_validate(permiso_in)
        # Alternativa si PermisoCreate no es SQLModel:
        # db_permiso = Permiso(**permiso_in.model_dump())

        db.add(db_permiso)
        db.commit()
        db.refresh(db_permiso)
        logger.info(f"Permiso creado: ID={db_permiso.id}, Accion={db_permiso.nombre_accion}, Recurso={db_permiso.nombre_recurso}")
        return db_permiso
    except IntegrityError as e: # Captura error si la tupla accion/recurso ya existe
        db.rollback()
        logger.warning(
            f"Intento de crear permiso duplicado: "
            f"Accion='{permiso_in.nombre_accion}', Recurso='{permiso_in.nombre_recurso}'. Error: {e}"
        )
        # Lanza un HTTP Exception que el servicio/endpoint puede manejar
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El permiso '{permiso_in.nombre_accion}:{permiso_in.nombre_recurso}' ya existe."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando permiso: {e}", exc_info=True)
        raise

def update_permiso(
    db: Session, *, db_permiso: Permiso, permiso_in: Union[PermisoUpdate, Dict[str, Any]]
) -> Permiso:
    """Actualiza un permiso existente."""
    try:
        if isinstance(permiso_in, dict):
            update_data = permiso_in
        else:
            # Excluir valores no establecidos para actualización parcial
            update_data = permiso_in.model_dump(exclude_unset=True)

        # Actualizar el objeto modelo con los nuevos datos
        db_permiso.sqlmodel_update(update_data)
        # Alternativa si db_permiso no es SQLModel o para más control:
        # for key, value in update_data.items():
        #     setattr(db_permiso, key, value)

        db.add(db_permiso) # Añadir a la sesión para marcarlo como 'dirty'
        db.commit()
        db.refresh(db_permiso)
        logger.info(f"Permiso actualizado: ID={db_permiso.id}")
        return db_permiso
    except IntegrityError as e: # Captura error si se intenta cambiar a una tupla accion/recurso que ya existe
         db.rollback()
         logger.warning(
             f"Error de integridad actualizando permiso ID {db_permiso.id}. ¿Conflicto accion/recurso? Error: {e}"
         )
         raise HTTPException(
             status_code=status.HTTP_409_CONFLICT,
             detail="Conflicto al actualizar el permiso, la combinación acción/recurso ya podría existir."
         )
    except Exception as e:
        db.rollback()
        logger.error(f"Error actualizando permiso ID {db_permiso.id}: {e}", exc_info=True)
        raise
# app/repositories/permiso_repository.py
# ... (imports)

def delete_permiso(db: Session, *, db_permiso: Permiso) -> Permiso:
    """
    Elimina un permiso de la base de datos.

    NOTA: La tabla 'rol_permiso' tiene definida la restricción
    FOREIGN KEY (permiso_id) REFERENCES permiso(id) ON DELETE CASCADE.
    Esto significa que la base de datos eliminará automáticamente cualquier
    asociación existente entre este permiso y los roles al eliminar el permiso.
    No se requiere una verificación explícita de dependencias en 'rol_permiso'
    en este código para prevenir errores de FK.
    """
    permiso_id = db_permiso.id # Guardar ID para log
    permiso_repr = f"'{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' (ID: {permiso_id})" # Para logs/errores
    logger.info(f"Intentando eliminar permiso: {permiso_repr}")
    try:
        # Opcional: Si se quisiera PREVENIR la eliminación de permisos en uso
        # (en lugar de permitir la cascada), aquí se añadiría una consulta
        # a 'rol_permiso' y se lanzaría un HTTPException 409 CONFLICT si hay > 0 asociaciones.

        db.delete(db_permiso)
        db.commit()
        logger.info(f"Permiso eliminado exitosamente: {permiso_repr}")
        return db_permiso # Devolver el objeto eliminado (desvinculado de la sesión)
    except Exception as e:
        db.rollback()
        # Un error aquí sería inesperado debido al CASCADE,
        # podría ser otro tipo de problema (conexión, lock, etc.)
        logger.error(f"Error inesperado eliminando permiso {permiso_repr}: {e}", exc_info=True)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error interno del servidor al intentar eliminar el permiso {permiso_repr}."
            )