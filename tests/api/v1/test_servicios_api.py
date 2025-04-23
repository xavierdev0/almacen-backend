# app/tests/api/v1/test_servicios_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
from decimal import Decimal
import logging

# (Imports sin cambios)
from app.core.config import settings
from app.schemas.service_schema import (
    ServicioDefinicionCreate, ServicioDefinicionRead, ServicioDefinicionUpdate
)
from app.models import ServicioDefinicion
from tests.conftest import (
    TestingSessionLocal,
    DEFINICIONES_ENDPOINT
)
# Importar operario_client y dibujante_client si no están ya importados globalmente
from tests.conftest import operario_client, dibujante_client

logger = logging.getLogger(__name__)

# --- Helpers ---
def create_valid_servicio_payload(suffix: str) -> dict:
    """Crea un payload válido y JSON-serializable para ServicioDefinicionCreate."""
    schema_instance = ServicioDefinicionCreate(
        codigo=f"SERV-{suffix}", 
        nombre=f"Servicio Helper {suffix}",
        unidad_cobro="pieza",
        costo_por_unidad=Decimal("10.0"),
        requiere_dibujo_cnc=False,
        tiempo_setup_min=Decimal("0.0"),
        tiempo_preparado_min_por_unidad=Decimal("0.0"),
        factor_ih=Decimal("1.0"),
        # El resto de campos opcionales (como descripcion, costo_por_minuto, etc.)
        # no son estrictamente necesarios aquí si el schema los marca como Optional
    )
    # Usar mode='json' para serializar Decimal correctamente
    return schema_instance.model_dump(mode='json')


