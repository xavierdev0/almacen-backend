# app/models/order_models.py

from datetime import datetime
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .client_model import Cliente
    from .user_models import Usuario, Rol
    from .inventory_models import (
        StockItemDimensional, MaterialConsumible, MaterialSimple
    )
    from .service_models import ServicioDefinicion
    from .billing_models import VentaFactura

# -----------------------------------------------------
# Modelo para Pedido del Cliente (Contenedor Principal)
# -----------------------------------------------------

class PedidoCliente(SQLModel, table=True):
    """Representa la solicitud global de un cliente, que agrupa proformas."""
    __tablename__ = "pedido_cliente"

    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id", index=True)
    usuario_id_vendedor: int = Field(foreign_key="usuario.id", index=True)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    estado: str = Field(default="NUEVO", index=True, max_length=50) # ENUM
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación N:1 con Cliente
    cliente: "Cliente" = Relationship(back_populates="pedidos")

    # Relación N:1 con Usuario (Vendedor)
    vendedor: "Usuario" = Relationship(back_populates="pedidos_creados")

    # Relación 1:N con Proforma (un pedido tiene 1 o 2 proformas)
    proformas: List["Proforma"] = Relationship(back_populates="pedido")

    # Relación 1:1 con OrdenProduccion (un pedido genera una orden)
    # 'uselist=False' indica que es una relación uno a uno (o uno a cero/uno)
    orden_produccion: Optional["OrdenProduccion"] = Relationship(
        back_populates="pedido", sa_relationship_kwargs={'uselist': False}
    )

    # Relación 1:N con VentaFactura (un pedido puede tener varias facturas si hay pagos parciales/ajustes)
    facturas: List["VentaFactura"] = Relationship(back_populates="pedido")

# -----------------------------------------------------
# Modelo para Proformas (Productos o Servicios)
# -----------------------------------------------------

class Proforma(SQLModel, table=True):
    """Representa una cotización/proforma, ya sea de productos o servicios."""
    id: Optional[int] = Field(default=None, primary_key=True)
    pedido_cliente_id: int = Field(foreign_key="pedido_cliente.id", index=True)
    tipo: str = Field(max_length=50) # 'PRODUCTO' o 'SERVICIO'
    # Clave foránea a sí misma para vincular proforma de producto y servicio
    proforma_vinculada_id: Optional[int] = Field(
        default=None, foreign_key="proforma.id", index=True, nullable=True
    )
    usuario_id_creador: int = Field(foreign_key="usuario.id", index=True)
    estado: str = Field(default="BORRADOR", index=True, max_length=50) # ENUM
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )
    fecha_aprobacion: Optional[datetime] = Field(default=None, nullable=True)
    fecha_reserva_expira: Optional[datetime] = Field(default=None, nullable=True)
    estado_reserva: Optional[str] = Field(default="NO_APLICA", max_length=50, nullable=True) # ENUM
    subtotal: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2, nullable=True)
    impuestos: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2, nullable=True)
    total: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2, nullable=True)
    notas: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)

    # Relación N:1 con PedidoCliente
    pedido: PedidoCliente = Relationship(back_populates="proformas")

    # Relación N:1 con Usuario (Creador)
    creador: "Usuario" = Relationship(back_populates="proformas_creadas")

    # Relación 1:1 Auto-referenciada (para vincular producto <-> servicio)
    proforma_vinculada: Optional["Proforma"] = Relationship(
        back_populates="proforma_vinculada_con", # Nombre del atributo en el otro lado
        sa_relationship_kwargs=dict(
            remote_side="Proforma.id", # Columna remota (la propia id)
            uselist=False # Indica que es una relación uno a uno
        )
    )
    # Atributo necesario para el back_populates de la relación anterior
    proforma_vinculada_con: Optional["Proforma"] = Relationship(back_populates="proforma_vinculada")

    # Relación 1:N con LineaProformaMaterial
    lineas_material: List["LineaProformaMaterial"] = Relationship(back_populates="proforma")

    # Relación 1:N con LineaProformaServicio
    lineas_servicio: List["LineaProformaServicio"] = Relationship(back_populates="proforma")

    # Relación con VentaFactura (lado N de la relación N:M implícita)
    facturas_productos: List["VentaFactura"] = Relationship(
        back_populates="proforma_productos",
        # Añadir esta línea especificando la FK en la tabla VentaFactura
        sa_relationship_kwargs={'foreign_keys': '[VentaFactura.proforma_productos_id]'}
    )
    facturas_servicios: List["VentaFactura"] = Relationship(
        back_populates="proforma_servicios",
        # Añadir esta línea especificando la FK en la tabla VentaFactura
        sa_relationship_kwargs={'foreign_keys': '[VentaFactura.proforma_servicios_id]'}
    )


