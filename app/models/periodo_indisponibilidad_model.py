# app/models/periodo_indisponibilidad_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, Integer, ForeignKey, Text, Index
from sqlalchemy import DateTime # Para DATETIME
from typing import Optional
from datetime import datetime

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .usuario_model import Usuario


class PeriodoIndisponibilidad(SQLModel, table=True):
    __tablename__ = "periodo_indisponibilidad"
    __table_args__ = (
        Index("fk_periodo_indisponibilidad_usuario_idx", "usuario_id"),
        Index("idx_indisp_fechas", "fecha_inicio", "fecha_fin"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(
        sa_column=Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    )
    fecha_inicio: datetime = Field(sa_column=Column(DateTime, nullable=False))
    fecha_fin: Optional[datetime] = Field(default=None, sa_column=Column(DateTime))
    motivo: Optional[str] = Field(default=None, sa_column=Column(Text))

    # Relacion
    usuario: Optional["Usuario"] = Relationship(back_populates="periodos_indisponibilidad")