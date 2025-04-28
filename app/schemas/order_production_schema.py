# app/schemas/order_production_schema.py

from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from decimal import Decimal

# --- Importar Schemas Relacionados ---
# Necesitamos importar los schemas Read de las entidades relacionadas
# para poder anidarlos en nuestras respuestas.
# Asegúrate de que las rutas de importación sean correctas según tu estructura.

# Si TYPE_CHECKING bloquea las importaciones, asegúrate de que no haya dependencias circulares
# o usa string hints ("UsuarioRead") y llama a model_rebuild() al final.
if TYPE_CHECKING:
    from .usuario_schema import UsuarioRead    
    from .rol_permiso_schema import RolRead
    # Los siguientes podrían ser necesarios si decides anidar detalles de líneas:
    # from .order_schema import LineaProformaMaterialRead, LineaProformaServicioRead

# Importar directamente si no hay problemas de importación circular
#from .usuario_schema import UsuarioRead
from .usuario_schema import UsuarioRead
#from .rol_permiso_schema import RolRead
from .rol_permiso_schema import RolRead

# ===============================================================
# === Schemas para AsignacionTareaOrden                     ===
# ===============================================================

class AsignacionTareaOrdenBase(SQLModel):
    """Schema base con campos comunes de AsignacionTareaOrden."""
    orden_id: int = Field(description="ID de la Orden de Producción a la que pertenece.")
    # IDs de las líneas específicas (opcionalmente retornados)
    linea_proforma_servicio_id: Optional[int] = Field(default=None, description="ID de la línea de servicio específica (si aplica).")
    linea_proforma_material_id: Optional[int] = Field(default=None, description="ID de la línea de material específica (si aplica).")
    # Información clave de la tarea
    tipo_tarea: str = Field(max_length=100, description="Tipo de tarea (ej: DIBUJO_CNC, CORTE_MATERIAL).")
    estado_tarea: str = Field(max_length=50, description="Estado actual de la tarea (ej: PENDIENTE, EN_PROGRESO).")
    notas: Optional[str] = Field(default=None, description="Notas o comentarios sobre la tarea.")
    # IDs de usuario/rol (la información completa irá en Read)
    usuario_id_asignado: Optional[int] = Field(default=None, description="ID del usuario asignado a la tarea (si aplica).") # Nota: Modelo es NOT NULL, pero aquí puede ser None antes de asignar
    rol_id_contexto: int = Field(description="ID del Rol requerido o en cuyo contexto se realiza la tarea.")


class AsignacionTareaOrdenRead(SQLModel): # O heredar de Base si existe
    """Schema para devolver información detallada de una tarea asignada."""
    # Campos básicos
    id: int
    orden_id: int
    linea_proforma_servicio_id: Optional[int]
    linea_proforma_material_id: Optional[int]
    tipo_tarea: str
    estado_tarea: str
    notas: Optional[str]
    # IDs (útil tenerlos explícitos)
    usuario_id_asignado: int # Es NOT NULL en BD, así que el ID debe estar
    rol_id_contexto: int    # Es NOT NULL en BD, así que el ID debe estar
    # Fechas
    fecha_asignacion: Optional[datetime]
    fecha_inicio_tarea: Optional[datetime]
    fecha_fin_tarea: Optional[datetime]

    # Información anidada (Asumiendo que el servicio SIEMPRE carga estas relaciones para el Read)
    # Si hay casos donde no se cargan, mantener Optional y manejar en el frontend.
    # Pero si la FK es NOT NULL, lo lógico es que el objeto relacionado exista y se cargue.
    usuario_asignado: UsuarioRead = Field(description="Datos del usuario asignado.")
    rol_contexto: RolRead = Field(description="Datos del rol asociado al contexto de la tarea.")


    model_config = {"from_attributes": True}

# ===============================================================
# === Schemas para OrdenProduccion                          ===
# ===============================================================

class OrdenProduccionBase(SQLModel):
    """Schema base con campos comunes de OrdenProduccion."""
    pedido_cliente_id: int = Field(description="ID del PedidoCliente que generó esta orden.")
    estado: str = Field(max_length=50, description="Estado actual de la orden de producción.")
    prioridad: int = Field(default=0, description="Prioridad de la orden (mayor número = más prioridad).")
    # Campos opcionales que podrían definirse/actualizarse
    fecha_estimada_finalizacion: Optional[datetime] = Field(default=None, description="Fecha estimada de finalización.")
    notas_supervisor: Optional[str] = Field(default=None, description="Notas añadidas por el supervisor.")
    ruta_imagen_final: Optional[str] = Field(default=None, max_length=512, description="Ruta a la imagen del resultado final.")
    # ID del supervisor (la info completa va en Read)
    usuario_id_supervisor: Optional[int] = Field(default=None, description="ID del supervisor que finalizó la orden.")


class OrdenProduccionRead(OrdenProduccionBase):
    """Schema para devolver información detallada de una Orden de Producción."""
    id: int
    # Fechas clave
    fecha_creacion: Optional[datetime]
    fecha_inicio_espera: Optional[datetime] # Para calcular tiempo en espera
    fecha_asignacion: Optional[datetime] = None
    fecha_real_finalizacion: Optional[datetime] = None

    # Información anidada del supervisor (si está asignado)
    supervisor: Optional[UsuarioRead] = Field(default=None, description="Datos del supervisor asignado.")

    # Lista de tareas asociadas a esta orden
    asignaciones_tareas: List[AsignacionTareaOrdenRead] = Field(default=[], description="Lista de tareas requeridas para esta orden.")

    # Opcional: Incluir info básica del pedido o cliente? Por ahora solo ID.
    # pedido: Optional[PedidoClienteRead] = None

    model_config = {"from_attributes": True}

class OrdenProduccionCreate(SQLModel):
    """
    Schema para la creación interna de una Orden de Producción.
    Normalmente no se expone directamente como API, sino que se usa en el servicio.
    """
    pedido_cliente_id: int
    estado: str = "PENDIENTE_ASIGNACION" # Estado inicial
    prioridad: int = 0 # Prioridad inicial
    # Otros campos se rellenan al crearse o actualizarse

class OrdenProduccionUpdate(SQLModel):
    """Schema para actualizar una Orden de Producción (ej: estado, supervisor). Todos opcionales."""
    estado: Optional[str] = Field(default=None, max_length=50)
    usuario_id_supervisor: Optional[int] = Field(default=None)
    fecha_asignacion: Optional[datetime] = Field(default=None)
    fecha_estimada_finalizacion: Optional[datetime] = Field(default=None)
    fecha_real_finalizacion: Optional[datetime] = Field(default=None)
    notas_supervisor: Optional[str] = Field(default=None)
    ruta_imagen_final: Optional[str] = Field(default=None, max_length=512)
    prioridad: Optional[int] = Field(default=None)


# --- Actualizar Forward References ---
# Necesario si hay referencias circulares entre los schemas definidos AQUÍ.
# Por ahora, AsignacionTareaOrdenRead usa UsuarioRead/RolRead (importados)
# y OrdenProduccionRead usa AsignacionTareaOrdenRead (definido antes).
# No parece haber referencias circulares *dentro* de este archivo.
# AsignacionTareaOrdenRead.model_rebuild() # No necesario por ahora
# OrdenProduccionRead.model_rebuild() # No necesario por ahora