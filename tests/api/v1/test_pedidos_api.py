# app/tests/api/v1/test_pedidos_api.py

import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas para crear payloads y validar respuestas
from app.schemas.order_schema import PedidoClienteCreate, PedidoClienteRead
# Importar modelos y repositorios para verificaciones en BD
from app.models import PedidoCliente, Usuario, Cliente
from app.repositories import order_repository

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
PEDIDOS_ENDPOINT = f"{API_V1_STR}/pedidos"

# ==================================
# --- Tests para POST /pedidos ---
# ==================================
from tests.conftest import TestingSessionLocal # Importar factory de sesión
import logging # Añadir

logger = logging.getLogger(__name__) # Añadir

"""

def test_create_pedido_success_vendedor(
    vendedor_client: TestClient, db_session: Session, cliente_de_prueba: Cliente, vendedor_user: Usuario
):
    "Prueba la creación exitosa de un pedido por un Vendedor."
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data
    new_pedido_id = data["id"]
    assert data["estado"] == "NUEVO"
    assert data["cliente_id"] == cliente_de_prueba.id
    assert data["usuario_id_vendedor"] == vendedor_user.id
    assert data["cliente"]["id"] == cliente_de_prueba.id
    assert data["vendedor"]["id"] == vendedor_user.id

    # --- CORRECCIÓN ---
    # Verificar en la BD usando expire_all o una nueva sesión
    db_session.expire_all() # Fuerza a la sesión a releer de la BD
    # --- FIN CORRECCIÓN ---
    db_pedido = order_repository.get_pedido_by_id(db=db_session, pedido_id=new_pedido_id)
    # Añadir mensaje más descriptivo al assert
    assert db_pedido is not None, f"Pedido ID {new_pedido_id} creado vía API no fue encontrado en BD por el test (después de expire_all)."
    assert db_pedido.cliente_id == cliente_de_prueba.id
    assert db_pedido.usuario_id_vendedor == vendedor_user.id
    assert db_pedido.estado == "NUEVO"

def test_create_pedido_success_admin(
    admin_client: TestClient, db_session: Session, cliente_de_prueba: Cliente, admin_user: Usuario
):
    "Prueba la creación exitosa de un pedido por un Administrador."
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = admin_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    new_pedido_id = data["id"] # Obtener ID
    assert data["cliente_id"] == cliente_de_prueba.id
    assert data["usuario_id_vendedor"] == admin_user.id

    # --- CORRECCIÓN ---
    # Verificar en BD (simplificado, usando expire_all)
    db_session.expire_all()
    # --- FIN CORRECCIÓN ---
    # Añadir mensaje más descriptivo al assert
    assert order_repository.get_pedido_by_id(db=db_session, pedido_id=new_pedido_id) is not None, f"Pedido ID {new_pedido_id} creado vía API (Admin) no fue encontrado en BD por el test (después de expire_all)."

"""








# ===============================================================================

def test_create_pedido_success_vendedor(
    vendedor_client: TestClient, db_session: Session, cliente_de_prueba: Cliente, vendedor_user: Usuario
):
    """Prueba la creación exitosa de un pedido por un Vendedor."""
    logger.debug(f"Test 'test_create_pedido_success_vendedor' iniciando con db_session ID: {id(db_session)}")
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data
    new_pedido_id = data["id"]
    logger.info(f"Test 'test_create_pedido_success_vendedor': Pedido ID {new_pedido_id} creado vía API.")
    # ... (other assertions on response data) ...

    # --- CORRECCIÓN: Verificar en la BD usando una nueva sesión ---
    db_pedido = None
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_create_pedido_success_vendedor': Abierta verification_db ID {id(verification_db)} para buscar Pedido ID {new_pedido_id}.")
             db_pedido = order_repository.get_pedido_by_id(db=verification_db, pedido_id=new_pedido_id)
             logger.debug(f"Test 'test_create_pedido_success_vendedor': Resultado de get_pedido_by_id con verification_db: {'Encontrado' if db_pedido else 'No Encontrado'}")
             assert db_pedido is not None, f"Pedido ID {new_pedido_id} creado vía API no fue encontrado en BD por el test (con sesión de verificación)."
             # Realizar assertions aquí dentro, usando el objeto de la sesión de verificación
             assert db_pedido.cliente_id == cliente_de_prueba.id
             assert db_pedido.usuario_id_vendedor == vendedor_user.id
             assert db_pedido.estado == "NUEVO"
             logger.info(f"Test 'test_create_pedido_success_vendedor': Pedido ID {new_pedido_id} verificado exitosamente en BD.")
    except Exception as e:
        logger.error(f"Error durante verificación en BD para test_create_pedido_success_vendedor: {e}", exc_info=True)
        pytest.fail(f"Error durante verificación en BD para test_create_pedido_success_vendedor: {e}")

