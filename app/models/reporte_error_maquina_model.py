# app/models/reporte_error_maquina_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, Integer, ForeignKey, Text, Boolean, TIMESTAMP, Index
from sqlalchemy import DateTime # Para DATETIME
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .maquina_model import Maquina
    from .usuario_model import Usuario


class ReporteErrorMaquina(SQLModel, table=True):
    __tablename__ = "reporte_error_maquina"
    __table_args__ = (
        Index("fk_reporte_error_maquina_maquina_idx", "maquina_id"),
        Index("fk_reporte_error_maquina_usuario_idx", "usuario_id_reportador"),
        Index("idx_error_resuelto", "esta_resuelto"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    maquina_id: int = Field(
        sa_column=Column(Integer, ForeignKey("maquina.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    )
    usuario_id_reportador: int = Field(
        sa_column=Column(Integer, ForeignKey("usuario.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    )
    fecha_reporte: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    )
    descripcion_error: str = Field(sa_column=Column(Text, nullable=False))
    esta_resuelto: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, default=False))
    fecha_resolucion: Optional[datetime] = Field(default=None, sa_column=Column(DateTime))
    detalles_resolucion: Optional[str] = Field(default=None, sa_column=Column(Text))

    # Relaciones
    maquina: Optional["Maquina"] = Relationship(back_populates="reportes_error")
    reportador: Optional["Usuario"] = Relationship(back_populates="errores_reportados")