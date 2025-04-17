# app/models/__init__.py
# app/models/__init__.py
"""
Este archivo __init__.py convierte al directorio 'models' en un paquete de Python
y re-exporta todas las clases de modelos SQLModel definidas en los módulos
separados.

Esto permite importar los modelos de forma más conveniente desde otras partes
de la aplicación, por ejemplo:
  from app.models import Usuario, PedidoCliente
en lugar de:
  from app.models.user_models import Usuario
  from app.models.order_models import PedidoCliente
"""

# Importaciones desde user_models.py
from .user_models import (
    UsuarioRol,
    RolPermiso,
    Usuario,
    Rol,
    Permiso,
    PeriodoIndisponibilidad
)

# Importaciones desde inventory_models.py
from .inventory_models import (
    MaterialDimensional,
    StockItemDimensional,
    MaterialConsumible,
    MaterialSimple
)

# Importaciones desde machine_models.py
from .machine_models import (
    MaquinaHerramienta,
    UsuarioAreaTrabajo,
    AreaTrabajo,
    Maquina,
    Herramienta,
    RegistroMantenimiento,
    ReporteErrorMaquina
)

# Importaciones desde service_models.py
from .service_models import (
    ServicioDefinicion,
    Formula,
    FormulaItem
)

# Importaciones desde order_models.py
from .order_models import (
    PedidoCliente,
    Proforma,
    LineaProformaMaterial,
    LineaProformaServicio,
    OrdenProduccion,
    AsignacionTareaOrden
)

# Importaciones desde client_model.py
from .client_model import Cliente

# Importaciones desde billing_models.py
from .billing_models import VentaFactura


# Opcional: Definir __all__ para controlar qué se importa con 'from app.models import *'
# Es buena práctica definirlo explícitamente si se planea usar 'import *'
# aunque la importación explícita (from app.models import MiModelo) es generalmente preferida.
__all__ = [
    # User Models
    "UsuarioRol",
    "RolPermiso",
    "Usuario",
    "Rol",
    "Permiso",
    "PeriodoIndisponibilidad",
    # Inventory Models
    "MaterialDimensional",
    "StockItemDimensional",
    "MaterialConsumible",
    "MaterialSimple",
    # Machine Models
    "MaquinaHerramienta",
    "UsuarioAreaTrabajo",
    "AreaTrabajo",
    "Maquina",
    "Herramienta",
    "RegistroMantenimiento",
    "ReporteErrorMaquina",
    # Service Models
    "ServicioDefinicion",
    "Formula",
    "FormulaItem",
    # Order Models
    "PedidoCliente",
    "Proforma",
    "LineaProformaMaterial",
    "LineaProformaServicio",
    "OrdenProduccion",
    "AsignacionTareaOrden",
    # Client Models
    "Cliente",
    # Billing Models
    "VentaFactura",
]