# -----------------------------------------------------
# Modelo para Líneas de Proforma (Materiales)
# -----------------------------------------------------

class LineaProformaMaterial(SQLModel, table=True):
    """Representa una línea de item de material en una proforma."""
    __tablename__ = "linea_proforma_material"

    id: Optional[int] = Field(default=None, primary_key=True)
    proforma_id: int = Field(foreign_key="proforma.id", index=True)
    tipo_material_origen: str = Field(max_length=50) # ENUM: 'STOCK_DIMENSIONAL', 'CONSUMIBLE', 'SIMPLE'
    stock_item_dimensional_id: Optional[int] = Field(
        default=None, foreign_key="stock_item_dimensional.id", index=True, nullable=True
    )
    material_consumible_id: Optional[int] = Field(
        default=None, foreign_key="material_consumible.id", index=True, nullable=True
    )
    material_simple_id: Optional[int] = Field(
        default=None, foreign_key="material_simple.id", index=True, nullable=True
    )
    descripcion_item: str = Field(max_length=255)
    cantidad: Decimal = Field(max_digits=10, decimal_places=3)
    unidad: str = Field(max_length=50)
    precio_unitario: Decimal = Field(max_digits=12, decimal_places=2)
    total_linea: Decimal = Field(max_digits=15, decimal_places=2)
    detalles_corte_solicitado: Optional[str] = Field(default=None) # Podría ser JSON serializado

    # Relación N:1 con Proforma
    proforma: Proforma = Relationship(back_populates="lineas_material")

    # Relaciones N:1 con los posibles orígenes del material
    stock_item: Optional["StockItemDimensional"] = Relationship(back_populates="lineas_proforma")
    material_consumible: Optional["MaterialConsumible"] = Relationship(back_populates="lineas_proforma")
    material_simple: Optional["MaterialSimple"] = Relationship(back_populates="lineas_proforma")

    # Relación 1:N con LineaProformaServicio (si un servicio se aplica a esta línea)
    servicios_asociados: List["LineaProformaServicio"] = Relationship(back_populates="linea_material_asociada")

    # Relación 1:N con AsignacionTareaOrden (tareas específicas para esta línea)
    tareas_asignadas: List["AsignacionTareaOrden"] = Relationship(back_populates="linea_material")


# -----------------------------------------------------
# Modelo para Líneas de Proforma (Servicios)
# -----------------------------------------------------

class LineaProformaServicio(SQLModel, table=True):
    """Representa una línea de item de servicio en una proforma."""
    __tablename__ = "linea_proforma_servicio"

    id: Optional[int] = Field(default=None, primary_key=True)
    proforma_id: int = Field(foreign_key="proforma.id", index=True)
    servicio_definicion_id: int = Field(foreign_key="servicio_definicion.id", index=True)
    linea_proforma_material_id: Optional[int] = Field(
        default=None, foreign_key="linea_proforma_material.id", index=True, nullable=True
    )
    descripcion_servicio: str = Field(max_length=255)
    cantidad: Decimal = Field(max_digits=10, decimal_places=3)
    precio_unitario: Decimal = Field(max_digits=12, decimal_places=2)
    total_linea: Decimal = Field(max_digits=15, decimal_places=2)
    ruta_imagen_cnc: Optional[str] = Field(default=None, max_length=512, nullable=True)
    detalles_adicionales: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)

    # Relación N:1 con Proforma
    proforma: Proforma = Relationship(back_populates="lineas_servicio")

    # Relación N:1 con ServicioDefinicion
    servicio_definicion: "ServicioDefinicion" = Relationship(back_populates="lineas_proforma")

    # Relación N:1 con LineaProformaMaterial (servicio aplicado a un material)
    linea_material_asociada: Optional["LineaProformaMaterial"] = Relationship(back_populates="servicios_asociados")

    # Relación 1:N con AsignacionTareaOrden (tareas específicas para esta línea)
    tareas_asignadas: List["AsignacionTareaOrden"] = Relationship(back_populates="linea_servicio")


# -----------------------------------------------------
# Modelo para Órdenes de Producción
# -----------------------------------------------------

