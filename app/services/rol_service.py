# app/services/rol_service.py

import logging
from typing import Optional, Sequence, List

from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.orm import selectinload

# Importar repositorios y modelos
from app.repositories import rol_repository
from app.repositories import permiso_repository # Import necesario si se usa directamente
from app.models import Rol, Permiso # Importar Permiso también
# Importar schemas
from app.schemas.rol_permiso_schema import (
    RolCreate, RolUpdate, RolRead, RolReadWithPermissions, PermisoRead
)
# Importar el servicio de permisos para buscar permisos
from app.services import permiso_service


logger = logging.getLogger(__name__)

# =====================
#  Gestión de Roles (CRUD)
# =====================

def create_new_rol(db: Session, *, rol_in: RolCreate) -> Rol:
    """
    Crea un nuevo rol, validando duplicados a través del repositorio.

    Args:
        db: Sesión de base de datos.
        rol_in: Datos del rol a crear (esquema RolCreate).

    Returns:
        El objeto Rol creado.

    Raises:
        HTTPException: 409 si el rol ya existe (manejo de IntegrityError del repo).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando crear rol: Nombre='{rol_in.nombre}'")
    # Validación de duplicado (IntegrityError -> 409) manejada en el repo
    try:
        rol = rol_repository.create_rol(db=db, rol_in=rol_in)
        return rol
    except HTTPException: # Re-lanzar excepciones HTTP (ej: 409 del repo)
        raise
    except Exception as e:
        logger.error(f"Error inesperado al crear rol: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el rol."
        )

def get_rol_by_id(
    db: Session, *, rol_id: int, include_permissions: bool = False
) -> Rol:
    """
    Obtiene un rol por su ID, opcionalmente cargando sus permisos asociados.

    Delega la carga de datos al repositorio, seleccionando la función adecuada
    según si se requieren o no los permisos.

    Args:
        db: Sesión de base de datos.
        rol_id: El ID del rol a buscar.
        include_permissions: Si es True, intenta cargar los permisos asociados
                             al rol (usando eager loading en el repositorio).

    Returns:
        El objeto Rol encontrado.

    Raises:
        HTTPException: 404 si el rol con el ID especificado no se encuentra.
    """
    logger.debug(f"Buscando rol con ID: {rol_id}, incluir permisos: {include_permissions}")

    if include_permissions:
        rol = rol_repository.get_rol_with_permissions(db=db, rol_id=rol_id)
    else:
        rol = rol_repository.get_rol(db=db, rol_id=rol_id)

    if not rol:
        logger.warning(f"Rol con ID {rol_id} no encontrado.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rol con ID {rol_id} no encontrado."
        )

    # Log opcional para verificar carga de permisos si se solicitaron
    if include_permissions:
        if rol.permisos is not None:
             logger.debug(f"Permisos cargados para Rol ID {rol_id}: {len(rol.permisos) if isinstance(rol.permisos, list) else 'N/A'}")
        else:
             logger.debug(f"Se solicitó incluir permisos para Rol ID {rol_id}, pero la relación 'permisos' es None o no está cargada.")

    return rol


def get_all_roles(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Rol]:
    """
    Obtiene una lista paginada de todos los roles.

    Por defecto, no carga los permisos asociados para optimizar el rendimiento.
    Delega la consulta al repositorio.

    Args:
        db: Sesión de base de datos.
        skip: Número de registros a saltar (para paginación).
        limit: Número máximo de registros a devolver (para paginación).

    Returns:
        Una secuencia (lista) de objetos Rol.

    Raises:
        HTTPException: 500 si ocurre un error interno inesperado al listar.
    """
    logger.debug(f"Listando roles con skip={skip}, limit={limit}")
    try:
        roles = rol_repository.list_roles(db=db, skip=skip, limit=limit)
        return roles
    except Exception as e:
         logger.error(f"Error inesperado al listar roles: {e}", exc_info=True)
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Error interno del servidor al listar roles."
         )

def update_existing_rol(
    db: Session, *, rol_id: int, rol_in: RolUpdate
) -> Rol:
    """
    Actualiza un rol existente.

    Primero obtiene el rol, luego verifica si el nombre está cambiando y si el
    nuevo nombre ya existe en otro rol. Finalmente, delega la actualización
    al repositorio.

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol a actualizar.
        rol_in: Datos con los campos a actualizar (esquema RolUpdate).

    Returns:
        El objeto Rol actualizado.

    Raises:
        HTTPException: 404 si el rol original no se encuentra.
        HTTPException: 409 si el nuevo nombre ya está en uso por otro rol.
        HTTPException: 409 si el repositorio detecta un conflicto al guardar (IntegrityError).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando actualizar rol ID: {rol_id}")
    # Obtenemos el rol sin permisos, ya que no son necesarios para la actualización básica del rol.
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)

    update_data = rol_in.model_dump(exclude_unset=True)

    # Verificar conflicto de nombre solo si el nombre se está intentando cambiar
    new_name = update_data.get("nombre")
    if new_name is not None and new_name != db_rol.nombre:
        existing_rol = rol_repository.get_rol_by_name(db=db, nombre=new_name)
        if existing_rol and existing_rol.id != rol_id:
             logger.warning(f"Conflicto al actualizar rol ID {rol_id}: El nombre '{new_name}' ya existe (ID: {existing_rol.id}).")
             raise HTTPException(
                 status_code=status.HTTP_409_CONFLICT,
                 detail=f"El nombre de rol '{new_name}' ya está en uso."
             )

    # La validación final de duplicado/conflicto ocurre en el repositorio al hacer commit.
    try:
        updated_rol = rol_repository.update_rol(
            db=db, db_rol=db_rol, rol_in=update_data
        )
        return updated_rol
    except HTTPException: # Re-lanzar 409 del repo
        raise
    except Exception as e:
        logger.error(f"Error inesperado al actualizar rol ID {rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al actualizar el rol ID {rol_id}."
        )

