# app/models/venta_factura_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, DECIMAL, Integer, ForeignKey, TIMESTAMP, String, Index, UniqueConstraint
from sqlalchemy import DateTime # Para DATETIME
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime
from decimal import Decimal

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .proforma_model import Proforma
    from .cliente_model import Cliente


class VentaFactura(SQLModel, table=True):
    __tablename__ = "venta_factura"
    __table_args__ = (
        UniqueConstraint("proforma_id", name="proforma_id_UNIQUE"),
        UniqueConstraint("ref_factura_externa", name="ref_factura_externa_UNIQUE"),
        Index("fk_venta_factura_proforma_idx", "proforma_id"),
        Index("fk_venta_factura_cliente_idx", "cliente_id"),
        Index("idx_venta_fecha", "fecha_factura"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    proforma_id: int = Field(
        sa_column=Column(Integer, ForeignKey("proforma.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False, unique=True)
    )
    cliente_id: int = Field(
        sa_column=Column(Integer, ForeignKey("cliente.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    )
    monto_total_final: Decimal = Field(sa_column=Column(DECIMAL(15, 2), nullable=False))
    fecha_factura: datetime = Field(sa_column=Column(DateTime, nullable=False))
    ref_factura_externa: Optional[str] = Field(
        default=None, max_length=255,
        sa_column=Column(String(255), index=True, comment='Referencia del sistema externo de facturación')
    )
    estado_pago: Optional[str] = Field(default="PENDIENTE", max_length=100) # Considerar ENUM si hay estados fijos
    fecha_creacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    )

    # Relaciones
    proforma: Optional["Proforma"] = Relationship(back_populates="venta_factura")
    cliente: Optional["Cliente"] = Relationship(back_populates="ventas_facturas")