# app/repositories/rol_repository.py

import logging
from typing import Optional, Sequence

from sqlmodel import Session, select

# Importa el modelo Rol desde la ubicación centralizada
from app.models import Rol

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

# Podrías añadir funciones create_rol, update_rol, delete_rol si son necesarias
# para una gestión completa de roles por parte de un administrador.