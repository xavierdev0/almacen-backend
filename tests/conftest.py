# >>> INICIO: Código a MODIFICAR en app/tests/conftest.py <<<
import os
import sys
from typing import Generator, Any, Dict, List, Set, Tuple, Union, Callable

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient # <--- Asegurar que TestClient está importado
from sqlmodel import SQLModel, Session, create_engine, select
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import alembic.config
import alembic.command
import sqlalchemy as sa

# --- 1. Carga de Configuración de Prueba ---
# ... (sin cambios) ...
env_path = '.env.test'
if os.path.exists(env_path):
    print(f"\nCargando configuración de prueba desde: {env_path}")
    load_dotenv(dotenv_path=env_path, override=True)
else:
    print(f"\nADVERTENCIA: No se encontró {env_path}.")
    pytest.exit(f"Archivo de configuración de prueba '{env_path}' no encontrado.", returncode=1)


# --- 2. Importar Componentes de la App ---
# ... (sin cambios) ...
from app.core.config import settings
from app.main import app # <--- Importar app
from app.core.database import get_db
from app.models import Usuario, Rol, Permiso, UsuarioRol, RolPermiso # <--- Incluir Permiso
from app.services import usuario_service
from app.schemas.usuario_schema import UsuarioCreate
from app.initial_data import initial_roles, initial_permissions, role_permission_mapping
from app.repositories import usuario_repository, permiso_repository # <--- Incluir permiso_repository


# --- 3. Configuración de Base de Datos de Prueba ---
# ... (sin cambios) ...
TEST_DATABASE_URL = settings.DATABASE_URL
print(f"URL de base de datos para pruebas (desde settings): {TEST_DATABASE_URL[:TEST_DATABASE_URL.find('@') + 1]}***")
engine = create_engine(TEST_DATABASE_URL, echo=False, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)


# --- 5. Fixture Principal de Setup (Session Scope) ---
# ... (sin cambios) ...
@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    # ... (código existente) ...
    print("\n--- [SETUP SESIÓN] Iniciando preparación de BD de prueba ---")
    alembic_cfg = alembic.config.Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", TEST_DATABASE_URL)
    try:
        alembic.command.upgrade(alembic_cfg, "head")
        print("Migraciones aplicadas exitosamente (schema + seeding).")
    except Exception as e:
        print(f"\nERROR aplicando migraciones: {e}")
        import traceback
        traceback.print_exc()
        pytest.fail(f"Fallo crítico al aplicar migraciones Alembic: {e}")
        return
    print("--- [SETUP SESIÓN] Base de datos lista para las pruebas (via Alembic). ---")
    yield
    print("\n--- [TEARDOWN SESIÓN] Limpiando BD de prueba (drop_all) ---")
    try:
        SQLModel.metadata.drop_all(bind=engine)
        print("--- [TEARDOWN SESIÓN] BD limpiada exitosamente. ---")
    except Exception as drop_exc:
        print(f"ERROR durante drop_all al final de la sesión: {drop_exc}")

# --- 6. Fixture para Sobrescribir Dependencia get_db ---
# ... (sin cambios) ...
def override_get_db() -> Generator[Session, None, None]:
    db = None
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        if db is not None:
            db.close()
app.dependency_overrides[get_db] = override_get_db


# --- 7. Fixtures de Pytest para Tests ---

# ... (fixtures db_session, module_db_session sin cambios) ...
@pytest.fixture(scope="function")
def db_session(setup_test_database) -> Generator[Session, None, None]: # Depende de setup
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()

@pytest.fixture(scope="module")
def module_db_session(setup_test_database) -> Generator[Session, None, None]: # Depende de setup
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()


# *** INICIO SECCIÓN MODIFICADA ***

@pytest.fixture(scope="module")
def base_client(setup_test_database) -> Generator[TestClient, None, None]:
    """Cliente de prueba base, no autenticado (module scope)."""
    # Asegurarse que app tiene los overrides aplicados ANTES de crear TestClient
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        print(f"DEBUG [conftest]: Creado base_client (module scope) ID: {id(test_client)}")
        yield test_client
    print(f"DEBUG [conftest]: Finalizado contexto base_client (module scope) ID: {id(test_client)}")

# ... (fixtures seeded_roles, vendedor_role_id, test_user_factory, admin_user, vendedor_user, get_auth_token, admin_token, vendedor_token sin cambios) ...
# --- Asegúrate que estas fixtures usan module_db_session o db_session según corresponda ---

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

@pytest.fixture(scope="module")
def vendedor_role_id(seeded_roles: Dict[str, Rol]) -> int: # Ya no necesita db directa
    role = seeded_roles.get("Vendedor")
    if not role or not role.id: # Verificar ID también
        pytest.fail("Rol 'Vendedor' o su ID no encontrado en roles pre-cargados.")
    return role.id

