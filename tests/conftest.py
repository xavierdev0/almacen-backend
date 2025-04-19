# tests/conftest.py
import os
import sys
from typing import Generator, Any, Dict, List, Set, Tuple, Union # Añadir Set, Tuple, Union

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine, select # <<< Asegurar import SQLModel
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import alembic.config
import alembic.command
import sqlalchemy as sa

# --- 1. Carga de Configuración de Prueba ---
env_path = '.env.test'
if os.path.exists(env_path):
    print(f"\nCargando configuración de prueba desde: {env_path}")
    load_dotenv(dotenv_path=env_path, override=True)
else:
    print(f"\nADVERTENCIA: No se encontró {env_path}.")
    pytest.exit(f"Archivo de configuración de prueba '{env_path}' no encontrado.", returncode=1)

# --- 2. Importar Componentes de la App DESPUÉS de cargar .env.test ---
from app.core.config import settings
from app.main import app
from app.core.database import get_db
# Importar modelos necesarios para seeding y fixtures
from app.models import Usuario, Rol, Permiso, UsuarioRol, RolPermiso
# Importar servicios y schemas para crear usuarios de prueba
from app.services import usuario_service
from app.schemas.usuario_schema import UsuarioCreate
# Importar datos iniciales centralizados
from app.initial_data import initial_roles, initial_permissions, role_permission_mapping
from app.repositories import usuario_repository

# --- 3. Configuración de Base de Datos de Prueba ---
TEST_DATABASE_URL = settings.DATABASE_URL
print(f"URL de base de datos para pruebas (desde settings): {TEST_DATABASE_URL[:TEST_DATABASE_URL.find('@') + 1]}***")
# Usamos recreate_engine para asegurar que se use la URL de prueba cargada
engine = create_engine(TEST_DATABASE_URL, echo=False, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)



# --- 5. Fixture Principal de Setup (Session Scope) ---
@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """
    Prepara la BD de prueba para TODA la sesión de tests:
    1. Aplica migraciones Alembic (schema + seeding completo). <-- AHORA HACE TODO
    2. LIMPIA la BD al final de la sesión.
    """
    print("\n--- [SETUP SESIÓN] Iniciando preparación de BD de prueba ---")
    # 1. Aplicar Migraciones (Ahora incluye schema + seeding completo)
    print("Ejecutando 'alembic upgrade head'...")
    alembic_cfg = alembic.config.Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", TEST_DATABASE_URL)
    try:
        # Esto ahora aplica fa15..., cb1b..., y 39f5...
        alembic.command.upgrade(alembic_cfg, "head")
        print("Migraciones aplicadas exitosamente (schema + seeding).")
    except Exception as e:
        print(f"\nERROR aplicando migraciones: {e}")
        import traceback
        traceback.print_exc()
        pytest.fail(f"Fallo crítico al aplicar migraciones Alembic: {e}")
        return # Detener setup si migraciones fallan

    print("--- [SETUP SESIÓN] Base de datos lista para las pruebas (via Alembic). ---")

    yield # Aquí se ejecutan todas las pruebas de la sesión

    # --- 3. Limpieza al final de la SESIÓN (Sin cambios) ---
    print("\n--- [TEARDOWN SESIÓN] Limpiando BD de prueba (drop_all) ---")
    try:
        SQLModel.metadata.drop_all(bind=engine)
        print("--- [TEARDOWN SESIÓN] BD limpiada exitosamente. ---")
    except Exception as drop_exc:
        print(f"ERROR durante drop_all al final de la sesión: {drop_exc}")

# --- 6. Fixture para Sobrescribir Dependencia get_db (sin cambios) ---
def override_get_db() -> Generator[Session, None, None]:
    db = None
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        if db is not None:
            # No hacemos commit aquí, dejamos que los tests/fixtures lo manejen
            # Solo cerramos la sesión
            db.close()
app.dependency_overrides[get_db] = override_get_db


# --- 7. Fixtures de Pytest para Tests (Sin cambios respecto a la última versión) ---

# Sesión por función para aislamiento
@pytest.fixture(scope="function")
def db_session(setup_test_database) -> Generator[Session, None, None]: # Depende de setup
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        # Rollback para deshacer cambios no commiteados en esta sesión de función
        db.rollback()
        db.close()

