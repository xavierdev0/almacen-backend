# app/services/inventory_service.py
import logging
from typing import Optional, Sequence, Dict, Any
from decimal import Decimal

from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError # Para capturar errores del repo

# Importar Repositorio, Modelos y Schemas
from app.repositories import inventory_repository
from app.models.inventory_models import (
    MaterialDimensional,
    StockItemDimensional,
    MaterialConsumible,
    MaterialSimple
)
from app.schemas.inventory_schema import (
    MaterialDimensionalCreate, MaterialDimensionalUpdate,
    MaterialConsumibleCreate, MaterialConsumibleUpdate,
    MaterialSimpleCreate, MaterialSimpleUpdate,
    StockItemDimensionalCreate # Aunque no la usemos toda ahora
)

logger = logging.getLogger(__name__)

# =============================================
#  Servicios para MaterialDimensional
# =============================================

def create_material_dimensional_service(db: Session, *, mat_dim_in: MaterialDimensionalCreate) -> MaterialDimensional:
    """Crea un nuevo tipo de material dimensional, validando SKU."""
    logger.info(f"Servicio: Intentando crear MaterialDimensional SKU: {mat_dim_in.sku}")
    # Validar SKU duplicado ANTES de intentar crear
    existing = inventory_repository.get_material_dimensional_by_sku(db, sku=mat_dim_in.sku)
    if existing:
        logger.warning(f"Conflicto: SKU '{mat_dim_in.sku}' ya existe para MaterialDimensional.")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El SKU '{mat_dim_in.sku}' ya está registrado para un material dimensional."
        )
    try:
        mat_dim_data = MaterialDimensional.model_validate(mat_dim_in)
        new_mat_dim = inventory_repository.create_material_dimensional(db=db, mat_dim_data=mat_dim_data)
        return new_mat_dim
    except IntegrityError: # Captura por si acaso (race condition)
        db.rollback()
        logger.error(f"Error de Integridad (inesperado) al crear MaterialDimensional SKU '{mat_dim_in.sku}'.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al crear MaterialDimensional: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear material dimensional.")

def get_material_dimensional_by_id_service(db: Session, *, mat_dim_id: int) -> MaterialDimensional:
    """Obtiene un tipo de material dimensional por ID."""
    logger.debug(f"Servicio: Buscando MaterialDimensional ID: {mat_dim_id}")
    mat_dim = inventory_repository.get_material_dimensional_by_id(db=db, mat_dim_id=mat_dim_id)
    if not mat_dim:
        logger.warning(f"Servicio: MaterialDimensional ID {mat_dim_id} no encontrado.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Material dimensional con ID {mat_dim_id} no encontrado.")
    return mat_dim

def list_materiales_dimensionales_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialDimensional]:
    """Lista tipos de materiales dimensionales."""
    logger.debug(f"Servicio: Listando materiales dimensionales, skip={skip}, limit={limit}")
    try:
        return inventory_repository.list_materiales_dimensionales(db=db, skip=skip, limit=limit)
    except Exception as e:
        logger.error(f"Error inesperado en servicio al listar MaterialDimensional: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar materiales dimensionales.")

def update_material_dimensional_service(db: Session, *, mat_dim_id: int, mat_dim_in: MaterialDimensionalUpdate) -> MaterialDimensional:
    """Actualiza un tipo de material dimensional."""
    logger.info(f"Servicio: Intentando actualizar MaterialDimensional ID: {mat_dim_id}")
    db_mat_dim = get_material_dimensional_by_id_service(db=db, mat_dim_id=mat_dim_id) # Maneja 404
    update_data = mat_dim_in.model_dump(exclude_unset=True)
    if not update_data:
        logger.warning(f"Servicio: No se proporcionaron datos para actualizar MaterialDimensional ID {mat_dim_id}.")
        return db_mat_dim # Devolver sin cambios si no hay nada que actualizar
    try:
        # SKU no debe actualizarse a través de este método general
        if "sku" in update_data:
            logger.warning(f"Intento de actualizar SKU para MaterialDimensional ID {mat_dim_id} ignorado.")
            del update_data["sku"]

        return inventory_repository.update_material_dimensional(db=db, db_mat_dim=db_mat_dim, update_data=update_data)
    except Exception as e: # El repo maneja IntegrityError si ocurre
        # No necesitamos capturar IntegrityError aquí de nuevo si el repo lo relanza
        db.rollback()
        logger.error(f"Error inesperado en servicio al actualizar MaterialDimensional ID {mat_dim_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar material dimensional.")

