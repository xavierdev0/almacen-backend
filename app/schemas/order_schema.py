



# app/schemas/order_schema.py

from decimal import Decimal
from sqlmodel import SQLModel, Field
from pydantic import BaseModel, field_validator, model_validator # Podríamos necesitarlo para otros schemas aquí
from typing import Optional, List, Any # Necesario para relaciones en Read
from datetime import datetime
from decimal import Decimal

# Importar schemas relacionados para anidación en PedidoClienteRead
# Asegúrate de que estos schemas existan y estén definidos adecuadamente
from .client_schema import ClienteRead
from .usuario_schema import UsuarioRead 
from .inventory_schema import (
    StockItemDimensionalRead, MaterialConsumibleRead, MaterialSimpleRead
)
from .service_schema import ServicioDefinicionRead


# --- Lista de tipos de Proforma permitidos ---
ALLOWED_PROFORMA_TIPO = ["PRODUCTO", "SERVICIO"]
# --- Lista de estados de Proforma permitidos ---
ALLOWED_PROFORMA_ESTADO = [
    "BORRADOR", "PENDIENTE_APROBACION", "APROBADA",
    "RECHAZADA", "CANCELADA", "EXPIRADA", "POSPUESTA"
]

ALLOWED_TIPO_MATERIAL_ORIGEN = ["STOCK_DIMENSIONAL", "CONSUMIBLE", "SIMPLE"]


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

    proformas: List["ProformaRead"] = [] # <-- Incluir lista de proformas
    # orden_produccion: Optional["OrdenProduccionRead"] = None # <-- Se añadirá después

    model_config = {"from_attributes": True}


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
    lineas_material: List["LineaProformaMaterialRead"] = []
    lineas_servicio: List["LineaProformaServicioRead"] = []

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

# ==========================================================
# Schemas para LineaProformaMaterial (NUEVO)
# ==========================================================

class LineaProformaMaterialBase(SQLModel):
    """Schema base para líneas de material en proforma."""
    tipo_material_origen: str = Field(
        ..., max_length=50, description=f"Origen ({', '.join(ALLOWED_TIPO_MATERIAL_ORIGEN)})"
    )
    # IDs opcionales del origen - solo uno debe ser no nulo
    stock_item_dimensional_id: Optional[int] = Field(default=None, foreign_key="stock_item_dimensional.id")
    material_consumible_id: Optional[int] = Field(default=None, foreign_key="material_consumible.id")
    material_simple_id: Optional[int] = Field(default=None, foreign_key="material_simple.id")
    # Campos comunes
    cantidad: Decimal = Field(..., max_digits=10, decimal_places=3, gt=0, description="Cantidad del material")
    detalles_corte_solicitado: Optional[str] = Field(default=None, description="Detalles específicos del corte o preparación")

    @field_validator('tipo_material_origen')
    def validate_tipo_origen(cls, v: str) -> str:
        if v not in ALLOWED_TIPO_MATERIAL_ORIGEN:
            raise ValueError(f"Tipo origen debe ser uno de: {', '.join(ALLOWED_TIPO_MATERIAL_ORIGEN)}")
        return v

    # Validador a nivel de modelo para asegurar que solo se proporcione un ID de origen
    @model_validator(mode='after')
    def check_single_material_id(cls, data: Any) -> Any:
        if isinstance(data, SQLModel): # Adaptar si no hereda de SQLModel
             provided_ids = [
                 data.stock_item_dimensional_id,
                 data.material_consumible_id,
                 data.material_simple_id
             ]
             # Contar cuántos IDs tienen valor (no son None)
             num_provided = sum(1 for id_val in provided_ids if id_val is not None)
             if num_provided != 1:
                 raise ValueError("Debe proporcionar exactamente un ID de origen (stock_item_dimensional_id, material_consumible_id, o material_simple_id)")
        return data

