# app/api/v1/endpoints/pedidos.py

import logging
from typing import List, Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path
from sqlmodel import Session

# Importar dependencias necesarias
from app.api.deps import get_db, require_permission, get_current_active_user
# Importar el servicio correspondiente
from app.services import order_service
# Importar los schemas necesarios
from app.schemas.order_schema import PedidoClienteCreate, PedidoClienteRead
# Importar el modelo Usuario para tipar current_user
from app.models import Usuario

logger = logging.getLogger(__name__)

# Crear el router específico para pedidos
router = APIRouter(
    prefix="/pedidos", # Prefijo para todas las rutas de este router
    tags=["Pedidos"],  # Etiqueta para agrupar en la documentación OpenAPI
    responses={ # Respuestas comunes (pueden ser sobreescritas por endpoints específicos)
        404: {"description": "Pedido no encontrado"},
        403: {"description": "Permiso insuficiente"},
        401: {"description": "No autenticado"},
        409: {"description": "Conflicto de datos"},
    }
)

# --- Endpoint para Crear un PedidoCliente ---
@router.post(
    "", # Ruta: POST /api/v1/pedidos
    response_model=PedidoClienteRead, # Lo que devolverá la API
    status_code=status.HTTP_201_CREATED, # Código para creación exitosa
    summary="Crear un nuevo Pedido de Cliente",
    description="Crea un registro inicial para un pedido de cliente. El vendedor se asigna automáticamente basado en el usuario autenticado.",
    dependencies=[Depends(require_permission("crear:pedido_cliente"))] # Permiso requerido
)
def create_pedido_endpoint(
    *, # Forza argumentos keyword-only después de esto
    db: Annotated[Session, Depends(get_db)],
    pedido_in: PedidoClienteCreate, # El cuerpo de la solicitud validado por el schema
    current_user: Annotated[Usuario, Depends(get_current_active_user)] # Obtener el usuario logueado
):
    """
    Endpoint para crear un nuevo PedidoCliente.

    - Requiere permiso: `crear:pedido_cliente`.
    - Asigna el usuario autenticado como vendedor.
    """
    logger.info(f"API: Solicitud para crear PedidoCliente por Vendedor ID: {current_user.id} para Cliente ID: {pedido_in.cliente_id}")
    try:
        # Llama al servicio, pasando la sesión, los datos de entrada y el ID del vendedor
        nuevo_pedido = order_service.create_pedido_service(
            db=db,
            pedido_in=pedido_in,
            vendedor_id=current_user.id
        )
        # El servicio ya devuelve el objeto PedidoCliente creado
        return nuevo_pedido
    except HTTPException as http_exc:
        # Si el servicio lanzó una HTTPException (ej: 404 cliente no encontrado), la relanzamos
        logger.warning(f"HTTPException al crear pedido: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        # Captura cualquier otro error inesperado del servicio o repositorio
        logger.error(f"Error inesperado en endpoint create_pedido: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al procesar la solicitud de creación del pedido."
        )


# --- Endpoint para Obtener un PedidoCliente por ID ---
@router.get(
    "/{pedido_id}", # Ruta: GET /api/v1/pedidos/{pedido_id}
    response_model=PedidoClienteRead,
    summary="Obtener un PedidoCliente por su ID",
    description="Recupera los detalles de un pedido específico, incluyendo información del cliente y vendedor.",
    dependencies=[Depends(require_permission("leer:pedido_cliente"))] # Permiso requerido
)
def get_pedido_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    pedido_id: int = Path(..., description="ID del PedidoCliente a obtener", gt=0) # Parámetro de ruta validado
    # current_user: Annotated[Usuario, Depends(get_current_active_user)] # No necesario si solo valida permiso
):
    """
    Endpoint para obtener los detalles de un PedidoCliente específico.

    - Requiere permiso: `leer:pedido_cliente`.
    """
    logger.info(f"API: Solicitud para obtener PedidoCliente ID: {pedido_id}")
    try:
        # Llama al servicio para obtener el pedido
        # El servicio se encarga de manejar el caso "no encontrado" (404)
        # Pasamos load_related=True (valor por defecto en el servicio) para que PedidoClienteRead funcione
        pedido = order_service.get_pedido_service(db=db, pedido_id=pedido_id, load_related=True)
        return pedido
    except HTTPException as http_exc:
        logger.warning(f"HTTPException al obtener pedido ID {pedido_id}: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en endpoint get_pedido: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al obtener el pedido."
        )


# --- Endpoint para Listar PedidoClientes ---
@router.get(
    "", # Ruta: GET /api/v1/pedidos
    response_model=List[PedidoClienteRead],
    summary="Listar Pedidos de Clientes",
    description="Obtiene una lista paginada de pedidos, con opciones de filtrado por cliente, vendedor y estado.",
    dependencies=[Depends(require_permission("leer:pedido_cliente"))] # Permiso requerido
)
def list_pedidos_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0, description="Número de pedidos a saltar"),
    limit: int = Query(100, ge=1, le=200, description="Número máximo de pedidos a devolver"),
    cliente_id: Optional[int] = Query(None, description="Filtrar por ID de cliente"),
    vendedor_id: Optional[int] = Query(None, description="Filtrar por ID de vendedor"),
    estado: Optional[str] = Query(None, description="Filtrar por estado del pedido")
    # current_user: Annotated[Usuario, Depends(get_current_active_user)] # Podría usarse para filtrar por vendedor si no es admin/supervisor
):
    """
    Endpoint para listar PedidoClientes con filtros y paginación.

    - Requiere permiso: `leer:pedido_cliente`.
    - TODO: Implementar lógica para restringir la vista si el usuario no es Admin/Supervisor?
    """
    logger.info(f"API: Solicitud para listar PedidoCliente - skip:{skip}, limit:{limit}, cliente:{cliente_id}, vendedor:{vendedor_id}, estado:{estado}")
    # Por ahora, el permiso 'leer:pedido_cliente' da acceso a todos. Se puede refinar luego.
    try:
        # Llama al servicio para listar, pasando los filtros
        # El servicio usa load_related=True por defecto para que PedidoClienteRead funcione
        pedidos = order_service.list_pedidos_service(
            db=db,
            skip=skip,
            limit=limit,
            cliente_id=cliente_id,
            vendedor_id=vendedor_id,
            estado=estado,
            load_related=True
        )
        return pedidos
    except HTTPException as http_exc:
        logger.warning(f"HTTPException al listar pedidos: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en endpoint list_pedidos: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al listar los pedidos."
        )