def delete_material_dimensional_service(db: Session, *, mat_dim_id: int) -> MaterialDimensional:
    """Elimina un tipo de material dimensional."""
    logger.warning(f"Servicio: Intentando eliminar MaterialDimensional ID: {mat_dim_id}")
    db_mat_dim = get_material_dimensional_by_id_service(db=db, mat_dim_id=mat_dim_id) # Maneja 404
    try:
        deleted_mat = inventory_repository.delete_material_dimensional(db=db, mat_dim_id=mat_dim_id)
        # El repo ya devuelve None si no existe, pero get_ lo valida antes
        return deleted_mat # type: ignore # Ignorar posible None si confiamos en get_
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de Integridad al eliminar MaterialDimensional ID {mat_dim_id}. Probablemente referenciado: {e}")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se puede eliminar el material dimensional ID {mat_dim_id} porque está en uso (stock existente).")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al eliminar MaterialDimensional ID {mat_dim_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar material dimensional.")


# =============================================
#  Servicios para MaterialConsumible
# =============================================
# (Implementación análoga a MaterialDimensional, ajustando nombres y validando SKU)

def create_material_consumible_service(db: Session, *, mat_cons_in: MaterialConsumibleCreate) -> MaterialConsumible:
    logger.info(f"Servicio: Intentando crear MaterialConsumible SKU: {mat_cons_in.sku}")
    existing = inventory_repository.get_material_consumible_by_sku(db, sku=mat_cons_in.sku)
    if existing:
        logger.warning(f"Conflicto: SKU '{mat_cons_in.sku}' ya existe para MaterialConsumible.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El SKU '{mat_cons_in.sku}' ya está registrado para un material consumible.")
    try:
        mat_cons_data = MaterialConsumible.model_validate(mat_cons_in)
        # Inicializar stock_actual a 0 si no se proporciona un valor inicial explícito
        if mat_cons_data.stock_actual is None: mat_cons_data.stock_actual = Decimal("0.0")
        return inventory_repository.create_material_consumible(db=db, mat_cons_data=mat_cons_data)
    except IntegrityError: db.rollback(); raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar.")
    except Exception as e: db.rollback(); logger.error(f"Error crear MatCons: {e}", exc_info=True); raise HTTPException(status_code=500)

def get_material_consumible_by_id_service(db: Session, *, mat_cons_id: int) -> MaterialConsumible:
    logger.debug(f"Servicio: Buscando MaterialConsumible ID: {mat_cons_id}")
    mat = inventory_repository.get_material_consumible_by_id(db=db, mat_cons_id=mat_cons_id)
    if not mat: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Material consumible ID {mat_cons_id} no encontrado.")
    return mat

def list_materiales_consumibles_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialConsumible]:
    logger.debug(f"Servicio: Listando materiales consumibles, skip={skip}, limit={limit}")
    try: return inventory_repository.list_materiales_consumibles(db=db, skip=skip, limit=limit)
    except Exception as e: logger.error(f"Error listar MatCons: {e}", exc_info=True); raise HTTPException(status_code=500)

def update_material_consumible_service(db: Session, *, mat_cons_id: int, mat_cons_in: MaterialConsumibleUpdate) -> MaterialConsumible:
    logger.info(f"Servicio: Intentando actualizar MaterialConsumible ID: {mat_cons_id}")
    db_mat = get_material_consumible_by_id_service(db=db, mat_cons_id=mat_cons_id)
    update_data = mat_cons_in.model_dump(exclude_unset=True)
    if not update_data: return db_mat
    try:
        update_data.pop("sku", None) # Ignorar SKU
        update_data.pop("stock_actual", None) # Ignorar stock_actual
        return inventory_repository.update_material_consumible(db=db, db_mat_cons=db_mat, update_data=update_data)
    except Exception as e: db.rollback(); logger.error(f"Error update MatCons ID {mat_cons_id}: {e}", exc_info=True); raise HTTPException(status_code=500)

