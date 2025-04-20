# app/repositories/usuario_repository.py
from sqlmodel import Session, select, SQLModel
from typing import Optional, Sequence, Union, Dict, Any
import logging

from app.models.user_models import Usuario, Rol, UsuarioRol
from app.schemas.usuario_schema import UsuarioUpdate
from sqlalchemy.orm import selectinload

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read
# =====================

def get_usuario_by_username(db: Session, username: str) -> Optional[Usuario]:
    """
    Obtiene un usuario específico por su nombre de usuario (username).

    Args:
        db: La sesión de base de datos activa.
        username: El nombre de usuario a buscar.

    Returns:
        El objeto Usuario si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Usuario).where(Usuario.username == username)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo usuario {username}: {str(e)}")
        raise

def get_usuario_by_email(db: Session, email: str) -> Optional[Usuario]:
    """
    Obtiene un usuario específico por su dirección de correo electrónico.

    Args:
        db: La sesión de base de datos activa.
        email: El correo electrónico del usuario a buscar.

    Returns:
        El objeto Usuario si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Usuario).where(Usuario.email == email)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo usuario {email}: {str(e)}")
        raise

def get_usuario(db: Session, user_id: int) -> Optional[Usuario]:
    """
    Obtiene un usuario específico por su ID, cargando también sus roles asociados.

    Utiliza carga 'eager' (selectinload) para la relación 'roles' para evitar
    consultas N+1 si se accede a los roles del usuario posteriormente.

    Args:
        db: La sesión de base de datos activa.
        user_id: El ID del usuario a buscar.

    Returns:
        El objeto Usuario con sus roles cargados si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = (
            select(Usuario)
            .where(Usuario.id == user_id)
            .options(selectinload(Usuario.roles)) # Carga Eager de roles
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
    """
    Obtiene una lista paginada y filtrada de usuarios, cargando sus roles.

    Permite paginación mediante 'skip' y 'limit', y filtrado básico por
    campos del modelo Usuario. También carga 'eager' los roles de cada usuario.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de registros a saltar (para paginación).
        limit: Número máximo de registros a devolver (para paginación).
        filters: Un diccionario opcional donde las claves son nombres de campos
                 del modelo Usuario y los valores son los valores a filtrar.
                 Se ignorarán claves que no correspondan a campos del modelo.

    Returns:
        Una secuencia (lista) de objetos Usuario que coinciden con los criterios.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        query = select(Usuario)
        if filters:
            for field, value in filters.items():
                # Asegurarse que el campo existe en el modelo Usuario
                if hasattr(Usuario, field):
                    query = query.where(getattr(Usuario, field) == value)
                else:
                    logger.warning(f"Intento de filtrar por campo inexistente en Usuario: {field}")

        query = query.options(selectinload(Usuario.roles)) # Cargar roles
        query = query.offset(skip).limit(limit)

        users = db.exec(query).all()
        return users

    except Exception as e:
        logger.error(f"Error listando usuarios: {str(e)}")
        raise

# =====================
#  Funciones Write
# =====================

