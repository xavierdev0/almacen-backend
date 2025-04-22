# app/tests/api/v1/test_clientes_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
import logging # Añadir import logging

# Importar settings para prefijo API
from app.core.config import settings
# Importar schemas para crear payloads y validar respuestas
from app.schemas.client_schema import ClienteCreate, ClienteRead, ClienteUpdate
# Importar modelo y repositorio para verificaciones en BD
from app.models import Cliente
from app.repositories import cliente_repository
from tests.conftest import TestingSessionLocal


# --- Constantes ---
API_V1_STR = settings.API_V1_STR
CLIENTES_ENDPOINT = f"{API_V1_STR}/clientes"
logger = logging.getLogger(__name__) # Crear logger


# ==================================
# --- Tests para Crear Clientes ---
# ==================================
# (Sin cambios aquí, ya pasaban)
def test_create_cliente_success_vendedor(vendedor_client: TestClient, db_session: Session):
    """Prueba la creación exitosa de un cliente por un Vendedor."""
    unique_suffix = uuid.uuid4().hex[:6]
    nombre_cliente = f"Nuevo Cliente Vendedor {unique_suffix}"
    email_cliente = f"vendedor_crea_{unique_suffix}@test.com"
    id_fiscal = f"111{unique_suffix}"

    cliente_data = ClienteCreate(
        nombre=nombre_cliente,
        email=email_cliente,
        identificacion_fiscal=id_fiscal,
        tipo_identificacion="CEDULA", # Asegurarse que sea válido
        telefono="1234567890",
        direccion="Calle Falsa 123"
    )

    response = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())

    # Verificar respuesta HTTP 201
    assert response.status_code == status.HTTP_201_CREATED

    # Verificar contenido de la respuesta (ClienteRead)
    data = response.json()
    assert data["nombre"] == nombre_cliente
    assert data["email"] == email_cliente
    assert data["identificacion_fiscal"] == id_fiscal
    assert data["tipo_identificacion"] == "CEDULA" # Verifica normalización/valor guardado
    assert data["telefono"] == "1234567890"
    assert data["direccion"] == "Calle Falsa 123"
    assert "id" in data
    new_cliente_id = data["id"]

    # Verificar en la BD
    db_cliente = cliente_repository.get_cliente_by_id(db=db_session, cliente_id=new_cliente_id)
    assert db_cliente is not None
    assert db_cliente.nombre == nombre_cliente
    assert db_cliente.email == email_cliente
    assert db_cliente.identificacion_fiscal == id_fiscal

def test_create_cliente_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la creación exitosa de un cliente por un Admin."""
    unique_suffix = uuid.uuid4().hex[:6]
    nombre_cliente = f"Nuevo Cliente Admin {unique_suffix}"
    email_cliente = f"admin_crea_{unique_suffix}@test.com"
    id_fiscal = f"222{unique_suffix}"

    cliente_data = ClienteCreate(
        nombre=nombre_cliente,
        email=email_cliente,
        identificacion_fiscal=id_fiscal,
        tipo_identificacion="RUC"
    )
    response = admin_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["nombre"] == nombre_cliente
    assert data["email"] == email_cliente
    # Verificar en BD (simplificado)
    assert cliente_repository.get_cliente_by_id(db=db_session, cliente_id=data["id"]) is not None

def test_create_cliente_duplicate_email(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba que crear cliente con email duplicado falle (409)."""
    unique_suffix = uuid.uuid4().hex[:6]
    cliente_data = ClienteCreate(
        nombre=f"Duplicado Email {unique_suffix}",
        email=cliente_de_prueba.email, # Email existente
        identificacion_fiscal=f"333{unique_suffix}" # ID Fiscal diferente
    )
    response = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "correo electrónico" in response.json()["detail"].lower()
    assert cliente_de_prueba.email in response.json()["detail"]

