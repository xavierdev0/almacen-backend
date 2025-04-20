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

# =====================
#  Funciones Read (Getters)
# =====================

def get_rol_by_name(db: Session, *, nombre: str) -> Optional[Rol]:
    """
    Obtiene un rol específico por su nombre.

    Args:
        db: La sesión de base de datos activa.
        nombre: El nombre exacto del rol a buscar.

    Returns:
        El objeto Rol si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Rol).where(Rol.nombre == nombre)
        rol = db.exec(statement).first()
        return rol
    except Exception as e:
        logger.error(f"Error obteniendo rol por nombre '{nombre}': {e}", exc_info=True)
        raise

def get_rol(db: Session, *, rol_id: int) -> Optional[Rol]:
    """
    Obtiene un rol específico por su ID utilizando db.get().

    Args:
        db: La sesión de base de datos activa.
        rol_id: El ID del rol a buscar.

    Returns:
        El objeto Rol si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        # db.get es eficiente para buscar por clave primaria
        rol = db.get(Rol, rol_id)
        return rol
    except Exception as e:
        logger.error(f"Error obteniendo rol por ID '{rol_id}': {e}", exc_info=True)
        raise


def get_rol_with_permissions(db: Session, *, rol_id: int) -> Optional[Rol]:
    """
    Obtiene un rol específico por su ID, cargando la relación de permisos.

    Utiliza carga 'eager' (selectinload) para la relación 'permisos' para
    evitar consultas adicionales si se accede a los permisos posteriormente.

    Args:
        db: La sesión de base de datos activa.
        rol_id: El ID del rol a buscar.

    Returns:
        El objeto Rol con sus permisos cargados si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
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
        db: La sesión de base de datos activa.
        skip: Número de roles a saltar (para paginación).
        limit: Número máximo de roles a devolver (para paginación).

    Returns:
        Una secuencia (lista) de objetos Rol.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Rol).offset(skip).limit(limit)
        roles = db.exec(statement).all()
        return roles
    except Exception as e:
        logger.error(f"Error listando roles: {e}", exc_info=True)
        raise

def get_roles_by_ids(db: Session, *, role_ids: List[int]) -> Sequence[Rol]:
    """
    Obtiene una secuencia de objetos Rol basada en una lista de IDs.

    Utiliza una consulta con `IN` para eficiencia.

    Args:
        db: Sesión de base de datos activa.
        role_ids: Lista de IDs de roles a buscar.

    Returns:
        Una secuencia (lista) de objetos Rol encontrados. Puede estar vacía si
        ningún ID es válido o la lista de entrada está vacía.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
                   Permite que el servicio maneje el error.
    """
    if not role_ids:
        return [] # Optimización: no consultar si la lista de IDs está vacía
    try:
        # Usamos 'in_' para buscar eficientemente múltiples IDs
        statement = select(Rol).where(Rol.id.in_(role_ids))
        roles = db.exec(statement).all()
        return roles
    except Exception as e:
        logger.error(f"Error obteniendo roles por IDs ({role_ids}): {e}", exc_info=True)
        raise # Relanzar para que el servicio maneje


# =====================
#  Funciones Write (Create, Update, Delete)
# =====================

def create_rol(db: Session, *, rol_in: RolCreate) -> Rol:
    """
    Crea un nuevo rol en la base de datos.

    Valida los datos de entrada y maneja posibles errores de integridad,
    específicamente para nombres de rol duplicados (constraint único).

    Args:
        db: La sesión de base de datos activa.
        rol_in: Objeto RolCreate con los datos del rol a crear.

    Returns:
        El objeto Rol recién creado y refrescado desde la base de datos.

    Raises:
        HTTPException: 409 (Conflict) si ya existe un rol con el mismo nombre.
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    try:
        db_rol = Rol.model_validate(rol_in)
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        logger.info(f"Rol creado: ID={db_rol.id}, Nombre='{db_rol.nombre}'")
        return db_rol
    except IntegrityError as e: # Captura error si el constraint único del nombre falla
        db.rollback()
        logger.warning(f"Intento de crear rol duplicado: Nombre='{rol_in.nombre}'. Error: {e}")
        # Lanza una excepción HTTP específica para que el servicio la maneje
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El rol '{rol_in.nombre}' ya existe."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando rol: {e}", exc_info=True)
        raise # Relanza otras excepciones para manejo general

