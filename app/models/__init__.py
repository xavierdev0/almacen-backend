# app/models/__init__.py

# Importa Enums
from .enums import (
    TipoProductoServicioEnum,
    EstadoProformaEnum,
    TipoItemProformaEnum,
    EstadoOrdenProduccionEnum,
    TipoMaquinaEnum,
    EstadoMaquinaEnum,
    TipoMantenimientoEnum
)

# Importa Modelos y Link Models (si se definieron en el mismo archivo del modelo principal)
from .usuario_model import Usuario, UsuarioRolLink
from .rol_model import Rol, RolPermisoLink
from .permiso_model import Permiso
from .cliente_model import Cliente
from .tipo_material_model import TipoMaterial
from .item_inventario_model import ItemInventario
from .definicion_producto_servicio_model import DefinicionProductoServicio
from .proforma_model import Proforma, LineaProforma
from .orden_produccion_model import OrdenProduccion
from .asignacion_orden_produccion_model import AsignacionOrdenProduccion
from .maquina_model import Maquina
from .registro_mantenimiento_model import RegistroMantenimiento
from .reporte_error_maquina_model import ReporteErrorMaquina
from .periodo_indisponibilidad_model import PeriodoIndisponibilidad
from .venta_factura_model import VentaFactura

# Opcional: Lista __all__ para controlar 'from app.models import *'
__all__ = [
     "Usuario", "UsuarioRolLink", "Rol", "RolPermisoLink", "Permiso", "Cliente",
     "TipoMaterial", "ItemInventario", "DefinicionProductoServicio", "Proforma",
     "LineaProforma", "OrdenProduccion", "AsignacionOrdenProduccion", "Maquina",
     "RegistroMantenimiento", "ReporteErrorMaquina", "PeriodoIndisponibilidad",
     "VentaFactura",
    # Enums
     "TipoProductoServicioEnum", "EstadoProformaEnum", "TipoItemProformaEnum",
     "EstadoOrdenProduccionEnum", "TipoMaquinaEnum", "EstadoMaquinaEnum",
     "TipoMantenimientoEnum"
 ]


print("Modelos SQLModel (versión refinada) cargados") # Opcional