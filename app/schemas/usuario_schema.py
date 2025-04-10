# app/schemas/usuario_schema.py
from sqlmodel import SQLModel, Field # Usamos SQLModel para schemas relacionados con la tabla
from pydantic import BaseModel, EmailStr, field_validator # BaseModel para schemas no mapeados 1:1
from typing import Optional
from datetime import datetime
import re # Para validación con regex
# Importación necesaria para el validador si usas Pydantic v2+
from pydantic_core.core_schema import FieldValidationInfo

# --- Schemas SQLModel-based ---

class UsuarioCreate(SQLModel):
    """
    Schema para crear un nuevo usuario.
    Recibe datos en el body de la solicitud POST.
    """
    email: EmailStr = Field(
        ..., # Requerido
        description="Correo electrónico único del usuario."
    )
    username: str = Field(
        ..., # Requerido
        min_length=3,
        max_length=20,
        description="Nombre de usuario único (3-20 caracteres: minúsculas, números y _)."
    )
    password: str = Field(
        ..., # Requerido
        min_length=8,
        max_length=50, # Limitar longitud máxima razonable
        description="Contraseña del usuario (mínimo 8 caracteres)."
    )
    nombre_completo: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Nombre completo del usuario (opcional)."
    )
    # 'esta_activo' generalmente se establece por defecto en la lógica/DB, no en la creación inicial por el usuario.


class UsuarioRead(SQLModel):
    """
    Schema para devolver información del usuario en respuestas API.
    Excluye información sensible como la contraseña.
    """
    id: int = Field(...)
    email: EmailStr = Field(...)
    username: str = Field(...)
    nombre_completo: Optional[str] = Field(default=None)
    esta_activo: bool = Field(...)
    fecha_creacion: datetime = Field(...) # Ejemplo dinámico

    # Config para permitir la creación desde atributos de objeto ORM
    model_config = {
        "from_attributes": True
    }
    # Si necesitas devolver roles, añadirías aquí:
    # roles: List[RolRead] = [] # Necesitarías definir RolRead en rol_schema.py


class UsuarioUpdate(SQLModel):
    """
    Schema para actualizar información del perfil de usuario.
    Todos los campos son opcionales. No incluye cambio de contraseña.
    """
    email: Optional[EmailStr] = Field(
        default=None,
        description="Nuevo correo electrónico único (opcional)."
    )
    nombre_completo: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Nuevo nombre completo (opcional)."
    )
    esta_activo: Optional[bool] = Field(
        default=None,
        description="Estado de activación del usuario (opcional)."
    )
    # Username generalmente no se permite cambiar o requiere lógica especial,
    # por lo que se omite aquí comúnmente.


# --- Schema Pydantic BaseModel ---

class UsuarioUpdatePassword(BaseModel):
    """Schema específico para solicitar un cambio de contraseña."""
    old_password: str = Field(
        ...,
        description="La contraseña actual del usuario."
        )
    new_password: str = Field(
        ...,
        min_length=8,
        max_length=50,
        description="La nueva contraseña (mínimo 8 caracteres)."
    )
    confirm_password: str = Field(
        ...,
        min_length=8,
        max_length=50,
        description="Confirmación de la nueva contraseña."
    )

    # Opcional: Validación para asegurar que la nueva contraseña no sea igual a la antigua
    @field_validator('new_password')
    def passwords_match(cls, v: str, info: FieldValidationInfo) -> str:
        # info.data contiene los datos ya validados del modelo
        if 'old_password' in info.data and v == info.data['old_password']:
            raise ValueError('La nueva contraseña no puede ser igual a la anterior.')
        return v

