# app/models/inventory_models.py

from datetime import datetime
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .order_models import OrdenProduccion, LineaProformaMaterial
    from .service_models import FormulaItem

# -----------------------------------------------------
# Modelo para Tipos de Material Dimensional
# -----------------------------------------------------

class MaterialDimensional(SQLModel, table=True):
    """Define un tipo de material que se maneja por dimensiones (ej: planchas, tablones)."""
    # Nombre explícito de tabla (opcional si coincide con la inferencia)
    __tablename__ = "material_dimensional"

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str = Field(max_length=100, unique=True, index=True)
    nombre: str = Field(max_length=255)
    descripcion: Optional[str] = Field(default=None) # Considerar: sa_column=Column(Text)
    espesor_nominal: Decimal = Field(max_digits=10, decimal_places=3)
    unidad_dimension: str = Field(default="mm", max_length=10)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con StockItemDimensional (un tipo de material tiene muchas piezas en stock)
    items_stock: List["StockItemDimensional"] = Relationship(back_populates="definicion_material")

# -----------------------------------------------------
# Modelo para Stock Físico de Material Dimensional
# -----------------------------------------------------

class StockItemDimensional(SQLModel, table=True):
    """Representa una pieza física específica de material dimensional en el inventario."""
    __tablename__ = "stock_item_dimensional"

    id: Optional[int] = Field(default=None, primary_key=True)
    material_dimensional_id: int = Field(foreign_key="material_dimensional.id", index=True)
    longitud_actual: Decimal = Field(max_digits=10, decimal_places=3)
    ancho_actual: Decimal = Field(max_digits=10, decimal_places=3)
    # El espesor se obtiene a través de la relación con MaterialDimensional
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    es_merma: bool = Field(default=False)
    stock_item_padre_id: Optional[int] = Field(
        default=None, foreign_key="stock_item_dimensional.id", index=True, nullable=True
    )
    orden_produccion_generadora_id: Optional[int] = Field(
        default=None, foreign_key="orden_produccion.id", index=True, nullable=True
    )
    # El ENUM de la DB se maneja como str aquí, la validación puede estar en otro nivel
    estado: str = Field(default="DISPONIBLE", index=True, max_length=50)
    fecha_ingreso: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación N:1 con MaterialDimensional (muchas piezas pertenecen a un tipo)
    definicion_material: MaterialDimensional = Relationship(back_populates="items_stock")

    # Relación N:1 con OrdenProduccion (muchas mermas pueden ser generadas por una orden)
    orden_generadora: Optional["OrdenProduccion"] = Relationship(back_populates="items_merma_generados")

    # Relación Auto-referenciada para Padre/Hijos (Merma)
    # Un item puede ser padre de varias mermas (hijos)
    items_merma_hijos: List["StockItemDimensional"] = Relationship(
        back_populates="item_padre"
        # sa_relationship_kwargs={'cascade': 'all, delete-orphan'} # Opcional: si se borra el padre, borrar mermas hijas
    )
    # Una merma (hijo) tiene un solo padre
    item_padre: Optional["StockItemDimensional"] = Relationship(
        back_populates="items_merma_hijos",
        sa_relationship_kwargs=dict(remote_side="StockItemDimensional.id") # Necesario para auto-referencia N:1
    )

    # Relación con LineaProformaMaterial (a definir en order_models.py)
    lineas_proforma: List["LineaProformaMaterial"] = Relationship(back_populates="stock_item")


# -----------------------------------------------------
# Modelo para Materiales Consumibles
# -----------------------------------------------------

class MaterialConsumible(SQLModel, table=True):
    """Define un tipo de material consumible (ej: lija, pintura, diluyente)."""
    __tablename__ = "material_consumible"

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str = Field(max_length=100, unique=True, index=True)
    nombre: str = Field(max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_medida: str = Field(max_length=50)
    rendimiento_m2: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=3, nullable=True)
    stock_actual: Decimal = Field(default=0, max_digits=10, decimal_places=3)
    stock_minimo: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=3, nullable=True)
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con FormulaItem (a definir en service_models.py)
    items_formula: List["FormulaItem"] = Relationship(back_populates="material_consumible")

    # Relación con LineaProformaMaterial (a definir en order_models.py)
    lineas_proforma: List["LineaProformaMaterial"] = Relationship(back_populates="material_consumible")

# -----------------------------------------------------
# Modelo para Materiales Simples
# -----------------------------------------------------

class MaterialSimple(SQLModel, table=True):
    """Define un tipo de material simple (ej: clavos, tornillos)."""
    __tablename__ = "material_simple"

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str = Field(max_length=100, unique=True, index=True)
    nombre: str = Field(max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_medida: str = Field(max_length=50)
    stock_actual: Decimal = Field(default=0, max_digits=10, decimal_places=3)
    stock_minimo: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=3, nullable=True)
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con FormulaItem (a definir en service_models.py)
    items_formula: List["FormulaItem"] = Relationship(back_populates="material_simple")

    # Relación con LineaProformaMaterial (a definir en order_models.py)
    lineas_proforma: List["LineaProformaMaterial"] = Relationship(back_populates="material_simple")