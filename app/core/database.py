# app/core/database.py

from sqlmodel import SQLModel, Session, create_engine
# Usamos sessionmaker de sqlalchemy.orm directamente, es compatible
from sqlalchemy.orm import sessionmaker
from typing import Generator

# Importa tu objeto de configuración (ajusta la ruta si es necesario)
from app.core.config import settings

# 1. URL de la Base de Datos desde la configuración
# Asegúrate de que tu .env tenga una línea como:
# DATABASE_URL=mysql+mysqlconnector://tu_usuario:tu_contraseña@localhost:3306/tu_base_de_datos
DATABASE_URL = settings.DATABASE_URL

# Argumentos específicos para el engine (pueden variar según driver/necesidad)
# Para MySQL con mysql-connector-python, usualmente no se necesitan args especiales aquí.
connect_args = {}

# 2. Crear el Engine de SQLAlchemy/SQLModel
# pool_recycle: Reutiliza conexiones después de X segundos (ej. 3600 = 1 hora) para evitar timeouts de MySQL.
# pool_pre_ping: Verifica la conexión antes de usarla del pool.
# echo=True: Imprime las sentencias SQL ejecutadas (útil para depuración, quitar en producción).
engine = create_engine(
    DATABASE_URL,
    echo=False, # Cambiar a True para depuración SQL
    connect_args=connect_args,
    pool_recycle=3600,
    pool_pre_ping=True
)

# 3. Crear la fábrica de Sesiones (SessionLocal)
# autocommit=False y autoflush=False son configuraciones estándar para usar con FastAPI.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session # Usamos la Session de SQLModel/SQLAlchemy
)

# 4. Dependencia de FastAPI para obtener la sesión de BD
def get_db() -> Generator[Session, None, None]:
    """
    Generador de dependencia para obtener una sesión de base de datos.

    Yields:
        Session: Objeto de sesión de base de datos.

    Asegura que la sesión se cierre después de su uso.
    """
    # Llama a la fábrica para obtener una sesión
    db = SessionLocal()
    try:
        # Entrega la sesión al contexto que la pidió (ej. tu endpoint)
        yield db
    finally:
        # Siempre cierra la sesión al finalizar, incluso si hubo errores
        db.close()


# ---------------------------------------------------------------------------
# Opcional: Función para crear tablas (¡Cuidado si usas Alembic!)
# ---------------------------------------------------------------------------
# Generalmente, Alembic maneja la creación y actualización de tablas.
# Esta función es más útil para pruebas rápidas o configuraciones iniciales MUY simples.
# NO la llames desde tu aplicación principal si estás usando migraciones de Alembic.
def create_db_and_tables():
     """
     Crea todas las tablas definidas en los metadatos de SQLModel.
     ADVERTENCIA: Usar con precaución si se gestionan migraciones con Alembic.
     """
     # Asegúrate de que todos tus modelos SQLModel sean importados ANTES de llamar a create_all
     # Ejemplo: from app.models.usuario_model import Usuario
     #          from app.models.rol_model import Rol
     #          ...etc para todos los modelos...
     print("Intentando crear tablas (si no existen)...")
     SQLModel.metadata.create_all(engine)
     print("Tablas verificadas/creadas.")
# ---------------------------------------------------------------------------