# app/repositories/inventory_repository.py
import logging
from typing import Optional, Sequence, Union, Dict, Any, List
from decimal import Decimal

from sqlmodel import Session, select, SQLModel, and_ # Importar 'and_'
from sqlalchemy.exc import IntegrityError

# Importar Modelos
from app.models.inventory_models import (
    MaterialDimensional,
    StockItemDimensional,
    MaterialConsumible,
    MaterialSimple
)

logger = logging.getLogger(__name__)

# =======================================
# Repositorio para MaterialDimensional
# =======================================

def get_material_dimensional_by_id(db: Session, *, mat_dim_id: int) -> Optional[MaterialDimensional]:
    """Obtiene un tipo de material dimensional por ID."""
    try:
        return db.get(MaterialDimensional, mat_dim_id)
    except Exception as e:
        logger.error(f"Error obteniendo MaterialDimensional ID {mat_dim_id}: {e}", exc_info=True)
        raise

def get_material_dimensional_by_sku(db: Session, *, sku: str) -> Optional[MaterialDimensional]:
    """Obtiene un tipo de material dimensional por SKU."""
    try:
        statement = select(MaterialDimensional).where(MaterialDimensional.sku == sku)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo MaterialDimensional SKU '{sku}': {e}", exc_info=True)
        raise

def list_materiales_dimensionales(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialDimensional]:
    """Lista tipos de materiales dimensionales."""
    try:
        statement = select(MaterialDimensional).offset(skip).limit(limit).order_by(MaterialDimensional.id)
        return db.exec(statement).all()
    except Exception as e:
        logger.error(f"Error listando MaterialDimensional: {e}", exc_info=True)
        raise

def create_material_dimensional(db: Session, *, mat_dim_data: MaterialDimensional) -> MaterialDimensional:
    """Crea un nuevo tipo de material dimensional."""
    db_mat_dim = mat_dim_data
    try:
        db.add(db_mat_dim)
        db.commit()
        db.refresh(db_mat_dim)
        logger.info(f"MaterialDimensional creado: ID={db_mat_dim.id}, SKU='{db_mat_dim.sku}'")
        return db_mat_dim
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"Error de integridad al crear MaterialDimensional SKU '{db_mat_dim.sku}': {e}")
        raise e # Relanzar para que el servicio maneje 409
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado creando MaterialDimensional SKU '{db_mat_dim.sku}': {e}", exc_info=True)
        raise

def update_material_dimensional(db: Session, *, db_mat_dim: MaterialDimensional, update_data: Dict[str, Any]) -> MaterialDimensional:
    """Actualiza un tipo de material dimensional."""
    try:
        # Evitar actualizar SKU si se incluye accidentalmente
        update_data.pop("sku", None)
        if not update_data: return db_mat_dim # Nada que actualizar
        db_mat_dim.sqlmodel_update(update_data)
        db.add(db_mat_dim)
        db.commit()
        db.refresh(db_mat_dim)
        logger.info(f"MaterialDimensional actualizado: ID={db_mat_dim.id}")
        return db_mat_dim
    except IntegrityError as e: # Podría ocurrir si se intentara cambiar SKU a uno existente (aunque lo prevenimos arriba)
        db.rollback()
        logger.warning(f"Error de integridad al actualizar MaterialDimensional ID {db_mat_dim.id}: {e}")
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado actualizando MaterialDimensional ID {db_mat_dim.id}: {e}", exc_info=True)
        raise

def delete_material_dimensional(db: Session, *, mat_dim_id: int) -> Optional[MaterialDimensional]:
    """Elimina un tipo de material dimensional."""
    try:
        db_mat_dim = db.get(MaterialDimensional, mat_dim_id)
        if not db_mat_dim: return None
        logger.warning(f"Intentando eliminar MaterialDimensional: ID={mat_dim_id}, SKU='{db_mat_dim.sku}'")
        db.delete(db_mat_dim)
        db.commit()
        logger.warning(f"MaterialDimensional eliminado: ID={mat_dim_id}")
        return db_mat_dim
    except IntegrityError as e: # Fallará si hay StockItemDimensional referenciándolo
        db.rollback()
        logger.error(f"Error de integridad al eliminar MaterialDimensional ID {mat_dim_id}. Probablemente referenciado por stock: {e}")
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado eliminando MaterialDimensional ID {mat_dim_id}: {e}", exc_info=True)
        raise

