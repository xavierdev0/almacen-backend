# app/schemas/client_schema.py
from sqlmodel import SQLModel, Field
from pydantic import EmailStr, field_validator, ValidationInfo # ValidationInfo para Pydantic v2+
from typing import Optional
from datetime import datetime
import re # Para validaciones de identificación si se añaden

# Lista permitida de tipos de identificación según el ENUM del SQL
ALLOWED_TIPO_IDENTIFICACION = ["RUC", "CEDULA", "PASAPORTE", "OTRO"]

class ClienteBase(SQLModel):
    """Schema base con campos comunes para Cliente."""
    nombre: str = Field(
        ..., # Requerido en la base
        max_length=255,
        description="Nombre completo o razón social del cliente."
    )
    tipo_identificacion: Optional[str] = Field(
        default=None,
        max_length=50,
        description=f"Tipo de identificación fiscal (ej: {', '.join(ALLOWED_TIPO_IDENTIFICACION)})."
    )
    identificacion_fiscal: Optional[str] = Field(
        default=None,
        max_length=50,
        index=True, # Aunque es de DB, indicarlo aquí ayuda a la claridad
        description="Número de RUC, Cédula, Pasaporte u otro identificador fiscal único."
    )
    persona_contacto: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nombre de la persona de contacto principal en la empresa cliente."
    )
    email: Optional[EmailStr] = Field( # Usar EmailStr para validación automática
        default=None,
        index=True, # Claridad
        description="Correo electrónico de contacto principal del cliente (único si se proporciona)."
    )
    telefono: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Número de teléfono de contacto principal."
    )
    direccion: Optional[str] = Field(
        default=None,
        description="Dirección física o fiscal del cliente."
    )

    @field_validator('tipo_identificacion')
    def validate_tipo_identificacion(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v.upper() not in ALLOWED_TIPO_IDENTIFICACION:
            raise ValueError(f"Tipo de identificación debe ser uno de: {', '.join(ALLOWED_TIPO_IDENTIFICACION)}")
        return v.upper() if v is not None else None # Guardar en mayúsculas o None

    # - Que si se proporciona 'identificacion_fiscal', también se proporcione 'tipo_identificacion'.
    # - Validar el formato de 'identificacion_fiscal' según el 'tipo_identificacion' (ej., validar RUC/Cédula Ecuador).

class ClienteCreate(ClienteBase):
    """Schema para crear un nuevo Cliente via API."""
    # Hereda todos los campos de ClienteBase.
    # 'nombre' es el único estrictamente requerido por la DB, pero aquí
    # dejamos los demás como opcionales según la definición de ClienteBase.
    pass # No necesita campos adicionales por ahora

class ClienteRead(ClienteBase):
    """Schema para devolver información del Cliente en respuestas API."""
    id: int
    fecha_creacion: Optional[datetime] = None
    fecha_ultima_actualizacion: Optional[datetime] = None

    # Podríamos añadir relaciones aquí si fuera necesario, ej:
    # pedidos: List["PedidoClienteRead"] = [] # Requeriría definir PedidoClienteRead

    model_config = {
        "from_attributes": True # Para SQLModel/SQLAlchemy (Pydantic v2)
        # "orm_mode": True # Para Pydantic v1
    }

class ClienteUpdate(SQLModel): # No hereda de Base para que todos sean opcionales
    """
    Schema para actualizar un Cliente existente via API.
    Todos los campos son opcionales.
    """
    nombre: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nuevo nombre completo o razón social del cliente."
    )
    tipo_identificacion: Optional[str] = Field(
        default=None,
        max_length=50,
        description=f"Nuevo tipo de identificación fiscal (ej: {', '.join(ALLOWED_TIPO_IDENTIFICACION)})."
    )
    identificacion_fiscal: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Nuevo número de RUC, Cédula, Pasaporte u otro identificador fiscal único."
    )
    persona_contacto: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nuevo nombre de la persona de contacto principal."
    )
    email: Optional[EmailStr] = Field(
        default=None,
        description="Nuevo correo electrónico de contacto principal (único si se proporciona)."
    )
    telefono: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Nuevo número de teléfono de contacto principal."
    )
    direccion: Optional[str] = Field(
        default=None,
        description="Nueva dirección física o fiscal del cliente."
    )

    # Re-aplicar validación para los campos que se actualizan
    @field_validator('tipo_identificacion')
    def validate_update_tipo_identificacion(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v.upper() not in ALLOWED_TIPO_IDENTIFICACION:
            raise ValueError(f"Tipo de identificación debe ser uno de: {', '.join(ALLOWED_TIPO_IDENTIFICACION)}")
        return v.upper() if v is not None else None

    # Considerar añadir validaciones cruzadas aquí si es necesario, por ejemplo,
    # asegurar que si se cambia la identificación, el tipo sea coherente.
    # Ejemplo (requiere importar ValidationInfo de pydantic):
    # @field_validator('identificacion_fiscal')
    # def check_identificacion_with_tipo(cls, v: Optional[str], info: ValidationInfo) -> Optional[str]:
    #     tipo = info.data.get('tipo_identificacion') # Obtener el valor del otro campo
    #     if v is not None and tipo is None:
    #         # O si 'tipo' ya existe en el objeto original si no se actualiza
    #         # Esto puede volverse complejo y es mejor manejarlo en la capa de servicio
    #         pass # Lógica de validación
    #     return v