def test_create_cliente_duplicate_identificacion(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba que crear cliente con identificación fiscal duplicada falle (409)."""
    unique_suffix = uuid.uuid4().hex[:6]
    cliente_data = ClienteCreate(
        nombre=f"Duplicado ID Fiscal {unique_suffix}",
        email=f"otroemail_{unique_suffix}@test.com", # Email diferente
        identificacion_fiscal=cliente_de_prueba.identificacion_fiscal # ID Fiscal existente
    )
    response = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "identificación fiscal" in response.json()["detail"].lower()
    assert cliente_de_prueba.identificacion_fiscal in response.json()["detail"]

def test_create_cliente_invalid_data(vendedor_client: TestClient):
    """Prueba crear cliente con datos inválidos (422)."""
    # Caso 1: Email inválido
    invalid_email_payload = {"nombre": "Test Email Malo", "email": "esto-no-es-email"}
    response_email = vendedor_client.post(CLIENTES_ENDPOINT, json=invalid_email_payload)
    assert response_email.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("email" in e.get("loc", []) for e in response_email.json().get("detail", []))

    # Caso 2: Tipo identificación inválido
    invalid_tipo_payload = {"nombre": "Test Tipo Malo", "tipo_identificacion": "INVENTADO"}
    response_tipo = vendedor_client.post(CLIENTES_ENDPOINT, json=invalid_tipo_payload)
    assert response_tipo.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("tipo_identificacion" in e.get("loc", []) for e in response_tipo.json().get("detail", []))

    # Caso 3: Nombre requerido ausente
    missing_name_payload = {"email": "sin_nombre@test.com"}
    response_name = vendedor_client.post(CLIENTES_ENDPOINT, json=missing_name_payload)
    assert response_name.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("nombre" in e.get("loc", []) for e in response_name.json().get("detail", []))

def test_create_cliente_unauthenticated(base_client: TestClient):
    """Prueba que crear cliente sin autenticación falle (401)."""
    cliente_data = ClienteCreate(nombre="No Auth Test")
    response = base_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- Tests para Listar Clientes (GET /) ---

def test_list_clientes_success_vendedor(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba listar clientes como Vendedor."""
    response = vendedor_client.get(CLIENTES_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    # Verificar que el cliente de prueba está en la lista
    assert any(c["id"] == cliente_de_prueba.id for c in data)
    # Verificar estructura básica de un elemento
    if data:
        assert "id" in data[0]
        assert "nombre" in data[0]
        assert "email" in data[0]

def test_list_clientes_success_admin(admin_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba listar clientes como Admin."""
    response = admin_client.get(CLIENTES_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert any(c["id"] == cliente_de_prueba.id for c in data)

def test_list_clientes_pagination(vendedor_client: TestClient, db_session: Session):
    """Prueba la paginación al listar clientes de forma más robusta."""
    # Crear suficientes clientes para asegurar que la paginación tenga efecto
    # y podamos comparar resultados con y sin skip.
    ids_creados_en_test = []
    num_to_create = 3 # Crear 3 es suficiente para probar skip=1 y limit=1, 2
    for i in range(num_to_create):
        unique_suffix = uuid.uuid4().hex[:4]
        nombre = f"Pag Cliente {i} {unique_suffix}"
        c_data = ClienteCreate(nombre=nombre, email=f"pag_{i}_{unique_suffix}@test.com")
        resp = vendedor_client.post(CLIENTES_ENDPOINT, json=c_data.model_dump())
        assert resp.status_code == status.HTTP_201_CREATED
        ids_creados_en_test.append(resp.json()["id"])

    # 1. Probar limit
    limit_val = 1
    response_limit = vendedor_client.get(f"{CLIENTES_ENDPOINT}?limit={limit_val}")
    assert response_limit.status_code == status.HTTP_200_OK
    data_limit = response_limit.json()
    assert isinstance(data_limit, list)
    # Asegurarse que devuelve como máximo el límite solicitado
    assert len(data_limit) <= limit_val
    if data_limit: # Si devuelve algo, verificar estructura
         assert "id" in data_limit[0]

    limit_val = 2
    response_limit_2 = vendedor_client.get(f"{CLIENTES_ENDPOINT}?limit={limit_val}")
    assert response_limit_2.status_code == status.HTTP_200_OK
    data_limit_2 = response_limit_2.json()
    assert isinstance(data_limit_2, list)
    assert len(data_limit_2) <= limit_val
    if len(data_limit_2) > 1: # Si devuelve al menos 2, verificar IDs diferentes
        assert data_limit_2[0]["id"] != data_limit_2[1]["id"]

    # 2. Probar skip
    skip_val = 1
    # Obtener resultados sin skip (primeros 2 elementos)
    response_no_skip = vendedor_client.get(f"{CLIENTES_ENDPOINT}?limit=2")
    assert response_no_skip.status_code == status.HTTP_200_OK
    data_no_skip = response_no_skip.json()

    # Obtener resultados con skip (saltando el primero, obtener hasta 5)
    response_skip = vendedor_client.get(f"{CLIENTES_ENDPOINT}?skip={skip_val}&limit=5")
    assert response_skip.status_code == status.HTTP_200_OK
    data_skip = response_skip.json()

    # Verificar que los resultados son diferentes si hay suficientes datos
    if len(data_no_skip) > skip_val:
        # El primer elemento de la lista sin skip NO debe estar en la lista con skip
        first_element_id = data_no_skip[0]["id"]
        ids_in_skipped_list = {c["id"] for c in data_skip}
        assert first_element_id not in ids_in_skipped_list, \
            f"El elemento saltado (ID: {first_element_id}) fue encontrado en la lista con skip."
    elif len(data_no_skip) <= skip_val and data_skip:
        # Si se saltaron todos los elementos iniciales, la lista con skip debe ser diferente (o vacía)
         assert data_skip != data_no_skip

def test_list_clientes_unauthenticated(base_client: TestClient):
    """Prueba que listar clientes sin autenticación falle (401)."""
    response = base_client.get(CLIENTES_ENDPOINT)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- Tests para Obtener Cliente por ID (GET /{id}) ---
# (Sin cambios aquí, ya pasaban)
def test_get_cliente_success_vendedor(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba obtener un cliente existente por ID como Vendedor."""
    cliente_id = cliente_de_prueba.id
    response = vendedor_client.get(f"{CLIENTES_ENDPOINT}/{cliente_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == cliente_id
    assert data["nombre"] == cliente_de_prueba.nombre
    assert data["email"] == cliente_de_prueba.email

def test_get_cliente_not_found(vendedor_client: TestClient):
    """Prueba obtener un cliente inexistente por ID (404)."""
    response = vendedor_client.get(f"{CLIENTES_ENDPOINT}/999999")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_get_cliente_unauthenticated(base_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba obtener cliente por ID sin autenticación (401)."""
    response = base_client.get(f"{CLIENTES_ENDPOINT}/{cliente_de_prueba.id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- Tests para Actualizar Clientes (PUT /{id}) ---

def test_update_cliente_success_vendedor(vendedor_client: TestClient, db_session: Session, cliente_de_prueba: Cliente):
    """Prueba actualizar un cliente existente como Vendedor."""
    cliente_id = cliente_de_prueba.id
    unique_suffix = uuid.uuid4().hex[:6]
    new_nombre = f"Cliente Actualizado {unique_suffix}"
    new_email = f"actualizado_{unique_suffix}@test.com"
    new_telefono = "111222333"

    update_payload = ClienteUpdate(
        nombre=new_nombre,
        email=new_email,
        telefono=new_telefono
    ).model_dump(exclude_unset=True)

    # --- Ejecutar la API ---
    response = vendedor_client.put(f"{CLIENTES_ENDPOINT}/{cliente_id}", json=update_payload)

    # 1. Verificar respuesta de la API (como antes)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == cliente_id
    assert data["nombre"] == new_nombre
    assert data["email"] == new_email
    assert data["telefono"] == new_telefono
    assert data["identificacion_fiscal"] == cliente_de_prueba.identificacion_fiscal

    # --- Verificación en BD (con nueva sesión dedicada) ---
    # Cerrar la sesión de prueba original para eliminar cualquier estado en caché.
    # La fixture 'db_session' se encargará de su propio cierre/rollback final de todos modos.
    # Es importante cerrar *antes* de abrir la nueva para asegurar limpieza.
    logger.debug(f"Cerrando sesión de test original (ID: {id(db_session)}) para verificación BD.")
    db_session.close()

    # Abrir una nueva sesión SOLO para verificar el estado post-API en la BD
    logger.debug("Abriendo nueva sesión de verificación BD...")
    try:
        # Usar 'with' asegura que la sesión de verificación se cierre
        with TestingSessionLocal() as verification_db:
            logger.info(f"Verificando BD con nueva sesión (ID: {id(verification_db)}) para cliente ID: {cliente_id}")
            # Usar la nueva sesión para obtener el cliente
            db_cliente_updated = cliente_repository.get_cliente_by_id(db=verification_db, cliente_id=cliente_id)

            assert db_cliente_updated is not None, "El cliente no se encontró en la BD con la nueva sesión"
            assert db_cliente_updated.nombre == new_nombre, "El nombre en la BD no coincide con el actualizado"
            assert db_cliente_updated.email == new_email, "El email en la BD no coincide con el actualizado"
            assert db_cliente_updated.telefono == new_telefono, "El teléfono en la BD no coincide con el actualizado"
            logger.info(f"Verificación en BD exitosa para cliente ID: {cliente_id}")
    except Exception as e:
        logger.error(f"Error durante la verificación en BD con nueva sesión: {e}", exc_info=True)
        pytest.fail(f"La verificación en BD falló después de cerrar y reabrir sesión: {e}")
    finally:
        logger.debug("Sesión de verificación BD cerrada (implícitamente por 'with' o explícitamente si no se usa 'with').")





def test_update_cliente_conflict_email(vendedor_client: TestClient, db_session: Session):
    """Prueba que actualizar a un email duplicado falle (409)."""
    # Crear dos clientes
    suffix1 = uuid.uuid4().hex[:6]
    cliente1_data = ClienteCreate(nombre=f"C1 {suffix1}", email=f"c1_{suffix1}@test.com", identificacion_fiscal=f"id1{suffix1}")
    resp1 = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente1_data.model_dump())
    assert resp1.status_code == status.HTTP_201_CREATED
    cliente1_id = resp1.json()["id"]
    cliente1_email = resp1.json()["email"]

    suffix2 = uuid.uuid4().hex[:6]
    cliente2_data = ClienteCreate(nombre=f"C2 {suffix2}", email=f"c2_{suffix2}@test.com", identificacion_fiscal=f"id2{suffix2}")
    resp2 = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente2_data.model_dump())
    assert resp2.status_code == status.HTTP_201_CREATED
    cliente2_id = resp2.json()["id"]

    # Intentar actualizar cliente 2 con el email del cliente 1
    update_payload = ClienteUpdate(email=cliente1_email).model_dump(exclude_unset=True)
    response_update = vendedor_client.put(f"{CLIENTES_ENDPOINT}/{cliente2_id}", json=update_payload)

    assert response_update.status_code == status.HTTP_409_CONFLICT
    assert "correo electrónico" in response_update.json()["detail"].lower()

def test_update_cliente_not_found(vendedor_client: TestClient):
    """Prueba actualizar un cliente inexistente (404)."""
    update_payload = ClienteUpdate(nombre="No Importa").model_dump(exclude_unset=True)
    response = vendedor_client.put(f"{CLIENTES_ENDPOINT}/999999", json=update_payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_cliente_invalid_data(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba actualizar cliente con datos inválidos (422)."""
    cliente_id = cliente_de_prueba.id
    invalid_payload = {"email": "email-invalido"} # No cumple EmailStr
    response = vendedor_client.put(f"{CLIENTES_ENDPOINT}/{cliente_id}", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_cliente_unauthenticated(base_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba actualizar cliente sin autenticación (401)."""
    update_payload = ClienteUpdate(nombre="No Auth").model_dump(exclude_unset=True)
    response = base_client.put(f"{CLIENTES_ENDPOINT}/{cliente_de_prueba.id}", json=update_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- Tests para Eliminar Clientes (DELETE /{id}) ---

def test_delete_cliente_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba eliminar un cliente existente como Admin."""
    # Crear un cliente específicamente para este test (para asegurar que no tenga dependencias)
    unique_suffix = uuid.uuid4().hex[:6]
    cliente_data = ClienteCreate(nombre=f"Cliente a Borrar {unique_suffix}", email=f"borrar_{unique_suffix}@test.com")
    resp_create = admin_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert resp_create.status_code == status.HTTP_201_CREATED
    cliente_id_to_delete = resp_create.json()["id"]

    # Eliminarlo
    response_delete = admin_client.delete(f"{CLIENTES_ENDPOINT}/{cliente_id_to_delete}")
    assert response_delete.status_code == status.HTTP_204_NO_CONTENT

    # Verificar en BD que ya no existe
    db_session.expire_all() # Invalida la caché de la sesión del test
    assert cliente_repository.get_cliente_by_id(db=db_session, cliente_id=cliente_id_to_delete) is None

def test_delete_cliente_not_found_admin(admin_client: TestClient):
    """Prueba eliminar un cliente inexistente (404)."""
    response = admin_client.delete(f"{CLIENTES_ENDPOINT}/999998")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_cliente_forbidden_vendedor(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba que un Vendedor NO puede eliminar un cliente (403)."""
    cliente_id = cliente_de_prueba.id
    response = vendedor_client.delete(f"{CLIENTES_ENDPOINT}/{cliente_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'eliminar:cliente'" in response.json()["detail"]

def test_delete_cliente_unauthenticated(base_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba eliminar cliente sin autenticación (401)."""
    response = base_client.delete(f"{CLIENTES_ENDPOINT}/{cliente_de_prueba.id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# (test_delete_cliente_with_dependencies_conflict_admin sigue pendiente)