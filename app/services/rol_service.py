# app/services/rol_service.py

import logging
from typing import Optional, Sequence, List

from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.orm import selectinload

# Importar repositorios y modelos
from app.repositories import rol_repository # Ya importado
# Añadir permiso_repository para buscar permisos si es necesario directamente
from app.repositories import permiso_repository
from app.models import Rol, Permiso # Importar Permiso también
# Importar schemas
from app.schemas.rol_permiso_schema import (
    RolCreate, RolUpdate, RolRead, RolReadWithPermissions, PermisoRead
)
# Importar el servicio de permisos para buscar permisos
from app.services import permiso_service


logger = logging.getLogger(__name__)

def create_new_rol(db: Session, *, rol_in: RolCreate) -> Rol:
    """
    Crea un nuevo rol, validando duplicados a través del repositorio.

    Args:
        db: Sesión de base de datos.
        rol_in: Datos del rol a crear.

    Returns:
        El objeto Rol creado.

    Raises:
        HTTPException: Si el rol ya existe (409) o error interno (500).
    """
    logger.info(f"Intentando crear rol: Nombre='{rol_in.nombre}'")
    # Validación de duplicado (IntegrityError -> 409) manejada en el repo
    try:
        rol = rol_repository.create_rol(db=db, rol_in=rol_in)
        return rol
    except HTTPException:
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
    Obtiene un rol por su ID, opcionalmente cargando sus permisos
    delegando la carga de datos al repositorio.
    """
    logger.debug(f"Buscando rol con ID: {rol_id}, incluir permisos: {include_permissions}")

    # Llamar a la función de repositorio adecuada
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

    # Puedes mantener este log si quieres verificar que la carga funcionó
    if include_permissions and rol.permisos is not None:
         logger.debug(f"Permisos cargados para Rol ID {rol_id} vía repositorio: {len(rol.permisos)}")
    elif include_permissions:
         logger.debug(f"Se solicitó incluir permisos para Rol ID {rol_id}, pero la relación 'permisos' no está cargada/vacía.")

    return rol


def get_all_roles(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Rol]:
    """
    Obtiene una lista paginada de todos los roles.
    Nota: Por defecto, no carga los permisos asociados para eficiencia.

    Args:
        db: Sesión de base de datos.
        skip: Número de registros a saltar.
        limit: Número máximo de registros a devolver.

    Returns:
        Una secuencia de objetos Rol.
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

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol a actualizar.
        rol_in: Datos con los campos a actualizar.

    Returns:
        El objeto Rol actualizado.

    Raises:
        HTTPException: Si no se encuentra (404), hay conflicto de nombre (409) o error interno (500).
    """
    logger.info(f"Intentando actualizar rol ID: {rol_id}")
    # Usamos include_permissions=False ya que no necesitamos los permisos para actualizar el rol en sí
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)

    update_data = rol_in.model_dump(exclude_unset=True)

    # Verificar si el nombre está cambiando y si ya existe
    new_name = update_data.get("nombre")
    if new_name is not None and new_name != db_rol.nombre:
        existing_rol = rol_repository.get_rol_by_name(db=db, nombre=new_name)
        if existing_rol and existing_rol.id != rol_id:
             logger.warning(f"Conflicto al actualizar rol ID {rol_id}: El nombre '{new_name}' ya existe (ID: {existing_rol.id}).")
             raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"El nombre de rol '{new_name}' ya está en uso."
                )

    # La validación de duplicado/conflicto también se maneja en el repo al hacer commit
    try:
        updated_rol = rol_repository.update_rol(
            db=db, db_rol=db_rol, rol_in=update_data
        )
        return updated_rol
    except HTTPException: # Relanzar 409 del repo
         raise
    except Exception as e:
        logger.error(f"Error inesperado al actualizar rol ID {rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al actualizar el rol ID {rol_id}."
        )

def delete_existing_rol(db: Session, *, rol_id: int) -> Rol:
    """
    Elimina un rol existente. Verifica dependencias en el repositorio.

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol a eliminar.

    Returns:
        El objeto Rol eliminado.

    Raises:
        HTTPException: Si no se encuentra (404), está en uso (409) o error interno (500).
    """
    logger.info(f"Intentando eliminar rol ID: {rol_id}")
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False) # No necesitamos permisos aquí

    try:
        # La lógica de verificar si el rol está asignado a usuarios ya está en el repositorio
        deleted_rol = rol_repository.delete_rol(db=db, db_rol=db_rol)
        return deleted_rol
    except HTTPException: # Relanzar 409 del repo si está en uso
        raise
    except Exception as e:
        logger.error(f"Error inesperado al eliminar rol ID {rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al eliminar el rol ID {rol_id}."
        )



def add_permission_to_role(db: Session, *, rol_id: int, permiso_id: int) -> Rol:
    """
    Asigna un permiso existente a un rol existente.

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol al que se asignará el permiso.
        permiso_id: ID del permiso a asignar.

    Returns:
        El objeto Rol actualizado con la relación de permisos (potencialmente) actualizada.

    Raises:
        HTTPException: 404 si el rol o el permiso no existen,
                       409 si el permiso ya está asignado al rol,
                       500 si ocurre un error interno.
    """
    logger.info(f"Intentando asignar permiso ID={permiso_id} a rol ID={rol_id}")
    # Obtener el rol, asegurando cargar los permisos para verificar si ya existe la asociación
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=True)

    # Obtener el permiso
    db_permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id) # Maneja 404 para permiso

    # Verificar si el permiso ya está en la lista de permisos del rol
    # Comparamos por ID para estar seguros
    if db_permiso.id in [p.id for p in db_rol.permisos]:
        logger.warning(f"El permiso ID={permiso_id} ya está asignado al rol ID={rol_id}.")
        # Devolver el rol sin cambios o lanzar un error de conflicto
        # Lanzar 409 es más explícito para la API
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El permiso '{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' ya está asignado al rol '{db_rol.nombre}'."
        )

    # Añadir el permiso a la relación (SQLAlchemy maneja la tabla de enlace)
    try:
        db_rol.permisos.append(db_permiso)
        db.add(db_rol)
        db.commit()
        # Refrescar para asegurar que el estado de la sesión refleje la DB
        # especialmente útil si se devuelve RolReadWithPermissions
        db.refresh(db_rol)
        # Cargar explícitamente la relación después del commit si es necesario
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

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol del que se quitará el permiso.
        permiso_id: ID del permiso a quitar.

    Returns:
        El objeto Rol actualizado.

    Raises:
        HTTPException: 404 si el rol o el permiso no existen,
                       404 si el permiso no está actualmente asignado a ese rol,
                       500 si ocurre un error interno.
    """
    logger.info(f"Intentando quitar permiso ID={permiso_id} del rol ID={rol_id}")
    # Obtener el rol, asegurando cargar los permisos para verificar la asociación
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=True)

    # Obtener el permiso (solo para verificar que existe y para logs/mensajes)
    db_permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id)

    # Verificar si el permiso está realmente asignado a este rol
    permiso_encontrado = None
    for p in db_rol.permisos:
        if p.id == permiso_id:
            permiso_encontrado = p
            break

    if permiso_encontrado is None:
        logger.warning(f"Intento de quitar permiso ID={permiso_id} del rol ID={rol_id}, pero no estaba asignado.")
        # Usar 404 es apropiado: la asociación específica no existe
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El permiso '{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' no está asignado al rol '{db_rol.nombre}'."
        )

    # Quitar el permiso de la relación (SQLAlchemy maneja la tabla de enlace)
    try:
        db_rol.permisos.remove(permiso_encontrado)
        db.add(db_rol)
        db.commit()
        # Refrescar para asegurar que el estado de la sesión refleje la DB
        db.refresh(db_rol)
        db.refresh(db_rol, attribute_names=["permisos"]) # Asegurar que la lista se actualice
        logger.info(f"Permiso ID={permiso_id} quitado exitosamente del rol ID={rol_id}.")
        return db_rol
    except Exception as e:
        db.rollback()
        logger.error(f"Error quitando permiso ID={permiso_id} de rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al quitar el permiso del rol."
        )

