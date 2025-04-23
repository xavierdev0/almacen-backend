# app/tests/conftest.py
from decimal import Decimal
import os
from typing import Generator, Dict, List, Callable

import pytest
from fastapi import FastAPI # Necesario indirectamente para TestClient(app)
from fastapi.testclient import TestClient
from fastapi import status
from sqlmodel import SQLModel, Session, create_engine, select
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import alembic.config
import alembic.command
import sqlalchemy as sa # Necesario para sa.delete
import uuid
from app.core.config import settings

CLIENTES_ENDPOINT = f"{settings.API_V1_STR}/clientes"
API_V1_STR = settings.API_V1_STR
INVENTARIO_ENDPOINT = f"{API_V1_STR}/inventario"
MAT_DIM_ENDPOINT = f"{INVENTARIO_ENDPOINT}/materiales-dimensionales"
MAT_CONS_ENDPOINT = f"{INVENTARIO_ENDPOINT}/materiales-consumibles"
MAT_SIMP_ENDPOINT = f"{INVENTARIO_ENDPOINT}/materiales-simples"
STOCK_ITEM_DIM_ENDPOINT = f"{INVENTARIO_ENDPOINT}/stock-items-dimensionales"
SERVICIOS_ENDPOINT = f"{API_V1_STR}/servicios" # O donde la tengas definida
DEFINICIONES_ENDPOINT = f"{SERVICIOS_ENDPOINT}/definiciones"

# ==================================
#  1. Carga de Configuración de Prueba
# ==================================
env_path = '.env.test'
if os.path.exists(env_path):
    print(f"\nCargando configuración de prueba desde: {env_path}")
    load_dotenv(dotenv_path=env_path, override=True)
else:
    print(f"\nADVERTENCIA: No se encontró {env_path}.")
    # Salir si no se encuentra el archivo de configuración esencial para pruebas
    pytest.exit(f"Archivo de configuración de prueba '{env_path}' no encontrado.", returncode=1)


# ==================================
#  2. Importar Componentes de la App
# ==================================
from app.core.config import settings
from app.main import app # Importar la instancia de la aplicación FastAPI
from app.core.database import get_db # Importar la dependencia original de DB
# Importar todos los modelos que puedan ser usados en tests o seeding
from app.models import Usuario, Rol, Permiso, UsuarioRol, RolPermiso, Cliente
# Importar servicios/repositorios usados por fixtures o tests
from app.services import usuario_service

from app.schemas.usuario_schema import UsuarioCreate
from app.schemas.client_schema import ClienteCreate
from app.models.inventory_models import MaterialConsumible, MaterialDimensional, MaterialSimple, StockItemDimensional  # Import the missing model
from app.schemas.inventory_schema import MaterialConsumibleCreate, MaterialDimensionalCreate, MaterialSimpleCreate, StockItemDimensionalCreate  # Import the missing schema

# Importar initial_data aunque no se use directamente, las migraciones de Alembic dependen de él.
from app.initial_data import initial_roles, initial_permissions, role_permission_mapping
# Importar repositorios necesarios
from app.repositories import usuario_repository
# 'permiso_repository' no se usaba directamente aquí y fue eliminado.

from app.models import ServicioDefinicion
from app.schemas.service_schema import ServicioDefinicionCreate

# ==========================================
#  3. Configuración de Base de Datos de Prueba
# ==========================================
TEST_DATABASE_URL = settings.DATABASE_URL
# Imprimir URL ofuscada para seguridad
print(f"URL de base de datos para pruebas (desde settings): {TEST_DATABASE_URL[:TEST_DATABASE_URL.find('@') + 1]}***")
# Crear el motor de la base de datos de prueba
engine = create_engine(TEST_DATABASE_URL, echo=False, pool_pre_ping=True)
# Crear una fábrica de sesiones de prueba
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)


