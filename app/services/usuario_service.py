# app/services/usuario_service.py
import logging
from sqlmodel import Session
from fastapi import HTTPException, status
from typing import Optional, Union, List
import traceback

import re

from app.models.user_models import Usuario, Rol
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioUpdatePassword
from app.repositories import usuario_repository, rol_repository
from app.services import rol_service  # Importing rol_service
from app.core.security import get_password_hash, verify_password


logger = logging.getLogger(__name__)


# --- Helpers ---
def _sanitize_email(email: str) -> str:
    """Normaliza emails a minúsculas y remueve espacios."""
    return email.strip().lower()

def _sanitize_username(username: str) -> str:
    """Normaliza username y valida formato."""
    sanitized = username.strip().lower()
    if not re.match(r"^[a-z0-9_]+$", sanitized):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username solo puede contener letras, números y guiones bajos"
        )
    return sanitized



# --- Creación ---
def create_new_user(db: Session, user_in: UsuarioCreate) -> Usuario:
    """
    Crea un nuevo usuario con validación y asignación de roles especificada.
    Si no se especifican roles, el usuario se crea sin roles iniciales.
    """
    # Sanitización y Validación de Duplicados (igual que antes)
    try:
        email = _sanitize_email(user_in.email)
        username = _sanitize_username(user_in.username) # Sanitización básica

        logger.info(f"Intentando crear usuario: Username='{username}', Email='{email[:5]}***'")

        if usuario_repository.get_usuario_by_email(db, email):
            logger.warning(f"Email ya registrado: '{email[:5]}***'")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo electrónico ya está registrado.")

        if usuario_repository.get_usuario_by_username(db, username):
            logger.warning(f"Username ya registrado: '{username}'")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de usuario no está disponible.")

        # --- Validación de Roles ---
        roles_to_assign: List[Rol] = [] # Lista para guardar objetos Rol validados
        if user_in.rol_ids:
            # Eliminar duplicados y ordenar para consistencia
            unique_rol_ids = sorted(list(set(user_in.rol_ids)))
            if unique_rol_ids: # Solo proceder si hay IDs únicos
                logger.info(f"Validando IDs de rol proporcionados: {unique_rol_ids} para usuario '{username}'")
                # Usar la nueva función del repositorio para buscar roles
                roles_found = rol_repository.get_roles_by_ids(db=db, role_ids=unique_rol_ids)

                # Validar que se encontraron todos los roles solicitados
                if len(roles_found) != len(unique_rol_ids):
                    found_ids = {role.id for role in roles_found}
                    missing_ids = [rid for rid in unique_rol_ids if rid not in found_ids]
                    logger.error(f"No se encontraron los siguientes IDs de rol al crear usuario '{username}': {missing_ids}")
                    # Usar 404 es apropiado si los IDs de rol no existen
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Uno o más IDs de rol proporcionados no existen: {missing_ids}"
                    )
                roles_to_assign = list(roles_found) # Guardar los objetos Rol validados
                logger.info(f"Roles validados para asignar a '{username}': {[r.nombre for r in roles_to_assign]}")
            else:
                 logger.warning(f"Lista de 'rol_ids' proporcionada para usuario '{username}' estaba vacía o contenía solo duplicados.")
        else:
             logger.warning(f"No se proporcionaron 'rol_ids' para el nuevo usuario '{username}'. Se creará sin roles iniciales.")

        # --- Creación del Usuario (Preparación) ---
        hashed_password = get_password_hash(user_in.password)
        # Excluir campos sensibles y el nuevo campo rol_ids del schema
        user_data_dict = user_in.model_dump(exclude={"password", "rol_ids"})

        # Crear la instancia del modelo Usuario
        db_user = Usuario(
            contrasena_hash=hashed_password,
            esta_activo=True, # Los usuarios se crean activos por defecto
            **user_data_dict # Pasar email, username, nombre_completo, etc.
        )

        # --- Guardar Usuario en BD ---
        # Usar la función del repositorio para crear el usuario base
        created_user = usuario_repository.create_usuario(db=db, usuario_data=db_user)
        logger.info(f"Usuario ID={created_user.id} ('{created_user.username}') creado en BD.")

        # --- Asignación de Roles (NUEVO) ---
        if roles_to_assign:
            logger.info(f"Asignando {len(roles_to_assign)} roles al usuario ID={created_user.id}...")
            assigned_count = 0
            # Iterar sobre los objetos Rol validados
            for rol in roles_to_assign:
                try:
                    # Usar la función existente del repositorio para asignar cada rol
                    # Esta función ya maneja commit y refresh si es necesario internamente (revisar repo)
                    usuario_repository.assign_rol_to_usuario(
                        db=db, db_usuario=created_user, db_rol=rol
                    )
                    assigned_count += 1
                except Exception as role_assign_exc:
                    # Capturar error específico de asignación si ocurre
                    logger.error(f"Error asignando rol ID={rol.id} ('{rol.nombre}') al usuario ID={created_user.id} "
                                 f"después de la creación: {role_assign_exc}", exc_info=True)
                    # Decisión: ¿Continuar asignando otros roles o detenerse y revertir?
                    # Por simplicidad, continuamos, pero el usuario puede quedar con roles parciales.
                    # Podría implementarse una lógica de rollback más compleja si es crítico.

            logger.info(f"Se asignaron {assigned_count} de {len(roles_to_assign)} roles solicitados al usuario ID={created_user.id}.")
            # Refrescar el usuario una vez al final para asegurar que la relación roles esté actualizada
            # si las asignaciones individuales no lo hicieron ya.
            db.refresh(created_user)
            # Cargar explícitamente roles si es necesario devolverlos inmediatamente (opcional)
            # db.refresh(created_user, attribute_names=["roles"])

        return created_user 

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en create_new_user para username='{user_in.username}': {e}", exc_info=True)
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el usuario."
        )

