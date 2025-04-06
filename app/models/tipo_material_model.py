# app/models/tipo_material_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, String, Text
from typing import Optional, List

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .item_inventario_model import ItemInventario

class TipoMaterial(SQLModel, table=True):
    __tablename__ = "tipo_material"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150, sa_column=Column(String(150), nullable=False))
    descripcion: Optional[str] = Field(default=None, sa_column=Column(Text))
    unidad_medida: Optional[str] = Field(default=None, max_length=50, sa_column=Column(String(50), comment='ej: m², kg, L, unidad'))

    # Relacion
    items_inventario: List["ItemInventario"] = Relationship(back_populates="tipo_material")