# ===========================================
#  4. Fixture Principal de Setup (Session Scope)
# ===========================================
@pytest.fixture(scope="session", autouse=True)
def setup_test_database() -> Generator[None, None, None]:
    """
    Fixture principal (scope='session', autouse=True) para preparar la BD de pruebas.

    Ejecuta las migraciones de Alembic (head) antes de que comience cualquier test
    en la sesión y limpia la base de datos (drop_all) al finalizar todos los tests.
    Falla la sesión de pruebas si las migraciones no se pueden aplicar.

    Yields:
        None: No retorna valor, solo maneja setup y teardown.
    """
    print("\n--- [SETUP SESIÓN] Iniciando preparación de BD de prueba ---")
    alembic_cfg = alembic.config.Config("alembic.ini")
    # Asegurar que Alembic use la URL de la BD de prueba
    alembic_cfg.set_main_option("sqlalchemy.url", TEST_DATABASE_URL)
    try:
        # Aplicar todas las migraciones (schema + datos iniciales)
        alembic.command.upgrade(alembic_cfg, "head")
        print("Migraciones aplicadas exitosamente (schema + seeding).")
    except Exception as e:
        print(f"\nERROR aplicando migraciones: {e}")
        import traceback
        traceback.print_exc()
        pytest.fail(f"Fallo crítico al aplicar migraciones Alembic: {e}")
        return # Salir del generador en caso de fallo

    print("--- [SETUP SESIÓN] Base de datos lista para las pruebas (via Alembic). ---")
    yield # Punto donde se ejecutan los tests de la sesión
    print("\n--- [TEARDOWN SESIÓN] Limpiando BD de prueba (drop_all) ---")
    try:
        # Eliminar todas las tablas al final de la sesión
        SQLModel.metadata.drop_all(bind=engine)
        print("--- [TEARDOWN SESIÓN] BD limpiada exitosamente. ---")
    except Exception as drop_exc:
        print(f"ERROR durante drop_all al final de la sesión: {drop_exc}")

# =================================================
#  5. Fixture para Sobrescribir Dependencia get_db
# =================================================
def override_get_db() -> Generator[Session, None, None]:
    """
    Generador de dependencia para sobrescribir `get_db` en la app FastAPI.

    Proporciona una sesión de base de datos de prueba (`TestingSessionLocal`)
    y asegura que se cierre correctamente después de su uso.

    Yields:
        Session: Una instancia de sesión de base de datos de prueba.
    """
    db = None
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        if db is not None:
            db.close()

# Aplicar el override a la instancia de la app globalmente para todos los tests
app.dependency_overrides[get_db] = override_get_db


# =================================
#  6. Fixtures de Sesión de BD para Tests
# =================================

@pytest.fixture(scope="function")
def db_session(setup_test_database: None) -> Generator[Session, None, None]:
    """
    Fixture (scope='function') que proporciona una sesión de BD de prueba limpia.

    Depende de `setup_test_database` para asegurar que la BD esté lista.
    Realiza rollback al final de cada test para aislar los tests.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD (inyectado por pytest).

    Yields:
        Session: Una sesión de BD de prueba limpia para un test individual.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        # Rollback para deshacer cambios no confirmados del test
        db.rollback()
        db.close()

@pytest.fixture(scope="module")
def module_db_session(setup_test_database: None) -> Generator[Session, None, None]:
    """
    Fixture (scope='module') que proporciona una sesión de BD de prueba compartida por un módulo.

    Depende de `setup_test_database`. Realiza rollback al final del módulo.
    Útil para fixtures de módulo que necesitan interactuar con la BD una vez.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD.

    Yields:
        Session: Una sesión de BD de prueba compartida para un módulo de tests.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        # Rollback al final del módulo
        db.rollback()
        db.close()


# ============================
#  7. Fixtures de TestClient
# ============================

@pytest.fixture(scope="module")
def base_client(setup_test_database: None) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='module') que proporciona un cliente de prueba base (`TestClient`).

    Este cliente no está autenticado y comparte el mismo scope que las fixtures
    de creación de usuarios y tokens (módulo), asegurando que la app tenga
    la dependencia de BD sobreescrita.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD.

    Yields:
        TestClient: Una instancia de TestClient no autenticada.
    """
    # Asegurar que el override esté aplicado antes de instanciar TestClient
    # Aunque ya se hizo globalmente, es una doble verificación/clarificación.
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        print(f"DEBUG [conftest]: Creado base_client (module scope) ID: {id(test_client)}")
        yield test_client
    print(f"DEBUG [conftest]: Finalizado contexto base_client (module scope) ID: {id(test_client)}")


@pytest.fixture(scope="function")
def admin_client(admin_token: str) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='function') que proporciona un cliente de prueba INDEPENDIENTE
    autenticado como Administrador.

    Crea una nueva instancia de TestClient para cada test, asegurando aislamiento.
    Utiliza el token de administrador obtenido de la fixture `admin_token`.

    Args:
        admin_token: Token JWT del usuario administrador (inyectado por pytest).

    Yields:
        TestClient: Instancia de TestClient autenticada como admin.
    """
    # Asegurar override ANTES de crear TestClient para este scope también
    app.dependency_overrides[get_db] = override_get_db
    # Crear instancia independiente para cada test
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {admin_token}"
        print(f"DEBUG [conftest - admin_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Admin ...{admin_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - admin_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")


