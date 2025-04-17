# app/models/machine_models.py

from datetime import datetime, date # Importar date también
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .user_models import Usuario # Necesario para las relaciones

# -----------------------------------------------------
# Modelos de Tablas de Enlace (Muchos a Muchos)
# -----------------------------------------------------

class MaquinaHerramienta(SQLModel, table=True):
    """Modelo de tabla de enlace para la relación N:M entre Maquina y Herramienta."""
    __tablename__ = "maquina_herramienta"

    maquina_id: Optional[int] = Field(
        default=None, foreign_key="maquina.id", primary_key=True
    )
    herramienta_id: Optional[int] = Field(
        default=None, foreign_key="herramienta.id", primary_key=True
    )
    fecha_asignacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    posicion: Optional[str] = Field(default=None, max_length=50)

    # Relaciones para acceder fácilmente desde el link model (opcional pero útil)
    maquina: "Maquina" = Relationship(back_populates="herramientas_link")
    herramienta: "Herramienta" = Relationship(back_populates="maquinas_link")


class UsuarioAreaTrabajo(SQLModel, table=True):
    """Modelo de tabla de enlace para la relación N:M entre Usuario y AreaTrabajo."""
    __tablename__ = "usuario_area_trabajo"

    usuario_id: Optional[int] = Field(
        default=None, foreign_key="usuario.id", primary_key=True
    )
    area_trabajo_id: Optional[int] = Field(
        default=None, foreign_key="area_trabajo.id", primary_key=True
    )

    # Relaciones para acceder fácilmente desde el link model (opcional pero útil)
    usuario: "Usuario" = Relationship(back_populates="areas_trabajo_link")
    area_trabajo: "AreaTrabajo" = Relationship(back_populates="usuarios_link")

# -----------------------------------------------------
# Modelos Principales
# -----------------------------------------------------

class AreaTrabajo(SQLModel, table=True):
    """Representa un área física o lógica dentro del almacén/taller."""
    __tablename__ = "area_trabajo"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True, max_length=150)
    descripcion: Optional[str] = Field(default=None)

    # Relación 1:N con Maquina (un área puede tener varias máquinas)
    maquinas: List["Maquina"] = Relationship(back_populates="area_trabajo")

    # Relación N:M con Usuario (vía UsuarioAreaTrabajo)
    # El atributo 'usuarios' se puede obtener a través del link model si se necesita
    usuarios_link: List["UsuarioAreaTrabajo"] = Relationship(back_populates="area_trabajo")


class Maquina(SQLModel, table=True):
    """Representa una máquina utilizada en el proceso productivo."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150)
    tipo: str = Field(max_length=50) # Ej: 'CNC_ROUTER', 'CNC_LASER', 'CORTE_SIERRA'
    modelo: Optional[str] = Field(default=None, max_length=150)
    numero_serie: Optional[str] = Field(default=None, unique=True, index=True, max_length=150)
    area_trabajo_id: Optional[int] = Field(default=None, foreign_key="area_trabajo.id", index=True, nullable=True)
    margen_perdida_mm: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=2, nullable=True)
    estado: str = Field(default="OPERATIVA", max_length=50) # Ej: 'OPERATIVA', 'EN_MANTENIMIENTO', 'AVERIADA'
    fecha_adquisicion: Optional[date] = Field(default=None, nullable=True) # Usamos date para solo fecha
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación N:1 con AreaTrabajo (una máquina pertenece a un área, opcionalmente)
    area_trabajo: Optional["AreaTrabajo"] = Relationship(back_populates="maquinas")

    # Relación N:M con Herramienta (vía MaquinaHerramienta)
    herramientas_link: List["MaquinaHerramienta"] = Relationship(back_populates="maquina")

    # Relación 1:N con RegistroMantenimiento
    registros_mantenimiento: List["RegistroMantenimiento"] = Relationship(back_populates="maquina")

    # Relación 1:N con ReporteErrorMaquina
    reportes_errores: List["ReporteErrorMaquina"] = Relationship(back_populates="maquina")


class Herramienta(SQLModel, table=True):
    """Representa una herramienta o accesorio que puede ser usado por una máquina."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150)
    tipo: Optional[str] = Field(default=None, max_length=100)
    descripcion: Optional[str] = Field(default=None)
    codigo_interno: Optional[str] = Field(default=None, unique=True, index=True, max_length=50)

    # Relación N:M con Maquina (vía MaquinaHerramienta)
    maquinas_link: List["MaquinaHerramienta"] = Relationship(back_populates="herramienta")


