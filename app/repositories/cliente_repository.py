# app/repositories/cliente_repository.py
import logging
from typing import Optional, Sequence, Union, Dict, Any

from sqlmodel import Session, select, SQLModel
from sqlalchemy.exc import IntegrityError # Para capturar errores de constraints
from fastapi import HTTPException, status # Solo para tipado en docstring, no lanzar aquí

from app.models.client_model import Cliente
# Importar schemas solo si son estrictamente necesarios aquí (poco común)
# from app.schemas.client_schema import ClienteUpdate

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read (Getters)
# =====================

def get_cliente_by_id(db: Session, *, cliente_id: int) -> Optional[Cliente]:
    """
    Obtiene un cliente específico por su ID.

    Args:
        db: La sesión de base de datos activa.
        cliente_id: El ID del cliente a buscar.

    Returns:
        El objeto Cliente si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción de base de datos.
    """
    try:
        # db.get es la forma más directa de buscar por PK con SQLModel/SQLAlchemy
        cliente = db.get(Cliente, cliente_id)
        return cliente
    except Exception as e:
        logger.error(f"Error obteniendo cliente por ID {cliente_id}: {e}", exc_info=True)
        raise

def get_cliente_by_identificacion(db: Session, *, identificacion: str) -> Optional[Cliente]:
    """
    Obtiene un cliente específico por su número de identificación fiscal.

    Args:
        db: La sesión de base de datos activa.
        identificacion: El número de identificación fiscal a buscar.

    Returns:
        El objeto Cliente si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción de base de datos.
    """
    if not identificacion: # Evitar consulta si la identificación está vacía
        return None
    try:
        statement = select(Cliente).where(Cliente.identificacion_fiscal == identificacion)
        cliente = db.exec(statement).first()
        return cliente
    except Exception as e:
        logger.error(f"Error obteniendo cliente por identificación '{identificacion}': {e}", exc_info=True)
        raise

def get_cliente_by_email(db: Session, *, email: str) -> Optional[Cliente]:
    """
    Obtiene un cliente específico por su dirección de correo electrónico.

    Args:
        db: La sesión de base de datos activa.
        email: El correo electrónico a buscar.

    Returns:
        El objeto Cliente si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción de base de datos.
    """
    if not email: # Evitar consulta si el email está vacío
        return None
    try:
        statement = select(Cliente).where(Cliente.email == email)
        cliente = db.exec(statement).first()
        return cliente
    except Exception as e:
        logger.error(f"Error obteniendo cliente por email '{email}': {e}", exc_info=True)
        raise

def list_clientes(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Cliente]:
    """
    Obtiene una lista paginada de clientes.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de clientes a saltar.
        limit: Número máximo de clientes a devolver.

    Returns:
        Una secuencia (lista) de objetos Cliente.

    Raises:
        Exception: Relanza cualquier excepción de base de datos.
    """
    try:
        statement = select(Cliente).offset(skip).limit(limit).order_by(Cliente.id) # Ordenar para consistencia
        clientes = db.exec(statement).all()
        return clientes
    except Exception as e:
        logger.error(f"Error listando clientes: {e}", exc_info=True)
        raise

# =====================
#  Funciones Write (Create, Update, Delete)
# =====================

def create_cliente(db: Session, *, cliente_data: Cliente) -> Cliente:
    """
    Crea un nuevo cliente en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        cliente_data: Un objeto Cliente (previamente validado por el schema/servicio).

    Returns:
        El objeto Cliente recién creado y refrescado.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: email o
                        identificación duplicada). La capa de servicio debe
                        capturarla y traducirla a HTTPException 409.
        Exception: Relanza otras excepciones de base de datos.
    """
    db_cliente = cliente_data # Asumimos que ya es un objeto Cliente
    try:
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        logger.info(f"Cliente creado: ID={db_cliente.id}, Nombre='{db_cliente.nombre}'")
        return db_cliente
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"Error de integridad al crear cliente '{db_cliente.nombre}': {e}")
        # Relanzar para que el servicio maneje el conflicto (409)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado creando cliente '{db_cliente.nombre}': {e}", exc_info=True)
        raise # Relanza otras excepciones

def update_cliente(
    db: Session, *, db_cliente: Cliente, update_data: Dict[str, Any]
) -> Cliente:
    """
    Actualiza un cliente existente en la base de datos.

    Aplica actualizaciones parciales usando sqlmodel_update.

    Args:
        db: La sesión de base de datos activa.
        db_cliente: El objeto Cliente existente obtenido de la DB.
        update_data: Un diccionario con los campos a actualizar (ya filtrados
                     y validados por el servicio, idealmente).

    Returns:
        El objeto Cliente actualizado y refrescado.

    Raises:
        IntegrityError: Si la actualización causa una violación de constraint.
                        La capa de servicio debe manejarla (409).
        Exception: Relanza otras excepciones de base de datos.
    """
    try:
        # update_data ya debería ser un dict aquí, proveniente del servicio
        if not update_data:
            logger.warning(f"Intento de actualizar cliente {db_cliente.id} sin datos.")
            return db_cliente # No hay nada que actualizar

        # Usar sqlmodel_update para aplicar los cambios al objeto existente
        db_cliente.sqlmodel_update(update_data)

        db.add(db_cliente) # Marcar el objeto como modificado
        db.commit()
        db.refresh(db_cliente)
        logger.info(f"Cliente actualizado: ID={db_cliente.id}")
        return db_cliente
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"Error de integridad al actualizar cliente ID {db_cliente.id}: {e}")
        # Relanzar para que el servicio maneje el conflicto (409)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado actualizando cliente ID {db_cliente.id}: {e}", exc_info=True)
        raise # Relanza otras excepciones

def delete_cliente(db: Session, *, cliente_id: int) -> Optional[Cliente]:
    """
    Elimina un cliente de la base de datos por su ID.

    Busca al cliente y si existe, intenta eliminarlo. La DB impedirá
    la eliminación si existen registros dependientes (Pedidos, Facturas)
    debido a la constraint ON DELETE RESTRICT.

    Args:
        db: La sesión de base de datos activa.
        cliente_id: El ID del cliente a eliminar.

    Returns:
        El objeto Cliente que fue eliminado, o None si el cliente no se encontró.

    Raises:
        IntegrityError: Si la eliminación es bloqueada por la DB debido a
                        registros dependientes. El servicio debe manejarla (409).
        Exception: Relanza otras excepciones de base de datos.
    """
    try:
        cliente = db.get(Cliente, cliente_id)
        if not cliente:
            logger.warning(f"Intento de eliminar cliente ID {cliente_id} no encontrado.")
            return None # No encontrado

        cliente_repr = f"ID={cliente.id}, Nombre='{cliente.nombre}'"
        logger.info(f"Intentando eliminar cliente: {cliente_repr}")
        db.delete(cliente)
        db.commit()
        logger.warning(f"Cliente eliminado: {cliente_repr}") # Usar warning para eliminaciones
        return cliente # Devuelve el objeto eliminado (desvinculado de la sesión)

    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al eliminar cliente ID {cliente_id}. Probablemente tiene pedidos/facturas asociados: {e}")
        # Relanzar para que el servicio maneje el conflicto (409)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado eliminando cliente ID {cliente_id}: {e}", exc_info=True)
        raise # Relanza otras excepciones