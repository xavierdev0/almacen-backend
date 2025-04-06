# app/models/cliente_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, String, Text, TIMESTAMP, Index, UniqueConstraint
from sqlalchemy.sql import func
from typing import Optional, List
from datetime import datetime

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .proforma_model import Proforma
    from .venta_factura_model import VentaFactura

class Cliente(SQLModel, table=True):
    __tablename__ = "cliente"
    __table_args__ = (
        UniqueConstraint("email", name="email_UNIQUE"),
        UniqueConstraint("identificacion_fiscal", name="identificacion_fiscal_UNIQUE"),
        Index("idx_cliente_nombre", "nombre"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=255, sa_column=Column(String(255), nullable=False, index=True))
    persona_contacto: Optional[str] = Field(default=None, max_length=255)
    email: Optional[str] = Field(default=None, max_length=255)
    telefono: Optional[str] = Field(default=None, max_length=20)
    direccion: Optional[str] = Field(default=None, sa_column=Column(Text))
    identificacion_fiscal: Optional[str] = Field(default=None, max_length=50, sa_column=Column(String(50), index=True, comment='RUC/CI u otro identificador'))
    fecha_creacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    )
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    # Relaciones
    proformas: List["Proforma"] = Relationship(back_populates="cliente")
    ventas_facturas: List["VentaFactura"] = Relationship(back_populates="cliente")