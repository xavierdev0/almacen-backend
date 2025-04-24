



# app/schemas/order_schema.py

from decimal import Decimal
from sqlmodel import SQLModel, Field
from pydantic import BaseModel, field_validator # Podríamos necesitarlo para otros schemas aquí
from typing import Optional, List # Necesario para relaciones en Read
from datetime import datetime

# Importar schemas relacionados para anidación en PedidoClienteRead
# Asegúrate de que estos schemas existan y estén definidos adecuadamente
from .client_schema import ClienteRead
from .usuario_schema import UsuarioRead # Usaremos UsuarioRead para mostrar info del vendedor
# Importaremos ProformaRead y OrdenProduccionRead cuando los creemos
# from .order_schema import ProformaRead, OrdenProduccionRead


# --- Lista de tipos de Proforma permitidos ---
ALLOWED_PROFORMA_TIPO = ["PRODUCTO", "SERVICIO"]
# --- Lista de estados de Proforma permitidos ---
ALLOWED_PROFORMA_ESTADO = [
    "BORRADOR", "PENDIENTE_APROBACION", "APROBADA",
    "RECHAZADA", "CANCELADA", "EXPIRADA", "POSPUESTA"
]



# -----------------------------------------------------
# Schemas para PedidoCliente
# -----------------------------------------------------

class PedidoClienteBase(SQLModel):
    """
    Schema base para PedidoCliente.
    Contiene campos comunes que podrían usarse en Create y Read,
    aunque en este caso, solo cliente_id es relevante para Create desde la API.
    El estado podría ir aquí si se compartiera mucho, pero lo pondremos en Read.
    """
    # cliente_id es fundamental para cualquier pedido.
    cliente_id: int = Field(
        ..., # Requerido en la creación vía API
        foreign_key="cliente.id", # Información contextual
        description="ID del Cliente al que pertenece el pedido."
    )
    # Nota: usuario_id_vendedor se obtendrá del usuario autenticado,
    #       estado, fecha_creacion, etc., se manejan internamente o en Read.

class PedidoClienteCreate(PedidoClienteBase):
    """
    Schema para crear un nuevo PedidoCliente via API.
    Solo requiere el ID del cliente, ya que el vendedor se obtiene del token
    y el estado inicial se define en el servicio.
    """
    # Hereda cliente_id de PedidoClienteBase
    pass # No necesita campos adicionales por ahora.

class PedidoClienteRead(SQLModel): # No hereda de Base para definir explícitamente todos los campos de salida
    """
    Schema para devolver la información de un PedidoCliente en respuestas API.
    Incluye información anidada del cliente y vendedor para mayor utilidad.
    """
    id: int
    estado: str # Devolveremos el estado actual
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]

    # Información del cliente anidada (usando ClienteRead)
    cliente_id: int # Mantenemos el ID por si acaso
    cliente: ClienteRead # Objeto Cliente completo (o lo que defina ClienteRead)

    # Información del vendedor anidada (usando UsuarioRead)
    usuario_id_vendedor: int # Mantenemos el ID
    vendedor: UsuarioRead # Objeto Usuario completo (o lo que defina UsuarioRead)

    # Podríamos añadir listas de Proformas y la Orden aquí en el futuro:
    # proformas: List["ProformaRead"] = []
    # orden_produccion: Optional["OrdenProduccionRead"] = None

    model_config = {
        "from_attributes": True # Necesario para mapear desde el modelo SQLAlchemy/SQLModel
    }

class PedidoClienteUpdate(SQLModel):
    """
    Schema para actualizar un PedidoCliente existente (ej: cambiar estado).
    Todos los campos son opcionales.
    """
    # El único campo que probablemente se actualizaría directamente en PedidoCliente es el estado.
    # Otros cambios (como añadir proformas) se harían a través de endpoints específicos.
    estado: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Nuevo estado del pedido (ej: APROBADO, CANCELADO)."
    )
    # No permitimos cambiar cliente_id ni vendedor_id en una actualización directa.

# --- Definiciones Forward para relaciones en PedidoClienteRead (cuando se creen los schemas) ---
# ProformaRead.model_rebuild()
# OrdenProduccionRead.model_rebuild()



