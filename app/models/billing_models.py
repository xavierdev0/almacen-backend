# app/models/billing_models.py

from datetime import datetime
from decimal import Decimal
from typing import Optional, TYPE_CHECKING # No necesitamos List aquí

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .order_models import PedidoCliente, Proforma
    from .client_model import Cliente

# -----------------------------------------------------
# Modelo para Venta/Factura
# -----------------------------------------------------

class VentaFactura(SQLModel, table=True):
    """Representa la factura generada para una venta, vinculada a un pedido."""
    __tablename__ = "venta_factura"

    id: Optional[int] = Field(default=None, primary_key=True)
    pedido_cliente_id: int = Field(foreign_key="pedido_cliente.id", index=True)
    # FKs opcionales a las proformas específicas incluidas en esta factura
    proforma_productos_id: Optional[int] = Field(
        default=None, foreign_key="proforma.id", index=True, nullable=True
    )
    proforma_servicios_id: Optional[int] = Field(
        default=None, foreign_key="proforma.id", index=True, nullable=True
    )
    # FK a cliente (denormalizada de pedido_cliente para conveniencia)
    cliente_id: int = Field(foreign_key="cliente.id", index=True)
    monto_total_final: Decimal = Field(max_digits=15, decimal_places=2)
    fecha_factura: datetime = Field()
    ref_factura_externa: Optional[str] = Field(
        default=None, unique=True, index=True, max_length=255, nullable=True
    )
    estado_factura_externa: Optional[str] = Field(default=None, max_length=100, nullable=True)
    estado_pago: str = Field(default="PENDIENTE", max_length=50) # ENUM
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)

    # Relación N:1 con PedidoCliente
    pedido: "PedidoCliente" = Relationship(back_populates="facturas")

    # Relación N:1 con Proforma (para productos)
    # Se necesita foreign_keys por haber dos FK a la misma tabla Proforma
    proforma_productos: Optional["Proforma"] = Relationship(
        back_populates="facturas_productos",
        sa_relationship_kwargs={'foreign_keys': '[VentaFactura.proforma_productos_id]'}
    )

    # Relación N:1 con Proforma (para servicios)
    # Se necesita foreign_keys por haber dos FK a la misma tabla Proforma
    proforma_servicios: Optional["Proforma"] = Relationship(
        back_populates="facturas_servicios",
        sa_relationship_kwargs={'foreign_keys': '[VentaFactura.proforma_servicios_id]'}
    )

    # Relación N:1 con Cliente
    cliente: "Cliente" = Relationship(back_populates="facturas")


# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .order_models import PedidoCliente, Proforma
    from .client_model import Cliente

    # Recordatorio: Añadir/Verificar back_populates correspondientes en otros modelos:
    # class PedidoCliente(...):
    #     facturas: List["VentaFactura"] = Relationship(back_populates="pedido")
    #
    # class Proforma(...):
    #     facturas_productos: List["VentaFactura"] = Relationship(back_populates="proforma_productos")
    #     facturas_servicios: List["VentaFactura"] = Relationship(back_populates="proforma_servicios")
    #
    # class Cliente(...):
    #     facturas: List["VentaFactura"] = Relationship(back_populates="cliente")