# app/models/client_model.py

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .order_models import PedidoCliente
    from .billing_models import VentaFactura

# -----------------------------------------------------
# Modelo para Clientes
# -----------------------------------------------------

class Cliente(SQLModel, table=True):
    """Representa a un cliente del negocio."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=255)
    # ENUM manejado como str, validación en otro nivel
    tipo_identificacion: Optional[str] = Field(default=None, max_length=50, nullable=True) # Ej: 'RUC', 'CEDULA'
    identificacion_fiscal: Optional[str] = Field(
        default=None, unique=True, index=True, max_length=50, nullable=True
    )
    persona_contacto: Optional[str] = Field(default=None, max_length=255, nullable=True)
    email: Optional[str] = Field(
        default=None, unique=True, index=True, max_length=255, nullable=True
    )
    telefono: Optional[str] = Field(default=None, max_length=50, nullable=True)
    direccion: Optional[str] = Field(default=None, nullable=True) # Considerar sa_column=Column(Text)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con PedidoCliente (un cliente puede tener muchos pedidos)
    pedidos: List["PedidoCliente"] = Relationship(back_populates="cliente")

    # Relación 1:N con VentaFactura (un cliente puede tener muchas facturas)
    # El campo cliente_id en VentaFactura está denormalizado, pero la relación es útil.
    facturas: List["VentaFactura"] = Relationship(back_populates="cliente")


# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .order_models import PedidoCliente
    from .billing_models import VentaFactura # Necesario cuando se defina VentaFactura

    # Recordatorio: Añadir/Verificar back_populates correspondientes en otros modelos:
    # class PedidoCliente(...):
    #     cliente: "Cliente" = Relationship(back_populates="pedidos")
    #
    # class VentaFactura(...):
    #     cliente: "Cliente" = Relationship(back_populates="facturas")