@pytest.fixture(scope="function")
def vendedor_client(vendedor_token: str) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='function') que proporciona un cliente de prueba INDEPENDIENTE
    autenticado como Vendedor.

    Crea una nueva instancia de TestClient para cada test.
    Utiliza el token de vendedor obtenido de la fixture `vendedor_token`.

    Args:
        vendedor_token: Token JWT del usuario vendedor (inyectado por pytest).

    Yields:
        TestClient: Instancia de TestClient autenticada como vendedor.
    """
    # Asegurar override ANTES de crear TestClient
    app.dependency_overrides[get_db] = override_get_db
     # Crear instancia independiente para cada test
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {vendedor_token}"
        print(f"DEBUG [conftest - vendedor_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Vendedor ...{vendedor_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - vendedor_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")

          
@pytest.fixture(scope="function")
def cliente_de_prueba(vendedor_client: TestClient, db_session: Session) -> Cliente:
    """Fixture para crear un cliente de prueba antes de un test."""
    unique_suffix = uuid.uuid4().hex[:6]
    cliente_data = ClienteCreate(
        nombre=f"Cliente Prueba {unique_suffix}",
        email=f"cliente_{unique_suffix}@pruebas.com",
        identificacion_fiscal=f"999{unique_suffix}",
        tipo_identificacion="RUC",
        telefono="0987654321"
    )
    response = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    cliente_id = response.json()["id"]
    # Obtener el objeto completo desde la BD para devolverlo
    # Usamos una consulta directa para asegurar que leemos lo que se acaba de escribir
    cliente_db = db_session.get(Cliente, cliente_id)
    #cliente_db = cliente_repository.get_cliente_by_id(db=db_session, cliente_id=cliente_id)
    assert cliente_db is not None
    print(f"Cliente de prueba creado por fixture: ID={cliente_db.id}")
    return cliente_db

# ============================
#  8. Fixtures de Datos (Roles y Permisos)
# ============================

@pytest.fixture(scope="session")
def seeded_roles(setup_test_database: None) -> Dict[str, Rol]:
    """
    Fixture (scope='session') que obtiene los roles iniciales de la BD una vez por sesión.

    Consulta la base de datos (después de que `setup_test_database` aplicó las migraciones)
    y devuelve un diccionario mapeando nombres de rol a objetos Rol.
    Falla si no encuentra suficientes roles iniciales.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD.

    Returns:
        Dict[str, Rol]: Diccionario con los roles iniciales {nombre_rol: Rol}.
    """
    db = TestingSessionLocal()
    try:
        print("DEBUG: Obteniendo roles iniciales para fixtures (scope='session')...")
        roles_db = db.exec(select(Rol)).all()
        roles_map = {rol.nombre: rol for rol in roles_db}
        # Validación básica de que el seeding funcionó
        if not roles_map or len(roles_map) < 5: # Ajustar número según roles esperados
             pytest.fail(f"No se encontraron roles iniciales suficientes en la BD (Esperados: >=5, Encontrados: {len(roles_map)}).")
        print(f"DEBUG: Roles iniciales obtenidos: {list(roles_map.keys())}")
        return roles_map
    finally:
        db.close()

@pytest.fixture(scope="session")
def seeded_permissions(setup_test_database: None) -> Dict[str, Permiso]:
    """
    Fixture (scope='session') que obtiene los permisos iniciales de la BD una vez por sesión.

    Consulta la base de datos (después de `setup_test_database`) y devuelve un
    diccionario mapeando 'accion:recurso' a objetos Permiso.
    Falla si no encuentra permisos clave.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD.

    Returns:
        Dict[str, Permiso]: Diccionario con permisos iniciales {'accion:recurso': Permiso}.
    """
    db = TestingSessionLocal()
    try:
        print("DEBUG: Obteniendo permisos iniciales para fixtures (scope='session')...")
        perms_db = db.exec(select(Permiso)).all()
        # Crear llave como "accion:recurso" para fácil acceso
        perms_map = {f"{p.nombre_accion}:{p.nombre_recurso}": p for p in perms_db}
        if not perms_map:
             pytest.fail("No se encontraron permisos iniciales en la BD.")
        # Validar que algunos permisos esperados del seeding existen
        assert "leer:cliente" in perms_map, "Permiso 'leer:cliente' no encontrado en seeding."
        assert "gestionar:usuario" in perms_map, "Permiso 'gestionar:usuario' no encontrado en seeding."
        print(f"DEBUG: Permisos iniciales obtenidos: {list(perms_map.keys())[:5]}...") # Mostrar algunos
        return perms_map
    finally:
        db.close()


# ===================================
#  9. Fixtures de IDs Específicos (Roles/Permisos)
# ===================================
# Estas fixtures dependen de las fixtures de datos (seeded_roles, seeded_permissions)
# y proporcionan IDs específicos para usar en tests, evitando hardcodear IDs.

@pytest.fixture(scope="module") # Podría ser 'session' si no cambian
def vendedor_role_id(seeded_roles: Dict[str, Rol]) -> int:
    """Devuelve el ID del rol 'Vendedor' obtenido de los roles iniciales."""
    role = seeded_roles.get("Vendedor")
    if not role or not role.id:
        pytest.fail("Rol 'Vendedor' o su ID no encontrado en roles pre-cargados.")
    return role.id

@pytest.fixture(scope="module")
def operario_role_id(seeded_roles: Dict[str, Rol]) -> int:
    """Devuelve el ID del rol 'Operario' obtenido de los roles iniciales."""
    role = seeded_roles.get("Operario")
    if not role or not role.id:
        pytest.fail("Rol 'Operario' o su ID no encontrado en roles pre-cargados.")
    return role.id

@pytest.fixture(scope="module")
def dibujante_role_id(seeded_roles: Dict[str, Rol]) -> int:
    """Devuelve el ID del rol 'Dibujante' obtenido de los roles iniciales."""
    role = seeded_roles.get("Dibujante")
    if not role or not role.id:
        pytest.fail("Rol 'Dibujante' o su ID no encontrado en roles pre-cargados.")
    print(f"DEBUG [conftest]: Obtenido dibujante_role_id: {role.id} (module scope)")
    return role.id

@pytest.fixture(scope="module")
def permiso_leer_cliente_id(seeded_permissions: Dict[str, Permiso]) -> int:
    """Devuelve el ID del permiso 'leer:cliente' obtenido de los permisos iniciales."""
    perm = seeded_permissions.get("leer:cliente")
    if not perm or not perm.id:
        pytest.fail("Permiso 'leer:cliente' o su ID no encontrado en permisos pre-cargados.")
    return perm.id

@pytest.fixture(scope="module")
def permiso_gestionar_usuario_id(seeded_permissions: Dict[str, Permiso]) -> int:
    """Devuelve el ID del permiso 'gestionar:usuario' obtenido de los permisos iniciales."""
    perm = seeded_permissions.get("gestionar:usuario")
    if not perm or not perm.id:
        pytest.fail("Permiso 'gestionar:usuario' o su ID no encontrado en permisos pre-cargados.")
    return perm.id

# ============================
#  10. Fixtures de Usuarios de Prueba
# ============================

@pytest.fixture(scope="module")
def test_user_factory(module_db_session: Session, seeded_roles: Dict[str, Rol]) -> Generator[Callable[[str, str, str, List[str]], Usuario], None, None]: # Si da problemas cambiar a Callable:
    """
    Fixture tipo 'factory' (scope='module') para crear usuarios de prueba.

    Proporciona una función interna `_create_user` que puede ser llamada múltiples
    veces dentro del mismo módulo para crear usuarios. Maneja la limpieza
    (eliminación) de los usuarios creados al final del módulo.
    Utiliza la sesión de módulo para persistir usuarios entre tests del módulo.

    Args:
        module_db_session: Sesión de BD compartida por el módulo.
        seeded_roles: Diccionario de roles iniciales para asignar por nombre.

    Yields:
        Callable: La función `_create_user(username, email, password, roles_names)`.
    """
    #print(f"\nDEBUG: Iniciando test_user_factory (scope='module') con session id: {id(module_db_session)}")
    created_users_for_cleanup = [] # Lista para rastrear usuarios creados por esta factory

    def _create_user(username: str, email: str, password: str, roles_names: List[str] = None) -> Usuario:
        """Función interna para crear o retornar un usuario de prueba."""
        #print(f"DEBUG: _create_user: Intentando crear/obtener usuario '{username}'...")
        session = module_db_session # Usar la sesión del módulo
        try:
            # Intentar obtener usuario existente en caso de re-llamada en el mismo módulo
            existing = usuario_repository.get_usuario_by_username(db=session, username=username)
            if existing:
                #print(f"DEBUG: _create_user: Usuario '{username}' ya existía en sesión de módulo.")
                # Asegurar que esté en la lista de limpieza si no lo estaba
                if not any(u["id"] == existing.id for u in created_users_for_cleanup):
                    created_users_for_cleanup.append({"id": existing.id, "username": username})
                # Refrescar roles por si acaso
                session.refresh(existing, attribute_names=["roles"])
                return existing

            # Mapear nombres de roles a IDs usando los roles ya cargados
            role_ids_to_assign = []
            if roles_names:
                for name in roles_names:
                    role = seeded_roles.get(name)
                    if not role or not role.id: pytest.fail(f"Rol '{name}' no encontrado en roles pre-cargados para usuario '{username}'.")
                    role_ids_to_assign.append(role.id)

            # Crear el usuario usando el servicio (que maneja hashing y roles)
            user_in = UsuarioCreate(
                username=username, email=email, password=password,
                nombre_completo=f"Test {username.capitalize()}",
                # Pasar lista de IDs o None si no hay roles
                rol_ids=role_ids_to_assign if role_ids_to_assign else None
            )
            # Usar el servicio para encapsular lógica de creación
            user = usuario_service.create_new_user(db=session, user_in=user_in)

            # Verificar inmediatamente si el usuario se puede recuperar en la misma sesión
            retrieved_user = session.get(Usuario, user.id)
            if retrieved_user:
                #print(f"DEBUG: _create_user: VERIFICADO - Usuario ID={user.id} ('{retrieved_user.username}') creado y encontrado en sesión.")
                if roles_names:
                    session.refresh(retrieved_user, attribute_names=["roles"])
                    #print(f"DEBUG: _create_user: Roles asignados (verif.): {[r.nombre for r in retrieved_user.roles]}")
            else:
                # Esto no debería ocurrir si create_new_user funciona correctamente
                print(f"ERROR CRÍTICO: _create_user: Usuario ID={user.id} NO encontrado después de crear!")
                pytest.fail(f"No se pudo verificar creación del usuario '{username}' en la misma sesión.")

            # Añadir a la lista de limpieza
            created_users_for_cleanup.append({"id": user.id, "username": username})
            return retrieved_user # Devolver el usuario recuperado y refrescado

        except Exception as e:
            print(f"ERROR dentro de _create_user para {username}: {e}")
            import traceback
            traceback.print_exc()
            session.rollback() # Revertir cambios en caso de error
            raise

    yield _create_user # La factory devuelve la función interna

    # --- Código de limpieza (Teardown del módulo) ---
    #print(f"\nDEBUG: test_user_factory (TEARDOWN Módulo): Limpiando {len(created_users_for_cleanup)} usuarios: {[u['username'] for u in created_users_for_cleanup]}")
    if created_users_for_cleanup:
        user_ids = [u["id"] for u in created_users_for_cleanup]
        # Usar una nueva sesión efímera para la limpieza
        cleanup_db = TestingSessionLocal()
        try:
            # Eliminar primero las dependencias en UsuarioRol
            #print(f"DEBUG (Cleanup): Eliminando links usuario_rol para usuarios: {user_ids}")
            stmt_links = sa.delete(UsuarioRol).where(UsuarioRol.usuario_id.in_(user_ids))
            cleanup_db.execute(stmt_links)

            # Luego eliminar los usuarios
            #print(f"DEBUG (Cleanup): Eliminando usuarios: {user_ids}")
            stmt_users = sa.delete(Usuario).where(Usuario.id.in_(user_ids))
            result = cleanup_db.execute(stmt_users)
            cleanup_db.commit()
            #print(f"DEBUG (Cleanup): Usuarios de prueba y sus links eliminados: {user_ids} (Count: {result.rowcount})")
        except Exception as e:
            #print(f"ERROR limpiando usuarios de prueba: {e}")
            cleanup_db.rollback()
        finally:
            cleanup_db.close()

@pytest.fixture(scope="module")
def admin_user(test_user_factory: Callable) -> Usuario:
    """Fixture (scope='module') que crea/obtiene el usuario 'testadmin'."""
    return test_user_factory(username="testadmin", email="admin@test.com", password="password123", roles_names=["Administrador"])

@pytest.fixture(scope="module")
def vendedor_user(test_user_factory: Callable) -> Usuario:
    """Fixture (scope='module') que crea/obtiene el usuario 'testvendedor'."""
    return test_user_factory(username="testvendedor", email="vendedor@test.com", password="password123", roles_names=["Vendedor"])

@pytest.fixture(scope="module")
def dibujante_user(test_user_factory: Callable) -> Usuario:
    """Fixture (scope='module') que crea/obtiene el usuario 'testdibujante'."""
    return test_user_factory(username="testdibujante", email="dibujante@test.com", password="password123", roles_names=["Dibujante"])

@pytest.fixture(scope="module")
def operario_user(test_user_factory: Callable) -> Usuario:
    """Fixture (scope='module') que crea/obtiene el usuario 'testoperario'."""
    return test_user_factory(username="testoperario", email="operario@test.com", password="password123", roles_names=["Operario"])



# --- Fixtures para Tipos de Material ---
@pytest.fixture(scope="function")
def material_dimensional_de_prueba(admin_client: TestClient, db_session: Session) -> MaterialDimensional:
    """Fixture para crear un tipo de MaterialDimensional vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    payload_schema = MaterialDimensionalCreate(
        sku=f"FIX-DIM-{unique_suffix}",
        nombre=f"Plancha Fixture {unique_suffix}",
        espesor_nominal=Decimal("15.0"),
        unidad_dimension="mm"
    )
    payload_dict = payload_schema.model_dump(mode='json') # Correcto

    response = admin_client.post(MAT_DIM_ENDPOINT, json=payload_dict) # Usa el dict serializado
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear MaterialDimensional en fixture: {response.text}"
    data = response.json()
    mat_id = data["id"]

    # Usar la sesión original para cerrar (como buena práctica) y luego verificar con una nueva
    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(MaterialDimensional, mat_id)

    assert db_obj is not None, "No se pudo recuperar MaterialDimensional de BD en fixture (nueva sesión)"
    print(f"Fixture: MaterialDimensional creado: ID={db_obj.id}, SKU={db_obj.sku}")
    return db_obj # Devolver el objeto recuperado de la nueva sesión


