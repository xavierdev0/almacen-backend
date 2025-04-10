# tests/conftest.py
import pytest
from typing import Generator, Any
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool
from sqlalchemy.orm import sessionmaker

# Importa tu app FastAPI y la dependencia get_db
from app.main import app
from app.core.database import get_db
from app.core.config import settings # Para obtener settings de prueba si es necesario

# --- Configuración de Base de Datos de Prueba ---
# Usa una base de datos en memoria (SQLite) para pruebas rápidas y aisladas
DATABASE_URL_TEST = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL_TEST,
    connect_args={"check_same_thread": False}, # Necesario para SQLite en memoria
    poolclass=StaticPool, # Deshabilita el pooling para SQLite en memoria
)

# Crea una fábrica de sesiones específica para pruebas
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=Session
)

# --- Fixtures ---

@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    """Crea las tablas en la BD de prueba antes de iniciar los tests."""
    # Asegúrate de importar todos tus modelos SQLModel aquí
    # para que metadata los conozca
    from app import models # O importa individualmente si es necesario
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine) # Limpia después de los tests

@pytest.fixture(scope="function")
def db_session() -> Generator[Session, None, None]:
    """Fixture para obtener una sesión de BD de prueba por test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(db_session: Session) -> Generator[TestClient, None, None]:
    """Fixture para obtener un TestClient de FastAPI con la BD de prueba."""

    # Sobrescribe la dependencia get_db para usar la sesión de prueba
    def override_get_db() -> Generator[Session, None, None]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client

    # Limpia la sobrescritura después del test
    del app.dependency_overrides[get_db]

# Podrías añadir fixtures para crear usuarios de prueba, obtener tokens, etc.
# Ejemplo:
# @pytest.fixture(scope="function")
# def test_user(db_session: Session) -> models.Usuario:
#     from app.services import usuario_service
#     from app.schemas import UsuarioCreate
#     user_in = UsuarioCreate(email="test@example.com", username="testuser", password="password123")
#     return usuario_service.create_new_user(db_session, user_in)

# @pytest.fixture(scope="function")
# def auth_headers(client: TestClient, test_user: models.Usuario) -> dict[str, str]:
#     login_data = {"username": test_user.username, "password": "password123"}
#     response = client.post(f"{settings.API_V1_STR}/auth/token", data=login_data)
#     token = response.json()["access_token"]
#     return {"Authorization": f"Bearer {token}"}