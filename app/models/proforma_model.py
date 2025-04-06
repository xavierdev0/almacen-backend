# app/models/proforma_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, DECIMAL, Integer, ForeignKey, TIMESTAMP, Text, Index
from sqlalchemy import Enum as SQLAlchemyEnum # Importar Enum de SQLAlchemy
from sqlalchemy.sql import func
from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from .enums import EstadoProformaEnum, TipoItemProformaEnum

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .cliente_model import Cliente
    from .usuario_model import Usuario
    from .orden_produccion_model import OrdenProduccion
    from .venta_factura_model import VentaFactura
    from .item_inventario_model import ItemInventario # Necesario para relación inversa polimórfica
    from .definicion_producto_servicio_model import DefinicionProductoServicio # Necesario para relación inversa polimórfica


class Proforma(SQLModel, table=True):
    __tablename__ = "proforma"
    __table_args__ = (
        Index("fk_proforma_cliente_idx", "cliente_id"),
        Index("fk_proforma_usuario_idx", "usuario_id_creador"),
        Index("idx_proforma_estado", "estado"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: int = Field(
        sa_column=Column(Integer, ForeignKey("cliente.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    )
    usuario_id_creador: int = Field(
        sa_column=Column(Integer, ForeignKey("usuario.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    )
    estado: EstadoProformaEnum = Field(
        default=EstadoProformaEnum.BORRADOR,
        sa_column=Column(SQLAlchemyEnum(EstadoProformaEnum, name="estado_proforma_enum"), nullable=False, default=EstadoProformaEnum.BORRADOR)
    )
    fecha_creacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    )
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)
    )
    subtotal: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(15, 2)))
    impuestos: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(15, 2)))
    total: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(15, 2)))
    notas: Optional[str] = Field(default=None, sa_column=Column(Text))

    # Relaciones
    cliente: Optional["Cliente"] = Relationship(back_populates="proformas")
    creador: Optional["Usuario"] = Relationship(back_populates="proformas_creadas")
    lineas: List["LineaProforma"] = Relationship(back_populates="proforma", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    orden_produccion: Optional["OrdenProduccion"] = Relationship(back_populates="proforma")
    venta_factura: Optional["VentaFactura"] = Relationship(back_populates="proforma")

class LineaProforma(SQLModel, table=True):
    __tablename__ = "linea_proforma"
    __table_args__ = (
        Index("fk_linea_proforma_proforma_idx", "proforma_id"),
        Index("idx_linea_proforma_item", "item_id", "tipo_item"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    proforma_id: int = Field(
        sa_column=Column(Integer, ForeignKey("proforma.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    )
    tipo_item: TipoItemProformaEnum = Field(
        sa_column=Column(SQLAlchemyEnum(TipoItemProformaEnum, name="tipo_item_proforma_enum"), nullable=False)
    )
    item_id: int = Field(sa_column=Column(Integer, nullable=False, comment='ID polimórfico'))
    cantidad: Decimal = Field(sa_column=Column(DECIMAL(10, 3), nullable=False))
    precio_unitario: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(12, 2)))
    total_linea: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(15, 2)))
    detalles_descripcion: Optional[str] = Field(default=None, sa_column=Column(Text, comment='Ej: dimensiones corte'))

    # Relación N:1 a Proforma
    proforma: Optional[Proforma] = Relationship(back_populates="lineas")

    # --- Relaciones Inversas Polimórficas (Opcionales pero útiles para navegar desde Item/Definicion) ---
    item_inventario_relacionado: Optional["ItemInventario"] = Relationship(
         back_populates="lineas_proforma",
         sa_relationship_kwargs=dict(
             primaryjoin="and_(foreign(LineaProforma.item_id) == ItemInventario.id, LineaProforma.tipo_item == 'ITEM_INVENTARIO')",
             # foreign_keys="LineaProforma.item_id", # No es estrictamente FK
             viewonly=True,
             lazy="joined"
         )
     )
    producto_servicio_relacionado: Optional["DefinicionProductoServicio"] = Relationship(
         back_populates="lineas_proforma",
         sa_relationship_kwargs=dict(
             primaryjoin="and_(foreign(LineaProforma.item_id) == DefinicionProductoServicio.id, LineaProforma.tipo_item == 'PRODUCTO_SERVICIO')",
             # foreign_keys="LineaProforma.item_id",
             viewonly=True,
             lazy="joined"
         )
     )
    # ------------------------------------------------------------