def create_usuario(db: Session, usuario_data: Union[Usuario, Dict[str, Any]]) -> Usuario:
    """
    Crea un nuevo usuario en la base de datos.

    Acepta los datos del usuario como un objeto Usuario pre-construido o
    como un diccionario. Realiza commit y refresh. Hace rollback en caso de error.

    Args:
        db: La sesión de base de datos activa.
        usuario_data: Un objeto Usuario o un diccionario con los datos del
                      nuevo usuario.

    Returns:
        El objeto Usuario recién creado y refrescado desde la base de datos.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
    """
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
    """
    Actualiza un usuario existente en la base de datos.

    Utiliza `sqlmodel_update` para aplicar actualizaciones parciales de forma segura,
    excluyendo campos protegidos como 'id' y 'fecha_creacion'.
    Acepta los datos de actualización como un esquema Pydantic (UsuarioUpdate)
    o un diccionario. Hace rollback en caso de error.

    Args:
        db: La sesión de base de datos activa.
        db_user: El objeto Usuario existente que se va a actualizar.
        update_data: Un objeto UsuarioUpdate o un diccionario con los campos
                     a actualizar. Los campos no presentes o con valor None
                     en UsuarioUpdate no se actualizan (si se usa exclude_unset=True).

    Returns:
        El objeto Usuario actualizado y refrescado desde la base de datos.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
    """
    try:
        if isinstance(update_data, dict):
            update_dict = update_data
        else:
            # Excluir campos no enviados explícitamente por el cliente
            update_dict = update_data.model_dump(exclude_unset=True)

        # Campos que no deben ser actualizados directamente a través de este método
        protected_fields = {"id", "fecha_creacion"}
        clean_data = {k: v for k, v in update_dict.items() if k not in protected_fields}

        if not clean_data: # Si no hay datos válidos para actualizar
              logger.warning(f"Intento de actualizar usuario {db_user.id} sin datos válidos.")
              return db_user # Devolver sin cambios

        # Aplica las actualizaciones al objeto db_user
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
    """
    Elimina un usuario de la base de datos por su ID.

    Busca al usuario por ID y si existe, lo elimina.
    Gracias a 'ON DELETE CASCADE' en la FK de la tabla UsuarioRol,
    las asociaciones usuario-rol se eliminan automáticamente.
    Hace rollback en caso de error durante la eliminación.

    Args:
        db: La sesión de base de datos activa.
        user_id: El ID del usuario a eliminar.

    Returns:
        El objeto Usuario que fue eliminado, o None si el usuario no se encontró.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
    """
    try:
        user = db.get(Usuario, user_id)
        if user:
            user_repr = f"ID={user.id}, Username='{user.username}'"
            # La FK en usuario_rol tiene ON DELETE CASCADE, las asociaciones se borran solas.
            # No es necesario eliminar manualmente las entradas en UsuarioRol.
            db.delete(user)
            db.commit()
            logger.warning(f"Usuario eliminado: {user_repr}")
            return user
        return None # Usuario no encontrado
    except Exception as e:
        db.rollback()
        logger.error(f"Error eliminando usuario {user_id}: {str(e)}")
        raise

def assign_rol_to_usuario(db: Session, *, db_usuario: Usuario, db_rol: Rol) -> Usuario:
    """
    Asigna un rol específico a un usuario creando una entrada en la tabla UsuarioRol.

    Verifica primero si la asignación ya existe. Si no existe, crea la
    entrada en la tabla de asociación (UsuarioRol).
    Finalmente, refresca explícitamente la relación 'roles' del objeto Usuario
    para asegurar que refleje el estado actualizado tras el commit.
    Hace rollback en caso de error durante la asignación.

    Args:
        db: La sesión de base de datos activa.
        db_usuario: El objeto Usuario al que se le asignará el rol.
        db_rol: El objeto Rol que será asignado.

    Returns:
        El objeto Usuario con su relación 'roles' potencialmente actualizada.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
    """
    # Verifica si el rol ya está asignado a este usuario
    link_exists_statement = select(UsuarioRol).where(
        UsuarioRol.usuario_id == db_usuario.id,
        UsuarioRol.rol_id == db_rol.id
    )
    existing_link = db.exec(link_exists_statement).first()

    if existing_link:
        logger.debug(f"Rol ID {db_rol.id} ya asignado a usuario ID {db_usuario.id}.")
        # Aunque ya exista, refrescamos por si acaso el estado en memoria no está sincronizado
        try:
            db.refresh(db_usuario, attribute_names=["roles"])
            logger.debug(f"Refrescada relación roles para usuario ID {db_usuario.id} (asignación ya existía).")
        except Exception as refresh_err:
            # Loggear error de refresh pero continuar, puede que no sea crítico aquí
            logger.warning(f"Error al refrescar roles para usuario {db_usuario.id} (asignación ya existía): {refresh_err}")
        return db_usuario

    logger.info(f"Asignando rol ID {db_rol.id} ({db_rol.nombre}) a usuario ID {db_usuario.id} ({db_usuario.username})")
    db_usuario_rol = UsuarioRol(usuario_id=db_usuario.id, rol_id=db_rol.id)
    try:
        db.add(db_usuario_rol)
        db.commit()
        # Es crucial refrescar la relación después de modificar la tabla de asociación
        # db.refresh(db_usuario) por sí solo no carga/actualiza relaciones lazy/nuevas.
        db.refresh(db_usuario, attribute_names=["roles"]) # Recargar específicamente la relación
        logger.info(f"Rol asignado y relación 'roles' refrescada para usuario ID {db_usuario.id}.")
        return db_usuario
    except Exception as e:
        db.rollback()
        logger.error(
            f"Error asignando rol ID {db_rol.id} a usuario ID {db_usuario.id}: {e}",
            exc_info=True
        )
        raise # Relanzar la excepción original para manejo superior