# ============================================================
# --- Tests para Endpoints de Definición de Servicios ---
# ============================================================
class TestServicioDefinicionAPI:

    # --- POST /definiciones ---

    def test_create_servicio_success_admin(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_servicio_payload(suffix)
        response = admin_client.post(DEFINICIONES_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_201_CREATED # Verificar que ahora sí crea
        data = response.json()
        assert data["nombre"] == payload["nombre"]
        assert data["unidad_cobro"] == payload["unidad_cobro"]
        # Asegurarse que la comparación de Decimal funciona
        assert Decimal(data["costo_por_unidad"]) == Decimal(payload["costo_por_unidad"])
        with TestingSessionLocal() as verification_db:
            db_obj = verification_db.get(ServicioDefinicion, data["id"])
            assert db_obj is not None
            assert db_obj.nombre == payload["nombre"]

    def test_create_servicio_duplicate_name_admin(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        """Prueba crear servicio con nombre duplicado (409)."""
        # servicio_definicion_de_prueba ahora debería crearse correctamente
        payload_schema = ServicioDefinicionCreate(
            codigo=f"FIX-SERV-{servicio_definicion_de_prueba.codigo}",
            nombre=servicio_definicion_de_prueba.nombre, # Nombre existente
            unidad_cobro="hora",
            tiempo_setup_min=Decimal("0.0"),
            tiempo_preparado_min_por_unidad=Decimal("0.0"),
            factor_ih=Decimal("1.0"),
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_409_CONFLICT
        assert "nombre" in response.json()["detail"].lower()

    # (test_create_servicio_invalid_data y test_create_servicio_forbidden_vendedor permanecen iguales)
    def test_create_servicio_invalid_data(self, admin_client: TestClient):
        payload_no_name = {"unidad_cobro": "corte", "costo_por_unidad": "5.0"}
        response_no_name = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_no_name)
        assert response_no_name.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        payload_no_unit = {"nombre": "Servicio Sin Unidad", "costo_por_minuto": "1.0"}
        response_no_unit = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_no_unit)
        assert response_no_unit.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_servicio_forbidden_vendedor(self, vendedor_client: TestClient):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_servicio_payload(suffix)
        response = vendedor_client.post(DEFINICIONES_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    # --- GET /definiciones ---
    # (tests de listado permanecen mayormente iguales, pero el de paginación ahora debería funcionar)

    def test_list_servicios_success(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        # servicio_definicion_de_prueba ahora debería crearse
        response = admin_client.get(DEFINICIONES_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert any(s["id"] == servicio_definicion_de_prueba.id for s in data)

    def test_list_servicios_permission_vendedor(self, vendedor_client: TestClient):
        response = vendedor_client.get(DEFINICIONES_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK

    def test_list_servicios_permission_dibujante(self, dibujante_client: TestClient):
        response = dibujante_client.get(DEFINICIONES_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK

    def test_list_servicios_forbidden_operario(self, operario_client: TestClient):
        response = operario_client.get(DEFINICIONES_ENDPOINT)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_servicios_pagination(self, admin_client: TestClient):
        # Crear suficientes para probar (ahora deberían crearse)
        created_ids = []
        for i in range(3):
            suffix = uuid.uuid4().hex[:4]
            payload = create_valid_servicio_payload(suffix)
            resp_create = admin_client.post(DEFINICIONES_ENDPOINT, json=payload)
            assert resp_create.status_code == status.HTTP_201_CREATED # Verificar creación
            created_ids.append(resp_create.json()["id"])

        # Probar limit=1
        response_limit = admin_client.get(f"{DEFINICIONES_ENDPOINT}?limit=1")
        assert response_limit.status_code == status.HTTP_200_OK
        assert len(response_limit.json()) == 1 # Ahora debería haber resultados

        # Probar skip=1
        response_no_skip = admin_client.get(f"{DEFINICIONES_ENDPOINT}?limit=2")
        response_skip = admin_client.get(f"{DEFINICIONES_ENDPOINT}?skip=1&limit=2")
        assert response_skip.status_code == status.HTTP_200_OK
        # La verificación de skip debería funcionar ahora que hay datos
        if len(response_no_skip.json()) > 1:
             first_id_no_skip = response_no_skip.json()[0]["id"]
             ids_skipped = {s["id"] for s in response_skip.json()}
             assert first_id_no_skip not in ids_skipped

    # --- GET /definiciones/{id} ---
    # (tests sin cambios, pero ahora la fixture debería funcionar)
    def test_get_servicio_success(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        servicio_id = servicio_definicion_de_prueba.id
        response = admin_client.get(f"{DEFINICIONES_ENDPOINT}/{servicio_id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == servicio_id
        assert data["nombre"] == servicio_definicion_de_prueba.nombre

    def test_get_servicio_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{DEFINICIONES_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # --- PUT /definiciones/{id} ---
    # (tests sin cambios, pero ahora la fixture debería funcionar)
    def test_update_servicio_success(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        servicio_id = servicio_definicion_de_prueba.id
        update_schema = ServicioDefinicionUpdate(
            descripcion="Descripción Actualizada v2",
            costo_por_minuto=Decimal("2.5")
        )
        update_payload = update_schema.model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{DEFINICIONES_ENDPOINT}/{servicio_id}", json=update_payload)
        assert response_update.status_code == status.HTTP_200_OK
        data = response_update.json()
        assert data["id"] == servicio_id
        assert data["descripcion"] == update_schema.descripcion
        assert Decimal(data["costo_por_minuto"]) == update_schema.costo_por_minuto

        with TestingSessionLocal() as verification_db:
            db_obj = verification_db.get(ServicioDefinicion, servicio_id)
            assert db_obj is not None
            assert db_obj.descripcion == update_schema.descripcion
            assert db_obj.costo_por_minuto == update_schema.costo_por_minuto

    def test_update_servicio_duplicate_name(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        suffix = uuid.uuid4().hex[:6]
        payload_other = create_valid_servicio_payload(suffix)
        resp_other = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_other)
        assert resp_other.status_code == status.HTTP_201_CREATED # Asegurar que el otro se crea

        update_payload = ServicioDefinicionUpdate(nombre=payload_other["nombre"]).model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{DEFINICIONES_ENDPOINT}/{servicio_definicion_de_prueba.id}", json=update_payload)
        assert response_update.status_code == status.HTTP_409_CONFLICT

    # --- DELETE /definiciones/{id} ---
    # (tests sin cambios, pero ahora el create inicial debería funcionar)
    def test_delete_servicio_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_servicio_payload(suffix)
        response_create = admin_client.post(DEFINICIONES_ENDPOINT, json=payload)
        assert response_create.status_code == status.HTTP_201_CREATED # Verificar que crea
        created_id = response_create.json()["id"]

        response_delete = admin_client.delete(f"{DEFINICIONES_ENDPOINT}/{created_id}")
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT

        db_session.expire_all()
        assert db_session.get(ServicioDefinicion, created_id) is None

    def test_delete_servicio_not_found(self, admin_client: TestClient):
        response = admin_client.delete(f"{DEFINICIONES_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # @pytest.mark.skip(reason="PENDIENTE: Implementar cuando Formula o LineaProforma use ServicioDefinicion.")
    # def test_delete_servicio_conflict(self, admin_client: TestClient, ...)