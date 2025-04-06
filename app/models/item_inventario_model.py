# app/models/item_inventario_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, DECIMAL, Boolean, Integer, ForeignKey, TIMESTAMP, Index
from sqlalchemy.sql import func
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .tipo_material_model import TipoMaterial
    from .proforma_model import LineaProforma

class ItemInventario(SQLModel, table=True):
    __tablename__ = "item_inventario"
    __table_args__ = (
        Index("fk_item_inventario_tipo_material_idx", "tipo_material_id"),
        Index("fk_item_inventario_padre_idx", "item_inventario_padre_id"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    tipo_material_id: int = Field(
        sa_column=Column(Integer, ForeignKey("tipo_material.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    )
    longitud: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(10, 3), comment='Dimensión 1 (ej. metros, cm)'))
    ancho: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(10, 3), comment='Dimensión 2 (ej. metros, cm)'))
    espesor: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(10, 3), comment='Dimensión 3 (ej. metros, cm)'))
    cantidad: Decimal = Field(default=1, sa_column=Column(DECIMAL(10, 3), nullable=False, default=1, comment='Cantidad en unidad_medida o 1'))
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    es_merma: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, default=False))
    item_inventario_padre_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("item_inventario.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True, comment='FK a item_inventario si es merma')
    )
    fecha_creacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    )
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    # Relaciones
    tipo_material: Optional["TipoMaterial"] = Relationship(back_populates="items_inventario")
    item_padre: Optional["ItemInventario"] = Relationship(
        back_populates="items_merma", sa_relationship_kwargs=dict(remote_side="ItemInventario.id")
    )
    items_merma: List["ItemInventario"] = Relationship(back_populates="item_padre")
    lineas_proforma: List["LineaProforma"] = Relationship(back_populates="item_inventario_relacionado") # Relación inversa polimórfica