@pytest.fixture(scope="module")
def test_user_factory(module_db_session: Session, seeded_roles: Dict[str, Rol]):
    # ... (código sin cambios) ...
    print(f"\nDEBUG: Iniciando test_user_factory (scope='module') con session id: {id(module_db_session)}")
    created_users_for_cleanup = []
    def _create_user(username: str, email: str, password: str, roles_names: List[str] = None) -> Usuario:
        # ... (código interno sin cambios) ...
        print(f"DEBUG: _create_user: Intentando crear/obtener usuario '{username}'...")
        session = module_db_session
        try:
            existing = usuario_repository.get_usuario_by_username(db=session, username=username)
            if existing:
                print(f"DEBUG: _create_user: Usuario '{username}' ya existía en sesión de módulo.")
                if existing.id not in [u["id"] for u in created_users_for_cleanup]:
                     created_users_for_cleanup.append({"id": existing.id, "username": username})
                session.refresh(existing, attribute_names=["roles"])
                return existing

            role_ids_to_assign = []
            if roles_names:
                for name in roles_names:
                    role = seeded_roles.get(name)
                    if not role or not role.id: pytest.fail(f"Rol '{name}' no encontrado en roles pre-cargados.")
                    role_ids_to_assign.append(role.id)

            user_in = UsuarioCreate(
                username=username, email=email, password=password,
                nombre_completo=f"Test {username.capitalize()}",
                rol_ids=role_ids_to_assign if role_ids_to_assign else None
            )
            user = usuario_service.create_new_user(db=session, user_in=user_in)
            retrieved_user = session.get(Usuario, user.id)
            if retrieved_user:
                print(f"DEBUG: _create_user: VERIFICADO - Usuario ID={user.id} ('{retrieved_user.username}') creado y encontrado en sesión.")
                if roles_names:
                    session.refresh(retrieved_user, attribute_names=["roles"])
                    print(f"DEBUG: _create_user: Roles asignados (verif.): {[r.nombre for r in retrieved_user.roles]}")
            else:
                print(f"ERROR CRÍTICO: _create_user: Usuario ID={user.id} NO encontrado después de crear!")
                pytest.fail(f"No se pudo verificar creación del usuario '{username}' en la misma sesión.")
            created_users_for_cleanup.append({"id": user.id, "username": username})
            return user
        except Exception as e:
             print(f"ERROR dentro de _create_user para {username}: {e}")
             import traceback
             traceback.print_exc()
             session.rollback()
             raise
    yield _create_user
    print(f"\nDEBUG: test_user_factory (TEARDOWN Módulo): Limpiando {len(created_users_for_cleanup)} usuarios: {[u['username'] for u in created_users_for_cleanup]}")
    if created_users_for_cleanup:
        # ... (lógica de limpieza sin cambios) ...
        user_ids = [u["id"] for u in created_users_for_cleanup]
        cleanup_db = TestingSessionLocal()
        try:
            print(f"DEBUG (Cleanup): Eliminando links usuario_rol para usuarios: {user_ids}")
            stmt_links = sa.delete(UsuarioRol).where(UsuarioRol.usuario_id.in_(user_ids))
            cleanup_db.execute(stmt_links)
            print(f"DEBUG (Cleanup): Eliminando usuarios: {user_ids}")
            stmt_users = sa.delete(Usuario).where(Usuario.id.in_(user_ids))
            result = cleanup_db.execute(stmt_users)
            cleanup_db.commit()
            print(f"DEBUG (Cleanup): Usuarios de prueba y sus links eliminados: {user_ids} (Count: {result.rowcount})")
        except Exception as e:
             print(f"ERROR limpiando usuarios de prueba: {e}")
             cleanup_db.rollback()
        finally:
             cleanup_db.close()

@pytest.fixture(scope="module")
def admin_user(test_user_factory) -> Usuario:
    return test_user_factory(username="testadmin", email="admin@test.com", password="password123", roles_names=["Administrador"])

@pytest.fixture(scope="module")
def vendedor_user(test_user_factory) -> Usuario:
    return test_user_factory(username="testvendedor", email="vendedor@test.com", password="password123", roles_names=["Vendedor"])

@pytest.fixture(scope="module")
def get_auth_token() -> Callable: # Ya no necesita cliente como argumento
    """Fábrica para obtener tokens (crea cliente temporalmente)."""
    def _get_token(username: str, password: str) -> str:
        # Crear cliente temporal SOLO para obtener el token
        # Asegurarse que app tenga los overrides aquí también
        app.dependency_overrides[get_db] = override_get_db
        with TestClient(app) as temp_client:
            print(f"DEBUG [get_auth_token]: Creando temp_client ID={id(temp_client)} para obtener token de {username}")
            response = temp_client.post(
                f"{settings.API_V1_STR}/auth/token",
                data={"username": username, "password": password}
            )
            print(f"DEBUG [get_auth_token]: Respuesta de /auth/token: {response.status_code}")
            if response.status_code != 200:
                pytest.fail(f"No se pudo obtener token para {username}. Status: {response.status_code}, Body: {response.text}")
            token = response.json()["access_token"]
            print(f"DEBUG [get_auth_token]: Token obtenido para {username}: ...{token[-6:]}")
            return token
    return _get_token

