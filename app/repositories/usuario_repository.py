# app/repositories/usuario_repository.py
from sqlmodel import Session, select, SQLModel
from typing import Optional, Sequence, Union, Dict, Any
import logging

from app.models.user_models import Usuario, Rol, UsuarioRol
from app.schemas.usuario_schema import UsuarioUpdate
from sqlalchemy.orm import selectinload

logger = logging.getLogger(__name__)

# --- Funciones Read ---
def get_usuario_by_username(db: Session, username: str) -> Optional[Usuario]:
    """Obtiene un usuario por su username."""
    try:
        statement = select(Usuario).where(Usuario.username == username)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo usuario {username}: {str(e)}")
        raise

def get_usuario_by_email(db: Session, email: str) -> Optional[Usuario]:
    """Obtiene un usuario por su email."""
    try:
        statement = select(Usuario).where(Usuario.email == email)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo usuario {email}: {str(e)}")
        raise
    
def get_usuario(db: Session, user_id: int) -> Optional[Usuario]:
    """Obtiene un usuario por su ID."""
    try:
        statement = (
            select(Usuario)
            .where(Usuario.id == user_id)
            .options(selectinload(Usuario.roles)) # <-- AÑADIDO: Carga Eager de roles
        )
        user = db.exec(statement).first()
        return user
    except Exception as e:
        logger.error(f"Error obteniendo usuario ID {user_id}: {str(e)}")
        raise

def get_usuarios(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filters: Optional[Dict[str, Any]] = None
) -> Sequence[Usuario]:
    try:
        query = select(Usuario)
        if filters:
            for field, value in filters.items():
                # Asegurarse que el campo existe en el modelo Usuario
                if hasattr(Usuario, field):
                    query = query.where(getattr(Usuario, field) == value)
                else:
                    logger.warning(f"Intento de filtrar por campo inexistente en Usuario: {field}")
        # Considerar cargar roles aquí también si se listan usuarios con sus roles
        query = query.options(selectinload(Usuario.roles))
        query = query.offset(skip).limit(limit)

        users = db.exec(query).all()
        return users
    
    except Exception as e:
        logger.error(f"Error listando usuarios: {str(e)}")
        raise

# --- Funciones Write ---
def create_usuario(db: Session, usuario_data: Union[Usuario, Dict[str, Any]]) -> Usuario:
    """Crea un nuevo usuario con rollback automático en errores."""
    try:
        if isinstance(usuario_data, dict):
            db_user = Usuario(**usuario_data)
        else:
            db_user = usuario_data
            
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Usuario creado: ID={db_user.id}, Username='{db_user.username}'")
        return db_user
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando usuario: {str(e)}")
        raise

def update_usuario(
    db: Session, 
    *, 
    db_user: Usuario,
    update_data: Union[UsuarioUpdate, Dict[str, Any]]
) -> Usuario:
    """Actualiza un usuario existente usando sqlmodel_update."""
    try:
        if isinstance(update_data, dict):
            update_dict = update_data
        else:
            update_dict = update_data.model_dump(exclude_unset=True)
        
        # Actualización segura excluyendo campos protegidos
        protected_fields = {"id", "fecha_creacion", "contrasena_hash"}
        clean_data = {k: v for k, v in update_dict.items() if k not in protected_fields}
        
        # SQLModel 0.0.14+
        db_user.sqlmodel_update(clean_data)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Usuario actualizado: {db_user.id}")
        return db_user
    except Exception as e:
        db.rollback()
        logger.error(f"Error actualizando usuario {db_user.id}: {str(e)}")
        raise

def delete_usuario(db: Session, user_id: int) -> Optional[Usuario]:
    """Elimina un usuario de forma segura."""
    try:
        user = db.get(Usuario, user_id)
        if user:
            user_repr = f"ID={user.id}, Username='{user.username}'"
            # La FK en usuario_rol tiene ON DELETE CASCADE, las asociaciones se borran solas.
            db.delete(user)
            db.commit()
            logger.warning(f"Usuario eliminado: {user_repr}")
            return user
        return None
    except Exception as e:
        db.rollback()
        logger.error(f"Error eliminando usuario {user_id}: {str(e)}")
        raise