# Sesión por módulo para setup de datos compartidos
@pytest.fixture(scope="module")
def module_db_session(setup_test_database) -> Generator[Session, None, None]: # Depende de setup
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        # Rollback para deshacer cambios no commiteados en esta sesión de módulo
        db.rollback()
        db.close()

# Cliente básico
@pytest.fixture(scope="module")
def client(setup_test_database) -> Generator[TestClient, None, None]: # Depende de setup
    # Asegurarnos que las overrides estén aplicadas antes de crear el cliente
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client

# Roles iniciales (scope session)
@pytest.fixture(scope="session")
def seeded_roles(setup_test_database) -> Dict[str, Rol]: # Depende de setup
    db = TestingSessionLocal()
    try:
        print("DEBUG: Obteniendo roles iniciales para fixtures (scope='session')...")
        roles_db = db.exec(select(Rol)).all()
        roles_map = {rol.nombre: rol for rol in roles_db}
        if not roles_map or len(roles_map) < 5:
             pytest.fail("No se encontraron roles iniciales suficientes en la BD.")
        return roles_map
    finally:
        db.close()

# ID Rol Vendedor (scope module)
@pytest.fixture(scope="module")
def vendedor_role_id(seeded_roles: Dict[str, Rol]) -> int: # Ya no necesita db directa
    role = seeded_roles.get("Vendedor")
    if not role or not role.id: # Verificar ID también
        pytest.fail("Rol 'Vendedor' o su ID no encontrado en roles pre-cargados.")
    return role.id

# Fábrica de Usuarios (scope module)
@pytest.fixture(scope="module")
def test_user_factory(module_db_session: Session, seeded_roles: Dict[str, Rol]):
    """Fábrica para crear usuarios de prueba con roles específicos."""
    print(f"\nDEBUG: Iniciando test_user_factory (scope='module') con session id: {id(module_db_session)}")
    created_users_for_cleanup = [] # Guardar IDs para limpieza

    def _create_user(username: str, email: str, password: str, roles_names: List[str] = None) -> Usuario:
        print(f"DEBUG: _create_user: Intentando crear/obtener usuario '{username}'...")
        # Asegurarse de usar la sesión correcta (module_db_session)
        session = module_db_session
        try:
            # Buscar si ya existe en esta sesión de módulo
            existing = usuario_repository.get_usuario_by_username(db=session, username=username)
            if existing:
                print(f"DEBUG: _create_user: Usuario '{username}' ya existía en sesión de módulo.")
                # Asegurar que esté en la lista de limpieza si no lo estaba ya
                if existing.id not in [u["id"] for u in created_users_for_cleanup]:
                     created_users_for_cleanup.append({"id": existing.id, "username": username})
                # Recargar roles por si acaso se modificaron en otro test del módulo
                session.refresh(existing, attribute_names=["roles"])
                return existing

            role_ids_to_assign = []
            if roles_names:
                for name in roles_names:
                    role = seeded_roles.get(name) # Usar roles pre-cargados
                    if not role or not role.id: pytest.fail(f"Rol '{name}' no encontrado en roles pre-cargados.")
                    role_ids_to_assign.append(role.id)

            user_in = UsuarioCreate(
                username=username, email=email, password=password,
                nombre_completo=f"Test {username.capitalize()}",
                rol_ids=role_ids_to_assign if role_ids_to_assign else None
            )
            # Usar el servicio para crear el usuario (maneja hashing, etc.)
            user = usuario_service.create_new_user(db=session, user_in=user_in)

            # Verificar inmediatamente en la MISMA sesión
            retrieved_user = session.get(Usuario, user.id)
            if retrieved_user:
                print(f"DEBUG: _create_user: VERIFICADO - Usuario ID={user.id} ('{retrieved_user.username}') creado y encontrado en sesión.")
                # Forzar carga de roles si se asignaron para asegurar que estén disponibles
                if roles_names:
                    session.refresh(retrieved_user, attribute_names=["roles"])
                    print(f"DEBUG: _create_user: Roles asignados (verif.): {[r.nombre for r in retrieved_user.roles]}")
            else:
                # Esto sería muy extraño si create_new_user no falló
                print(f"ERROR CRÍTICO: _create_user: Usuario ID={user.id} NO encontrado después de crear!")
                pytest.fail(f"No se pudo verificar creación del usuario '{username}' en la misma sesión.")

            # Añadir a la lista para limpieza al final del módulo
            created_users_for_cleanup.append({"id": user.id, "username": username})
            return user # Devolver el usuario recién creado o existente

        except Exception as e:
             print(f"ERROR dentro de _create_user para {username}: {e}")
             import traceback
             traceback.print_exc()
             # Intentar rollback en la sesión del módulo
             session.rollback()
             raise

    yield _create_user # La factory devuelve la función interna

    # --- Limpieza al final del MÓDULO (Sin cambios en la lógica, solo verificación) ---
    print(f"\nDEBUG: test_user_factory (TEARDOWN Módulo): Limpiando {len(created_users_for_cleanup)} usuarios: {[u['username'] for u in created_users_for_cleanup]}")
    if created_users_for_cleanup:
        user_ids = [u["id"] for u in created_users_for_cleanup]
        # Usar una nueva sesión dedicada para limpieza es más seguro
        cleanup_db = TestingSessionLocal()
        try:
            # 1. Eliminar asociaciones usuario-rol primero
            print(f"DEBUG (Cleanup): Eliminando links usuario_rol para usuarios: {user_ids}")
            stmt_links = sa.delete(UsuarioRol).where(UsuarioRol.usuario_id.in_(user_ids))
            cleanup_db.execute(stmt_links)

            # 2. Eliminar usuarios
            print(f"DEBUG (Cleanup): Eliminando usuarios: {user_ids}")
            stmt_users = sa.delete(Usuario).where(Usuario.id.in_(user_ids))
            result = cleanup_db.execute(stmt_users)

            # 3. Hacer commit de ambas eliminaciones juntas
            cleanup_db.commit()
            print(f"DEBUG (Cleanup): Usuarios de prueba y sus links eliminados: {user_ids} (Count: {result.rowcount})")
        except Exception as e:
             print(f"ERROR limpiando usuarios de prueba: {e}")
             cleanup_db.rollback()
        finally:
             cleanup_db.close() # Siempre cerrar la sesión de limpieza

