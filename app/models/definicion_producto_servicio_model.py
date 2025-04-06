# app/models/definicion_producto_servicio_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, DECIMAL, String, Text
from sqlalchemy import Enum as SQLAlchemyEnum # Importar Enum de SQLAlchemy
from typing import Optional, List
from decimal import Decimal
from .enums import TipoProductoServicioEnum # Importa tu Enum de Python

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .proforma_model import LineaProforma

class DefinicionProductoServicio(SQLModel, table=True):
    __tablename__ = "definicion_producto_servicio"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=255, sa_column=Column(String(255), nullable=False))
    descripcion: Optional[str] = Field(default=None, sa_column=Column(Text))
    tipo: TipoProductoServicioEnum = Field(sa_column=Column(SQLAlchemyEnum(TipoProductoServicioEnum, name="tipo_producto_servicio_enum"), nullable=False)) # Dar nombre al ENUM en BD
    precio_estandar: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(12, 2)))
    unidad: Optional[str] = Field(default=None, max_length=50, sa_column=Column(String(50), comment='ej: unidad, hora, corte, m², etc.'))

    # Relacion inversa polimórfica
    lineas_proforma: List["LineaProforma"] = Relationship(back_populates="producto_servicio_relacionado")