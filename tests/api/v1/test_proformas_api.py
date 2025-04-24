# app/tests/api/v1/test_proformas_api.py

from decimal import Decimal
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
import logging

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas
from app.schemas.order_schema import ProformaUpdate, ProformaRead, PedidoClienteCreate, LineaProformaMaterialCreate, LineaProformaServicioCreate
# Importar modelos y repositorios
from app.models import Proforma, PedidoCliente, Usuario, Cliente
from app.models import (
    MaterialConsumible, MaterialSimple, StockItemDimensional, ServicioDefinicion,
    LineaProformaMaterial, LineaProformaServicio # Para verificar en BD
)

from tests.conftest import ( # Importar fixtures de materiales/servicios
    material_consumible_de_prueba,
    material_simple_de_prueba,
    stock_item_dimensional_de_prueba,
    servicio_definicion_de_prueba
)

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




# ================================================================
# --- Tests para POST /proformas/{id}/lineas-material ---
# ================================================================

def test_add_linea_material_consumible_success(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible
):
    """Prueba añadir una línea de material consumible a una proforma PRODUCTO."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    material_id = material_consumible_de_prueba.id
    cantidad_a_anadir = Decimal("5.5")

    payload_schema = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_id,
        cantidad=cantidad_a_anadir
    )
    payload_dict = payload_schema.model_dump(mode='json')

    response = vendedor_client.post(
        f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material",
        json=payload_dict
    )

    # Verificar respuesta 201
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["id"] == proforma_id
    assert data["tipo"] == "PRODUCTO"

    # Verificar que la línea está en la respuesta
    assert len(data.get("lineas_material", [])) > 0
    nueva_linea_resp = data["lineas_material"][-1] # Asume que es la última añadida
    assert nueva_linea_resp["descripcion_item"] == material_consumible_de_prueba.nombre
    assert Decimal(nueva_linea_resp["cantidad"]) == cantidad_a_anadir
    assert nueva_linea_resp["unidad"] == material_consumible_de_prueba.unidad_medida
    # TODO: Verificar precio y total basados en lógica de precios real
    # assert Decimal(nueva_linea_resp["precio_unitario"]) == ...
    # assert Decimal(nueva_linea_resp["total_linea"]) == ...
    assert Decimal(data["subtotal"]) > 0 # Verificar que el subtotal se actualizó
    assert Decimal(data["total"]) > 0    # Verificar que el total se actualizó

    # Verificar en BD
    linea_id = nueva_linea_resp["id"]
    try:
        with TestingSessionLocal() as verification_db:
            db_linea = verification_db.get(LineaProformaMaterial, linea_id)
            assert db_linea is not None
            assert db_linea.material_consumible_id == material_id
            assert db_linea.cantidad == cantidad_a_anadir

            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None
            assert db_proforma.subtotal == Decimal(nueva_linea_resp["total_linea"]) # Asumiendo 1 línea
            assert db_proforma.total > 0
    except Exception as e:
        pytest.fail(f"Error verificación BD en test_add_linea_material_consumible_success: {e}")

# (Tests similares para MaterialSimple y StockItemDimensional)

def test_add_linea_material_wrong_proforma_type(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible
):
    """Prueba añadir línea de material a proforma de SERVICIO (400)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"] # <-- Proforma incorrecta
    payload = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_consumible_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Solo se pueden añadir líneas de material a proformas de tipo 'PRODUCTO'" in response.json()["detail"]

def test_add_linea_material_wrong_proforma_state(
    admin_client: TestClient,
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible
):
    """Prueba añadir línea a proforma que no está en BORRADOR (409)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    # Cambiar estado a PENDIENTE primero
    payload_update = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)
    resp_update = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_update)
    assert resp_update.status_code == status.HTTP_200_OK

    # Intentar añadir línea
    payload_linea = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_consumible_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = admin_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload_linea)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "Debe estar en 'BORRADOR'" in response.json()["detail"]

def test_add_linea_material_not_found(
    vendedor_client: TestClient, pedido_con_proformas: dict
):
    """Prueba añadir línea con ID de material inexistente (404)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=99999, # <-- ID inexistente
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Material de origen no encontrado" in response.json()["detail"]

