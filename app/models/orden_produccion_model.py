# app/models/orden_produccion_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, Integer, ForeignKey, TIMESTAMP, Text, Index, UniqueConstraint
from sqlalchemy import Enum as SQLAlchemyEnum, DateTime # Para DATETIME
from sqlalchemy.sql import func
from typing import Optional, List
from datetime import datetime
from .enums import EstadoOrdenProduccionEnum

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .proforma_model import Proforma
    from .asignacion_orden_produccion_model import AsignacionOrdenProduccion


class OrdenProduccion(SQLModel, table=True):
    __tablename__ = "orden_produccion"
    __table_args__ = (
        UniqueConstraint("proforma_id", name="proforma_id_UNIQUE"),
        Index("fk_orden_produccion_proforma_idx", "proforma_id"),
        Index("idx_orden_prod_estado", "estado"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    proforma_id: int = Field(
        sa_column=Column(Integer, ForeignKey("proforma.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False, unique=True)
    )
    estado: EstadoOrdenProduccionEnum = Field(
        default=EstadoOrdenProduccionEnum.PENDIENTE,
        sa_column=Column(SQLAlchemyEnum(EstadoOrdenProduccionEnum, name="estado_orden_produccion_enum"), nullable=False, default=EstadoOrdenProduccionEnum.PENDIENTE)
    )
    fecha_creacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    )
    fecha_estimada_finalizacion: Optional[datetime] = Field(default=None, sa_column=Column(DateTime))
    fecha_real_finalizacion: Optional[datetime] = Field(default=None, sa_column=Column(DateTime))
    notas_supervisor: Optional[str] = Field(default=None, sa_column=Column(Text))
    ruta_imagen_final: Optional[str] = Field(default=None, max_length=512)

    # Relaciones
    proforma: Optional["Proforma"] = Relationship(back_populates="orden_produccion")
    asignaciones: List["AsignacionOrdenProduccion"] = Relationship(back_populates="orden", sa_relationship_kwargs={"cascade": "all, delete-orphan"})