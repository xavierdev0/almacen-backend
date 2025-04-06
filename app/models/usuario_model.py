# app/models/usuario_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, String, Text, TIMESTAMP, Boolean, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from typing import Optional, List
from datetime import datetime

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .rol_model import Rol, UsuarioRolLink
    from .proforma_model import Proforma
    from .orden_produccion_model import AsignacionOrdenProduccion
    from .maquina_model import RegistroMantenimiento, ReporteErrorMaquina
    from .periodo_indisponibilidad_model import PeriodoIndisponibilidad

# Modelo de enlace N:M Usuario <-> Rol
class UsuarioRolLink(SQLModel, table=True):
    __tablename__ = "usuario_rol"
    usuario_id: Optional[int] = Field(
        default=None, 
        sa_column=Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    )
    rol_id: Optional[int] = Field(
        default=None, 
        sa_column=Column(Integer, ForeignKey("rol.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    )

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
    # Constraints a nivel de tabla
    __table_args__ = (
        UniqueConstraint("username", name="username_UNIQUE"),
        UniqueConstraint("email", name="email_UNIQUE"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=100, sa_column=Column(String(100), nullable=False, index=True, comment='Nombre de usuario para login'))
    email: str = Field(max_length=255, sa_column=Column(String(255), nullable=False, index=True))
    contrasena_hash: str = Field(max_length=255, sa_column=Column(String(255), nullable=False))
    nombre_completo: Optional[str] = Field(default=None, max_length=255)
    esta_activo: bool = Field(default=True, sa_column=Column(Boolean, nullable=False, default=True))
    fecha_creacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    )
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default=None, sa_column=Column(TIMESTAMP(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    # Relaciones
    roles: List["Rol"] = Relationship(back_populates="usuarios", link_model=UsuarioRolLink)
    proformas_creadas: List["Proforma"] = Relationship(back_populates="creador")
    asignaciones_ordenes: List["AsignacionOrdenProduccion"] = Relationship(back_populates="usuario")
    mantenimientos_realizados: List["RegistroMantenimiento"] = Relationship(back_populates="tecnico")
    errores_reportados: List["ReporteErrorMaquina"] = Relationship(back_populates="reportador")
    periodos_indisponibilidad: List["PeriodoIndisponibilidad"] = Relationship(back_populates="usuario")

# from datetime import datetime, UTC
#class Usuario(SQLModel, table=True):
#    __tablename__ = "usuarios"
#    
#    id: Optional[int] = Field(default=None, primary_key=True)
#   username: str = Field(max_length=100, unique=True, index=True)
#    email: str = Field(max_length=255, unique=True, index=True)
#    contrasena_hash: str = Field(max_length=255)
#    nombre_completo: str = Field(max_length=255)
#    esta_activo: bool = Field(default=True)
#    fecha_creacion: datetime = Field(default_factory=lambda: datetime.now(UTC))
#    fecha_ultima_actualizacion: datetime = Field(default_factory=lambda: datetime.now(UTC), sa_column_kwargs={"onupdate": lambda: datetime.now(UTC)})
