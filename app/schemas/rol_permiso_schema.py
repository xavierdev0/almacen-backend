# app/schemas/rol_permiso_schema.py

from typing import Optional, List 
from sqlmodel import SQLModel, Field
from datetime import datetime

# --- Schema para Roles ---

class RolBase(SQLModel):
    """Schema base para Rol con campos comunes."""
    nombre: str = Field(
        ..., # (...) indica que es requerido en Pydantic/SQLModel base
        index=True,
        unique=True, # Aunque unique es de DB, es bueno indicarlo
        max_length=100,
        description="Nombre único del Rol (ej: Administrador, Vendedor)."
    )
    descripcion: Optional[str] = Field(
        default=None,
        description="Descripción opcional del Rol."
    )

class RolRead(RolBase):
    """Schema para leer datos de un Rol desde la API."""
    id: int
    fecha_creacion: Optional[datetime] = None
    fecha_ultima_actualizacion: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }

# Podrías añadir RolCreate, RolUpdate aquí si necesitaras endpoints para gestionarlos

class RolCreate(RolBase):
    """Schema para crear un nuevo Rol via API."""
    # Hereda 'nombre' (requerido) y 'descripcion' (opcional) de RolBase
    pass # No necesita campos adicionales por ahora


class RolUpdate(SQLModel): # No hereda de RolBase para hacer todos los campos opcionales
    """
    Schema para actualizar un Rol existente via API.
    Todos los campos son opcionales.
    """
    nombre: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Nuevo nombre único para el Rol."
    )
    descripcion: Optional[str] = Field(
        default=None,
        description="Nueva descripción para el Rol (None para no cambiar, '' para borrar)."
    )

# --- Schema Base para Permisos ---
class PermisoBase(SQLModel):
    """Schema base para Permiso con campos comunes."""
    nombre_accion: str = Field(
        ..., # Requerido
        max_length=100,
        description="Acción permitida (ej: crear, leer, gestionar)."
        )
    nombre_recurso: str = Field(
        ..., # Requerido
        max_length=100,
        description="Recurso sobre el que aplica la acción (ej: proforma, usuario)."
        )
    descripcion: Optional[str] = Field(
        default=None,
        description="Descripción opcional del Permiso."
        )

# --- Schema para Leer Permisos ---
class PermisoRead(PermisoBase):
    """Schema para leer datos de un Permiso desde la API."""
    id: int
    fecha_creacion: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }


# --- NUEVOS SCHEMAS DE ESCRITURA PARA PERMISOS ---

class PermisoCreate(PermisoBase):
    """Schema para crear un nuevo Permiso via API."""
    # Hereda 'nombre_accion', 'nombre_recurso' (requeridos)
    # y 'descripcion' (opcional) de PermisoBase
    pass # No necesita campos adicionales

class PermisoUpdate(SQLModel): # No hereda para hacer campos opcionales
    """
    Schema para actualizar un Permiso existente via API.
    Todos los campos son opcionales.
    """
    nombre_accion: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Nueva acción para el Permiso."
        )
    nombre_recurso: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Nuevo recurso para el Permiso."
        )
    descripcion: Optional[str] = Field(
        default=None,
        description="Nueva descripción para el Permiso."
        )
    



class RolReadWithPermissions(RolRead):
    """
    Schema para leer datos de un Rol desde la API, incluyendo
    la lista de permisos asociados.
    """
    permisos: List[PermisoRead] = [] # Lista de Permisos (usando PermisoRead)

    # model_config se hereda de RolRead, así que from_attributes ya está habilitado.