def test_add_linea_material_invalid_payload(
    vendedor_client: TestClient, pedido_con_proformas: dict
):
    """Prueba añadir línea con cantidad inválida (422)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    invalid_payload = { # Falta tipo_material_origen, material_id
        "cantidad": 0 # Cantidad debe ser > 0
    }
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_add_linea_material_forbidden(
    operario_client: TestClient, # Usar cliente sin permiso
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible
):
    """Prueba añadir línea sin permiso (403)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_consumible_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = operario_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'anadir:linea_proforma'" in response.json()["detail"]


# ==============================================================
# --- Tests para POST /proformas/{id}/lineas-servicio ---
# ==============================================================

def test_add_linea_servicio_success(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir una línea de servicio a una proforma SERVICIO."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    servicio_id = servicio_definicion_de_prueba.id
    cantidad_a_anadir = Decimal("2")

    payload_schema = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_id,
        cantidad=cantidad_a_anadir
    )
    payload_dict = payload_schema.model_dump(mode='json')

    response = vendedor_client.post(
        f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio",
        json=payload_dict
    )

    # Verificar respuesta 201
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["id"] == proforma_id
    assert data["tipo"] == "SERVICIO"

    # Verificar que la línea está en la respuesta
    assert len(data.get("lineas_servicio", [])) > 0
    nueva_linea_resp = data["lineas_servicio"][-1]
    assert nueva_linea_resp["descripcion_servicio"] == servicio_definicion_de_prueba.nombre
    assert Decimal(nueva_linea_resp["cantidad"]) == cantidad_a_anadir
    # TODO: Verificar precio y total
    assert Decimal(data["subtotal"]) > 0
    assert Decimal(data["total"]) > 0

    # Verificar en BD
    linea_id = nueva_linea_resp["id"]
    try:
        with TestingSessionLocal() as verification_db:
            db_linea = verification_db.get(LineaProformaServicio, linea_id)
            assert db_linea is not None
            assert db_linea.servicio_definicion_id == servicio_id
            assert db_linea.cantidad == cantidad_a_anadir

            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None
            assert db_proforma.subtotal == Decimal(nueva_linea_resp["total_linea"])
            assert db_proforma.total > 0
    except Exception as e:
        pytest.fail(f"Error verificación BD en test_add_linea_servicio_success: {e}")

# (Añadir test para línea de servicio asociada a material)

def test_add_linea_servicio_wrong_proforma_type(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio a proforma de PRODUCTO (400)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"] # <-- Proforma incorrecta
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_definicion_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Solo se pueden añadir líneas de servicio a proformas de tipo 'SERVICIO'" in response.json()["detail"]

def test_add_linea_servicio_wrong_proforma_state(
    admin_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio a proforma no en BORRADOR (409)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    # Cambiar estado a PENDIENTE primero
    payload_update = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)
    resp_update = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_update)
    assert resp_update.status_code == status.HTTP_200_OK

    # Intentar añadir línea
    payload_linea = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_definicion_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = admin_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload_linea)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "Debe estar en 'BORRADOR'" in response.json()["detail"]

def test_add_linea_servicio_def_not_found(
    vendedor_client: TestClient, pedido_con_proformas: dict
):
    """Prueba añadir línea con ID de servicio inexistente (404)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=99999, # <-- ID inexistente
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "ServicioDefinicion con ID 99999 no encontrado" in response.json()["detail"]

# (Añadir tests para linea_material_id inválido)

def test_add_linea_servicio_forbidden(
    operario_client: TestClient, # Usar cliente sin permiso
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio sin permiso (403)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_definicion_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = operario_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'anadir:linea_proforma'" in response.json()["detail"]