# =======================================
# Repositorio para MaterialConsumible
# =======================================
# (Similar a MaterialDimensional: get_by_id, get_by_sku, list, create, update, delete)
# ... Implementación análoga ...

def get_material_consumible_by_id(db: Session, *, mat_cons_id: int) -> Optional[MaterialConsumible]:
    try: return db.get(MaterialConsumible, mat_cons_id)
    except Exception as e: logger.error(f"Error get MatCons ID {mat_cons_id}: {e}", exc_info=True); raise

def get_material_consumible_by_sku(db: Session, *, sku: str) -> Optional[MaterialConsumible]:
    try: return db.exec(select(MaterialConsumible).where(MaterialConsumible.sku == sku)).first()
    except Exception as e: logger.error(f"Error get MatCons SKU {sku}: {e}", exc_info=True); raise

def list_materiales_consumibles(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialConsumible]:
    try: return db.exec(select(MaterialConsumible).offset(skip).limit(limit).order_by(MaterialConsumible.id)).all()
    except Exception as e: logger.error(f"Error list MatCons: {e}", exc_info=True); raise

def create_material_consumible(db: Session, *, mat_cons_data: MaterialConsumible) -> MaterialConsumible:
    db_mat = mat_cons_data
    try:
        db.add(db_mat); db.commit(); db.refresh(db_mat)
        logger.info(f"MaterialConsumible creado: ID={db_mat.id}, SKU='{db_mat.sku}'")
        return db_mat
    except IntegrityError as e: db.rollback(); logger.warning(f"IntegrityError create MatCons SKU '{db_mat.sku}': {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error create MatCons SKU '{db_mat.sku}': {e}", exc_info=True); raise

def update_material_consumible(db: Session, *, db_mat_cons: MaterialConsumible, update_data: Dict[str, Any]) -> MaterialConsumible:
    """Actualiza campos definitorios (nombre, desc, etc.), no stock_actual."""
    try:
        update_data.pop("sku", None)
        update_data.pop("stock_actual", None) # No actualizar stock aquí
        if not update_data: return db_mat_cons
        db_mat_cons.sqlmodel_update(update_data)
        db.add(db_mat_cons); db.commit(); db.refresh(db_mat_cons)
        logger.info(f"MaterialConsumible actualizado: ID={db_mat_cons.id}")
        return db_mat_cons
    except IntegrityError as e: db.rollback(); logger.warning(f"IntegrityError update MatCons ID {db_mat_cons.id}: {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error update MatCons ID {db_mat_cons.id}: {e}", exc_info=True); raise

def delete_material_consumible(db: Session, *, mat_cons_id: int) -> Optional[MaterialConsumible]:
    try:
        db_mat = db.get(MaterialConsumible, mat_cons_id)
        if not db_mat: return None
        logger.warning(f"Intentando eliminar MaterialConsumible: ID={mat_cons_id}, SKU='{db_mat.sku}'")
        db.delete(db_mat); db.commit()
        logger.warning(f"MaterialConsumible eliminado: ID={mat_cons_id}")
        return db_mat
    except IntegrityError as e: # Fallará si está en FormulaItem o LineaProformaMaterial
        db.rollback(); logger.error(f"IntegrityError delete MatCons ID {mat_cons_id}. Referenciado?: {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error delete MatCons ID {mat_cons_id}: {e}", exc_info=True); raise

