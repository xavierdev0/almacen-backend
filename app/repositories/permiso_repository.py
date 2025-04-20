# app/repositories/permiso_repository.py

import logging
from typing import Optional, Sequence, Union, Dict, Any

from sqlmodel import Session, select, SQLModel
from sqlalchemy.exc import IntegrityError # Para capturar errores de constraints únicos
from fastapi import HTTPException, status

# Importamos los modelos y schemas necesarios
from app.models import Permiso
from app.schemas.rol_permiso_schema import PermisoCreate, PermisoUpdate

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read (Getters)
# =====================

def get_permiso(db: Session, permiso_id: int) -> Optional[Permiso]:
    """
    Obtiene un permiso específico por su ID utilizando db.get().

    Args:
        db: La sesión de base de datos activa.
        permiso_id: El ID del permiso a buscar.

    Returns:
        El objeto Permiso si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        # db.get es eficiente para buscar por clave primaria
        return db.get(Permiso, permiso_id)
    except Exception as e:
        logger.error(f"Error obteniendo permiso ID {permiso_id}: {e}", exc_info=True)
        raise

def get_permiso_by_accion_recurso(
    db: Session, *, nombre_accion: str, nombre_recurso: str
) -> Optional[Permiso]:
    """
    Obtiene un permiso por su combinación única de acción y recurso.

    Esta combinación actúa como una clave natural y debe ser única según
    el constraint de la base de datos.

    Args:
        db: La sesión de base de datos activa.
        nombre_accion: El nombre de la acción del permiso.
        nombre_recurso: El nombre del recurso del permiso.

    Returns:
        El objeto Permiso si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
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
    """
    Obtiene una lista paginada de todos los permisos.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de permisos a saltar (para paginación).
        limit: Número máximo de permisos a devolver (para paginación).

    Returns:
        Una secuencia (lista) de objetos Permiso.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Permiso).offset(skip).limit(limit)
        return db.exec(statement).all()
    except Exception as e:
        logger.error(f"Error listando permisos: {e}", exc_info=True)
        raise

# =====================
#  Funciones Write (Create, Update, Delete)
# =====================

def create_permiso(db: Session, *, permiso_in: PermisoCreate) -> Permiso:
    """
    Crea un nuevo permiso en la base de datos.

    Valida los datos de entrada y maneja posibles errores de integridad,
    específicamente para la combinación duplicada de acción/recurso.

    Args:
        db: La sesión de base de datos activa.
        permiso_in: Objeto PermisoCreate con los datos del permiso a crear.

    Returns:
        El objeto Permiso recién creado y refrescado desde la base de datos.

    Raises:
        HTTPException: 409 (Conflict) si ya existe un permiso con la misma
                       combinación de acción y recurso.
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    try:
        db_permiso = Permiso.model_validate(permiso_in)
        db.add(db_permiso)
        db.commit()
        db.refresh(db_permiso)
        logger.info(f"Permiso creado: ID={db_permiso.id}, Accion={db_permiso.nombre_accion}, Recurso={db_permiso.nombre_recurso}")
        return db_permiso
    except IntegrityError as e: # Captura error si el constraint único de (accion, recurso) falla
        db.rollback()
        logger.warning(
            f"Intento de crear permiso duplicado: "
            f"Accion='{permiso_in.nombre_accion}', Recurso='{permiso_in.nombre_recurso}'. Error: {e}"
        )
        # Lanza una excepción HTTP específica para que el servicio la maneje.
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El permiso '{permiso_in.nombre_accion}:{permiso_in.nombre_recurso}' ya existe."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando permiso: {e}", exc_info=True)
        raise # Relanza otras excepciones

def update_permiso(
    db: Session, *, db_permiso: Permiso, permiso_in: Union[PermisoUpdate, Dict[str, Any]]
) -> Permiso:
    """
    Actualiza un permiso existente en la base de datos.

    Aplica los cambios utilizando `sqlmodel_update` y maneja posibles
    errores de integridad si la actualización resulta en una combinación
    duplicada de acción/recurso.

    Args:
        db: La sesión de base de datos activa.
        db_permiso: El objeto Permiso existente que se va a actualizar.
        permiso_in: Un objeto PermisoUpdate o un diccionario con los datos a actualizar.
                    Se recomienda usar PermisoUpdate con `exclude_unset=True` en el servicio.

    Returns:
        El objeto Permiso actualizado y refrescado desde la base de datos.

    Raises:
        HTTPException: 409 (Conflict) si la actualización causa un conflicto de
                       acción/recurso duplicado.
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    try:
        if isinstance(permiso_in, dict):
            update_data = permiso_in
        else:
            # Se asume que en el servicio se llamó con exclude_unset=True
            update_data = permiso_in.model_dump(exclude_unset=True)

        # Actualizar el objeto modelo con los nuevos datos
        db_permiso.sqlmodel_update(update_data)

        db.add(db_permiso) # Añadir a la sesión para marcarlo como modificado antes del commit
        db.commit()
        db.refresh(db_permiso)
        logger.info(f"Permiso actualizado: ID={db_permiso.id}")
        return db_permiso
    except IntegrityError as e: # Captura error si el cambio viola el constraint único (accion, recurso)
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
        raise # Relanza otras excepciones


def delete_permiso(db: Session, *, db_permiso: Permiso) -> Permiso:
    """
    Elimina un permiso de la base de datos.

    Aprovecha la configuración `ON DELETE CASCADE` de la llave foránea en la
    tabla `rol_permiso` (asociación Rol-Permiso) para que la base de datos
    elimine automáticamente las asociaciones existentes. No realiza
    verificaciones explícitas de dependencias en este código.

    Args:
        db: La sesión de base de datos activa.
        db_permiso: El objeto Permiso a eliminar.

    Returns:
        El objeto Permiso que fue eliminado (desvinculado de la sesión).

    Raises:
        HTTPException: 500 (Internal Server Error) si ocurre un error inesperado
                       durante la eliminación. (Un error de FK sería inesperado aquí).
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    permiso_id = db_permiso.id
    permiso_repr = f"'{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' (ID: {permiso_id})"
    logger.info(f"Intentando eliminar permiso: {permiso_repr}")
    try:
        # Opcional: Si se quisiera PREVENIR la eliminación de permisos en uso activamente
        # (en lugar de confiar/permitir la cascada), se podría añadir aquí una consulta
        # a 'rol_permiso' contando las filas con este permiso_id. Si count > 0,
        # se lanzaría un HTTPException 409 CONFLICT.
        # Ejemplo: count_statement = select(func.count(RolPermiso.rol_id)).where(RolPermiso.permiso_id == permiso_id)
        #          count = db.exec(count_statement).scalar_one()
        #          if count > 0: raise HTTPException(status_code=409, detail="Permiso en uso")

        db.delete(db_permiso)
        db.commit()
        logger.info(f"Permiso eliminado exitosamente: {permiso_repr}")
        # El objeto devuelto está desvinculado de la sesión después del commit/delete.
        return db_permiso
    except Exception as e:
        db.rollback()
        # Un error aquí sería inesperado dado el ON DELETE CASCADE asumido.
        # Podría indicar un problema de configuración, de conexión, locks, etc.
        logger.error(f"Error inesperado eliminando permiso {permiso_repr}: {e}", exc_info=True)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error interno del servidor al intentar eliminar el permiso {permiso_repr}."
            )