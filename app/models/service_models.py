# app/models/service_models.py

from datetime import datetime
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .inventory_models import MaterialConsumible, MaterialSimple
    from .order_models import LineaProformaServicio

# -----------------------------------------------------
# Modelo para Definición de Servicios
# -----------------------------------------------------

class ServicioDefinicion(SQLModel, table=True):
    """Define un tipo de servicio ofrecido por el negocio."""
    __tablename__ = "servicio_definicion"

    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(max_length=50, unique=True, index=True)
    nombre: str = Field(max_length=255)
    descripcion: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)
    unidad_cobro: str = Field(max_length=50) # ej: hora, minuto, pieza, m lineal
    costo_por_unidad: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=2, nullable=True)
    costo_por_minuto: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2, nullable=True)
    tiempo_setup_min: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2, nullable=True)
    tiempo_preparado_min_por_unidad: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2, nullable=True)
    factor_ih: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=3, nullable=True)
    factor_st: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=3, nullable=True)
    factor_m: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=3, nullable=True)
    requiere_dibujo_cnc: bool = Field(default=False)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con Formula (un servicio puede tener varias fórmulas asociadas)
    formulas: List["Formula"] = Relationship(back_populates="servicio_definicion")

    # Relación 1:N con LineaProformaServicio (un tipo de servicio puede estar en muchas líneas de proforma)
    lineas_proforma: List["LineaProformaServicio"] = Relationship(back_populates="servicio_definicion")

# -----------------------------------------------------
# Modelo para Fórmulas de Materiales por Servicio
# -----------------------------------------------------

class Formula(SQLModel, table=True):
    """Define una fórmula específica de materiales requeridos para un servicio."""
    id: Optional[int] = Field(default=None, primary_key=True)
    servicio_definicion_id: int = Field(foreign_key="servicio_definicion.id", index=True)
    nombre: str = Field(max_length=150)
    descripcion: Optional[str] = Field(default=None)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación N:1 con ServicioDefinicion (una fórmula pertenece a un servicio)
    servicio_definicion: ServicioDefinicion = Relationship(back_populates="formulas")

    # Relación 1:N con FormulaItem (una fórmula se compone de varios items/materiales)
    items: List["FormulaItem"] = Relationship(back_populates="formula") # cascade="all, delete-orphan" podría ser útil aquí

# -----------------------------------------------------
# Modelo para Items dentro de una Fórmula
# -----------------------------------------------------

class FormulaItem(SQLModel, table=True):
    """Detalla un material (Consumible o Simple) y su cantidad dentro de una fórmula."""
    __tablename__ = "formula_item"

    id: Optional[int] = Field(default=None, primary_key=True)
    formula_id: int = Field(foreign_key="formula.id", index=True)
    # El ENUM se maneja como str, la validación de tipo vs FK en la app
    tipo_material: str = Field(max_length=50) # 'CONSUMIBLE' o 'SIMPLE'
    material_consumible_id: Optional[int] = Field(default=None, foreign_key="material_consumible.id", index=True, nullable=True)
    material_simple_id: Optional[int] = Field(default=None, foreign_key="material_simple.id", index=True, nullable=True)
    cantidad_necesaria: Decimal = Field(max_digits=10, decimal_places=3)
    unidad_rendimiento: str = Field(default="m2", max_length=50) # Unidad base para la cantidad (ej: por m2 de servicio)
    descripcion_uso: Optional[str] = Field(default=None)

    # Relación N:1 con Formula (un item pertenece a una fórmula)
    formula: Formula = Relationship(back_populates="items")

    # Relación N:1 con MaterialConsumible (un item PUEDE ser un consumible)
    material_consumible: Optional["MaterialConsumible"] = Relationship(back_populates="items_formula")

    # Relación N:1 con MaterialSimple (un item PUEDE ser un material simple)
    material_simple: Optional["MaterialSimple"] = Relationship(back_populates="items_formula")


# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .inventory_models import MaterialConsumible, MaterialSimple
    from .order_models import LineaProformaServicio # Importar para la relación en ServicioDefinicion

    # Recordatorio: Añadir back_populates correspondientes en otros modelos:
    # class MaterialConsumible(...) / MaterialSimple(...):
    #     items_formula: List["FormulaItem"] = Relationship(back_populates="material_...")
    #
    # class LineaProformaServicio(...):
    #     servicio_definicion: ServicioDefinicion = Relationship(back_populates="lineas_proforma")