def delete_existing_rol(db: Session, *, rol_id: int) -> Rol:
    """
    Elimina un rol existente.

    Verifica que el rol exista y luego delega la eliminación al repositorio,
    el cual debería verificar si el rol está en uso (asociado a usuarios).

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol a eliminar.

    Returns:
        El objeto Rol que fue eliminado.

    Raises:
        HTTPException: 404 si el rol no se encuentra.
        HTTPException: 409 si el rol está en uso (según la lógica del repositorio).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando eliminar rol ID: {rol_id}")
    # Obtenemos el rol sin permisos, no son necesarios para eliminar.
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)

    try:
        # La lógica de verificar si el rol está asignado a usuarios debe residir en el repositorio.
        deleted_rol = rol_repository.delete_rol(db=db, db_rol=db_rol)
        return deleted_rol
    except HTTPException: # Re-lanzar 409 del repo si está en uso
        raise
    except Exception as e:
        logger.error(f"Error inesperado al eliminar rol ID {rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al eliminar el rol ID {rol_id}."
        )


# =========================
#  Gestión de Permisos-Rol
# =========================

def add_permission_to_role(db: Session, *, rol_id: int, permiso_id: int) -> Rol:
    """
    Asigna un permiso existente a un rol existente.

    Verifica que tanto el rol como el permiso existan.
    Comprueba si el permiso ya está asignado al rol para evitar duplicados.
    Si todo es correcto, añade la relación y guarda los cambios.

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol al que se asignará el permiso.
        permiso_id: ID del permiso a asignar.

    Returns:
        El objeto Rol actualizado, con la relación de permisos reflejando el cambio.

    Raises:
        HTTPException: 404 si el rol o el permiso no existen.
        HTTPException: 409 si el permiso ya está asignado a este rol.
        HTTPException: 500 si ocurre un error interno al asignar.
    """
    logger.info(f"Intentando asignar permiso ID={permiso_id} a rol ID={rol_id}")
    # Obtener el rol, asegurando cargar los permisos para verificar si ya existe la asociación.
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=True)

    # Obtener el permiso (esto ya maneja el 404 si el permiso no existe)
    db_permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id)

    # Verificar si el permiso ya está en la lista de permisos del rol
    if db_permiso in db_rol.permisos: # SQLAlchemy debería poder comparar objetos por identidad
        logger.warning(f"El permiso ID={permiso_id} ya está asignado al rol ID={rol_id}.")
        # Lanzar 409 es más explícito para la API que devolver el objeto sin cambios.
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El permiso '{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' ya está asignado al rol '{db_rol.nombre}'."
        )

    # Añadir el permiso a la relación (SQLAlchemy maneja la tabla de enlace)
    try:
        db_rol.permisos.append(db_permiso)
        db.add(db_rol) # Marcar el rol como modificado
        db.commit()
        # Refrescar el rol para asegurar que el estado refleje la BD,
        # especialmente la colección de permisos actualizada.
        db.refresh(db_rol)
        # Refrescar explícitamente la relación puede ser necesario en algunas configuraciones
        db.refresh(db_rol, attribute_names=["permisos"])
        logger.info(f"Permiso ID={permiso_id} asignado exitosamente a rol ID={rol_id}.")
        return db_rol
    except Exception as e:
        db.rollback()
        logger.error(f"Error asignando permiso ID={permiso_id} a rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al asignar el permiso al rol."
        )


def remove_permission_from_role(db: Session, *, rol_id: int, permiso_id: int) -> Rol:
    """
    Quita un permiso previamente asignado de un rol.

    Verifica que el rol y el permiso existan.
    Comprueba que el permiso esté actualmente asignado al rol.
    Si es así, elimina la relación y guarda los cambios.

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol del que se quitará el permiso.
        permiso_id: ID del permiso a quitar.

    Returns:
        El objeto Rol actualizado, con la relación de permisos reflejando el cambio.

    Raises:
        HTTPException: 404 si el rol o el permiso no existen.
        HTTPException: 404 si el permiso no está actualmente asignado a ese rol.
        HTTPException: 500 si ocurre un error interno al quitar la asignación.
    """
    logger.info(f"Intentando quitar permiso ID={permiso_id} del rol ID={rol_id}")
    # Obtener el rol, asegurando cargar los permisos para verificar la asociación.
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=True)

    # Obtener el permiso (principalmente para verificar existencia y usar en mensajes).
    db_permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id)

    # Verificar si el permiso está realmente asignado a este rol
    if db_permiso not in db_rol.permisos:
        logger.warning(f"Intento de quitar permiso ID={permiso_id} del rol ID={rol_id}, pero no estaba asignado.")
        # Usar 404 es apropiado: la relación específica rol-permiso no existe.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El permiso '{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' no está asignado al rol '{db_rol.nombre}'."
        )

    # Quitar el permiso de la relación (SQLAlchemy maneja la tabla de enlace)
    try:
        db_rol.permisos.remove(db_permiso)
        db.add(db_rol) # Marcar el rol como modificado
        db.commit()
        # Refrescar el rol para asegurar que el estado refleje la BD,
        # especialmente la colección de permisos actualizada.
        db.refresh(db_rol)
        # Refrescar explícitamente la relación
        db.refresh(db_rol, attribute_names=["permisos"])
        logger.info(f"Permiso ID={permiso_id} quitado exitosamente del rol ID={rol_id}.")
        return db_rol
    except Exception as e:
        db.rollback()
        logger.error(f"Error quitando permiso ID={permiso_id} de rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al quitar el permiso del rol."
        )