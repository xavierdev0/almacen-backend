
import enum

class TipoProductoServicioEnum(str, enum.Enum):
    PRODUCTO = "PRODUCTO"
    SERVICIO = "SERVICIO"

class EstadoProformaEnum(str, enum.Enum):
    BORRADOR = "BORRADOR"
    PENDIENTE_COTIZACION = "PENDIENTE_COTIZACION"
    PENDIENTE_PAGO = "PENDIENTE_PAGO"
    APROBADA = "APROBADA"
    RECHAZADA = "RECHAZADA"
    CANCELADA = "CANCELADA"

class TipoItemProformaEnum(str, enum.Enum):
    ITEM_INVENTARIO = "ITEM_INVENTARIO"
    PRODUCTO_SERVICIO = "PRODUCTO_SERVICIO"

class EstadoOrdenProduccionEnum(str, enum.Enum):
    PENDIENTE = "PENDIENTE"
    ASIGNADA = "ASIGNADA"
    EN_PROGRESO_CORTE = "EN_PROGRESO_CORTE"
    EN_PROGRESO_CNC = "EN_PROGRESO_CNC"
    EN_REVISION = "EN_REVISION"
    COMPLETADA = "COMPLETADA"
    ENTREGADA = "ENTREGADA"
    CANCELADA = "CANCELADA"

class TipoMaquinaEnum(str, enum.Enum):
    CNC = "CNC"
    CORTE = "CORTE"
    OTRO = "OTRO"

class EstadoMaquinaEnum(str, enum.Enum):
    OPERATIVA = "OPERATIVA"
    EN_MANTENIMIENTO = "EN_MANTENIMIENTO"
    AVERIADA = "AVERIADA"

class TipoMantenimientoEnum(str, enum.Enum):
    PREVENTIVO = "PREVENTIVO"
    CORRECTIVO = "CORRECTIVO"