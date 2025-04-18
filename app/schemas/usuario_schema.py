# app/schemas/usuario_schema.py
from sqlmodel import SQLModel, Field # Usamos SQLModel para schemas relacionados con la tabla
from pydantic import BaseModel, EmailStr, field_validator # BaseModel para schemas no mapeados 1:1
from typing import Optional, List
from datetime import datetime
import re # Para validación con regex
from .rol_permiso_schema import RolRead

# Importación necesaria para el validador si usas Pydantic v2+
from pydantic_core.core_schema import FieldValidationInfo

# --- Schemas SQLModel-based ---

class UsuarioBase(SQLModel):
    """Schema base con campos comunes para no repetir."""
    email: EmailStr = Field(
        ..., # Requerido
        description="Correo electrónico único del usuario."
    )
    username: str = Field(
        ..., # Requerido
        min_length=3,
        max_length=100, # Aumentado por si acaso, DB es 100
        description="Nombre de usuario único (3-100 caracteres)."
    )
    nombre_completo: Optional[str] = Field(
        default=None,
        max_length=255, # Coincidir con DB
        description="Nombre completo del usuario (opcional)."
    )

class UsuarioCreate(UsuarioBase): # Hereda email, username, nombre_completo
    """
    Schema para crear un nuevo usuario via API.
    Permite especificar los roles iniciales.
    """
    password: str = Field(
        ..., # Requerido
        min_length=8,
        max_length=50, # Limitar longitud máxima razonable en input
        description="Contraseña del usuario (mínimo 8 caracteres)."
    )
    # --- CAMPO AÑADIDO ---
    rol_ids: Optional[List[int]] = Field(
        default=None, # Es opcional proporcionar roles al crear
        description="Lista opcional de IDs de los roles a asignar inicialmente al usuario."
    )


class UsuarioRead(UsuarioBase): # Hereda email, username, nombre_completo
    """
    Schema para devolver información del usuario en respuestas API.
    Excluye información sensible como la contraseña. Incluye roles.
    """
    id: int
    esta_activo: bool
    fecha_creacion: Optional[datetime] = None
    # Incluir roles usando el schema RolRead importado
    roles: List[RolRead] = [] # Lista vacía por defecto

    model_config = {
        "from_attributes": True
    }

class UsuarioUpdate(SQLModel):
    """
    Schema para actualizar información del perfil de usuario.
    Todos los campos son opcionales. No incluye cambio de contraseña ni roles.
    """
    email: Optional[EmailStr] = Field(
        default=None,
        description="Nuevo correo electrónico único (opcional)."
    )
    username: Optional[str] = Field( # Permitir cambio de username (opcional)
        default=None,
        min_length=3,
        max_length=100,
        description="Nuevo nombre de usuario único (opcional)."
    )
    nombre_completo: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nuevo nombre completo (opcional)."
    )
    esta_activo: Optional[bool] = Field(
        default=None,
        description="Estado de activación del usuario (opcional, para Admins)."
    )
    # La asignación de roles se manejará por endpoints específicos (Paso 4)

# --- Schema Pydantic BaseModel ---

class UsuarioUpdatePassword(BaseModel):
    """Schema específico para solicitar un cambio de contraseña."""
    old_password: str = Field(..., description="La contraseña actual del usuario.")
    new_password: str = Field(
        ...,
        min_length=8,
        max_length=50,
        description="La nueva contraseña (mínimo 8 caracteres)."
    )
    confirm_password: str = Field(
        ...,
        description="Confirmación de la nueva contraseña."
    )

    # Validación para asegurar que new_password y confirm_password coinciden
    @field_validator('confirm_password')
    def passwords_match(cls, v: str, info: FieldValidationInfo) -> str:
        if 'new_password' in info.data and v != info.data['new_password']:
            raise ValueError('La nueva contraseña y la confirmación no coinciden.')
        return v