def remove_rol_from_usuario(db: Session, *, db_usuario: Usuario, db_rol: Rol) -> Usuario:
    """
    Quita un rol específico de un usuario eliminando la entrada correspondiente en UsuarioRol.

    Busca la entrada de asociación entre el usuario y el rol. Si existe,
    la elimina de la tabla UsuarioRol.
    Finalmente, refresca explícitamente la relación 'roles' del objeto Usuario
    para asegurar que refleje el estado actualizado tras el commit.
    Hace rollback en caso de error durante la eliminación de la asociación.

    Args:
        db: La sesión de base de datos activa.
        db_usuario: El objeto Usuario del que se quitará el rol.
        db_rol: El objeto Rol que será quitado.

    Returns:
        El objeto Usuario con su relación 'roles' potencialmente actualizada.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
                   Es importante que el repositorio no lance HTTPErrors, eso
                   debe manejarse en la capa de servicio/API.
    """
    # Busca la entrada en la tabla de asociación para eliminarla
    link_statement = select(UsuarioRol).where(
        UsuarioRol.usuario_id == db_usuario.id,
        UsuarioRol.rol_id == db_rol.id
    )
    link_to_delete = db.exec(link_statement).first()

    if not link_to_delete:
        logger.warning(f"Intento de quitar rol ID={db_rol.id} de usuario ID={db_usuario.id}, pero la asignación no existe.")
        # Aunque no existía, refrescamos por si acaso el estado en memoria no está sincronizado
        try:
            db.refresh(db_usuario, attribute_names=["roles"])
            logger.debug(f"Refrescada relación roles para usuario ID {db_usuario.id} (asignación no existía).")
        except Exception as refresh_err:
             logger.warning(f"Error al refrescar roles para usuario {db_usuario.id} (asignación no existía): {refresh_err}")
        return db_usuario

    logger.info(f"Quitando rol ID={db_rol.id} ('{db_rol.nombre}') de usuario ID={db_usuario.id} ('{db_usuario.username}')")
    try:
        db.delete(link_to_delete)
        db.commit()
        # Es crucial refrescar la relación después de modificar la tabla de asociación
        # db.refresh(db_usuario) por sí solo no carga/actualiza relaciones lazy/nuevas.
        db.refresh(db_usuario, attribute_names=["roles"]) # Recargar específicamente la relación
        logger.info(f"Rol quitado y relación 'roles' refrescada para usuario ID {db_usuario.id}.")
        return db_usuario
    except Exception as e:
        db.rollback()
        logger.error(
            f"Error quitando rol ID={db_rol.id} de usuario ID={db_usuario.id}: {e}",
            exc_info=True
        )
        # Mantenemos el raise original; la capa superior decidirá cómo manejar el error (p.ej., HTTP 500)
        raise