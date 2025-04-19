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
        # *** CAMBIO: Eliminar 'contrasena_hash' de los campos protegidos aquí ***
        protected_fields = {"id", "fecha_creacion"} # <-- 'contrasena_hash' ELIMINADO
        clean_data = {k: v for k, v in update_dict.items() if k not in protected_fields}

        if not clean_data: # Si no hay nada que actualizar (quizás solo se envió un campo protegido)
             logger.warning(f"Intento de actualizar usuario {db_user.id} sin datos válidos.")
             return db_user # Devolver sin cambios

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
    # ... (código para verificar si el link ya existe) ...
    link_exists_statement = select(UsuarioRol).where(
        UsuarioRol.usuario_id == db_usuario.id,
        UsuarioRol.rol_id == db_rol.id
    )
    existing_link = db.exec(link_exists_statement).first()
    if existing_link:
        logger.debug(f"Rol ID {db_rol.id} ya asignado a usuario ID {db_usuario.id}.")
        # --- CAMBIO: Recargar roles incluso si ya existía, para asegurar estado fresco ---
        try:
            db.refresh(db_usuario, attribute_names=["roles"]) # Recargar solo roles
            logger.debug(f"Refrescada relación roles para usuario ID {db_usuario.id} (asignación ya existía).")
        except Exception as refresh_err:
             # Loggear error de refresh pero continuar, puede que no sea crítico aquí
             logger.warning(f"Error al refrescar roles para usuario {db_usuario.id} (asignación ya existía): {refresh_err}")
        # --- FIN CAMBIO ---
        return db_usuario

    logger.info(f"Asignando rol ID {db_rol.id} ({db_rol.nombre}) a usuario ID {db_usuario.id} ({db_usuario.username})")
    db_usuario_rol = UsuarioRol(usuario_id=db_usuario.id, rol_id=db_rol.id)
    try:
        db.add(db_usuario_rol)
        db.commit()
        # --- CAMBIO: Refrescar explícitamente la relación 'roles' ---
        # db.refresh(db_usuario) # Refrescar solo atributos escalares no es suficiente
        db.refresh(db_usuario, attribute_names=["roles"]) # Recargar específicamente la relación
        logger.info(f"Rol asignado y relación 'roles' refrescada para usuario ID {db_usuario.id}.")
        # --- FIN CAMBIO ---
        return db_usuario
    except Exception as e:
        db.rollback()
        logger.error(
            f"Error asignando rol ID {db_rol.id} a usuario ID {db_usuario.id}: {e}",
            exc_info=True
        )
        raise # Relanzar la excepción

# Modificar remove_rol_from_usuario
def remove_rol_from_usuario(db: Session, *, db_usuario: Usuario, db_rol: Rol) -> Usuario:
    # ... (código para buscar link_to_delete) ...
    link_statement = select(UsuarioRol).where(
        UsuarioRol.usuario_id == db_usuario.id,
        UsuarioRol.rol_id == db_rol.id
    )
    link_to_delete = db.exec(link_statement).first()

    if not link_to_delete:
        logger.warning(f"Intento de quitar rol ID={db_rol.id} ... pero la asignación no existe.")
         # --- CAMBIO: Recargar roles incluso si no existía, para asegurar estado fresco ---
        try:
            db.refresh(db_usuario, attribute_names=["roles"]) # Recargar solo roles
            logger.debug(f"Refrescada relación roles para usuario ID {db_usuario.id} (asignación no existía).")
        except Exception as refresh_err:
             logger.warning(f"Error al refrescar roles para usuario {db_usuario.id} (asignación no existía): {refresh_err}")
        # --- FIN CAMBIO ---
        return db_usuario

    logger.info(f"Quitando rol ID={db_rol.id} ('{db_rol.nombre}') de usuario ID={db_usuario.id} ('{db_usuario.username}')")
    try:
        db.delete(link_to_delete)
        db.commit()
         # --- CAMBIO: Refrescar explícitamente la relación 'roles' ---
        # db.refresh(db_usuario) # Refrescar solo atributos escalares no es suficiente
        db.refresh(db_usuario, attribute_names=["roles"]) # Recargar específicamente la relación
        logger.info(f"Rol quitado y relación 'roles' refrescada para usuario ID {db_usuario.id}.")
         # --- FIN CAMBIO ---
        return db_usuario
    except Exception as e:
        db.rollback()
        logger.error(
            f"Error quitando rol ID={db_rol.id} de usuario ID={db_usuario.id}: {e}",
            exc_info=True
        )
        # --- CAMBIO AQUÍ: Mantener el raise original (NO HTTP 500 desde repo) ---
        raise
        # --- FIN CAMBIO ---
        # raise HTTPException(
        #     status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #     detail="Error interno al quitar el rol al usuario."
        # )