# -----------------------------------------------------
# Schemas para Proforma (NUEVO)
# -----------------------------------------------------

class ProformaBase(SQLModel):
    """Schema base para Proforma con campos comunes."""
    # pedido_cliente_id y tipo son necesarios al crear
    pedido_cliente_id: int = Field(
        ..., foreign_key="pedido_cliente.id", description="ID del PedidoCliente al que pertenece."
    )
    tipo: str = Field(
        ..., max_length=50, description=f"Tipo de proforma ({', '.join(ALLOWED_PROFORMA_TIPO)})."
    )
    notas: Optional[str] = Field(
        default=None, description="Notas adicionales o comentarios sobre la proforma."
    )

    # Validador para el campo tipo
    @field_validator('tipo')
    def validate_tipo_proforma(cls, v: str) -> str:
        if v not in ALLOWED_PROFORMA_TIPO:
            raise ValueError(f"Tipo debe ser uno de: {', '.join(ALLOWED_PROFORMA_TIPO)}")
        return v

class ProformaCreate(ProformaBase):
    """
    Schema para crear una nueva Proforma via API.
    Normalmente, la creación inicial (par producto/servicio) se gestionará
    en el servicio asociado a la creación/gestión del PedidoCliente.
    Este schema podría usarse si se permitiera crear proformas individualmente.
    """
    # Hereda pedido_cliente_id, tipo y notas.
    # El resto de campos (usuario_id_creador, estado inicial, vinculación)
    # los establecerá la lógica de servicio.
    pass

class ProformaRead(SQLModel): # No hereda de Base para control explícito de salida
    """Schema para devolver información de Proforma en respuestas API."""
    id: int
    pedido_cliente_id: int
    tipo: str
    proforma_vinculada_id: Optional[int] = None # ID de la proforma vinculada (si existe)
    usuario_id_creador: int
    estado: str
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]
    fecha_aprobacion: Optional[datetime] = None
    fecha_reserva_expira: Optional[datetime] = None
    estado_reserva: Optional[str] = None
    subtotal: Optional[Decimal] = None
    impuestos: Optional[Decimal] = None
    total: Optional[Decimal] = None
    notas: Optional[str] = None

    # Información del creador (opcional, pero útil)
    # creador: Optional[UsuarioRead] = None # Descomentar si se quiere incluir

    # Listas de líneas (se añadirán cuando se definan sus schemas Read)
    # lineas_material: List["LineaProformaMaterialRead"] = []
    # lineas_servicio: List["LineaProformaServicioRead"] = []

    model_config = {"from_attributes": True}

class ProformaUpdate(SQLModel):
    """Schema para actualizar una Proforma (ej: estado, notas). Todos opcionales."""
    # No se permite cambiar pedido_cliente_id, tipo, ni creador.
    # La vinculación se manejaría con lógica específica.
    estado: Optional[str] = Field(
        default=None, max_length=50, description=f"Nuevo estado ({', '.join(ALLOWED_PROFORMA_ESTADO)})."
    )
    notas: Optional[str] = Field(
        default=None, description="Actualizar o añadir notas."
    )
    # Campos como subtotal, impuestos, total no se actualizan directamente,
    # se recalculan cuando se modifican las líneas.
    # La fecha_aprobacion, fecha_reserva_expira, estado_reserva se manejarían
    # por lógica de servicio basada en cambios de estado.

    # Validador para el campo estado (si se actualiza)
    @field_validator('estado')
    def validate_update_estado_proforma(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ALLOWED_PROFORMA_ESTADO:
            raise ValueError(f"Estado debe ser uno de: {', '.join(ALLOWED_PROFORMA_ESTADO)}")
        return v

# --- Definiciones Forward para relaciones futuras ---
# (Necesarias si definimos LineaProforma*Read aquí y los usamos en ProformaRead)
# class LineaProformaMaterialRead(SQLModel): ...
# class LineaProformaServicioRead(SQLModel): ...
# ProformaRead.model_rebuild()

# (Necesarias si usamos ProformaRead en PedidoClienteRead)
# PedidoClienteRead.model_rebuild()