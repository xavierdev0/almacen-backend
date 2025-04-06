# app/models/asignacion_orden_produccion_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, Integer, ForeignKey, TIMESTAMP, String, Index, UniqueConstraint
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .orden_produccion_model import OrdenProduccion
    from .usuario_model import Usuario


class AsignacionOrdenProduccion(SQLModel, table=True):
    __tablename__ = "asignacion_orden_produccion"
    __table_args__ = (
        UniqueConstraint("orden_id", "usuario_id", "rol_asignado_contexto", name="uq_orden_usuario_rol"),
        Index("fk_asignacion_orden_produccion_orden_idx", "orden_id"),
        Index("fk_asignacion_orden_produccion_usuario_idx", "usuario_id"),
    )

    id: Optional[int] = Field(default=None, primary_key=True) # PK simple es más fácil
    orden_id: int = Field(
        sa_column=Column(Integer, ForeignKey("orden_produccion.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    )
    usuario_id: int = Field(
        sa_column=Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    )
    rol_asignado_contexto: Optional[str] = Field(default=None, max_length=100, sa_column=Column(String(100), comment='Ej: dibujante_cotizacion, operario_corte'))
    fecha_asignacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    )

    # Relaciones
    orden: Optional["OrdenProduccion"] = Relationship(back_populates="asignaciones")
    usuario: Optional["Usuario"] = Relationship(back_populates="asignaciones_ordenes") # Asegurar 'asignaciones_ordenes' en Usuario