@pytest.fixture(scope="function")
def material_consumible_de_prueba(admin_client: TestClient, db_session: Session) -> MaterialConsumible:
    """Fixture para crear un tipo de MaterialConsumible vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    payload_schema = MaterialConsumibleCreate(
        sku=f"FIX-CONS-{unique_suffix}",
        nombre=f"Lija Fixture {unique_suffix}",
        unidad_medida="pliego",
        stock_minimo=Decimal("10.0")
    )
    payload_dict = payload_schema.model_dump(mode='json') # Correcto

    response = admin_client.post(MAT_CONS_ENDPOINT, json=payload_dict)
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear MaterialConsumible en fixture: {response.text}"
    data = response.json()
    mat_id = data["id"]

    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(MaterialConsumible, mat_id)

    assert db_obj is not None, "No se pudo recuperar MaterialConsumible de BD en fixture (nueva sesión)"
    print(f"Fixture: MaterialConsumible creado: ID={db_obj.id}, SKU={db_obj.sku}")
    return db_obj


@pytest.fixture(scope="function")
def material_simple_de_prueba(admin_client: TestClient, db_session: Session) -> MaterialSimple:
    """Fixture para crear un tipo de MaterialSimple vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    payload_schema = MaterialSimpleCreate(
        sku=f"FIX-SIMP-{unique_suffix}",
        nombre=f"Tornillo Fixture {unique_suffix}",
        unidad_medida="ciento",
        stock_minimo=Decimal("2.0")
    )
    payload_dict = payload_schema.model_dump(mode='json') 

    response = admin_client.post(MAT_SIMP_ENDPOINT, json=payload_dict)
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear MaterialSimple en fixture: {response.text}"
    data = response.json()
    mat_id = data["id"]

    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(MaterialSimple, mat_id)

    assert db_obj is not None, "No se pudo recuperar MaterialSimple de BD en fixture (nueva sesión)"
    print(f"Fixture: MaterialSimple creado: ID={db_obj.id}, SKU={db_obj.sku}")
    return db_obj

