# app/models/maquina_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy import Enum as SQLAlchemyEnum # Importar Enum de SQLAlchemy
from typing import Optional, List
from .enums import TipoMaquinaEnum, EstadoMaquinaEnum

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .registro_mantenimiento_model import RegistroMantenimiento
    from .reporte_error_maquina_model import ReporteErrorMaquina


class Maquina(SQLModel, table=True):
    __tablename__ = "maquina"
    __table_args__ = (
        UniqueConstraint("numero_serie", name="numero_serie_UNIQUE"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150, sa_column=Column(String(150), nullable=False))
    tipo: TipoMaquinaEnum = Field(sa_column=Column(SQLAlchemyEnum(TipoMaquinaEnum, name="tipo_maquina_enum"), nullable=False))
    modelo: Optional[str] = Field(default=None, max_length=150)
    numero_serie: Optional[str] = Field(default=None, max_length=150, sa_column=Column(String(150), index=True))
    estado: EstadoMaquinaEnum = Field(
        default=EstadoMaquinaEnum.OPERATIVA,
        sa_column=Column(SQLAlchemyEnum(EstadoMaquinaEnum, name="estado_maquina_enum"), nullable=False, default=EstadoMaquinaEnum.OPERATIVA)
    )

    # Relaciones
    registros_mantenimiento: List["RegistroMantenimiento"] = Relationship(back_populates="maquina", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    reportes_error: List["ReporteErrorMaquina"] = Relationship(back_populates="maquina", sa_relationship_kwargs={"cascade": "all, delete-orphan"})