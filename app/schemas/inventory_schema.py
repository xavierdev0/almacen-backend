
# app/schemas/inventory_schema.py
from sqlmodel import SQLModel, Field
from pydantic import condecimal # Para validación de decimales
from typing import Optional, List
from datetime import datetime
from decimal import Decimal # Asegurar importación

# --- Schemas para MaterialDimensional ---

class MaterialDimensionalBase(SQLModel):
    """Base schema for dimensional materials (sheets, planks)."""
    sku: str = Field(
        ...,
        max_length=100,
        index=True, # Claridad
        description="Stock Keeping Unit - Código único del tipo de material."
    )
    nombre: str = Field(
        ...,
        max_length=255,
        description="Nombre descriptivo (ej: Plancha MDF 18mm)."
    )
    descripcion: Optional[str] = Field(default=None, description="Descripción detallada.")
    # El espesor es clave para definir este tipo de material
    espesor_nominal: condecimal(max_digits=10, decimal_places=3) = Field( # type: ignore
        ...,
        description="Espesor estándar para este SKU."
    )
    unidad_dimension: str = Field(
        default="mm",
        max_length=10,
        description="Unidad para longitud, ancho, espesor (ej: mm, cm, m, pulgadas)."
    )

class MaterialDimensionalCreate(MaterialDimensionalBase):
    """Schema to create a new type of dimensional material."""
    pass # Hereda todo de la base

class MaterialDimensionalRead(MaterialDimensionalBase):
    """Schema to read dimensional material data from API."""
    id: int
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]

    model_config = {"from_attributes": True}

class MaterialDimensionalUpdate(SQLModel):
    """Schema to update a dimensional material type. All fields optional."""
    # SKU generalmente no se actualiza, se maneja con cuidado si se permite
    nombre: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None)
    espesor_nominal: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    unidad_dimension: Optional[str] = Field(default=None, max_length=10)

# --- Schemas para MaterialConsumible ---

class MaterialConsumibleBase(SQLModel):
    """Base schema for consumable materials (sandpaper, paint, thinner)."""
    sku: str = Field(..., max_length=100, index=True, description="SKU único del consumible.")
    nombre: str = Field(..., max_length=255, description="Nombre del consumible.")
    descripcion: Optional[str] = Field(default=None, description="Descripción detallada.")
    unidad_medida: str = Field(..., max_length=50, description="Unidad de medida (ej: rollo, litro, kg).")
    rendimiento_m2: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Rendimiento por metro cuadrado si aplica (ej: para pintura)."
    )
    # El stock actual se maneja en Read/Update, no se suele definir al crear el *tipo*
    stock_minimo: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Nivel mínimo de stock para alertas."
    )
    ubicacion: Optional[str] = Field(default=None, max_length=255, description="Ubicación en almacén.")

class MaterialConsumibleCreate(MaterialConsumibleBase):
    """Schema to create a new type of consumable material."""
    # Podríamos añadir un stock_inicial aquí si quisiéramos registrar la primera cantidad
    # stock_inicial: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=0.0)
    pass # Hereda de Base

class MaterialConsumibleRead(MaterialConsumibleBase):
    """Schema to read consumable material data from API."""
    id: int
    stock_actual: condecimal(max_digits=10, decimal_places=3) = Field(default=Decimal("0.0")) # type: ignore
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]

    model_config = {"from_attributes": True}

class MaterialConsumibleUpdate(SQLModel):
    """Schema to update a consumable material type. All fields optional."""
    # SKU no se actualiza
    nombre: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_medida: Optional[str] = Field(default=None, max_length=50)
    rendimiento_m2: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    # La actualización de stock_actual debería ser una operación separada (ej: ajuste de inventario)
    stock_minimo: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    ubicacion: Optional[str] = Field(default=None, max_length=255)

# --- Schemas para MaterialSimple ---

class MaterialSimpleBase(SQLModel):
    """Base schema for simple materials (nails, screws)."""
    sku: str = Field(..., max_length=100, index=True, description="SKU único del material simple.")
    nombre: str = Field(..., max_length=255, description="Nombre del material.")
    descripcion: Optional[str] = Field(default=None, description="Descripción detallada.")
    unidad_medida: str = Field(..., max_length=50, description="Unidad de medida (ej: unidad, caja, kg).")
    stock_minimo: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Nivel mínimo de stock para alertas."
    )
    ubicacion: Optional[str] = Field(default=None, max_length=255, description="Ubicación en almacén.")

class MaterialSimpleCreate(MaterialSimpleBase):
    """Schema to create a new type of simple material."""
    pass # Hereda de Base

class MaterialSimpleRead(MaterialSimpleBase):
    """Schema to read simple material data from API."""
    id: int
    stock_actual: condecimal(max_digits=10, decimal_places=3) = Field(default=Decimal("0.0")) # type: ignore
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]

    model_config = {"from_attributes": True}

class MaterialSimpleUpdate(SQLModel):
    """Schema to update a simple material type. All fields optional."""
    # SKU no se actualiza
    nombre: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_medida: Optional[str] = Field(default=None, max_length=50)
    stock_minimo: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    # stock_actual no se actualiza aquí

# --- Schemas para StockItemDimensional ---

class StockItemDimensionalBase(SQLModel):
    """Base schema for physical dimensional stock items."""
    material_dimensional_id: int = Field(
        ...,
        foreign_key="material_dimensional.id", # Info para dev
        description="ID del tipo de material dimensional al que pertenece."
    )
    longitud_actual: condecimal(max_digits=10, decimal_places=3) = Field( # type: ignore
        ...,
        description="Longitud actual de la pieza física."
    )
    ancho_actual: condecimal(max_digits=10, decimal_places=3) = Field( # type: ignore
        ...,
        description="Ancho actual de la pieza física."
    )
    ubicacion: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Ubicación específica de esta pieza en el almacén."
    )
    # Campos relacionados con merma y origen
    es_merma: bool = Field(default=False, description="Indica si esta pieza es resultado de un corte (merma).")
    stock_item_padre_id: Optional[int] = Field(
        default=None,
        foreign_key="stock_item_dimensional.id", # Info para dev
        description="ID de la pieza de la que provino esta merma (si aplica)."
    )
    orden_produccion_generadora_id: Optional[int] = Field(
        default=None,
        foreign_key="orden_produccion.id", # Info para dev
        description="ID de la orden de producción que generó esta merma (si aplica)."
    )

class StockItemDimensionalCreate(StockItemDimensionalBase):
    """Schema para registrar una nueva pieza física de material dimensional en stock."""
    # Hereda los campos necesarios. El estado inicial podría ser 'DISPONIBLE' por defecto (manejado en servicio/repo).
    # estado: Optional[str] = Field(default="DISPONIBLE", max_length=50) # Opcional aquí, default en otro lado
    pass

class StockItemDimensionalRead(StockItemDimensionalBase):
    """Schema para leer los datos de una pieza física de stock dimensional."""
    id: int
    estado: str = Field(max_length=50)
    fecha_ingreso: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]
    # Podríamos incluir opcionalmente datos del material dimensional asociado
    # definicion_material: Optional[MaterialDimensionalRead] = None # Si se necesita info completa

    model_config = {"from_attributes": True}

# Aún no definimos StockItemDimensionalUpdate, ya que la actualización
# puede ser compleja (cambio de estado, dimensiones por corte, etc.)
# y podría requerir operaciones de servicio más específicas.

