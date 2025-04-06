# app/models/permiso_model.py
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, Column, String, Text, UniqueConstraint
from typing import Optional, List

# Definición forward para relaciones
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .rol_model import Rol


from .rol_model import RolPermisoLink 

class Permiso(SQLModel, table=True):
    __tablename__ = "permiso"
    __table_args__ = (UniqueConstraint("nombre", name="nombre_UNIQUE"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100, sa_column=Column(String(100), nullable=False, index=True, comment='Ej: proforma:crear, inventario:leer'))
    descripcion: Optional[str] = Field(default=None, sa_column=Column(Text))

    # Relaciones
    roles: List["Rol"] = Relationship(back_populates="permisos", link_model=RolPermisoLink) # Usa string