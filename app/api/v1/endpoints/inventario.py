# app/api/v1/endpoints/inventario.py
import logging
from typing import List, Optional, Annotated, Sequence
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Body, Response
from sqlmodel import Session
from pydantic import BaseModel, Field

# Importar dependencias, servicios y schemas necesarios
from app.api.deps import get_db, require_permission
from app.services import inventory_service
from app.schemas.inventory_schema import (
    MaterialDimensionalCreate, MaterialDimensionalUpdate, MaterialDimensionalRead,
    MaterialConsumibleCreate, MaterialConsumibleUpdate, MaterialConsumibleRead,
    MaterialSimpleCreate, MaterialSimpleUpdate, MaterialSimpleRead, StockAdjustRequest,
    StockItemDimensionalCreate, StockItemDimensionalRead,
)

logger = logging.getLogger(__name__)

# --- Router Principal para Inventario ---
router = APIRouter(
    prefix="/inventario",
    tags=["Inventario"],
    responses={
        404: {"description": "Recurso de inventario no encontrado"},
        403: {"description": "Permiso insuficiente"},
        409: {"description": "Conflicto de datos (ej: SKU duplicado, dependencia)"}
    }
)

# --- Sub-Router para Tipos de Material Dimensional ---
router_mat_dim = APIRouter(prefix="/materiales-dimensionales")

@router_mat_dim.post(
    "",
    response_model=MaterialDimensionalRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear tipo de Material Dimensional",
    dependencies=[Depends(require_permission("gestionar:material_definicion"))]
)
def create_material_dimensional(
    *, # <--- Asegurar que los siguientes son kwargs
    db: Annotated[Session, Depends(get_db)],
    mat_dim_in: MaterialDimensionalCreate
):
    """Crea un nuevo tipo de material dimensional (ej: planchas, tablones)."""
    logger.info(f"[Permiso: gestionar:material_definicion] Crear MaterialDimensional SKU: {mat_dim_in.sku}")
    return inventory_service.create_material_dimensional_service(db=db, mat_dim_in=mat_dim_in)

