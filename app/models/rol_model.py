# app/models/rol_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, String, Text, Integer, ForeignKey, UniqueConstraint
from typing import Optional, List

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .usuario_model import Usuario # Para el type hint List["Usuario"]
    from .permiso_model import Permiso # Para el type hint List["Permiso"]

from .usuario_model import UsuarioRolLink

# Modelo de enlace N:M Rol <-> Permiso
class RolPermisoLink(SQLModel, table=True):
    __tablename__ = "rol_permiso"
    rol_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("rol.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    )
    permiso_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("permiso.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    )

class Rol(SQLModel, table=True):
    __tablename__ = "rol"
    __table_args__ = (UniqueConstraint("nombre", name="nombre_UNIQUE"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100, sa_column=Column(String(100), nullable=False, index=True, comment='Ej: Administrador, Vendedor, Supervisor'))
    descripcion: Optional[str] = Field(default=None, sa_column=Column(Text))

    # Relaciones - volvemos a usar List[...] directamente
    usuarios: List["Usuario"] = Relationship(back_populates="roles", link_model=UsuarioRolLink)
    permisos: List["Permiso"] = Relationship(back_populates="roles", link_model=RolPermisoLink)
    