# app/tests/api/v1/test_proformas_api.py

import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
import logging

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas
from app.schemas.order_schema import ProformaUpdate, ProformaRead, PedidoClienteCreate
# Importar modelos y repositorios
from app.models import Proforma, PedidoCliente, Usuario, Cliente
from app.repositories import order_repository
# Importar TestingSessionLocal y fixtures
from tests.conftest import TestingSessionLocal

logger = logging.getLogger(__name__)

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
PROFORMAS_ENDPOINT = f"{API_V1_STR}/proformas"
PEDIDOS_ENDPOINT = f"{API_V1_STR}/pedidos" # Necesario para crear el pedido/proformas


# ======================================================
# --- Tests para PATCH /proformas/{proforma_id} ---
# ======================================================

def test_update_proforma_estado_success(
    admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar el estado de BORRADOR a PENDIENTE_APROBACION como Admin."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)

    response = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)

    # Verificar respuesta
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == proforma_id
    assert data["estado"] == "PENDIENTE_APROBACION"

    # Verificar en BD
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None
            assert db_proforma.estado == "PENDIENTE_APROBACION"
            logger.info(f"Test 'test_update_proforma_estado_success': Estado verificado para ID {proforma_id}")
    except Exception as e:
        pytest.fail(f"Error verificación BD en test_update_proforma_estado_success: {e}")

def test_update_proforma_notas_success(
    vendedor_client: TestClient, pedido_con_proformas: dict, vendedor_user: Usuario
):
    """Prueba actualizar las notas como Vendedor (asume permiso 'actualizar:proforma_propia')."""
    # Asume que el Vendedor creó el pedido/proformas en la fixture
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    new_notes = f"Notas actualizadas por test - {uuid.uuid4().hex[:4]}"
    payload = ProformaUpdate(notas=new_notes).model_dump(exclude_unset=True)

    response = vendedor_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == proforma_id
    assert data["notas"] == new_notes

    # Verificar en BD
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None
            assert db_proforma.notas == new_notes
            logger.info(f"Test 'test_update_proforma_notas_success': Notas verificadas para ID {proforma_id}")
    except Exception as e:
        pytest.fail(f"Error verificación BD en test_update_proforma_notas_success: {e}")

def test_update_proforma_invalid_state_transition(
     admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba una transición de estado inválida (ej: PENDIENTE -> BORRADOR)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    # Primero cambiar a PENDIENTE
    payload_pendiente = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)
    resp_pendiente = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_pendiente)
    assert resp_pendiente.status_code == status.HTTP_200_OK

    # Intentar volver a BORRADOR (inválido según lógica de servicio)
    payload_borrador = ProformaUpdate(estado="BORRADOR").model_dump(exclude_unset=True)
    response_invalid = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_borrador)

    # Esperar 400 Bad Request (o 409 Conflict según implementación del servicio)
    assert response_invalid.status_code == status.HTTP_400_BAD_REQUEST
    assert "No se puede cambiar el estado" in response_invalid.json()["detail"]

def test_update_proforma_not_found(admin_client: TestClient):
    """Prueba actualizar una proforma inexistente (404)."""
    non_existent_id = 99992
    payload = ProformaUpdate(notas="Test").model_dump(exclude_unset=True)
    response = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{non_existent_id}", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_proforma_forbidden_operario(
    operario_client: TestClient, pedido_con_proformas: dict
):
    """Prueba que un Operario no puede actualizar proformas (403)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(notas="Intento de Operario").model_dump(exclude_unset=True)
    response = operario_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    # Verificar que requiere uno de los permisos de actualización
    assert "Permiso insuficiente: Se requiere uno de" in response.json()["detail"]
    assert "actualizar:proforma_propia" in response.json()["detail"]

def test_update_proforma_invalid_payload_estado(
    admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar con un valor de estado inválido (422)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    # Enviar directamente un diccionario con el valor inválido
    invalid_payload = {"estado": "ESTADO_INVENTADO"}
    response = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_proforma_unauthenticated(
    base_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar sin autenticación (401)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(notas="No Auth").model_dump(exclude_unset=True)
    response = base_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# (Aquí añadiríamos tests para GET /proformas/{id}, GET /pedidos/{id}/proformas
#  y los tests para añadir/quitar líneas en fases posteriores)