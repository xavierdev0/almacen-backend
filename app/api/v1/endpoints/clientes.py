# app/api/v1/endpoints/clientes.py
import logging
from typing import List, Annotated # Annotated para Depends más limpio

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response
from sqlmodel import Session

# Importar dependencias, servicios y schemas necesarios
from app.api.deps import get_db, require_permission # Usamos nuestra dependencia de permisos
from app.services import cliente_service
from app.schemas.client_schema import (
    ClienteCreate, ClienteUpdate, ClienteRead
)
# El modelo Usuario no suele necesitarse directamente en endpoints si usamos deps
# from app.models import Usuario

logger = logging.getLogger(__name__)

# Crear el router específico para clientes
router = APIRouter(
    prefix="/clientes", # Prefijo para todas las rutas de este router
    tags=["Clientes"],  # Etiqueta para agrupar en la documentación OpenAPI
    # Podríamos añadir respuestas comunes aquí si quisiéramos
    # responses={404: {"description": "Cliente no encontrado"}} # Ejemplo
)

# --- Endpoint para Crear un Cliente ---
@router.post(
    "", # Ruta: POST /api/v1/clientes
    response_model=ClienteRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo cliente",
    dependencies=[Depends(require_permission("crear:cliente"))], # Aplicar permiso
    responses={
        409: {"description": "Conflicto, email o identificación ya existen"},
        403: {"description": "Permiso insuficiente"},
        400: {"description": "Datos de entrada inválidos (validación schema)"}
    }
)
def create_new_cliente(
    *,
    db: Annotated[Session, Depends(get_db)],
    cliente_in: ClienteCreate # Cuerpo de la solicitud validado por el schema
    # current_user: Annotated[Usuario, Depends(get_current_active_user)] # No necesario si solo usamos permiso
):
    """
    Crea un nuevo cliente en el sistema.

    - **Requiere permiso:** `crear:cliente`.
    """
    logger.info(f"[Permiso: crear:cliente] Solicitud para crear cliente: {cliente_in.nombre}")
    # La lógica de validación de duplicados y creación está en el servicio
    # Las excepciones (409, 500) lanzadas por el servicio se propagarán
    cliente = cliente_service.create_cliente_service(db=db, cliente_in=cliente_in)
    return cliente

# --- Endpoint para Listar Clientes ---
@router.get(
    "", # Ruta: GET /api/v1/clientes
    response_model=List[ClienteRead],
    summary="Listar clientes",
    dependencies=[Depends(require_permission("leer:cliente"))], # Aplicar permiso
    responses={
        403: {"description": "Permiso insuficiente"}
    }
)
def list_all_clientes(
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0, description="Número de clientes a saltar"),
    limit: int = Query(100, ge=1, le=200, description="Número máximo de clientes a devolver")
):
    """
    Obtiene una lista paginada de clientes.

    - **Requiere permiso:** `leer:cliente`.
    """
    logger.debug(f"[Permiso: leer:cliente] Solicitud para listar clientes, skip={skip}, limit={limit}")
    clientes = cliente_service.get_clientes_service(db=db, skip=skip, limit=limit)
    return clientes

# --- Endpoint para Obtener un Cliente por ID ---
@router.get(
    "/{cliente_id}", # Ruta: GET /api/v1/clientes/{cliente_id}
    response_model=ClienteRead,
    summary="Obtener un cliente por ID",
    dependencies=[Depends(require_permission("leer:cliente"))], # Aplicar permiso
    responses={
        404: {"description": "Cliente no encontrado"},
        403: {"description": "Permiso insuficiente"}
    }
)
def get_single_cliente(
    *,
    db: Annotated[Session, Depends(get_db)],
    cliente_id: int = Path(..., description="ID del cliente a obtener", gt=0)
):
    """
    Obtiene los detalles de un cliente específico por su ID.

    - **Requiere permiso:** `leer:cliente`.
    """
    logger.debug(f"[Permiso: leer:cliente] Solicitud para obtener cliente ID: {cliente_id}")
    # El servicio maneja la lógica de búsqueda y el error 404
    cliente = cliente_service.get_cliente_by_id_service(db=db, cliente_id=cliente_id)
    return cliente

# --- Endpoint para Actualizar un Cliente ---
# Usaremos PUT para reemplazo total o parcial (depende de cómo se use ClienteUpdate)
# o PATCH para actualización parcial explícita. PUT es más simple aquí.
@router.put(
    "/{cliente_id}", # Ruta: PUT /api/v1/clientes/{cliente_id}
    response_model=ClienteRead,
    summary="Actualizar un cliente",
    dependencies=[Depends(require_permission("actualizar:cliente"))], # Aplicar permiso
    responses={
        404: {"description": "Cliente no encontrado"},
        409: {"description": "Conflicto, email o identificación ya existen en otro cliente"},
        403: {"description": "Permiso insuficiente"},
        400: {"description": "Datos de entrada inválidos (validación schema)"}
    }
)
def update_existing_cliente(
    *,
    db: Annotated[Session, Depends(get_db)],
    cliente_id: int = Path(..., description="ID del cliente a actualizar", gt=0),
    cliente_in: ClienteUpdate # Cuerpo con los campos a actualizar
):
    """
    Actualiza la información de un cliente existente.
    Solo los campos proporcionados en el cuerpo de la solicitud serán actualizados.

    - **Requiere permiso:** `actualizar:cliente`.
    """
    logger.info(f"[Permiso: actualizar:cliente] Solicitud para actualizar cliente ID: {cliente_id}")
    # El servicio maneja la búsqueda (404), validación de conflictos (409) y actualización
    updated_cliente = cliente_service.update_cliente_service(
        db=db, cliente_id=cliente_id, cliente_in=cliente_in
    )
    return updated_cliente

# --- Endpoint para Eliminar un Cliente ---
@router.delete(
    "/{cliente_id}", # Ruta: DELETE /api/v1/clientes/{cliente_id}
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un cliente",
    dependencies=[Depends(require_permission("eliminar:cliente"))], # Aplicar permiso
    responses={
        404: {"description": "Cliente no encontrado"},
        409: {"description": "Conflicto, el cliente tiene pedidos/facturas asociadas"},
        403: {"description": "Permiso insuficiente"}
    }
)
def delete_existing_cliente(
    *,
    db: Annotated[Session, Depends(get_db)],
    cliente_id: int = Path(..., description="ID del cliente a eliminar", gt=0)
):
    """
    Elimina un cliente existente.
    Falla si el cliente tiene pedidos o facturas asociados (debido a restricciones FK).

    - **Requiere permiso:** `eliminar:cliente`.
    """
    logger.warning(f"[Permiso: eliminar:cliente] Solicitud para eliminar cliente ID: {cliente_id}") # Warning para delete
    # El servicio maneja la búsqueda (404) y el error de integridad (409)
    cliente_service.delete_cliente_service(db=db, cliente_id=cliente_id)
    # Si el servicio no lanzó excepción, la eliminación fue exitosa (o el cliente no existía, lo cual es manejado por el 404 del get interno)
    return Response(status_code=status.HTTP_204_NO_CONTENT) # Respuesta estándar para DELETE exitoso