# Usuarios de prueba (usan scope module)
@pytest.fixture(scope="module")
def admin_user(test_user_factory) -> Usuario:
    return test_user_factory(username="testadmin", email="admin@test.com", password="password123", roles_names=["Administrador"])

@pytest.fixture(scope="module")
def vendedor_user(test_user_factory) -> Usuario:
    return test_user_factory(username="testvendedor", email="vendedor@test.com", password="password123", roles_names=["Vendedor"])

# Tokens y Clientes Autenticados (usan scope module)
@pytest.fixture(scope="module")
def get_auth_token(client: TestClient):
    # ... (código sin cambios) ...
    def _get_token(username: str, password: str) -> str:
        response = client.post(f"{settings.API_V1_STR}/auth/token", data={"username": username, "password": password})
        if response.status_code != 200:
             pytest.fail(f"No se pudo obtener token para {username}. Status: {response.status_code}, Body: {response.text}")
        return response.json()["access_token"]
    return _get_token

@pytest.fixture(scope="module")
def admin_token(get_auth_token, admin_user: Usuario) -> str:
    # Esperar a que admin_user esté completamente listo
    assert admin_user.id is not None
    return get_auth_token(username=admin_user.username, password="password123")

@pytest.fixture(scope="module")
def vendedor_token(get_auth_token, vendedor_user: Usuario) -> str:
    # Esperar a que vendedor_user esté completamente listo
    assert vendedor_user.id is not None
    return get_auth_token(username=vendedor_user.username, password="password123")

@pytest.fixture(scope="function")
def admin_client(client: TestClient, admin_token: str) -> TestClient:
    # Aplicar header al cliente base del módulo
    client.headers["Authorization"] = f"Bearer {admin_token}"
    print(f"DEBUG: Configurado admin_client con token: ...{admin_token[-6:]}")
    yield client # Devolver el cliente configurado
    # Limpiar header al final del módulo (buena práctica aunque el cliente es por módulo)
    if "Authorization" in client.headers:
         del client.headers["Authorization"]

@pytest.fixture(scope="function")
def vendedor_client(client: TestClient, vendedor_token: str) -> TestClient:
    # Aplicar header al cliente base del módulo
    client.headers["Authorization"] = f"Bearer {vendedor_token}"
    print(f"DEBUG: Configurado vendedor_client con token: ...{vendedor_token[-6:]}")
    yield client # Devolver el cliente configurado
    # Limpiar header al final del módulo
    if "Authorization" in client.headers:
        del client.headers["Authorization"]