# --- Actualización de Perfil ---
def update_user_profile(db: Session, *, current_user: Usuario, user_in: UsuarioUpdate) -> Usuario:
    """Actualiza perfil con sanitización."""
    try:
        update_data = user_in.model_dump(exclude_unset=True)
        
        # Sanitizar email si se actualiza
        if "email" in update_data:
            new_email = _sanitize_email(update_data["email"])
            if new_email != current_user.email:
                existing = usuario_repository.get_usuario_by_email(db, new_email)
                if existing:
                    raise HTTPException(400, "Email ya en uso")
                update_data["email"] = new_email

        updated_user = usuario_repository.update_usuario(
            db, 
            db_user=current_user, 
            update_data=update_data
        )
        logger.info(f"Usuario {updated_user.id} actualizado")
        return updated_user

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error actualizando perfil: {str(e)}")
        raise HTTPException(500, "Error interno al actualizar")

# --- Actualización de Contraseña ---
def update_user_password(
    db: Session, 
    *, 
    current_user: Usuario, 
    password_in: UsuarioUpdatePassword
) -> Usuario:
    """Cambia contraseña con validación de política."""
    try:
        # Verificar contraseña actual
        if not verify_password(password_in.old_password, current_user.contrasena_hash):
            raise HTTPException(400, "Contraseña actual incorrecta")

        # Validar nueva contraseña
        #if settings.ENFORCE_PASSWORD_POLICY:
        #    if len(password_in.new_password) < 12:
        #        raise HTTPException(400, "La contraseña debe tener al menos 12 caracteres")

        # Actualizar
        new_hash = get_password_hash(password_in.new_password)
        return usuario_repository.update_usuario(
            db,
            db_user=current_user,
            update_data={"contrasena_hash": new_hash}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error cambiando contraseña: {str(e)}")
        raise HTTPException(500, "Error interno al actualizar contraseña")

# --- Lectura ---
def get_user_info(db: Session, user_id: int) -> Usuario:
    """Obtiene usuario por ID."""
    try:
        user = usuario_repository.get_usuario(db=db, user_id=user_id)
        if not user:
            logger.warning(f"Usuario ID {user_id} no encontrado")
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuario no encontrado")
        return user
    except HTTPException: # Relanzar excepciones HTTP específicas
        raise
    except Exception as e:
        # --- REVERTIDO: Usar logger y HTTP 500 ---
        logger.error(f"Error inesperado obteniendo usuario ID {user_id}: {e}", exc_info=True)
        # --- FIN REVERTIDO ---
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error interno al recuperar usuario")


def assign_role_to_user_service(db: Session, *, user_id: int, rol_id: int) -> Usuario:
    """Asigna un rol existente a un usuario existente."""
    logger.info(f"Intentando asignar rol ID={rol_id} a usuario ID={user_id}")
    db_user = get_user_info(db=db, user_id=user_id)
    db_rol = rol_service.get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)
    try:
        updated_user = usuario_repository.assign_rol_to_usuario(
            db=db, db_usuario=db_user, db_rol=db_rol
        )
        return updated_user
    except HTTPException:
        raise
    except Exception as e:
        # --- REVERTIDO: Usar logger y HTTP 500 ---
        logger.error(f"Error inesperado asignando rol ID={rol_id} a usuario ID={user_id}: {e}", exc_info=True)
        db.rollback()
        # --- FIN REVERTIDO ---
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al asignar el rol."
        )
def remove_role_from_user_service(db: Session, *, user_id: int, rol_id: int) -> Usuario:
    """Quita un rol previamente asignado de un usuario."""
    logger.info(f"Intentando quitar rol ID={rol_id} de usuario ID={user_id}")
    db_user = get_user_info(db=db, user_id=user_id)
    db_rol = rol_service.get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)
    try:
        updated_user = usuario_repository.remove_rol_from_usuario(
            db=db, db_usuario=db_user, db_rol=db_rol
        )
        return updated_user
    except HTTPException:
        raise
    except Exception as e:
        # --- REVERTIDO: Usar logger y HTTP 500 ---
        logger.error(f"Error inesperado quitando rol ID={rol_id} de usuario ID={user_id}: {e}", exc_info=True)
        db.rollback()
        # --- FIN REVERTIDO ---
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al quitar el rol."
        )