@pytest.fixture(scope="function")
def servicio_definicion_de_prueba(admin_client: TestClient, db_session: Session) -> ServicioDefinicion:
    """Fixture para crear una definición de servicio de prueba vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    payload_schema = ServicioDefinicionCreate(
        codigo=f"FIX-SERV-{unique_suffix}",
        nombre=f"Servicio Test {unique_suffix}",
        unidad_cobro="hora",
        descripcion="Descripción Fixture", # Añadir descripción explícita
        costo_por_unidad=Decimal("0.0"), # Valor explícito aunque sea Optional
        costo_por_minuto=Decimal("1.5"), # Ya estaba explícito
        requiere_dibujo_cnc=False,
        tiempo_setup_min=Decimal("5.0"), # Valor explícito (antes usaba default)
        tiempo_preparado_min_por_unidad=Decimal("0.1"), # Valor explícito (antes usaba default)
        factor_ih=Decimal("1.1"), # Valor explícito (antes usaba default)
    )
    payload_dict = payload_schema.model_dump(mode='json')

    response = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_dict)

    assert response.status_code == status.HTTP_201_CREATED, \
        f"Fallo al crear ServicioDefinicion en fixture: {response.text}"
    data = response.json()
    servicio_id = data["id"]

    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(ServicioDefinicion, servicio_id)

    assert db_obj is not None, "No se pudo recuperar ServicioDefinicion de BD en fixture (nueva sesión)"
    print(f"Fixture: ServicioDefinicion creado: ID={db_obj.id}, Nombre={db_obj.nombre}")
    return db_obj

@pytest.fixture(scope="function")
def stock_item_dimensional_de_prueba(
    admin_client: TestClient,
    db_session: Session,
    material_dimensional_de_prueba: MaterialDimensional
) -> StockItemDimensional:
    """Fixture para crear una pieza de StockItemDimensional vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    # Asegurarse que material_dimensional_de_prueba.id es válido
    assert material_dimensional_de_prueba.id is not None, "Fixture material_dimensional_de_prueba no tiene ID"

    payload_schema = StockItemDimensionalCreate(
        material_dimensional_id=material_dimensional_de_prueba.id,
        longitud_actual=Decimal("2440.000"),
        ancho_actual=Decimal("1220.000"),
        ubicacion=f"TEST-{unique_suffix}"
    )
    payload_dict = payload_schema.model_dump(mode='json') # <<< CORRECCIÓN: nombre variable y mode='json'

    response = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=payload_dict)
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear StockItemDimensional en fixture: {response.text}"
    data = response.json()
    item_id = data["id"]

    # Verificar con nueva sesión para asegurar visibilidad
    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(StockItemDimensional, item_id)

    assert db_obj is not None, "No se pudo recuperar StockItemDimensional de BD en fixture (nueva sesión)" # <<< CORRECCIÓN: assert sobre el objeto de la nueva sesión
    print(f"Fixture: StockItemDimensional creado: ID={db_obj.id} para MaterialID={db_obj.material_dimensional_id}")
    return db_obj