def update_rol(
    db: Session, *, db_rol: Rol, rol_in: Union[RolUpdate, Dict[str, Any]]
) -> Rol:
    """
    Actualiza un rol existente en la base de datos.

    Aplica los cambios utilizando `sqlmodel_update` y maneja posibles
    errores de integridad si la actualización resulta en un nombre duplicado.

    Args:
        db: La sesión de base de datos activa.
        db_rol: El objeto Rol existente que se va a actualizar.
        rol_in: Un objeto RolUpdate o un diccionario con los datos a actualizar.
                Se recomienda usar RolUpdate con `exclude_unset=True` en el servicio.

    Returns:
        El objeto Rol actualizado y refrescado desde la base de datos.

    Raises:
        HTTPException: 409 (Conflict) si la actualización causa un conflicto de nombre.
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    try:
        if isinstance(rol_in, dict):
            update_data = rol_in
        else:
            # Se asume que en el servicio se llamó con exclude_unset=True
            update_data = rol_in.model_dump(exclude_unset=True)

        db_rol.sqlmodel_update(update_data)
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        logger.info(f"Rol actualizado: ID={db_rol.id}, Nombre='{db_rol.nombre}'")
        return db_rol
    except IntegrityError as e: # Captura error si el cambio de nombre viola el constraint único
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
        raise # Relanza otras excepciones

def delete_rol(db: Session, *, db_rol: Rol) -> Rol:
    """
    Elimina un rol de la base de datos, verificando dependencias primero.

    Comprueba si el rol está asignado a algún usuario antes de eliminarlo.
    Si está asignado, lanza un error HTTP 409. Asume que las asociaciones
    Rol-Permiso se manejan mediante ON DELETE CASCADE en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        db_rol: El objeto Rol a eliminar.

    Returns:
        El objeto Rol que fue eliminado (útil para logs o respuestas).

    Raises:
        HTTPException: 409 (Conflict) si el rol está asignado a uno o más usuarios.
        HTTPException: 500 (Internal Server Error) si ocurre otro error inesperado
                       durante la eliminación (p.ej., otros FK constraints).
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    rol_id = db_rol.id
    rol_nombre = db_rol.nombre
    try:
        # Contamos las asociaciones en UsuarioRol para verificar si el rol está en uso
        statement = select(sa.func.count(UsuarioRol.usuario_id)).where(UsuarioRol.rol_id == rol_id)
        # .scalar_one() podría ser más directo si esperamos un número
        user_count = db.exec(statement).first() # Devuelve el número o None

        if user_count is not None and user_count > 0:
            logger.warning(f"Intento de eliminar rol ID {rol_id} ('{rol_nombre}') que está asignado a {user_count} usuario(s).")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"No se puede eliminar el rol '{rol_nombre}' porque está asignado a {user_count} usuario(s)."
            )

        # Si user_count es 0 o None, proceder a eliminar
        # Nota: Asumimos ON DELETE CASCADE para la tabla RolPermiso definida en el modelo/DB.
        # No es necesario eliminar manualmente las asociaciones Rol-Permiso aquí.
        db.delete(db_rol)
        db.commit()
        logger.info(f"Rol eliminado: ID={rol_id}, Nombre='{rol_nombre}'")
        return db_rol
    except HTTPException: # Relanzar el 409 generado arriba
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error eliminando rol ID {rol_id}: {e}", exc_info=True)
        # Podría haber otros errores de FK si otras tablas referencian Rol sin ON DELETE CASCADE.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al intentar eliminar el rol '{rol_nombre}'."
        )