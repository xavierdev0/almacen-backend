# app/models/registro_mantenimiento_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, Integer, ForeignKey, Text, Index
from sqlalchemy import Enum as SQLAlchemyEnum, DateTime # Para DATETIME
from typing import Optional
from datetime import datetime
from .enums import TipoMantenimientoEnum

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .maquina_model import Maquina
    from .usuario_model import Usuario


class RegistroMantenimiento(SQLModel, table=True):
    __tablename__ = "registro_mantenimiento"
    __table_args__ = (
        Index("fk_registro_mantenimiento_maquina_idx", "maquina_id"),
        Index("fk_registro_mantenimiento_usuario_idx", "usuario_id_tecnico"),
        Index("idx_maint_fecha", "fecha_mantenimiento"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    maquina_id: int = Field(
        sa_column=Column(Integer, ForeignKey("maquina.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    )
    usuario_id_tecnico: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("usuario.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    )
    fecha_mantenimiento: datetime = Field(sa_column=Column(DateTime, nullable=False))
    tipo: TipoMantenimientoEnum = Field(sa_column=Column(SQLAlchemyEnum(TipoMantenimientoEnum, name="tipo_mantenimiento_enum"), nullable=False))
    descripcion: str = Field(sa_column=Column(Text, nullable=False))

    # Relaciones
    maquina: Optional["Maquina"] = Relationship(back_populates="registros_mantenimiento")
    tecnico: Optional["Usuario"] = Relationship(back_populates="mantenimientos_realizados")