def delete_material_consumible_service(db: Session, *, mat_cons_id: int) -> MaterialConsumible:
    logger.warning(f"Servicio: Intentando eliminar MaterialConsumible ID: {mat_cons_id}")
    db_mat = get_material_consumible_by_id_service(db=db, mat_cons_id=mat_cons_id)
    try:
        deleted = inventory_repository.delete_material_consumible(db=db, mat_cons_id=mat_cons_id)
        return deleted # type: ignore
    except IntegrityError: db.rollback(); raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se puede eliminar MatCons ID {mat_cons_id}, está en uso.")
    except Exception as e: db.rollback(); logger.error(f"Error delete MatCons ID {mat_cons_id}: {e}", exc_info=True); raise HTTPException(status_code=500)

def adjust_stock_consumible_service(db: Session, *, mat_cons_id: int, change_amount: Decimal) -> MaterialConsumible:
    """Ajusta el stock de un material consumible."""
    logger.info(f"Servicio: Ajustando stock MaterialConsumible ID {mat_cons_id}, cambio: {change_amount}")
    # get_material_consumible_by_id_service ya maneja 404
    get_material_consumible_by_id_service(db=db, mat_cons_id=mat_cons_id)
    try:
        updated_mat = inventory_repository.adjust_stock_consumible(db=db, mat_cons_id=mat_cons_id, change_amount=change_amount)
        return updated_mat # type: ignore # Repo devuelve Optional, pero ya verificamos existencia
    except ValueError as ve: # Captura error de stock negativo del repo
        logger.error(f"Error de valor al ajustar stock MatCons ID {mat_cons_id}: {ve}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e:
        logger.error(f"Error inesperado al ajustar stock MatCons ID {mat_cons_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al ajustar stock.")


# =============================================
#  Servicios para MaterialSimple
# =============================================
# (Implementación análoga a MaterialConsumible)
# ...

def create_material_simple_service(db: Session, *, mat_simp_in: MaterialSimpleCreate) -> MaterialSimple:
    logger.info(f"Servicio: Intentando crear MaterialSimple SKU: {mat_simp_in.sku}")
    existing = inventory_repository.get_material_simple_by_sku(db, sku=mat_simp_in.sku)
    if existing:
        logger.warning(f"Conflicto: SKU '{mat_simp_in.sku}' ya existe para MaterialSimple.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El SKU '{mat_simp_in.sku}' ya está registrado para un material simple.")
    try:
        mat_simp_data = MaterialSimple.model_validate(mat_simp_in)
        if mat_simp_data.stock_actual is None: mat_simp_data.stock_actual = Decimal("0.0")
        return inventory_repository.create_material_simple(db=db, mat_simp_data=mat_simp_data)
    except IntegrityError: db.rollback(); raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar.")
    except Exception as e: db.rollback(); logger.error(f"Error crear MatSimp: {e}", exc_info=True); raise HTTPException(status_code=500)

def get_material_simple_by_id_service(db: Session, *, mat_simp_id: int) -> MaterialSimple:
    logger.debug(f"Servicio: Buscando MaterialSimple ID: {mat_simp_id}")
    mat = inventory_repository.get_material_simple_by_id(db=db, mat_simp_id=mat_simp_id)
    if not mat: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Material simple ID {mat_simp_id} no encontrado.")
    return mat

def list_materiales_simples_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialSimple]:
    logger.debug(f"Servicio: Listando materiales simples, skip={skip}, limit={limit}")
    try: return inventory_repository.list_materiales_simples(db=db, skip=skip, limit=limit)
    except Exception as e: logger.error(f"Error listar MatSimp: {e}", exc_info=True); raise HTTPException(status_code=500)

