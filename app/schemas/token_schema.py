# app/schemas/token_schema.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import enum

class TokenType(str, enum.Enum):
    """Define el tipo de token permitido."""
    BEARER = "bearer"

class Token(BaseModel):
    """
    Schema para la respuesta de autenticación estándar OAuth2.
    Contiene el token de acceso y su tipo.
    """
    access_token: str = Field(
        ..., # El campo es requerido
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ4YXZpZXJ...",
        description="Token JWT para autenticación en endpoints protegidos."
    )
    token_type: TokenType = Field(
        default=TokenType.BEARER,
        example=TokenType.BEARER.value, # Usa el valor del Enum para el ejemplo
        description="Tipo de token emitido (siempre 'bearer')."
    )

class TokenData(BaseModel):
    """
    Schema para los datos decodificados del payload del token JWT.
    Utilizado internamente para validar y extraer la información del sujeto.
    """
    sub: str = Field(
        ..., # Subject (sujeto/identificador) es requerido
        example="xavierpauta", # O podría ser un ID de usuario numérico como string
        description="Identificador único del sujeto del token (generalmente username o ID)."
    )
    exp: Optional[datetime] = Field(
        default=None, # La librería jose/jwt valida la expiración por defecto
        description="Timestamp de expiración del token (opcional aquí, validado por jwt.decode)."
        )
    iat: Optional[datetime] = Field(
        default=None, # Tiempo de emisión (opcional aquí, añadido en security.py)
        description="Timestamp de emisión del token."
    )
