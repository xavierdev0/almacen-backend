# app/repositories/usuario_repository.py
from sqlmodel import Session, select, SQLModel
from typing import Optional, Sequence, Union, Dict, Any
import logging
from uuid import UUID

from app.models.user_models import Usuario
from app.schemas.usuario_schema import UsuarioUpdate

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
    
def get_usuario(db: Session, user_id: Union[int, UUID]) -> Optional[Usuario]:
    """Obtiene un usuario por su ID."""
    try:
        return db.get(Usuario, user_id)
    except Exception as e:
        logger.error(f"Error obteniendo usuario ID {user_id}: {str(e)}")
        raise

def get_usuarios(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    filters: Optional[Dict[str, Any]] = None
) -> Sequence[Usuario]:
    """Lista usuarios con paginación y filtros opcionales."""
    try:
        query = select(Usuario)
        
        if filters:
            for field, value in filters.items():
                query = query.where(getattr(Usuario, field) == value)
                
        return db.exec(query.offset(skip).limit(limit)).all()
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
        logger.info(f"Usuario creado: {db_user.email}")
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
        protected_fields = {"id", "fecha_creacion"}
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

def delete_usuario(db: Session, user_id: Union[int, UUID]) -> Optional[Usuario]:
    """Elimina un usuario de forma segura."""
    try:
        user = db.get(Usuario, user_id)
        if user:
            db.delete(user)
            db.commit()
            logger.warning(f"Usuario eliminado: {user_id}")
            return user
        return None
    except Exception as e:
        db.rollback()
        logger.error(f"Error eliminando usuario {user_id}: {str(e)}")
        raise