def update_material_simple_service(db: Session, *, mat_simp_id: int, mat_simp_in: MaterialSimpleUpdate) -> MaterialSimple:
    logger.info(f"Servicio: Intentando actualizar MaterialSimple ID: {mat_simp_id}")
    db_mat = get_material_simple_by_id_service(db=db, mat_simp_id=mat_simp_id)
    update_data = mat_simp_in.model_dump(exclude_unset=True)
    if not update_data: return db_mat
    try:
        update_data.pop("sku", None); update_data.pop("stock_actual", None)
        return inventory_repository.update_material_simple(db=db, db_mat_simp=db_mat, update_data=update_data)
    except Exception as e: db.rollback(); logger.error(f"Error update MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise HTTPException(status_code=500)

def delete_material_simple_service(db: Session, *, mat_simp_id: int) -> MaterialSimple:
    logger.warning(f"Servicio: Intentando eliminar MaterialSimple ID: {mat_simp_id}")
    db_mat = get_material_simple_by_id_service(db=db, mat_simp_id=mat_simp_id)
    try:
        deleted = inventory_repository.delete_material_simple(db=db, mat_simp_id=mat_simp_id)
        return deleted # type: ignore
    except IntegrityError: db.rollback(); raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se puede eliminar MatSimp ID {mat_simp_id}, está en uso.")
    except Exception as e: db.rollback(); logger.error(f"Error delete MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise HTTPException(status_code=500)

def adjust_stock_simple_service(db: Session, *, mat_simp_id: int, change_amount: Decimal) -> MaterialSimple:
    """Ajusta el stock de un material simple."""
    logger.info(f"Servicio: Ajustando stock MaterialSimple ID {mat_simp_id}, cambio: {change_amount}")
    get_material_simple_by_id_service(db=db, mat_simp_id=mat_simp_id) # Verifica 404
    try:
        updated_mat = inventory_repository.adjust_stock_simple(db=db, mat_simp_id=mat_simp_id, change_amount=change_amount)
        return updated_mat # type: ignore
    except ValueError as ve: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e: logger.error(f"Error ajustando stock MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise HTTPException(status_code=500)


# =============================================
#  Servicios para StockItemDimensional (Base)
# =============================================

def create_stock_item_service(db: Session, *, item_in: StockItemDimensionalCreate) -> StockItemDimensional:
    """Crea una nueva pieza física de stock dimensional."""
    logger.info(f"Servicio: Intentando crear StockItemDimensional para MaterialID: {item_in.material_dimensional_id}")
    # Validar que el material dimensional asociado existe
    get_material_dimensional_by_id_service(db=db, mat_dim_id=item_in.material_dimensional_id) # Maneja 404

    # Validar que el item padre existe si se proporciona
    if item_in.stock_item_padre_id is not None:
        get_stock_item_by_id_service(db=db, item_id=item_in.stock_item_padre_id) # Maneja 404

    # TODO: Validar si es merma, si las dimensiones son menores o iguales al padre (si existe padre)

    try:
        item_data = StockItemDimensional.model_validate(item_in)
        # Establecer estado inicial por defecto si no viene en el schema (o validar si viene)
        if not item_data.estado: item_data.estado = "DISPONIBLE"
        # Asegurarse que es_merma sea False por defecto si no se especifica
        if item_data.es_merma is None: item_data.es_merma = False

        new_item = inventory_repository.create_stock_item(db=db, item_data=item_data)
        return new_item
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al crear StockItemDimensional: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear item de stock dimensional.")

def get_stock_item_by_id_service(db: Session, *, item_id: int) -> StockItemDimensional:
    """Obtiene una pieza de stock dimensional por ID."""
    logger.debug(f"Servicio: Buscando StockItemDimensional ID: {item_id}")
    item = inventory_repository.get_stock_item_by_id(db=db, item_id=item_id)
    if not item:
        logger.warning(f"Servicio: StockItemDimensional ID {item_id} no encontrado.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item de stock dimensional con ID {item_id} no encontrado.")
    return item

def list_stock_items_service(
    db: Session, *,
    skip: int = 0, limit: int = 100,
    material_dimensional_id: Optional[int] = None,
    estado: Optional[str] = None,
    min_longitud: Optional[Decimal] = None,
    min_ancho: Optional[Decimal] = None
) -> Sequence[StockItemDimensional]:
    """Lista piezas de stock dimensional con filtros."""
    logger.debug(f"Servicio: Listando StockItemDimensional con filtros - MaterialID: {material_dimensional_id}, Estado: {estado}, MinL: {min_longitud}, MinA: {min_ancho}")
    try:
        return inventory_repository.list_stock_items(
            db=db, skip=skip, limit=limit,
            material_dimensional_id=material_dimensional_id,
            estado=estado, min_longitud=min_longitud, min_ancho=min_ancho
        )
    except Exception as e:
        logger.error(f"Error inesperado en servicio al listar StockItemDimensional: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar items de stock dimensional.")

# update_stock_item_service y delete_stock_item_service se pueden implementar
# más adelante o según se necesiten operaciones específicas (cambiar estado, etc.)