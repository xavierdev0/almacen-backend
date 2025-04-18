# app/schemas/rol_permiso_schema.py

from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

# --- Schema para Roles ---

class RolBase(SQLModel):
    """Schema base para Rol con campos comunes."""
    nombre: str = Field(index=True, unique=True, max_length=100)
    descripcion: Optional[str] = Field(default=None)

class RolRead(RolBase):
    """Schema para leer datos de un Rol desde la API."""
    id: int
    fecha_creacion: Optional[datetime] = None # Incluir si se quiere mostrar
    fecha_ultima_actualizacion: Optional[datetime] = None # Incluir si se quiere mostrar

    # Config para permitir la creación desde atributos de objeto ORM (modelo Rol)
    model_config = {
        "from_attributes": True
    }

# Podrías añadir RolCreate, RolUpdate aquí si necesitaras endpoints para gestionarlos

# --- Schema para Permisos ---

class PermisoBase(SQLModel):
    """Schema base para Permiso con campos comunes."""
    nombre_accion: str = Field(max_length=100)
    nombre_recurso: str = Field(max_length=100)
    descripcion: Optional[str] = Field(default=None)

class PermisoRead(PermisoBase):
    """Schema para leer datos de un Permiso desde la API."""
    id: int
    fecha_creacion: Optional[datetime] = None

    # Config para permitir la creación desde atributos de objeto ORM (modelo Permiso)
    model_config = {
        "from_attributes": True
    }

# Podrías añadir PermisoCreate, PermisoUpdate aquí si necesitaras endpoints para gestionarlos