# app/services/order_service.py

import logging
from typing import Optional, Sequence # Sequence es preferible para listas de retorno
from sqlmodel import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError # Para capturar errores del repo

# Importar Repositorios
from app.repositories import order_repository, cliente_repository # Necesitamos cliente_repo para validar

# Importar Modelos y Schemas
from app.models.order_models import PedidoCliente
from app.schemas.order_schema import PedidoClienteCreate, PedidoClienteRead # Usamos Create para entrada

logger = logging.getLogger(__name__)

# =======================================
# Funciones del Servicio para PedidoCliente
# =======================================

def create_pedido_service(
    db: Session, *, pedido_in: PedidoClienteCreate, vendedor_id: int
) -> PedidoCliente:
    """
    Crea un nuevo PedidoCliente, validando la existencia del cliente
    y asignando el vendedor autenticado.

    Args:
        db: La sesión de base de datos activa.
        pedido_in: Datos de entrada validados por el schema PedidoClienteCreate.
                   Solo contiene cliente_id.
        vendedor_id: ID del usuario (vendedor) autenticado que crea el pedido.

    Returns:
        El objeto PedidoCliente recién creado.

    Raises:
        HTTPException 404: Si el cliente_id proporcionado no existe.
        HTTPException 409: Si ocurre un conflicto inesperado al guardar (ej. FK vendedor inválida).
        HTTPException 500: Para otros errores internos inesperados.
    """
    logger.info(f"Servicio: Intentando crear PedidoCliente para Cliente ID: {pedido_in.cliente_id} por Vendedor ID: {vendedor_id}")

    # 1. Validar que el cliente existe
    cliente = cliente_repository.get_cliente_by_id(db=db, cliente_id=pedido_in.cliente_id)
    if not cliente:
        logger.warning(f"Cliente con ID {pedido_in.cliente_id} no encontrado al intentar crear pedido.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {pedido_in.cliente_id} no encontrado."
        )
    logger.debug(f"Cliente ID {pedido_in.cliente_id} validado: {cliente.nombre}")

    # 2. Preparar el objeto del modelo PedidoCliente
    #    Se asigna el vendedor_id y el estado inicial.
    pedido_data_dict = pedido_in.model_dump() # Obtener dict del schema de entrada
    pedido_model_instance = PedidoCliente(
        **pedido_data_dict, # Pasa cliente_id
        usuario_id_vendedor=vendedor_id,
        estado="NUEVO" # Estado inicial por defecto
        # fecha_creacion y fecha_ultima_actualizacion son manejadas por el modelo/DB
    )

    # 3. Intentar crear usando el repositorio
    try:
        nuevo_pedido = order_repository.create_pedido(db=db, pedido_data=pedido_model_instance)
        # Opcional: Cargar relaciones para devolver más info (si PedidoClienteRead lo requiere)
        # db.refresh(nuevo_pedido, attribute_names=["cliente", "vendedor"])
        return nuevo_pedido
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al crear pedido para cliente {pedido_in.cliente_id}: {e}", exc_info=True)
        # Podría ser un problema con vendedor_id si no se validó antes (aunque viene del token)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se pudo crear el pedido debido a un conflicto de datos (verifique cliente y vendedor)."
        )
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de DB al crear pedido para cliente {pedido_in.cliente_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el pedido [DB]."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al crear pedido para cliente {pedido_in.cliente_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el pedido [General]."
        )


def get_pedido_service(db: Session, *, pedido_id: int, load_related: bool = True) -> PedidoCliente:
    """
    Obtiene un PedidoCliente por su ID, cargando relaciones por defecto.

    Args:
        db: La sesión de base de datos activa.
        pedido_id: El ID del pedido a buscar.
        load_related: Si cargar relaciones (cliente, vendedor, proformas). True por defecto.

    Returns:
        El objeto PedidoCliente encontrado.

    Raises:
        HTTPException 404: Si el pedido no se encuentra.
        HTTPException 500: Para otros errores internos inesperados.
    """
    logger.debug(f"Servicio: Buscando PedidoCliente ID: {pedido_id}")
    try:
        pedido = order_repository.get_pedido_by_id(db=db, pedido_id=pedido_id, load_related=load_related)
        if not pedido:
            logger.warning(f"PedidoCliente con ID {pedido_id} no encontrado.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pedido con ID {pedido_id} no encontrado."
            )
        logger.info(f"PedidoCliente ID {pedido_id} encontrado.")
        return pedido
    except HTTPException: # Re-lanzar 404
        raise
    except SQLAlchemyError as e:
         logger.error(f"Error de DB al buscar PedidoCliente ID {pedido_id}: {e}", exc_info=True)
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Error interno del servidor al buscar el pedido [DB]."
         )
    except Exception as e:
        logger.error(f"Error inesperado al buscar PedidoCliente ID {pedido_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al buscar el pedido [General]."
        )

def list_pedidos_service(
    db: Session, *,
    skip: int = 0,
    limit: int = 100,
    cliente_id: Optional[int] = None,
    vendedor_id: Optional[int] = None,
    estado: Optional[str] = None,
    load_related: bool = True # Cargar cliente/vendedor por defecto para listas
) -> Sequence[PedidoCliente]:
    """
    Lista PedidoCliente con filtros y paginación, cargando relaciones por defecto.

    Args:
        db: Sesión de BD.
        skip: Registros a saltar.
        limit: Máximo de registros.
        cliente_id: Filtrar por cliente (opcional).
        vendedor_id: Filtrar por vendedor (opcional).
        estado: Filtrar por estado (opcional).
        load_related: Si cargar cliente/vendedor (True por defecto).

    Returns:
        Una secuencia de objetos PedidoCliente.

    Raises:
        HTTPException 500: Error interno.
    """
    logger.debug(f"Servicio: Listando PedidoCliente - skip:{skip}, limit:{limit}, cliente:{cliente_id}, vendedor:{vendedor_id}, estado:{estado}, related:{load_related}")
    try:
        pedidos = order_repository.list_pedidos(
            db=db,
            skip=skip,
            limit=limit,
            cliente_id=cliente_id,
            vendedor_id=vendedor_id,
            estado=estado,
            load_related=load_related
        )
        return pedidos
    except SQLAlchemyError as e:
         logger.error(f"Error de DB al listar PedidoCliente: {e}", exc_info=True)
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Error interno del servidor al listar pedidos [DB]."
         )
    except Exception as e:
        logger.error(f"Error inesperado al listar PedidoCliente: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al listar pedidos [General]."
        )


# (Aquí añadiremos funciones para Proformas, Líneas, Ordenes en fases posteriores)