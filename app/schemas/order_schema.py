



# app/schemas/order_schema.py

from sqlmodel import SQLModel, Field
from pydantic import BaseModel # Podríamos necesitarlo para otros schemas aquí
from typing import Optional, List # Necesario para relaciones en Read
from datetime import datetime

# Importar schemas relacionados para anidación en PedidoClienteRead
# Asegúrate de que estos schemas existan y estén definidos adecuadamente
from .client_schema import ClienteRead
from .usuario_schema import UsuarioRead # Usaremos UsuarioRead para mostrar info del vendedor
# Importaremos ProformaRead y OrdenProduccionRead cuando los creemos
# from .order_schema import ProformaRead, OrdenProduccionRead

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