class OrdenProduccion(SQLModel, table=True):
    """Representa la orden de trabajo para fabricar/preparar lo solicitado en un pedido."""
    __tablename__ = "orden_produccion"

    id: Optional[int] = Field(default=None, primary_key=True)
    # unique=True aquí asegura que un pedido solo genera una orden
    pedido_cliente_id: int = Field(foreign_key="pedido_cliente.id", unique=True, index=True)
    usuario_id_supervisor: Optional[int] = Field(default=None, foreign_key="usuario.id", index=True, nullable=True)
    estado: str = Field(default="PENDIENTE_ASIGNACION", index=True, max_length=50) # ENUM
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_inicio_espera: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_asignacion: Optional[datetime] = Field(default=None, nullable=True)
    fecha_estimada_finalizacion: Optional[datetime] = Field(default=None, nullable=True)
    fecha_real_finalizacion: Optional[datetime] = Field(default=None, nullable=True)
    notas_supervisor: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)
    ruta_imagen_final: Optional[str] = Field(default=None, max_length=512, nullable=True)
    prioridad: int = Field(default=0)

    # Relación 1:1 con PedidoCliente
    pedido: PedidoCliente = Relationship(back_populates="orden_produccion")

    # Relación N:1 con Usuario (Supervisor)
    supervisor: Optional["Usuario"] = Relationship(back_populates="ordenes_supervisadas")

    # Relación 1:N con StockItemDimensional (mermas generadas por esta orden)
    items_merma_generados: List["StockItemDimensional"] = Relationship(back_populates="orden_generadora")

    # Relación 1:N con AsignacionTareaOrden (tareas que componen esta orden)
    asignaciones_tareas: List["AsignacionTareaOrden"] = Relationship(back_populates="orden")


# -----------------------------------------------------
# Modelo para Asignación de Tareas de una Orden
# -----------------------------------------------------

class AsignacionTareaOrden(SQLModel, table=True):
    """Asigna una tarea específica de una orden a un usuario con un rol."""
    __tablename__ = "asignacion_tarea_orden"

    id: Optional[int] = Field(default=None, primary_key=True)
    orden_id: int = Field(foreign_key="orden_produccion.id", index=True)
    # La tarea puede aplicar a una línea específica de servicio o material
    linea_proforma_servicio_id: Optional[int] = Field(
        default=None, foreign_key="linea_proforma_servicio.id", index=True, nullable=True
    )
    linea_proforma_material_id: Optional[int] = Field(
        default=None, foreign_key="linea_proforma_material.id", index=True, nullable=True
    )
    usuario_id_asignado: int = Field(foreign_key="usuario.id", index=True)
    rol_id_contexto: int = Field(foreign_key="rol.id", index=True)
    tipo_tarea: str = Field(max_length=100) # Ej: DIBUJO_CNC, CORTE_MATERIAL
    estado_tarea: str = Field(default="PENDIENTE", max_length=50) # ENUM
    fecha_asignacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_inicio_tarea: Optional[datetime] = Field(default=None, nullable=True)
    fecha_fin_tarea: Optional[datetime] = Field(default=None, nullable=True)
    notas: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)

    # Relación N:1 con OrdenProduccion
    orden: OrdenProduccion = Relationship(back_populates="asignaciones_tareas")

    # Relación N:1 con LineaProformaServicio (opcional)
    linea_servicio: Optional[LineaProformaServicio] = Relationship(back_populates="tareas_asignadas")

    # Relación N:1 con LineaProformaMaterial (opcional)
    linea_material: Optional[LineaProformaMaterial] = Relationship(back_populates="tareas_asignadas")

    # Relación N:1 con Usuario (Asignado)
    usuario_asignado: "Usuario" = Relationship(back_populates="tareas_asignadas")

    # Relación N:1 con Rol (Contexto de la tarea)
    rol_contexto: "Rol" = Relationship(back_populates="asignaciones_tareas")


# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .client_model import Cliente
    from .user_models import Usuario, Rol
    from .inventory_models import StockItemDimensional, MaterialConsumible, MaterialSimple
    from .service_models import ServicioDefinicion
    from .billing_models import VentaFactura

    # Recordatorio: Añadir/Verificar back_populates correspondientes en otros modelos:
    # Cliente: pedidos: List["PedidoCliente"] = ...
    # Usuario: pedidos_creados: List["PedidoCliente"] = ..., proformas_creadas: List["Proforma"] = ..., ordenes_supervisadas: List["OrdenProduccion"] = ..., tareas_asignadas: List["AsignacionTareaOrden"] = ...
    # Rol: asignaciones_tareas: List["AsignacionTareaOrden"] = ...
    # StockItemDimensional: lineas_proforma: List["LineaProformaMaterial"] = ...
    # MaterialConsumible: lineas_proforma: List["LineaProformaMaterial"] = ...
    # MaterialSimple: lineas_proforma: List["LineaProformaMaterial"] = ...
    # ServicioDefinicion: lineas_proforma: List["LineaProformaServicio"] = ...
    # VentaFactura: pedido: PedidoCliente = ..., proforma_productos: Optional[Proforma] = ..., proforma_servicios: Optional[Proforma] = ...