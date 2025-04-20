# app/services/permiso_service.py

import logging
from typing import Optional, Sequence

from fastapi import HTTPException, status
from sqlmodel import Session

from app.repositories import permiso_repository
from app.models import Permiso # Importar el modelo
from app.schemas.rol_permiso_schema import PermisoCreate, PermisoUpdate

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read (Getters)
# =====================

def get_permiso_by_id(db: Session, *, permiso_id: int) -> Permiso:
    """
    Obtiene un permiso específico por su ID, delegando al repositorio.

    Args:
        db: Sesión de base de datos activa.
        permiso_id: ID del permiso a buscar.

    Returns:
        El objeto Permiso encontrado.

    Raises:
        HTTPException: 404 si el permiso con el ID especificado no se encuentra.
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
    Obtiene una lista paginada de todos los permisos, delegando al repositorio.

    Args:
        db: Sesión de base de datos activa.
        skip: Número de registros a saltar (para paginación).
        limit: Número máximo de registros a devolver (para paginación).

    Returns:
        Una secuencia (lista) de objetos Permiso.

    Raises:
        HTTPException: 500 si ocurre un error interno inesperado al listar.
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

# =====================
#  Funciones Write (Create, Update, Delete)
# =====================

def create_new_permiso(db: Session, *, permiso_in: PermisoCreate) -> Permiso:
    """
    Crea un nuevo permiso, delegando la creación y validación de duplicados al repositorio.

    Args:
        db: Sesión de base de datos activa.
        permiso_in: Datos del permiso a crear (esquema PermisoCreate).

    Returns:
        El objeto Permiso creado.

    Raises:
        HTTPException: 409 si el permiso ya existe (manejo de IntegrityError del repo).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando crear permiso: {permiso_in.nombre_accion}:{permiso_in.nombre_recurso}")
    # La validación de duplicado (IntegrityError -> HTTPException 409)
    # ya se maneja en permiso_repository.create_permiso
    try:
        permiso = permiso_repository.create_permiso(db=db, permiso_in=permiso_in)
        return permiso
    except HTTPException: # Re-lanzar excepciones HTTP (ej: 409 del repo)
        raise
    except Exception as e:
        logger.error(f"Error inesperado al crear permiso: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el permiso."
        )

def update_existing_permiso(
    db: Session, *, permiso_id: int, permiso_in: PermisoUpdate
) -> Permiso:
    """
    Actualiza un permiso existente.

    Primero obtiene el permiso, luego verifica si la combinación acción/recurso
    está cambiando y si la nueva combinación ya existe en otro permiso.
    Finalmente, delega la actualización al repositorio.

    Args:
        db: Sesión de base de datos activa.
        permiso_id: ID del permiso a actualizar.
        permiso_in: Datos con los campos a actualizar (esquema PermisoUpdate).

    Returns:
        El objeto Permiso actualizado.

    Raises:
        HTTPException: 404 si el permiso original no se encuentra.
        HTTPException: 409 si la nueva combinación acción/recurso ya existe en otro permiso.
        HTTPException: 409 si el repositorio detecta un conflicto al guardar (IntegrityError).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando actualizar permiso ID: {permiso_id}")
    # Obtener el permiso existente; esto maneja el caso 404 si no se encuentra.
    db_permiso = get_permiso_by_id(db=db, permiso_id=permiso_id)

    update_data = permiso_in.model_dump(exclude_unset=True)

    # Verificar conflicto de combinación acción/recurso si está cambiando
    new_action = update_data.get("nombre_accion")
    new_resource = update_data.get("nombre_recurso")

    # Solo realizar la verificación si se intenta cambiar la acción o el recurso
    if new_action is not None or new_resource is not None:
        # Determinar la combinación final a verificar
        check_action = new_action if new_action is not None else db_permiso.nombre_accion
        check_resource = new_resource if new_resource is not None else db_permiso.nombre_recurso

        # Solo verificar si la combinación resultante es diferente de la actual
        if (check_action != db_permiso.nombre_accion or
            check_resource != db_permiso.nombre_recurso):
            existing = permiso_repository.get_permiso_by_accion_recurso(
                db=db, nombre_accion=check_action, nombre_recurso=check_resource
            )
            # Si existe otro permiso diferente con esa combinación, hay conflicto
            if existing and existing.id != permiso_id:
                logger.warning(f"Conflicto al actualizar permiso ID {permiso_id}: "
                               f"La combinación {check_action}:{check_resource} ya existe (ID: {existing.id}).")
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"El permiso '{check_action}:{check_resource}' ya existe."
                )

    # La validación final de duplicado/conflicto también ocurre en el repo al hacer commit.
    try:
        updated_permiso = permiso_repository.update_permiso(
            db=db, db_permiso=db_permiso, permiso_in=update_data
        )
        return updated_permiso
    except HTTPException: # Re-lanzar 409 del repo
        raise
    except Exception as e:
        logger.error(f"Error inesperado al actualizar permiso ID {permiso_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al actualizar el permiso ID {permiso_id}."
        )

def delete_existing_permiso(db: Session, *, permiso_id: int) -> Permiso:
    """
    Elimina un permiso existente, delegando al repositorio.

    Primero verifica que el permiso exista. Luego llama al repositorio para
    eliminarlo, confiando en la lógica del repositorio (y la DB) para manejar
    las dependencias (como ON DELETE CASCADE).

    Args:
        db: Sesión de base de datos activa.
        permiso_id: ID del permiso a eliminar.

    Returns:
        El objeto Permiso que fue eliminado.

    Raises:
        HTTPException: 404 si el permiso no se encuentra.
        HTTPException: 500 si ocurre un error interno inesperado durante la eliminación.
    """
    logger.info(f"Intentando eliminar permiso ID: {permiso_id}")
    # Obtener el permiso; esto maneja el caso 404 si no se encuentra.
    db_permiso = get_permiso_by_id(db=db, permiso_id=permiso_id)

    try:
        # Delegar la eliminación al repositorio
        deleted_permiso = permiso_repository.delete_permiso(db=db, db_permiso=db_permiso)
        return deleted_permiso
    except Exception as e:
        # Capturar cualquier excepción durante la eliminación en el repositorio
        logger.error(f"Error inesperado al eliminar permiso ID {permiso_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al eliminar el permiso ID {permiso_id}."
        )