# ============================
#  11. Fixtures de Tokens de Autenticación
# ============================

@pytest.fixture(scope="module")
def get_auth_token(admin_user: Usuario, vendedor_user: Usuario) -> Callable:
    """
    Fixture tipo 'factory' (scope='module') para obtener tokens de autenticación.

    Proporciona una función interna `_get_token` que crea un cliente `TestClient`
    temporal solo para llamar al endpoint de login y obtener un token JWT.
    Depende de que los usuarios (admin, vendedor) ya existan por `test_user_factory`.

    Args:
        admin_user: Fixture que asegura la creación del admin user (inyectado por pytest).
        vendedor_user: Fixture que asegura la creación del vendedor user (inyectado por pytest).

    Yields:
        Callable: La función `_get_token(username, password)`.
    """
    # Asegurar que los usuarios base estén creados antes de devolver la factory
    assert admin_user and admin_user.id
    assert vendedor_user and vendedor_user.id

    def _get_token(username: str, password: str) -> str:
        """Función interna para obtener un token JWT para un usuario."""
        # Crear cliente temporal SOLO para obtener el token
        # Asegurarse que app tenga los overrides aquí también, por si acaso
        app.dependency_overrides[get_db] = override_get_db
        with TestClient(app) as temp_client:
            print(f"DEBUG [get_auth_token]: Creando temp_client ID={id(temp_client)} para obtener token de {username}")
            response = temp_client.post(
                f"{settings.API_V1_STR}/auth/token",
                # Usar 'data' para simular form data
                data={"username": username, "password": password}
            )
            print(f"DEBUG [get_auth_token]: Respuesta de /auth/token para {username}: {response.status_code}")
            if response.status_code != 200:
                pytest.fail(f"No se pudo obtener token para {username}. Status: {response.status_code}, Body: {response.text}")
            token_data = response.json()
            token = token_data["access_token"]
            print(f"DEBUG [get_auth_token]: Token obtenido para {username}: ...{token[-6:]}")
            return token
    return _get_token

