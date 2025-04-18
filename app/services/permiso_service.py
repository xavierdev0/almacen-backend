# app/services/permiso_service.py

import logging
from typing import Optional, Sequence

from fastapi import HTTPException, status
from sqlmodel import Session

from app.repositories import permiso_repository
from app.models import Permiso # Importar el modelo
from app.schemas.rol_permiso_schema import PermisoCreate, PermisoUpdate

logger = logging.getLogger(__name__)

def create_new_permiso(db: Session, *, permiso_in: PermisoCreate) -> Permiso:
    """
    Crea un nuevo permiso, validando duplicados a través del repositorio.

    Args:
        db: Sesión de base de datos.
        permiso_in: Datos del permiso a crear.

    Returns:
        El objeto Permiso creado.

    Raises:
        HTTPException: Si el permiso ya existe (409) o error interno (500).
    """
    logger.info(f"Intentando crear permiso: {permiso_in.nombre_accion}:{permiso_in.nombre_recurso}")
    # La validación de duplicado (IntegrityError -> HTTPException 409)
    # ya se maneja en permiso_repository.create_permiso
    try:
        permiso = permiso_repository.create_permiso(db=db, permiso_in=permiso_in)
        return permiso
    except HTTPException: # Relanzar excepciones HTTP (ej: 409 del repo)
         raise
    except Exception as e:
        logger.error(f"Error inesperado al crear permiso: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el permiso."
        )

def get_permiso_by_id(db: Session, *, permiso_id: int) -> Permiso:
    """
    Obtiene un permiso por su ID.

    Args:
        db: Sesión de base de datos.
        permiso_id: ID del permiso a buscar.

    Returns:
        El objeto Permiso encontrado.

    Raises:
        HTTPException: Si el permiso no se encuentra (404).
    """
    logger.debug(f"Buscando permiso con ID: {permiso_id}")
    permiso = permiso_repository.get_permiso(db=db, permiso_id=permiso_id)
    if not permiso:
        logger.warning(f"Permiso con ID {permiso_id} no encontrado.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Permiso con ID {permiso_id} no encontrado."
        )
    return permiso

def get_all_permisos(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Permiso]:
    """
    Obtiene una lista paginada de todos los permisos.

    Args:
        db: Sesión de base de datos.
        skip: Número de registros a saltar.
        limit: Número máximo de registros a devolver.

    Returns:
        Una secuencia de objetos Permiso.
    """
    logger.debug(f"Listando permisos con skip={skip}, limit={limit}")
    try:
        permisos = permiso_repository.list_permisos(db=db, skip=skip, limit=limit)
        return permisos
    except Exception as e:
         logger.error(f"Error inesperado al listar permisos: {e}", exc_info=True)
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Error interno del servidor al listar permisos."
         )

def update_existing_permiso(
    db: Session, *, permiso_id: int, permiso_in: PermisoUpdate
) -> Permiso:
    """
    Actualiza un permiso existente.

    Args:
        db: Sesión de base de datos.
        permiso_id: ID del permiso a actualizar.
        permiso_in: Datos con los campos a actualizar.

    Returns:
        El objeto Permiso actualizado.

    Raises:
        HTTPException: Si no se encuentra (404), hay conflicto (409) o error interno (500).
    """
    logger.info(f"Intentando actualizar permiso ID: {permiso_id}")
    db_permiso = get_permiso_by_id(db=db, permiso_id=permiso_id) # Reutiliza la función (maneja 404)

    update_data = permiso_in.model_dump(exclude_unset=True)

    # Verificar si la combinación acción/recurso está cambiando y si ya existe
    new_action = update_data.get("nombre_accion")
    new_resource = update_data.get("nombre_recurso")
    # Si al menos uno de los dos cambia
    if new_action is not None or new_resource is not None:
        check_action = new_action if new_action is not None else db_permiso.nombre_accion
        check_resource = new_resource if new_resource is not None else db_permiso.nombre_recurso

        # Solo verificar si la combinación resultante es diferente de la actual
        if (check_action != db_permiso.nombre_accion or
            check_resource != db_permiso.nombre_recurso):
            existing = permiso_repository.get_permiso_by_accion_recurso(
                db=db, nombre_accion=check_action, nombre_recurso=check_resource
            )
            if existing and existing.id != permiso_id:
                logger.warning(f"Conflicto al actualizar permiso ID {permiso_id}: "
                               f"La combinación {check_action}:{check_resource} ya existe (ID: {existing.id}).")
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"El permiso '{check_action}:{check_resource}' ya existe."
                )

    # La validación de duplicado/conflicto también se maneja en el repo al hacer commit
    try:
        updated_permiso = permiso_repository.update_permiso(
            db=db, db_permiso=db_permiso, permiso_in=update_data
        )
        return updated_permiso
    except HTTPException: # Relanzar 409 del repo
         raise
    except Exception as e:
        logger.error(f"Error inesperado al actualizar permiso ID {permiso_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al actualizar el permiso ID {permiso_id}."
        )

def delete_existing_permiso(db: Session, *, permiso_id: int) -> Permiso:
    """
    Elimina un permiso existente.

    Args:
        db: Sesión de base de datos.
        permiso_id: ID del permiso a eliminar.

    Returns:
        El objeto Permiso eliminado.

    Raises:
        HTTPException: Si no se encuentra (404) o error interno (500).
    """
    logger.info(f"Intentando eliminar permiso ID: {permiso_id}")
    db_permiso = get_permiso_by_id(db=db, permiso_id=permiso_id) # Reutiliza la función (maneja 404)

    try:
        deleted_permiso = permiso_repository.delete_permiso(db=db, db_permiso=db_permiso)
        # Aquí podríamos añadir lógica si delete_permiso devuelve None en caso de fallo por FK
        return deleted_permiso
    except Exception as e:
        logger.error(f"Error inesperado al eliminar permiso ID {permiso_id}: {e}", exc_info=True)
        # Podríamos verificar si 'e' es por restricción de FK
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al eliminar el permiso ID {permiso_id}."
        )