def adjust_stock_consumible(db: Session, *, mat_cons_id: int, change_amount: Decimal) -> Optional[MaterialConsumible]:
    """Ajusta el stock actual de un material consumible."""
    try:
        db_mat = db.get(MaterialConsumible, mat_cons_id)
        if not db_mat: return None
        new_stock = (db_mat.stock_actual or Decimal("0.0")) + change_amount
        if new_stock < 0:
             logger.error(f"Intento de ajuste de stock negativo para MatCons ID {mat_cons_id}. Actual: {db_mat.stock_actual}, Cambio: {change_amount}")
             # Decisión: ¿Lanzar error o simplemente dejar en 0? Lanzar error es más seguro.
             raise ValueError("El ajuste de stock resultaría en una cantidad negativa.")
        db_mat.stock_actual = new_stock
        db.add(db_mat); db.commit(); db.refresh(db_mat)
        logger.info(f"Stock ajustado para MaterialConsumible ID {mat_cons_id}: {change_amount}. Nuevo stock: {new_stock}")
        return db_mat
    except Exception as e:
        db.rollback()
        logger.error(f"Error ajustando stock MatCons ID {mat_cons_id}: {e}", exc_info=True)
        raise

# =======================================
# Repositorio para MaterialSimple
# =======================================
# (Similar a MaterialConsumible: get_by_id, get_by_sku, list, create, update, delete, adjust_stock)
# ... Implementación análoga ...

