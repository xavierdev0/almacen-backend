# app/repositories/order_repository.py

import logging
from typing import Optional, Sequence, List # Sequence es el tipo preferido para listas de retorno de ORM
from sqlmodel import Session, select, SQLModel
from sqlalchemy.orm import selectinload # Para carga eager opcional
from sqlalchemy.exc import IntegrityError, SQLAlchemyError # Capturar errores específicos

# Importar el modelo principal
from app.models.order_models import PedidoCliente
# Importar otros modelos necesarios para relaciones (si se usa selectinload)
from app.models.client_model import Cliente
from app.models.user_models import Usuario

logger = logging.getLogger(__name__)

# =======================================
# Funciones CRUD para PedidoCliente
# =======================================

def create_pedido(db: Session, *, pedido_data: PedidoCliente) -> PedidoCliente:
    """
    Crea un nuevo registro de PedidoCliente en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        pedido_data: Un objeto PedidoCliente (previamente validado y preparado por el servicio).

    Returns:
        El objeto PedidoCliente recién creado y refrescado desde la base de datos.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: FK inválida).
                       La capa de servicio debería manejar esto (ej: 404/400).
        SQLAlchemyError: Para otros errores relacionados con la base de datos.
        Exception: Para errores inesperados no específicos de SQLAlchemy.
    """
    db_pedido = pedido_data # Asumimos que ya es una instancia del modelo
    logger.debug(f"Repositorio: Intentando crear PedidoCliente para Cliente ID: {db_pedido.cliente_id}")
    try:
        db.add(db_pedido)
        db.commit()
        db.refresh(db_pedido) # Carga ID, fecha_creacion, etc. desde la BD
        logger.info(f"PedidoCliente creado con éxito: ID={db_pedido.id}")
        return db_pedido
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al crear PedidoCliente: {e}", exc_info=True)
        # Relanzar para que el servicio maneje (probablemente indica un ID de cliente/vendedor inválido)
        raise e
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de base de datos (SQLAlchemy) al crear PedidoCliente: {e}", exc_info=True)
        raise e # Relanzar para manejo genérico (probablemente 500 en API)
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al crear PedidoCliente: {e}", exc_info=True)
        raise e # Relanzar

def get_pedido_by_id(db: Session, *, pedido_id: int, load_related: bool = False) -> Optional[PedidoCliente]:
    """
    Obtiene un PedidoCliente específico por su ID.

    Permite opcionalmente cargar relaciones comunes (cliente, vendedor, proformas)
    de forma eager para evitar consultas N+1 posteriores.

    Args:
        db: La sesión de base de datos activa.
        pedido_id: El ID del pedido a buscar.
        load_related: Si es True, carga eager las relaciones cliente, vendedor y proformas.

    Returns:
        El objeto PedidoCliente si se encuentra, None en caso contrario.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Buscando PedidoCliente por ID: {pedido_id}, Cargar relacionados: {load_related}")
    try:
        query = select(PedidoCliente).where(PedidoCliente.id == pedido_id)
        if load_related:
            # Carga Eager: Trae los datos relacionados en la misma consulta inicial.
            # Es más eficiente si sabes que vas a necesitar estos datos después.
            query = query.options(
                selectinload(PedidoCliente.cliente), # Cargar Cliente
                selectinload(PedidoCliente.vendedor), # Cargar Usuario (Vendedor)
                selectinload(PedidoCliente.proformas) # Cargar la lista de Proformas asociadas
                # Añadir selectinload(PedidoCliente.orden_produccion) si se necesita
            )
        pedido = db.exec(query).first()
        if pedido:
            logger.debug(f"PedidoCliente ID {pedido_id} encontrado.")
        else:
            logger.debug(f"PedidoCliente ID {pedido_id} no encontrado.")
        return pedido
    except SQLAlchemyError as e:
        logger.error(f"Error de base de datos (SQLAlchemy) al buscar PedidoCliente ID {pedido_id}: {e}", exc_info=True)
        raise e
    except Exception as e:
        logger.error(f"Error inesperado al buscar PedidoCliente ID {pedido_id}: {e}", exc_info=True)
        raise e

def list_pedidos(
    db: Session, *,
    skip: int = 0,
    limit: int = 100,
    cliente_id: Optional[int] = None,
    vendedor_id: Optional[int] = None,
    estado: Optional[str] = None,
    load_related: bool = False # Opción para cargar relaciones en la lista
) -> Sequence[PedidoCliente]:
    """
    Obtiene una lista paginada y filtrada de PedidoCliente.

    Permite filtrar por cliente_id, vendedor_id y estado.
    Permite opcionalmente cargar relaciones comunes para cada pedido en la lista.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de registros a saltar.
        limit: Número máximo de registros a devolver.
        cliente_id: Filtrar por ID de cliente (opcional).
        vendedor_id: Filtrar por ID de vendedor (opcional).
        estado: Filtrar por estado exacto (opcional).
        load_related: Si es True, carga eager cliente y vendedor para cada pedido.

    Returns:
        Una secuencia (lista) de objetos PedidoCliente que coinciden.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Listando PedidoCliente con filtros - skip:{skip}, limit:{limit}, cliente:{cliente_id}, vendedor:{vendedor_id}, estado:{estado}, related:{load_related}")
    try:
        query = select(PedidoCliente)

        # Aplicar filtros
        if cliente_id is not None:
            query = query.where(PedidoCliente.cliente_id == cliente_id)
        if vendedor_id is not None:
            query = query.where(PedidoCliente.usuario_id_vendedor == vendedor_id)
        if estado is not None:
            query = query.where(PedidoCliente.estado == estado)

        # Aplicar carga eager si se solicita
        if load_related:
            query = query.options(
                selectinload(PedidoCliente.cliente),
                selectinload(PedidoCliente.vendedor)
                # Considerar NO cargar proformas aquí por defecto, podría ser pesado para una lista.
            )

        # Aplicar ordenamiento (ej: por fecha de creación descendente) y paginación
        query = query.order_by(PedidoCliente.fecha_creacion.desc()).offset(skip).limit(limit)

        pedidos = db.exec(query).all()
        logger.debug(f"Se encontraron {len(pedidos)} PedidoCliente.")
        return pedidos
    except SQLAlchemyError as e:
        logger.error(f"Error de base de datos (SQLAlchemy) al listar PedidoCliente: {e}", exc_info=True)
        raise e
    except Exception as e:
        logger.error(f"Error inesperado al listar PedidoCliente: {e}", exc_info=True)
        raise e