@pytest.fixture(scope="module")
def admin_token(get_auth_token, admin_user: Usuario) -> str:
     """Obtiene el token para el usuario admin (module scope)."""
     print("DEBUG [conftest]: Obteniendo admin_token (module scope)...")
     # Asegurarse que el usuario de la factory esté listo
     assert admin_user and admin_user.id, "Fixture admin_user no disponible"
     token = get_auth_token(username=admin_user.username, password="password123")
     print(f"DEBUG [conftest]: admin_token obtenido: ...{token[-6:]}")
     return token


@pytest.fixture(scope="module")
def vendedor_token(get_auth_token, vendedor_user: Usuario) -> str:
     """Obtiene el token para el usuario vendedor (module scope)."""
     print("DEBUG [conftest]: Obteniendo vendedor_token (module scope)...")
     assert vendedor_user and vendedor_user.id, "Fixture vendedor_user no disponible"
     token = get_auth_token(username=vendedor_user.username, password="password123")
     print(f"DEBUG [conftest]: vendedor_token obtenido: ...{token[-6:]}")
     return token


@pytest.fixture(scope="function")
def admin_client(admin_token: str) -> Generator[TestClient, None, None]:
    """Cliente de prueba INDEPENDIENTE autenticado como Admin (function scope)."""
    # --- CAMBIO AQUÍ: Asegurar override ANTES de crear TestClient ---
    app.dependency_overrides[get_db] = override_get_db
    # --- FIN CAMBIO ---
    # Crear instancia independiente para este test
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {admin_token}"
        print(f"DEBUG [conftest - admin_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Admin ...{admin_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - admin_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")
    # Opcional: Limpiar override si afecta otros tests (poco probable con scope function)
    # app.dependency_overrides.pop(get_db, None)



@pytest.fixture(scope="function")
def vendedor_client(vendedor_token: str) -> Generator[TestClient, None, None]:
    """Cliente de prueba INDEPENDIENTE autenticado como Vendedor (function scope)."""
    # --- CAMBIO AQUÍ: Asegurar override ANTES de crear TestClient ---
    app.dependency_overrides[get_db] = override_get_db
    # --- FIN CAMBIO ---
     # Crear instancia independiente para este test
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {vendedor_token}"
        print(f"DEBUG [conftest - vendedor_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Vendedor ...{vendedor_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - vendedor_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")
    # Opcional: Limpiar override si afecta otros tests
    # app.dependency_overrides.pop(get_db, None)

# --- Fixtures de Permisos ---
@pytest.fixture(scope="session")
def seeded_permissions(setup_test_database) -> Dict[str, Permiso]:
    """Obtiene los permisos iniciales de la BD (scope session)."""
    db = TestingSessionLocal()
    try:
        print("DEBUG: Obteniendo permisos iniciales para fixtures (scope='session')...")
        perms_db = db.exec(select(Permiso)).all()
        # Crear llave como "accion:recurso"
        perms_map = {f"{p.nombre_accion}:{p.nombre_recurso}": p for p in perms_db}
        if not perms_map:
             pytest.fail("No se encontraron permisos iniciales suficientes en la BD.")
        # Validar que al menos un permiso conocido existe
        assert "leer:cliente" in perms_map
        assert "gestionar:usuario" in perms_map # Verificar el nuevo también
        return perms_map
    finally:
        db.close()

@pytest.fixture(scope="module")
def permiso_leer_cliente_id(seeded_permissions: Dict[str, Permiso]) -> int:
    """Devuelve el ID del permiso 'leer:cliente'."""
    perm = seeded_permissions.get("leer:cliente")
    if not perm or not perm.id:
        pytest.fail("Permiso 'leer:cliente' o su ID no encontrado en permisos pre-cargados.")
    return perm.id

@pytest.fixture(scope="module")
def permiso_gestionar_usuario_id(seeded_permissions: Dict[str, Permiso]) -> int:
    """Devuelve el ID del permiso 'gestionar:usuario'."""
    perm = seeded_permissions.get("gestionar:usuario")
    if not perm or not perm.id:
        pytest.fail("Permiso 'gestionar:usuario' o su ID no encontrado en permisos pre-cargados.")
    return perm.id


@pytest.fixture(scope="module")
def operario_role_id(seeded_roles: Dict[str, Rol]) -> int:
    """Devuelve el ID del rol 'Operario'."""
    role = seeded_roles.get("Operario")
    if not role or not role.id:
        pytest.fail("Rol 'Operario' o su ID no encontrado en roles pre-cargados.")
    return role.id


@pytest.fixture(scope="module")
def dibujante_role_id(seeded_roles: Dict[str, Rol]) -> int:
    """Devuelve el ID del rol 'Dibujante'."""
    role = seeded_roles.get("Dibujante")
    if not role or not role.id:
        pytest.fail("Rol 'Dibujante' o su ID no encontrado en roles pre-cargados.")
    print(f"DEBUG [conftest]: Obtenido dibujante_role_id: {role.id} (module scope)") # Debug
    return role.id