def get_material_simple_by_id(db: Session, *, mat_simp_id: int) -> Optional[MaterialSimple]:
    try: return db.get(MaterialSimple, mat_simp_id)
    except Exception as e: logger.error(f"Error get MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise

def get_material_simple_by_sku(db: Session, *, sku: str) -> Optional[MaterialSimple]:
    try: return db.exec(select(MaterialSimple).where(MaterialSimple.sku == sku)).first()
    except Exception as e: logger.error(f"Error get MatSimp SKU {sku}: {e}", exc_info=True); raise

def list_materiales_simples(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialSimple]:
    try: return db.exec(select(MaterialSimple).offset(skip).limit(limit).order_by(MaterialSimple.id)).all()
    except Exception as e: logger.error(f"Error list MatSimp: {e}", exc_info=True); raise

def create_material_simple(db: Session, *, mat_simp_data: MaterialSimple) -> MaterialSimple:
    db_mat = mat_simp_data
    try:
        db.add(db_mat); db.commit(); db.refresh(db_mat)
        logger.info(f"MaterialSimple creado: ID={db_mat.id}, SKU='{db_mat.sku}'")
        return db_mat
    except IntegrityError as e: db.rollback(); logger.warning(f"IntegrityError create MatSimp SKU '{db_mat.sku}': {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error create MatSimp SKU '{db_mat.sku}': {e}", exc_info=True); raise

def update_material_simple(db: Session, *, db_mat_simp: MaterialSimple, update_data: Dict[str, Any]) -> MaterialSimple:
    """Actualiza campos definitorios (nombre, desc, etc.), no stock_actual."""
    try:
        update_data.pop("sku", None)
        update_data.pop("stock_actual", None) # No actualizar stock aquí
        if not update_data: return db_mat_simp
        db_mat_simp.sqlmodel_update(update_data)
        db.add(db_mat_simp); db.commit(); db.refresh(db_mat_simp)
        logger.info(f"MaterialSimple actualizado: ID={db_mat_simp.id}")
        return db_mat_simp
    except IntegrityError as e: db.rollback(); logger.warning(f"IntegrityError update MatSimp ID {db_mat_simp.id}: {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error update MatSimp ID {db_mat_simp.id}: {e}", exc_info=True); raise

def delete_material_simple(db: Session, *, mat_simp_id: int) -> Optional[MaterialSimple]:
    try:
        db_mat = db.get(MaterialSimple, mat_simp_id)
        if not db_mat: return None
        logger.warning(f"Intentando eliminar MaterialSimple: ID={mat_simp_id}, SKU='{db_mat.sku}'")
        db.delete(db_mat); db.commit()
        logger.warning(f"MaterialSimple eliminado: ID={mat_simp_id}")
        return db_mat
    except IntegrityError as e: # Fallará si está en FormulaItem o LineaProformaMaterial
        db.rollback(); logger.error(f"IntegrityError delete MatSimp ID {mat_simp_id}. Referenciado?: {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error delete MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise

def adjust_stock_simple(db: Session, *, mat_simp_id: int, change_amount: Decimal) -> Optional[MaterialSimple]:
    """Ajusta el stock actual de un material simple."""
    try:
        db_mat = db.get(MaterialSimple, mat_simp_id)
        if not db_mat: return None
        new_stock = (db_mat.stock_actual or Decimal("0.0")) + change_amount
        if new_stock < 0:
             logger.error(f"Intento de ajuste de stock negativo para MatSimp ID {mat_simp_id}. Actual: {db_mat.stock_actual}, Cambio: {change_amount}")
             raise ValueError("El ajuste de stock resultaría en una cantidad negativa.")
        db_mat.stock_actual = new_stock
        db.add(db_mat); db.commit(); db.refresh(db_mat)
        logger.info(f"Stock ajustado para MaterialSimple ID {mat_simp_id}: {change_amount}. Nuevo stock: {new_stock}")
        return db_mat
    except Exception as e:
        db.rollback(); logger.error(f"Error ajustando stock MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise


# =======================================
# Repositorio para StockItemDimensional
# =======================================

def get_stock_item_by_id(db: Session, *, item_id: int) -> Optional[StockItemDimensional]:
    """Obtiene una pieza de stock dimensional por ID."""
    try:
        return db.get(StockItemDimensional, item_id)
    except Exception as e:
        logger.error(f"Error obteniendo StockItemDimensional ID {item_id}: {e}", exc_info=True)
        raise

def create_stock_item(db: Session, *, item_data: StockItemDimensional) -> StockItemDimensional:
    """Crea una nueva pieza de stock dimensional."""
    db_item = item_data
    try:
        # Asegurar estado inicial si no se proporciona
        if not db_item.estado: db_item.estado = "DISPONIBLE"
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        logger.info(f"StockItemDimensional creado: ID={db_item.id}, MaterialID={db_item.material_dimensional_id}")
        return db_item
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando StockItemDimensional: {e}", exc_info=True)
        raise

def list_stock_items(
    db: Session, *,
    skip: int = 0,
    limit: int = 100,
    material_dimensional_id: Optional[int] = None,
    estado: Optional[str] = None,
    min_longitud: Optional[Decimal] = None,
    min_ancho: Optional[Decimal] = None,
    # Añadir más filtros según necesidad (ej: es_merma, ubicación)
) -> Sequence[StockItemDimensional]:
    """
    Lista piezas de stock dimensional con filtros opcionales.
    Crucial para encontrar material disponible para cortes.
    """
    try:
        statement = select(StockItemDimensional)
        conditions = []
        if material_dimensional_id is not None:
            conditions.append(StockItemDimensional.material_dimensional_id == material_dimensional_id)
        if estado is not None:
            conditions.append(StockItemDimensional.estado == estado)
        if min_longitud is not None:
            conditions.append(StockItemDimensional.longitud_actual >= min_longitud)
        if min_ancho is not None:
            conditions.append(StockItemDimensional.ancho_actual >= min_ancho)

        if conditions:
            statement = statement.where(and_(*conditions)) # Usar and_() para múltiples condiciones

        statement = statement.order_by(StockItemDimensional.id).offset(skip).limit(limit)
        items = db.exec(statement).all()
        return items
    except Exception as e:
        logger.error(f"Error listando StockItemDimensional: {e}", exc_info=True)
        raise

def update_stock_item(db: Session, *, db_item: StockItemDimensional, update_data: Dict[str, Any]) -> StockItemDimensional:
    """Actualiza una pieza de stock dimensional (estado, ubicación, dimensiones, etc.)."""
    try:
        # Campos que quizás no deban actualizarse aquí (depende de la lógica de negocio)
        # update_data.pop("material_dimensional_id", None)
        if not update_data: return db_item
        db_item.sqlmodel_update(update_data)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        logger.info(f"StockItemDimensional actualizado: ID={db_item.id}")
        return db_item
    except Exception as e:
        db.rollback()
        logger.error(f"Error actualizando StockItemDimensional ID {db_item.id}: {e}", exc_info=True)
        raise

# delete_stock_item se omite por ahora, preferible cambiar estado a 'DESECHADO'