@router_mat_dim.get(
    "",
    response_model=List[MaterialDimensionalRead],
    summary="Listar tipos de Material Dimensional",
    dependencies=[Depends(require_permission("leer:material_definicion"))]
)
def list_materiales_dimensionales(
    # Los parámetros de Query van primero, luego las dependencias
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Lista los tipos de materiales dimensionales definidos."""
    logger.debug(f"[Permiso: leer:material_definicion] Listar MaterialDimensional")
    return inventory_service.list_materiales_dimensionales_service(db=db, skip=skip, limit=limit)

@router_mat_dim.get(
    "/{mat_dim_id}",
    response_model=MaterialDimensionalRead,
    summary="Obtener tipo de Material Dimensional por ID",
    dependencies=[Depends(require_permission("leer:material_definicion"))]
)
def get_material_dimensional(
    # El parámetro de Path va primero
    mat_dim_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Obtiene detalles de un tipo específico de material dimensional."""
    logger.debug(f"[Permiso: leer:material_definicion] Obtener MaterialDimensional ID: {mat_dim_id}")
    return inventory_service.get_material_dimensional_by_id_service(db=db, mat_dim_id=mat_dim_id)

@router_mat_dim.put(
    "/{mat_dim_id}",
    response_model=MaterialDimensionalRead,
    summary="Actualizar tipo de Material Dimensional",
    dependencies=[Depends(require_permission("gestionar:material_definicion"))]
)
def update_material_dimensional(
    # Path param primero
    mat_dim_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    mat_dim_in: MaterialDimensionalUpdate # Body al final
):
    """Actualiza la definición de un tipo de material dimensional."""
    logger.info(f"[Permiso: gestionar:material_definicion] Actualizar MaterialDimensional ID: {mat_dim_id}")
    return inventory_service.update_material_dimensional_service(db=db, mat_dim_id=mat_dim_id, mat_dim_in=mat_dim_in)

@router_mat_dim.delete(
    "/{mat_dim_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar tipo de Material Dimensional",
    dependencies=[Depends(require_permission("gestionar:material_definicion"))]
)
def delete_material_dimensional(
    # Path param primero
    mat_dim_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Elimina un tipo de material dimensional (falla si está en uso)."""
    logger.warning(f"[Permiso: gestionar:material_definicion] Eliminar MaterialDimensional ID: {mat_dim_id}")
    inventory_service.delete_material_dimensional_service(db=db, mat_dim_id=mat_dim_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- Sub-Router para Tipos de Material Consumible ---
router_mat_cons = APIRouter(prefix="/materiales-consumibles")

@router_mat_cons.post("", response_model=MaterialConsumibleRead, status_code=status.HTTP_201_CREATED, summary="Crear tipo de Material Consumible", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def create_material_consumible(
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    mat_cons_in: MaterialConsumibleCreate
):
    """Crea un nuevo tipo de material consumible."""
    logger.info(f"[Permiso: gestionar:material_definicion] Crear MaterialConsumible SKU: {mat_cons_in.sku}")
    return inventory_service.create_material_consumible_service(db=db, mat_cons_in=mat_cons_in)

@router_mat_cons.get("", response_model=List[MaterialConsumibleRead], summary="Listar tipos de Material Consumible", dependencies=[Depends(require_permission("leer:material_definicion"))])
def list_materiales_consumibles(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Lista los tipos de materiales consumibles definidos."""
    logger.debug(f"[Permiso: leer:material_definicion] Listar MaterialConsumible")
    return inventory_service.list_materiales_consumibles_service(db=db, skip=skip, limit=limit)

@router_mat_cons.get("/{mat_cons_id}", response_model=MaterialConsumibleRead, summary="Obtener tipo de Material Consumible por ID", dependencies=[Depends(require_permission("leer:material_definicion"))])
def get_material_consumible(
    mat_cons_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Obtiene detalles de un tipo específico de material consumible."""
    logger.debug(f"[Permiso: leer:material_definicion] Obtener MaterialConsumible ID: {mat_cons_id}")
    return inventory_service.get_material_consumible_by_id_service(db=db, mat_cons_id=mat_cons_id)

@router_mat_cons.put("/{mat_cons_id}", response_model=MaterialConsumibleRead, summary="Actualizar tipo de Material Consumible", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def update_material_consumible(
    mat_cons_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    mat_cons_in: MaterialConsumibleUpdate
):
    """Actualiza la definición de un tipo de material consumible (no el stock)."""
    logger.info(f"[Permiso: gestionar:material_definicion] Actualizar MaterialConsumible ID: {mat_cons_id}")
    return inventory_service.update_material_consumible_service(db=db, mat_cons_id=mat_cons_id, mat_cons_in=mat_cons_in)

@router_mat_cons.delete("/{mat_cons_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar tipo de Material Consumible", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def delete_material_consumible(
    mat_cons_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Elimina un tipo de material consumible (falla si está en uso)."""
    logger.warning(f"[Permiso: gestionar:material_definicion] Eliminar MaterialConsumible ID: {mat_cons_id}")
    inventory_service.delete_material_consumible_service(db=db, mat_cons_id=mat_cons_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_mat_cons.post("/{mat_cons_id}/ajustar-stock", response_model=MaterialConsumibleRead, summary="Ajustar stock de Material Consumible", dependencies=[Depends(require_permission("ajustar:stock"))])
def adjust_stock_consumible(
    mat_cons_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    adjust_in: StockAdjustRequest = Body(...) # Body al final
):
    """Ajusta la cantidad de stock actual para un material consumible."""
    logger.info(f"[Permiso: ajustar:stock] Ajustar stock MaterialConsumible ID: {mat_cons_id}, Cambio: {adjust_in.change_amount}")
    return inventory_service.adjust_stock_consumible_service(db=db, mat_cons_id=mat_cons_id, change_amount=adjust_in.change_amount)


# --- Sub-Router para Tipos de Material Simple ---
router_mat_simp = APIRouter(prefix="/materiales-simples")

@router_mat_simp.post("", response_model=MaterialSimpleRead, status_code=status.HTTP_201_CREATED, summary="Crear tipo de Material Simple", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def create_material_simple(
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    mat_simp_in: MaterialSimpleCreate
):
    """Crea un nuevo tipo de material simple."""
    logger.info(f"[Permiso: gestionar:material_definicion] Crear MaterialSimple SKU: {mat_simp_in.sku}")
    return inventory_service.create_material_simple_service(db=db, mat_simp_in=mat_simp_in)

@router_mat_simp.get("", response_model=List[MaterialSimpleRead], summary="Listar tipos de Material Simple", dependencies=[Depends(require_permission("leer:material_definicion"))])
def list_materiales_simples(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Lista los tipos de materiales simples definidos."""
    logger.debug(f"[Permiso: leer:material_definicion] Listar MaterialSimple")
    return inventory_service.list_materiales_simples_service(db=db, skip=skip, limit=limit)

@router_mat_simp.get("/{mat_simp_id}", response_model=MaterialSimpleRead, summary="Obtener tipo de Material Simple por ID", dependencies=[Depends(require_permission("leer:material_definicion"))])
def get_material_simple(
    mat_simp_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Obtiene detalles de un tipo específico de material simple."""
    logger.debug(f"[Permiso: leer:material_definicion] Obtener MaterialSimple ID: {mat_simp_id}")
    return inventory_service.get_material_simple_by_id_service(db=db, mat_simp_id=mat_simp_id)

@router_mat_simp.put("/{mat_simp_id}", response_model=MaterialSimpleRead, summary="Actualizar tipo de Material Simple", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def update_material_simple(
    mat_simp_id: int = Path(..., gt=0), # <--- CORREGIDO: Orden
    *,                                  # <--- CORREGIDO: Añadido *
    db: Annotated[Session, Depends(get_db)],
    mat_simp_in: MaterialSimpleUpdate
):
    """Actualiza la definición de un tipo de material simple (no el stock)."""
    logger.info(f"[Permiso: gestionar:material_definicion] Actualizar MaterialSimple ID: {mat_simp_id}")
    return inventory_service.update_material_simple_service(db=db, mat_simp_id=mat_simp_id, mat_simp_in=mat_simp_in)

@router_mat_simp.delete("/{mat_simp_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar tipo de Material Simple", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def delete_material_simple(
    mat_simp_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Elimina un tipo de material simple (falla si está en uso)."""
    logger.warning(f"[Permiso: gestionar:material_definicion] Eliminar MaterialSimple ID: {mat_simp_id}")
    inventory_service.delete_material_simple_service(db=db, mat_simp_id=mat_simp_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router_mat_simp.post("/{mat_simp_id}/ajustar-stock", response_model=MaterialSimpleRead, summary="Ajustar stock de Material Simple", dependencies=[Depends(require_permission("ajustar:stock"))])
def adjust_stock_simple(
    mat_simp_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    adjust_in: StockAdjustRequest = Body(...)
):
    """Ajusta la cantidad de stock actual para un material simple."""
    logger.info(f"[Permiso: ajustar:stock] Ajustar stock MaterialSimple ID: {mat_simp_id}, Cambio: {adjust_in.change_amount}")
    return inventory_service.adjust_stock_simple_service(db=db, mat_simp_id=mat_simp_id, change_amount=adjust_in.change_amount)


# --- Sub-Router para Items de Stock Dimensional ---
router_stock_dim = APIRouter(prefix="/stock-items-dimensionales")

@router_stock_dim.post(
    "",
    response_model=StockItemDimensionalRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear/Registrar nueva pieza de Stock Dimensional",
    dependencies=[Depends(require_permission("ajustar:stock"))]
)
def create_stock_item_dimensional(
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    item_in: StockItemDimensionalCreate
):
    """Registra una nueva pieza física de material dimensional en el inventario."""
    logger.info(f"[Permiso: ajustar:stock] Crear StockItemDimensional para MaterialID: {item_in.material_dimensional_id}")
    return inventory_service.create_stock_item_service(db=db, item_in=item_in)

@router_stock_dim.get(
    "",
    response_model=List[StockItemDimensionalRead],
    summary="Listar piezas de Stock Dimensional (con filtros)",
    dependencies=[Depends(require_permission("leer:stock"))]
)
def list_stock_items_dimensionales(
    # Parámetros Query primero
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    material_dimensional_id: Optional[int] = Query(None, description="Filtrar por ID de tipo de material"),
    estado: Optional[str] = Query(None, description="Filtrar por estado (ej: DISPONIBLE, RESERVADO)"),
    min_longitud: Optional[Decimal] = Query(None, description="Filtrar por longitud mínima"),
    min_ancho: Optional[Decimal] = Query(None, description="Filtrar por ancho mínimo"),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Lista las piezas físicas de stock dimensional, permitiendo filtrar por criterios."""
    logger.debug(f"[Permiso: leer:stock] Listar StockItemDimensional con filtros")
    return inventory_service.list_stock_items_service(
        db=db, skip=skip, limit=limit,
        material_dimensional_id=material_dimensional_id, estado=estado,
        min_longitud=min_longitud, min_ancho=min_ancho
    )

@router_stock_dim.get(
    "/{item_id}",
    response_model=StockItemDimensionalRead,
    summary="Obtener una pieza de Stock Dimensional por ID",
    dependencies=[Depends(require_permission("leer:stock"))]
)
def get_stock_item_dimensional(
    item_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Obtiene los detalles de una pieza específica de stock dimensional."""
    logger.debug(f"[Permiso: leer:stock] Obtener StockItemDimensional ID: {item_id}")
    return inventory_service.get_stock_item_by_id_service(db=db, item_id=item_id)

# PUT/DELETE para StockItemDimensional se añadirán después si son necesarios.

# --- Incluir Sub-Routers en el Router Principal de Inventario ---
router.include_router(router_mat_dim)
router.include_router(router_mat_cons)
router.include_router(router_mat_simp)
router.include_router(router_stock_dim)