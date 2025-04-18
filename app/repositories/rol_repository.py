# app/repositories/rol_repository.py

import logging
from typing import Optional, Sequence, Union, Dict, Any, List
import sqlalchemy as sa

from sqlmodel import Session, select, SQLModel

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from sqlalchemy.orm import selectinload

from app.models import Rol, UsuarioRol
from app.schemas.rol_permiso_schema import RolCreate, RolUpdate

logger = logging.getLogger(__name__)

def get_rol_by_name(db: Session, *, nombre: str) -> Optional[Rol]:
    """
    Obtiene un rol específico por su nombre.

    Args:
        db: La sesión de base de datos.
        nombre: El nombre exacto del rol a buscar.

    Returns:
        El objeto Rol si se encuentra, None en caso contrario.
    """
    try:
        statement = select(Rol).where(Rol.nombre == nombre)
        rol = db.exec(statement).first()
        return rol
    except Exception as e:
        logger.error(f"Error obteniendo rol por nombre '{nombre}': {e}", exc_info=True)
        # Podrías relanzar una excepción personalizada o simplemente devolver None/relanzar e
        raise

def get_rol(db: Session, *, rol_id: int) -> Optional[Rol]:
    """
    Obtiene un rol específico por su ID.

    Args:
        db: La sesión de base de datos.
        rol_id: El ID del rol a buscar.

    Returns:
        El objeto Rol si se encuentra, None en caso contrario.
    """
    try:
        rol = db.get(Rol, rol_id)
        return rol
    except Exception as e:
        logger.error(f"Error obteniendo rol por ID '{rol_id}': {e}", exc_info=True)
        raise


def get_rol_with_permissions(db: Session, *, rol_id: int) -> Optional[Rol]:
    """
    Obtiene un rol específico por su ID, cargando eager la relación de permisos.
    """
    try:
        statement = select(Rol).where(Rol.id == rol_id).options(
            selectinload(Rol.permisos) # Carga Eager de la relación 'permisos'
        )
        rol = db.exec(statement).first()
        return rol
    except Exception as e:
        logger.error(f"Error obteniendo rol ID '{rol_id}' con permisos: {e}", exc_info=True)
        raise

def list_roles(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[Rol]:
    """
    Obtiene una lista paginada de roles.

    Args:
        db: La sesión de base de datos.
        skip: Número de roles a saltar.
        limit: Número máximo de roles a devolver.

    Returns:
        Una secuencia de objetos Rol.
    """
    try:
        statement = select(Rol).offset(skip).limit(limit)
        roles = db.exec(statement).all()
        return roles
    except Exception as e:
        logger.error(f"Error listando roles: {e}", exc_info=True)
        raise

def create_rol(db: Session, *, rol_in: RolCreate) -> Rol:
    """Crea un nuevo rol."""
    try:
        db_rol = Rol.model_validate(rol_in)
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        logger.info(f"Rol creado: ID={db_rol.id}, Nombre='{db_rol.nombre}'")
        return db_rol
    except IntegrityError as e: # Captura error si el nombre ya existe
        db.rollback()
        logger.warning(f"Intento de crear rol duplicado: Nombre='{rol_in.nombre}'. Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El rol '{rol_in.nombre}' ya existe."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando rol: {e}", exc_info=True)
        raise

def update_rol(
    db: Session, *, db_rol: Rol, rol_in: Union[RolUpdate, Dict[str, Any]]
) -> Rol:
    """Actualiza un rol existente."""
    try:
        if isinstance(rol_in, dict):
            update_data = rol_in
        else:
            update_data = rol_in.model_dump(exclude_unset=True)

        db_rol.sqlmodel_update(update_data)
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        logger.info(f"Rol actualizado: ID={db_rol.id}, Nombre='{db_rol.nombre}'")
        return db_rol
    except IntegrityError as e: # Captura error si se intenta cambiar a un nombre que ya existe
         db.rollback()
         logger.warning(
             f"Error de integridad actualizando rol ID {db_rol.id}. ¿Conflicto de nombre? Error: {e}"
         )
         raise HTTPException(
             status_code=status.HTTP_409_CONFLICT,
             detail="Conflicto al actualizar el rol, el nombre ya podría existir."
         )
    except Exception as e:
        db.rollback()
        logger.error(f"Error actualizando rol ID {db_rol.id}: {e}", exc_info=True)
        raise

def delete_rol(db: Session, *, db_rol: Rol) -> Rol:
    """Elimina un rol."""
    rol_id = db_rol.id
    rol_nombre = db_rol.nombre
    try:
        # Verificar si hay usuarios con este rol antes de eliminar
        # Contamos las asociaciones en UsuarioRol
        statement = select(sa.func.count(UsuarioRol.usuario_id)).where(UsuarioRol.rol_id == rol_id)
        user_count = db.exec(statement).first() # Puede ser 0 o None si no hay

        if user_count is not None and user_count > 0:
            logger.warning(f"Intento de eliminar rol ID {rol_id} ('{rol_nombre}') que está asignado a {user_count} usuario(s).")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"No se puede eliminar el rol '{rol_nombre}' porque está asignado a {user_count} usuario(s)."
            )
        # Si no hay usuarios, proceder a eliminar
        # Nota: La relación RolPermiso tiene ON DELETE CASCADE en el SQL,
        # así que no necesitamos eliminar manualmente esas asociaciones.
        db.delete(db_rol)
        db.commit()
        logger.info(f"Rol eliminado: ID={rol_id}, Nombre='{rol_nombre}'")
        return db_rol # Devolver el objeto eliminado
    except HTTPException: # Relanzar el 409
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error eliminando rol ID {rol_id}: {e}", exc_info=True)
        # Podría haber otros errores de FK si otras tablas referencian Rol sin ON DELETE
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al intentar eliminar el rol '{rol_nombre}'."
        )


def get_roles_by_ids(db: Session, *, role_ids: List[int]) -> Sequence[Rol]:
    """
    Obtiene una secuencia de objetos Rol basada en una lista de IDs.

    Args:
        db: Sesión de base de datos.
        role_ids: Lista de IDs de roles a buscar.

    Returns:
        Una secuencia de objetos Rol encontrados. Puede estar vacía si ningún ID es válido.
    """
    if not role_ids:
        return [] # Devolver lista vacía si no se proporcionan IDs
    try:
        # Usamos 'in_' para buscar múltiples IDs
        statement = select(Rol).where(Rol.id.in_(role_ids))
        roles = db.exec(statement).all()
        return roles
    except Exception as e:
        logger.error(f"Error obteniendo roles por IDs ({role_ids}): {e}", exc_info=True)
        raise # Relanzar para que el servicio maneje