class LineaProformaMaterialCreate(LineaProformaMaterialBase):
    """Schema para añadir una línea de material a una proforma via API."""
    # Hereda los campos de Base.
    # El servicio determinará 'descripcion_item', 'unidad', 'precio_unitario'
    # basado en el ID de origen proporcionado.
    pass

class LineaProformaMaterialRead(SQLModel): # No hereda de Base para control explícito
    """Schema para devolver información de línea de material."""
    id: int
    # tipo_material_origen: str # Podría incluirse si es útil
    descripcion_item: str
    cantidad: Decimal
    unidad: str
    precio_unitario: Decimal
    total_linea: Decimal
    detalles_corte_solicitado: Optional[str] = None
    # --- Opcional: Información anidada del material de origen ---
    # stock_item: Optional[StockItemDimensionalRead] = None
    # material_consumible: Optional[MaterialConsumibleRead] = None
    # material_simple: Optional[MaterialSimpleRead] = None
    # --- Opcional: Lista de servicios asociados a esta línea ---
    # servicios_asociados: List["LineaProformaServicioRead"] = []

    model_config = {"from_attributes": True}

# ==========================================================
# Schemas para LineaProformaServicio (NUEVO)
# ==========================================================

class LineaProformaServicioBase(SQLModel):
    """Schema base para líneas de servicio en proforma."""
    servicio_definicion_id: int = Field(..., foreign_key="servicio_definicion.id", description="ID de la definición del servicio")
    cantidad: Decimal = Field(..., max_digits=10, decimal_places=3, gt=0, description="Cantidad del servicio (según unidad de cobro)")
    # Opcional: ID de la línea de material a la que se aplica este servicio
    linea_proforma_material_id: Optional[int] = Field(
        default=None, foreign_key="linea_proforma_material.id", nullable=True,
        description="ID de la línea de material asociada (si aplica)"
    )
    # Campos para info específica (podrían ser rellenados por dibujante/servicio)
    ruta_imagen_cnc: Optional[str] = Field(
        default=None, max_length=512, nullable=True, description="Ruta al archivo CNC (si aplica)"
    )
    detalles_adicionales: Optional[str] = Field(
        default=None, nullable=True, description="Notas o detalles específicos del servicio"
    )

class LineaProformaServicioCreate(LineaProformaServicioBase):
    """Schema para añadir una línea de servicio a una proforma via API."""
    # Hereda los campos de Base.
    # El servicio determinará 'descripcion_servicio', 'precio_unitario'
    # basado en el servicio_definicion_id.
    pass

class LineaProformaServicioRead(SQLModel): # No hereda de Base
    """Schema para devolver información de línea de servicio."""
    id: int
    servicio_definicion_id: int
    linea_proforma_material_id: Optional[int] = None
    descripcion_servicio: str
    cantidad: Decimal
    # unidad_cobro: str # Podría venir del servicio_definicion anidado
    precio_unitario: Decimal
    total_linea: Decimal
    ruta_imagen_cnc: Optional[str] = None
    detalles_adicionales: Optional[str] = None
    # --- Opcional: Información anidada del servicio ---
    # servicio_definicion: Optional[ServicioDefinicionRead] = None

    model_config = {"from_attributes": True}


# --- Actualizar Forward References ---
# Es necesario si los schemas se referencian entre sí dentro de este mismo archivo
# (ej: PedidoClienteRead -> ProformaRead -> Linea...Read)
ProformaRead.model_rebuild()
PedidoClienteRead.model_rebuild()
# LineaProformaMaterialRead.model_rebuild() # Descomentar si se usa servicio_asociados
# LineaProformaServicioRead.model_rebuild() # Descomentar si se usa en LineaProformaMaterialRead



# --- Definiciones Forward para relaciones futuras ---
# (Necesarias si definimos LineaProforma*Read aquí y los usamos en ProformaRead)
# class LineaProformaMaterialRead(SQLModel): ...
# class LineaProformaServicioRead(SQLModel): ...
# ProformaRead.model_rebuild()

# (Necesarias si usamos ProformaRead en PedidoClienteRead)
# PedidoClienteRead.model_rebuild()