class RegistroMantenimiento(SQLModel, table=True):
    """Registra una actividad de mantenimiento realizada sobre una máquina."""
    __tablename__ = "registro_mantenimiento"

    id: Optional[int] = Field(default=None, primary_key=True)
    maquina_id: int = Field(foreign_key="maquina.id", index=True)
    usuario_id_tecnico: Optional[int] = Field(default=None, foreign_key="usuario.id", index=True, nullable=True)
    fecha_mantenimiento: datetime = Field()
    tipo: str = Field(max_length=50) # Ej: 'PREVENTIVO', 'CORRECTIVO', 'INSPECCION'
    descripcion: str = Field() # Considerar sa_column=Column(Text)
    costo_repuestos: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2, nullable=True)
    horas_mano_obra: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=2, nullable=True)

    # Relación N:1 con Maquina
    maquina: Maquina = Relationship(back_populates="registros_mantenimiento")

    # Relación N:1 con Usuario (Técnico)
    tecnico: Optional["Usuario"] = Relationship(back_populates="mantenimientos_realizados")


class ReporteErrorMaquina(SQLModel, table=True):
    """Registra un error o avería reportado para una máquina."""
    __tablename__ = "reporte_error_maquina"

    id: Optional[int] = Field(default=None, primary_key=True)
    maquina_id: int = Field(foreign_key="maquina.id", index=True)
    usuario_id_reportador: int = Field(foreign_key="usuario.id", index=True)
    fecha_reporte: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    descripcion_error: str = Field() # Considerar sa_column=Column(Text)
    codigo_error: Optional[str] = Field(default=None, max_length=100)
    prioridad: Optional[str] = Field(default="MEDIA", max_length=50) # Ej: 'BAJA', 'MEDIA', 'ALTA', 'CRITICA'
    esta_resuelto: bool = Field(default=False, index=True)
    fecha_resolucion: Optional[datetime] = Field(default=None, nullable=True)
    usuario_id_resolutor: Optional[int] = Field(default=None, foreign_key="usuario.id", index=True, nullable=True)
    detalles_resolucion: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)

    # Relación N:1 con Maquina
    maquina: Maquina = Relationship(back_populates="reportes_errores")

    # Relación N:1 con Usuario (Reportador)
    reportador: "Usuario" = Relationship(
        back_populates="errores_reportados",
        sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_reportador]'}
    )

    # Relación N:1 con Usuario (Resolutor)
    resolutor: Optional["Usuario"] = Relationship(
        back_populates="errores_resueltos",
        sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_resolutor]'}
    )

# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .user_models import Usuario # Importamos Usuario para type hints

    # Añadir las relaciones inversas correspondientes en user_models.py:
    # class Usuario(SQLModel, table=True):
    #     ...
    #     areas_trabajo_link: List["UsuarioAreaTrabajo"] = Relationship(back_populates="usuario")
    #     mantenimientos_realizados: List["RegistroMantenimiento"] = Relationship(back_populates="tecnico")
    #     errores_reportados: List["ReporteErrorMaquina"] = Relationship(back_populates="reportador", sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_reportador]'})
    #     errores_resueltos: List["ReporteErrorMaquina"] = Relationship(back_populates="resolutor", sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_resolutor]'})
    #     ...