@pytest.fixture(scope="module")
def admin_token(get_auth_token: Callable, admin_user: Usuario) -> str:
    """Fixture (scope='module') que obtiene y devuelve el token para 'testadmin'."""
    print("DEBUG [conftest]: Obteniendo admin_token (module scope)...")
    # Asegurarse que el usuario de la factory esté listo antes de pedir token
    assert admin_user and admin_user.username, "Fixture admin_user no disponible o sin username"
    token = get_auth_token(username=admin_user.username, password="password123")
    print(f"DEBUG [conftest]: admin_token obtenido: ...{token[-6:]}")
    return token

@pytest.fixture(scope="module")
def vendedor_token(get_auth_token: Callable, vendedor_user: Usuario) -> str:
    """Fixture (scope='module') que obtiene y devuelve el token para 'testvendedor'."""
    print("DEBUG [conftest]: Obteniendo vendedor_token (module scope)...")
    assert vendedor_user and vendedor_user.username, "Fixture vendedor_user no disponible o sin username"
    token = get_auth_token(username=vendedor_user.username, password="password123")
    print(f"DEBUG [conftest]: vendedor_token obtenido: ...{token[-6:]}")
    return token


@pytest.fixture(scope="module")
def dibujante_token(get_auth_token: Callable, dibujante_user: Usuario) -> str:
    """Fixture (scope='module') que obtiene y devuelve el token para 'testdibujante'."""
    print("DEBUG [conftest]: Obteniendo dibujante_token (module scope)...")
    assert dibujante_user and dibujante_user.username, "Fixture dibujante_user no disponible o sin username"
    token = get_auth_token(username=dibujante_user.username, password="password123")
    print(f"DEBUG [conftest]: dibujante_token obtenido: ...{token[-6:]}")
    return token

@pytest.fixture(scope="module")
def operario_token(get_auth_token: Callable, operario_user: Usuario) -> str:
    """Fixture (scope='module') que obtiene y devuelve el token para 'testoperario'."""
    print("DEBUG [conftest]: Obteniendo operario_token (module scope)...")
    assert operario_user and operario_user.username, "Fixture operario_user no disponible o sin username"
    token = get_auth_token(username=operario_user.username, password="password123")
    print(f"DEBUG [conftest]: operario_token obtenido: ...{token[-6:]}")
    return token

@pytest.fixture(scope="function")
def dibujante_client(dibujante_token: str) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='function') que proporciona un cliente de prueba INDEPENDIENTE
    autenticado como Dibujante.
    """
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {dibujante_token}"
        print(f"DEBUG [conftest - dibujante_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Dibujante ...{dibujante_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - dibujante_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")

@pytest.fixture(scope="function")
def operario_client(operario_token: str) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='function') que proporciona un cliente de prueba INDEPENDIENTE
    autenticado como Operario.
    """
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {operario_token}"
        print(f"DEBUG [conftest - operario_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Operario ...{operario_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - operario_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")