def update_pedido(db: Session, *, db_pedido: PedidoCliente, update_data: dict) -> PedidoCliente:
    """
    Actualiza un registro de PedidoCliente existente en la base de datos.
    Principalmente útil para cambiar el estado.

    Args:
        db: La sesión de base de datos activa.
        db_pedido: El objeto PedidoCliente existente obtenido de la BD.
        update_data: Un diccionario con los campos a actualizar (ya filtrados).

    Returns:
        El objeto PedidoCliente actualizado y refrescado.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Intentando actualizar PedidoCliente ID: {db_pedido.id} con datos: {update_data.keys()}")
    try:
        if not update_data:
            logger.warning(f"No se proporcionaron datos para actualizar PedidoCliente ID {db_pedido.id}.")
            return db_pedido # No hay nada que hacer

        # Aplicar los cambios usando sqlmodel_update
        db_pedido.sqlmodel_update(update_data)

        db.add(db_pedido) # Marcar como modificado
        db.commit()
        db.refresh(db_pedido) # Obtener estado actualizado de la BD
        logger.info(f"PedidoCliente ID {db_pedido.id} actualizado con éxito.")
        return db_pedido
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de base de datos (SQLAlchemy) al actualizar PedidoCliente ID {db_pedido.id}: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al actualizar PedidoCliente ID {db_pedido.id}: {e}", exc_info=True)
        raise e

# Nota: La función delete_pedido no se implementa aquí inicialmente, ya que eliminar
# un pedido probablemente requeriría eliminar en cascada o verificar muchas dependencias
# (Proformas, Orden, Facturas). Es más común marcarlo como 'CANCELADO' o 'ARCHIVADO'.
# Si se necesita eliminar, se añadiría aquí con manejo cuidadoso de IntegrityError.

# --- Funciones adicionales que podríamos necesitar más adelante ---
# def get_proforma_by_id(db: Session, proforma_id: int) -> Optional[Proforma]: ...
# def create_proforma(db: Session, proforma_data: Proforma) -> Proforma: ...
# def add_linea_material(db: Session, linea_data: LineaProformaMaterial) -> LineaProformaMaterial: ...
# def update_proforma_totals(db: Session, proforma_id: int) -> Proforma: ...
# ... y así sucesivamente para las otras entidades relacionadas con el pedido ...