def test_create_pedido_success_admin(
    admin_client: TestClient, db_session: Session, cliente_de_prueba: Cliente, admin_user: Usuario
):
    """Prueba la creación exitosa de un pedido por un Administrador."""
    logger.debug(f"Test 'test_create_pedido_success_admin' iniciando con db_session ID: {id(db_session)}")
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = admin_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    new_pedido_id = data["id"] # Obtener ID
    logger.info(f"Test 'test_create_pedido_success_admin': Pedido ID {new_pedido_id} creado vía API.")
    assert data["cliente_id"] == cliente_de_prueba.id
    assert data["usuario_id_vendedor"] == admin_user.id

    # --- CORRECCIÓN: Verificar en BD usando una nueva sesión ---
    db_pedido = None
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_create_pedido_success_admin': Abierta verification_db ID {id(verification_db)} para buscar Pedido ID {new_pedido_id}.")
            db_pedido = order_repository.get_pedido_by_id(db=verification_db, pedido_id=new_pedido_id)
            logger.debug(f"Test 'test_create_pedido_success_admin': Resultado de get_pedido_by_id con verification_db: {'Encontrado' if db_pedido else 'No Encontrado'}")
            assert db_pedido is not None, f"Pedido ID {new_pedido_id} creado vía API (Admin) no fue encontrado en BD por el test (con sesión de verificación)."
            logger.info(f"Test 'test_create_pedido_success_admin': Pedido ID {new_pedido_id} verificado exitosamente en BD.")
    except Exception as e:
        logger.error(f"Error durante verificación en BD para test_create_pedido_success_admin: {e}", exc_info=True)
        pytest.fail(f"Error durante verificación en BD para test_create_pedido_success_admin: {e}")

# =======================FIN CORRECCIÓN ==================================



def test_create_pedido_cliente_not_found(vendedor_client: TestClient):
    """Prueba crear un pedido para un cliente inexistente (404)."""
    non_existent_cliente_id = 99990
    payload = PedidoClienteCreate(cliente_id=non_existent_cliente_id)
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    # El servicio debe lanzar 404 si el cliente no existe
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Cliente con ID {non_existent_cliente_id} no encontrado" in response.json()["detail"]

def test_create_pedido_invalid_payload(vendedor_client: TestClient):
    """Prueba crear un pedido sin cliente_id (422 Unprocessable Entity)."""
    invalid_payload = {} # Falta cliente_id
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_create_pedido_forbidden_operario(
    operario_client: TestClient, cliente_de_prueba: Cliente
):
    """Prueba que un Operario no puede crear pedidos (403 Forbidden)."""
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = operario_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_403_FORBIDDEN
    # Asume que el permiso 'crear:pedido_cliente' existe y no está asignado a Operario
    assert "Permiso insuficiente: Se requiere 'crear:pedido_cliente'" in response.json()["detail"]