def assign_rol_to_usuario(db: Session, *, db_usuario: Usuario, db_rol: Rol) -> Usuario:
    """
    Asigna un rol a un usuario creando la entrada en la tabla de enlace UsuarioRol.

    Args:
        db: La sesión de base de datos.
        db_usuario: El objeto Usuario al que se le asignará el rol.
        db_rol: El objeto Rol que será asignado.

    Returns:
        El objeto Usuario actualizado (potencialmente con la relación 'roles' refrescada).

    Raises:
        Exception: Si ocurre un error durante la operación de base de datos.
    """

    # Otra forma de verificar sin cargar la relación completa:
    link_exists_statement = select(UsuarioRol).where(
        UsuarioRol.usuario_id == db_usuario.id,
        UsuarioRol.rol_id == db_rol.id
    )
    existing_link = db.exec(link_exists_statement).first()

    if existing_link:
        logger.debug(f"Rol ID {db_rol.id} ya asignado a usuario ID {db_usuario.id}.")
        # Devolver el usuario sin cambios o refrescado si se prefiere
        # db.refresh(db_usuario) # Opcional
        return db_usuario

    logger.info(f"Asignando rol ID {db_rol.id} ({db_rol.nombre}) a usuario ID {db_usuario.id} ({db_usuario.username})")
    db_usuario_rol = UsuarioRol(usuario_id=db_usuario.id, rol_id=db_rol.id)
    try:
        db.add(db_usuario_rol)
        db.commit()
        # Refrescar el usuario puede ser necesario para que la colección usuario.roles
        # refleje inmediatamente el nuevo rol añadido, dependiendo de la configuración
        # de la sesión y la estrategia de carga de relaciones.
        db.refresh(db_usuario)
        logger.info(f"Rol asignado correctamente.")
        return db_usuario
    except Exception as e:
        db.rollback()
        logger.error(
            f"Error asignando rol ID {db_rol.id} a usuario ID {db_usuario.id}: {e}",
            exc_info=True
        )
        raise # Relanzar la excepción para que la capa de servicio la maneje


# NUEVA FUNCIÓN para quitar rol
def remove_rol_from_usuario(db: Session, *, db_usuario: Usuario, db_rol: Rol) -> Usuario:
    """
    Quita un rol a un usuario eliminando la entrada en la tabla UsuarioRol.
    Verifica si la asignación existe antes de intentar eliminarla.
    """
    # Buscar la entrada específica en la tabla de enlace
    link_statement = select(UsuarioRol).where(
        UsuarioRol.usuario_id == db_usuario.id,
        UsuarioRol.rol_id == db_rol.id
    )
    link_to_delete = db.exec(link_statement).first()

    if not link_to_delete:
        logger.warning(f"Intento de quitar rol ID={db_rol.id} ('{db_rol.nombre}') de usuario ID={db_usuario.id} ('{db_usuario.username}'), pero la asignación no existe.")
        # Devolver el usuario sin cambios. No necesariamente un error 404 a nivel de repo.
        # El servicio decidirá si esto es un 404.
        return db_usuario

    # Si existe, eliminar la asociación
    logger.info(f"Quitando rol ID={db_rol.id} ('{db_rol.nombre}') de usuario ID={db_usuario.id} ('{db_usuario.username}')")
    try:
        db.delete(link_to_delete)
        db.commit()
        # Refrescar el usuario para reflejar el cambio en la relación roles
        db.refresh(db_usuario)
        # Cargar explícitamente si es necesario
        # db.refresh(db_usuario, attribute_names=["roles"])
        logger.info(f"Rol quitado correctamente.")
        return db_usuario
    except Exception as e:
        db.rollback()
        logger.error(
            f"Error quitando rol ID={db_rol.id} de usuario ID={db_usuario.id}: {e}",
            exc_info=True
        )
        # Relanzar para que el servicio lo maneje
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al quitar el rol al usuario."
        )
