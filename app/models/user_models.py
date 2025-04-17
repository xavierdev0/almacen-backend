# app/models/user_models.py

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint # Asegúrate de importar UniqueConstraint


# -----------------------------------------------------
# Modelos de Tablas de Enlace (Muchos a Muchos)
# -----------------------------------------------------

class UsuarioRol(SQLModel, table=True):
    """Modelo de tabla de enlace para la relación N:M entre Usuario y Rol."""
    usuario_id: Optional[int] = Field(
        default=None, foreign_key="usuario.id", primary_key=True
    )
    rol_id: Optional[int] = Field(
        default=None, foreign_key="rol.id", primary_key=True
    )


class RolPermiso(SQLModel, table=True):
    """Modelo de tabla de enlace para la relación N:M entre Rol y Permiso."""
    rol_id: Optional[int] = Field(
        default=None, foreign_key="rol.id", primary_key=True
    )
    permiso_id: Optional[int] = Field(
        default=None, foreign_key="permiso.id", primary_key=True
    )

if TYPE_CHECKING: # Asegúrate de importar estas clases aquí
    from .order_models import PedidoCliente, Proforma, OrdenProduccion, AsignacionTareaOrden
    from .machine_models import UsuarioAreaTrabajo, RegistroMantenimiento, ReporteErrorMaquina

# -----------------------------------------------------
# Modelos Principales
# -----------------------------------------------------

class Usuario(SQLModel, table=True):
    """Representa a un empleado/usuario del sistema."""
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, max_length=100, unique=True) # unique=True para SQLModel > 0.0.14
    email: str = Field(index=True, max_length=255, unique=True)    # unique=True para SQLModel > 0.0.14
    contrasena_hash: str = Field(max_length=255)
    nombre_completo: str = Field(max_length=255)
    esta_activo: bool = Field(default=True)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True) # Usamos default_factory para autogenerar en Python
    fecha_ultima_actualizacion: Optional[datetime] = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True) # onupdate para DB

    # Relación N:M con Rol
    roles: List["Rol"] = Relationship(back_populates="usuarios", link_model=UsuarioRol)

    # Relación 1:N con PeriodoIndisponibilidad
    periodos_indisponibilidad: List["PeriodoIndisponibilidad"] = Relationship(back_populates="usuario")

 # Relación 1:N con PedidoCliente (Usuario como vendedor)
    pedidos_creados: List["PedidoCliente"] = Relationship(back_populates="vendedor")

    # Relación 1:N con Proforma (Usuario como creador)
    proformas_creadas: List["Proforma"] = Relationship(back_populates="creador")

    # Relación 1:N con OrdenProduccion (Usuario como supervisor)
    ordenes_supervisadas: List["OrdenProduccion"] = Relationship(back_populates="supervisor")

    # Relación 1:N con AsignacionTareaOrden (Usuario como asignado)
    tareas_asignadas: List["AsignacionTareaOrden"] = Relationship(back_populates="usuario_asignado")

    # Relación N:M con AreaTrabajo (vía UsuarioAreaTrabajo)
    areas_trabajo_link: List["UsuarioAreaTrabajo"] = Relationship(back_populates="usuario")

    # Relación 1:N con RegistroMantenimiento (Usuario como tecnico)
    mantenimientos_realizados: List["RegistroMantenimiento"] = Relationship(back_populates="tecnico")

    # Relación 1:N con ReporteErrorMaquina (Usuario como reportador)
    # Se necesita foreign_keys por haber dos FK a Usuario en ReporteErrorMaquina
    errores_reportados: List["ReporteErrorMaquina"] = Relationship(
        back_populates="reportador",
        sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_reportador]'}
    )

    # Relación 1:N con ReporteErrorMaquina (Usuario como resolutor)
    # Se necesita foreign_keys por haber dos FK a Usuario en ReporteErrorMaquina
    errores_resueltos: List["ReporteErrorMaquina"] = Relationship(
        back_populates="resolutor",
        sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_resolutor]'}
    )


if TYPE_CHECKING: # Asegúrate de importar AsignacionTareaOrden aquí
    from .order_models import AsignacionTareaOrden
    # ... (otras importaciones necesarias para Usuario)

class Rol(SQLModel, table=True):
    """Representa un rol dentro del sistema (ej: Administrador, Vendedor)."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=100, unique=True)
    descripcion: Optional[str] = Field(default=None)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True)

    # Relación N:M con Usuario
    usuarios: List["Usuario"] = Relationship(back_populates="roles", link_model=UsuarioRol)

    # Relación N:M con Permiso
    permisos: List["Permiso"] = Relationship(back_populates="roles", link_model=RolPermiso)

    # Relación 1:N con AsignacionTareaOrden (Rol como contexto de la tarea)
    asignaciones_tareas: List["AsignacionTareaOrden"] = Relationship(back_populates="rol_contexto")

class Permiso(SQLModel, table=True):
    """Representa una acción permitida sobre un recurso (ej: crear proforma)."""
    __table_args__ = (UniqueConstraint("nombre_accion", "nombre_recurso", name="uq_permiso_accion_recurso"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_accion: str = Field(max_length=100)
    nombre_recurso: str = Field(max_length=100)
    descripcion: Optional[str] = Field(default=None)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)

    # Relación N:M con Rol
    roles: List["Rol"] = Relationship(back_populates="permisos", link_model=RolPermiso)


class PeriodoIndisponibilidad(SQLModel, table=True):
    """Registra los periodos en que un usuario no está disponible."""
    # Nombre de tabla explícito por si SQLModel infiere uno diferente
    __tablename__ = "periodo_indisponibilidad" 

    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id", index=True)
    fecha_inicio: datetime = Field()
    fecha_fin: Optional[datetime] = Field(default=None)
    motivo: Optional[str] = Field(default=None) # Considerar usar sa_column=Column(Text) si se espera texto largo

    # Relación N:1 con Usuario
    usuario: Usuario = Relationship(back_populates="periodos_indisponibilidad")


# --- Manejo de Referencias Circulares / Forward References ---
# Esto ayuda a MyPy/Pyright a entender los tipos en las relaciones
# aunque no es estrictamente necesario para que SQLModel/SQLAlchemy funcionen
# if TYPE_CHECKING:
#    # Importaciones de otros módulos si fueran necesarias para las relaciones
#    # from .order_models import AsignacionTareaOrden, PedidoCliente, Proforma, OrdenProduccion
#    # from .machine_models import UsuarioAreaTrabajo, RegistroMantenimiento, ReporteErrorMaquina
#    pass # No necesitamos imports cruzados *dentro* de este archivo por ahora