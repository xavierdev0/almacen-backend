# app/schemas/service_schema.py
from sqlmodel import SQLModel, Field
from pydantic import condecimal
from typing import Optional
from datetime import datetime
from decimal import Decimal


class ServicioDefinicionBase(SQLModel):
    """Schema base para la definición de servicios."""
    # --- CAMBIO: Añadido campo codigo ---
    codigo: str = Field(
        ...,
        max_length=50,
        index=True, # Info para dev
        unique=True, # Info para dev
        description="Código único para identificar el servicio."
    )
    # --- FIN CAMBIO ---
    nombre: str = Field(
        ...,
        max_length=255,
        description="Nombre único y descriptivo del servicio ofrecido (ej: Corte Recto MDF, Maquinado CNC Básico)."
    )
    descripcion: Optional[str] = Field(
        default=None,
        description="Descripción detallada del servicio."
    )
    unidad_cobro: str = Field(
        ...,
        max_length=50,
        description="Unidad en la que se mide/cobra el servicio (ej: pieza, hora, m2, corte, ml)."
    )
    # Campos de costeo (algunos pueden ser nulos si el costeo es diferente)
    costo_por_unidad: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Costo fijo por cada unidad de servicio (si aplica)."
    )
    costo_por_minuto: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Costo por minuto de ejecución del servicio (ej: tiempo máquina)."
    )
    tiempo_setup_min: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        # El default=0.0 está en la DB, lo reflejamos aquí
        default=Decimal("0.0"),
        description="Tiempo fijo de preparación/setup en minutos (independiente de la cantidad)."
    )
    tiempo_preparado_min_por_unidad: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        # El default=0.0 está en la DB
        default=Decimal("0.0"),
        description="Tiempo adicional de preparado en minutos por cada unidad de servicio."
    )
    factor_ih: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        # El default=1.0 está en la DB
        default=Decimal("1.0"),
        description="Factor de Imprevistos/Herramientas (multiplicador sobre costo base, ej: 1.1 para 10%)."
    )
    # --- CAMBIO: Añadido requiere_dibujo_cnc ---
    # (Asegúrate que este cambio de la vez anterior sigue aquí)
    requiere_dibujo_cnc: bool = Field(
        default=False,
        description="Indica si este servicio requiere un archivo de dibujo CNC."
    )

class ServicioDefinicionCreate(ServicioDefinicionBase):
    """Schema para crear una nueva definición de servicio."""
    # Hereda todos los campos necesarios de la base.
    pass


class ServicioDefinicionRead(ServicioDefinicionBase):
    """Schema para devolver información de definición de servicio."""
    id: int
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]
    # Fórmulas asociadas podrían añadirse aquí en el futuro:
    # formulas: List["FormulaRead"] = []

    model_config = {"from_attributes": True}

class ServicioDefinicionUpdate(SQLModel):
    """Schema para actualizar una definición de servicio. Todos los campos opcionales."""
    # --- CAMBIO: Añadido codigo (opcional) ---
    codigo: Optional[str] = Field(default=None, max_length=50)
    # --- FIN CAMBIO ---
    nombre: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_cobro: Optional[str] = Field(default=None, max_length=50)
    costo_por_unidad: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    costo_por_minuto: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    tiempo_setup_min: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    tiempo_preparado_min_por_unidad: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    factor_ih: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    # --- CAMBIO: Añadido requiere_dibujo_cnc (opcional) ---
    requiere_dibujo_cnc: Optional[bool] = Field(default=None)
    # --- FIN CAMBIO ---