def test_create_pedido_unauthenticated(base_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba crear un pedido sin autenticación (401 Unauthorized)."""
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = base_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# ========================================
# --- Tests para GET /pedidos/{pedido_id} ---
# ========================================



def test_get_pedido_success_vendedor(vendedor_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba obtener un pedido existente como Vendedor."""
    pedido_id = pedido_de_prueba.id
    response = vendedor_client.get(f"{PEDIDOS_ENDPOINT}/{pedido_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == pedido_id
    assert data["cliente"]["id"] == pedido_de_prueba.cliente_id
    assert data["vendedor"]["id"] == pedido_de_prueba.usuario_id_vendedor

def test_get_pedido_success_admin(admin_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba obtener un pedido existente como Admin."""
    pedido_id = pedido_de_prueba.id
    response = admin_client.get(f"{PEDIDOS_ENDPOINT}/{pedido_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == pedido_id

def test_get_pedido_not_found(vendedor_client: TestClient):
    """Prueba obtener un pedido inexistente (404)."""
    non_existent_pedido_id = 99991
    response = vendedor_client.get(f"{PEDIDOS_ENDPOINT}/{non_existent_pedido_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Pedido con ID {non_existent_pedido_id} no encontrado" in response.json()["detail"]

def test_get_pedido_forbidden_operario(operario_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba que un Operario no puede obtener detalles de un pedido (403)."""
    pedido_id = pedido_de_prueba.id
    response = operario_client.get(f"{PEDIDOS_ENDPOINT}/{pedido_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:pedido_cliente'" in response.json()["detail"]

def test_get_pedido_unauthenticated(base_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba obtener un pedido sin autenticación (401)."""
    pedido_id = pedido_de_prueba.id
    response = base_client.get(f"{PEDIDOS_ENDPOINT}/{pedido_id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# ==================================
# --- Tests para GET /pedidos ---
# ==================================

def test_list_pedidos_success(vendedor_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba listar pedidos como Vendedor."""
    response = vendedor_client.get(PEDIDOS_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    # Verificar que el pedido de prueba está en la lista
    assert any(p["id"] == pedido_de_prueba.id for p in data)
    # Verificar estructura básica de un elemento
    if data:
        assert "id" in data[0]
        assert "estado" in data[0]
        assert "cliente" in data[0]
        assert "vendedor" in data[0]

def test_list_pedidos_filtered(admin_client: TestClient, pedido_de_prueba: PedidoCliente, cliente_de_prueba: Cliente, vendedor_user: Usuario):
    """Prueba filtrar la lista de pedidos como Admin."""
    # Filtrar por cliente
    params_cliente = {"cliente_id": cliente_de_prueba.id}
    response_cliente = admin_client.get(PEDIDOS_ENDPOINT, params=params_cliente)
    assert response_cliente.status_code == status.HTTP_200_OK
    data_cliente = response_cliente.json()
    assert all(p["cliente"]["id"] == cliente_de_prueba.id for p in data_cliente)
    assert any(p["id"] == pedido_de_prueba.id for p in data_cliente) # Asegura que el de prueba esté

    # Filtrar por vendedor
    params_vendedor = {"vendedor_id": vendedor_user.id}
    response_vendedor = admin_client.get(PEDIDOS_ENDPOINT, params=params_vendedor)
    assert response_vendedor.status_code == status.HTTP_200_OK
    data_vendedor = response_vendedor.json()
    assert all(p["vendedor"]["id"] == vendedor_user.id for p in data_vendedor)
    assert any(p["id"] == pedido_de_prueba.id for p in data_vendedor)

    # Filtrar por estado
    params_estado = {"estado": "NUEVO"}
    response_estado = admin_client.get(PEDIDOS_ENDPOINT, params=params_estado)
    assert response_estado.status_code == status.HTTP_200_OK
    data_estado = response_estado.json()
    assert all(p["estado"] == "NUEVO" for p in data_estado)
    assert any(p["id"] == pedido_de_prueba.id for p in data_estado)

    # Filtrar por combinación (ej: cliente y estado)
    params_combo = {"cliente_id": cliente_de_prueba.id, "estado": "NUEVO"}
    response_combo = admin_client.get(PEDIDOS_ENDPOINT, params=params_combo)
    assert response_combo.status_code == status.HTTP_200_OK
    data_combo = response_combo.json()
    assert all(p["cliente"]["id"] == cliente_de_prueba.id and p["estado"] == "NUEVO" for p in data_combo)
    assert any(p["id"] == pedido_de_prueba.id for p in data_combo)

def test_list_pedidos_pagination(admin_client: TestClient, db_session: Session, cliente_de_prueba: Cliente):
    """Prueba la paginación al listar pedidos."""
    # Crear algunos pedidos adicionales para probar paginación
    ids_creados = []
    for i in range(3):
        resp = admin_client.post(PEDIDOS_ENDPOINT, json={"cliente_id": cliente_de_prueba.id})
        assert resp.status_code == status.HTTP_201_CREATED
        ids_creados.append(resp.json()["id"])

    # Probar limit
    response_limit = admin_client.get(f"{PEDIDOS_ENDPOINT}?limit=2")
    assert response_limit.status_code == status.HTTP_200_OK
    assert len(response_limit.json()) <= 2

    # Probar skip
    response_no_skip = admin_client.get(f"{PEDIDOS_ENDPOINT}?limit=5") # Obtener (hasta) 5 sin skip
    response_skip = admin_client.get(f"{PEDIDOS_ENDPOINT}?skip=1&limit=5") # Obtener (hasta) 5 saltando el primero
    assert response_skip.status_code == status.HTTP_200_OK
    data_no_skip = response_no_skip.json()
    data_skip = response_skip.json()

    if len(data_no_skip) > 1:
        first_id_no_skip = data_no_skip[0]["id"]
        ids_in_skipped_list = {p["id"] for p in data_skip}
        assert first_id_no_skip not in ids_in_skipped_list

def test_list_pedidos_forbidden_operario(operario_client: TestClient):
    """Prueba que un Operario no puede listar pedidos (403)."""
    response = operario_client.get(PEDIDOS_ENDPOINT)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:pedido_cliente'" in response.json()["detail"]

def test_list_pedidos_unauthenticated(base_client: TestClient):
    """Prueba listar pedidos sin autenticación (401)."""
    response = base_client.get(PEDIDOS_ENDPOINT)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED