# app/tests/api/v1/test_inventario_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
from decimal import Decimal
import logging

# Importar settings y config
from app.core.config import settings
# Importar schemas necesarios
from app.schemas.inventory_schema import (
    MaterialDimensionalCreate, MaterialDimensionalRead, MaterialDimensionalUpdate,
    MaterialConsumibleCreate, MaterialConsumibleRead, MaterialConsumibleUpdate,
    MaterialSimpleCreate, MaterialSimpleRead, MaterialSimpleUpdate,
    StockItemDimensionalCreate, StockItemDimensionalRead,
)
# Importar el schema de ajuste de stock
from app.api.v1.endpoints.inventario import StockAdjustRequest

# Importar modelos para verificaciones y fixtures
from app.models import (
    MaterialDimensional,
    MaterialConsumible,
    MaterialSimple,
    StockItemDimensional
)
# Importar repositorios para verificaciones (aunque usar .get es más simple)
from app.repositories import inventory_repository
# Importar constantes de endpoints y fábrica de sesión desde conftest
from tests.conftest import (
    TestingSessionLocal, # Importar la factory para sesiones de verificación
    MAT_DIM_ENDPOINT,
    MAT_CONS_ENDPOINT,
    MAT_SIMP_ENDPOINT,
    STOCK_ITEM_DIM_ENDPOINT
)
# Importar fixtures de cliente necesarias (si no están globales)
from tests.conftest import admin_client, vendedor_client, operario_client

logger = logging.getLogger(__name__)

# --- Helpers para Crear Payloads Válidos  ---
def create_valid_mat_dim_payload(suffix: str) -> dict:
    schema_instance = MaterialDimensionalCreate(
        sku=f"SKU-DIM-{suffix}",
        nombre=f"Plancha Test {suffix}",
        espesor_nominal=Decimal("18.0"),
        unidad_dimension="mm"
    )
    return schema_instance.model_dump(mode='json')

def create_valid_mat_cons_payload(suffix: str) -> dict:
    schema_instance = MaterialConsumibleCreate(
        sku=f"SKU-CONS-{suffix}",
        nombre=f"Consumible Test {suffix}",
        unidad_medida="litro"
    )
    return schema_instance.model_dump(mode='json')

def create_valid_mat_simp_payload(suffix: str) -> dict:
    schema_instance = MaterialSimpleCreate(
        sku=f"SKU-SIMP-{suffix}",
        nombre=f"Simple Test {suffix}",
        unidad_medida="unidad"
    )
    return schema_instance.model_dump(mode='json')

# =====================================================
# --- Tests para Endpoints de Material Dimensional ---
# =====================================================
class TestMaterialDimensionalAPI:

    def test_create_material_dimensional_success_admin(self, admin_client: TestClient, db_session: Session):
        unique_suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_dim_payload(unique_suffix)
        response = admin_client.post(MAT_DIM_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["sku"] == payload["sku"]
        assert data["nombre"] == payload["nombre"]
        assert Decimal(data["espesor_nominal"]) == Decimal(payload["espesor_nominal"])
        new_id = data["id"]

        try:
            with TestingSessionLocal() as verification_db:
                db_obj = verification_db.get(MaterialDimensional, new_id)
                assert db_obj is not None, f"MaterialDimensional ID {new_id} no encontrado en BD post-creación."
                assert db_obj.sku == payload["sku"]
                assert db_obj.espesor_nominal == Decimal(payload["espesor_nominal"])
                logger.info(f"Test 'test_create_material_dimensional_success_admin': MaterialDimensional ID {new_id} verificado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_create_material_dimensional_success_admin: {e}")

    def test_create_material_dimensional_duplicate_sku(self, admin_client: TestClient, material_dimensional_de_prueba: MaterialDimensional):
        payload_schema = MaterialDimensionalCreate(
             sku=material_dimensional_de_prueba.sku,
             nombre=f"Duplicado Dim Test",
             espesor_nominal=Decimal("10.0"),
             unidad_dimension="cm"
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(MAT_DIM_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_create_material_dimensional_invalid_data(self, admin_client: TestClient):
        payload_no_sku = {"nombre": "Test Sin SKU", "espesor_nominal": "10.0"}
        response_no_sku = admin_client.post(MAT_DIM_ENDPOINT, json=payload_no_sku)
        assert response_no_sku.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        payload_bad_thickness_dict = create_valid_mat_dim_payload("badthick")
        payload_bad_thickness_dict["espesor_nominal"] = "dieciocho"
        response_bad_thickness = admin_client.post(MAT_DIM_ENDPOINT, json=payload_bad_thickness_dict)
        assert response_bad_thickness.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_material_dimensional_forbidden(self, vendedor_client: TestClient):
        unique_suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_dim_payload(unique_suffix)
        response = vendedor_client.post(MAT_DIM_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_materiales_dimensionales_success(self, admin_client: TestClient, material_dimensional_de_prueba: MaterialDimensional):
        response_list = admin_client.get(MAT_DIM_ENDPOINT)
        assert response_list.status_code == status.HTTP_200_OK
        data = response_list.json()
        assert isinstance(data, list)
        assert any(item["id"] == material_dimensional_de_prueba.id for item in data)

    def test_list_materiales_dimensionales_permission_vendedor(self, vendedor_client: TestClient):
        response = vendedor_client.get(MAT_DIM_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK

    def test_get_material_dimensional_success(self, admin_client: TestClient, material_dimensional_de_prueba: MaterialDimensional):
        response_get = admin_client.get(f"{MAT_DIM_ENDPOINT}/{material_dimensional_de_prueba.id}")
        assert response_get.status_code == status.HTTP_200_OK
        data = response_get.json()
        assert data["id"] == material_dimensional_de_prueba.id
        assert data["sku"] == material_dimensional_de_prueba.sku

    def test_get_material_dimensional_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{MAT_DIM_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_material_dimensional_success(self, admin_client: TestClient, material_dimensional_de_prueba: MaterialDimensional):
        update_suffix = uuid.uuid4().hex[:4]
        update_schema = MaterialDimensionalUpdate(
            nombre=f"Plancha ACTUALIZADA {update_suffix}",
            descripcion="Nueva descripción fixture",
            espesor_nominal=Decimal("16.5")
        )
        update_payload = update_schema.model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{MAT_DIM_ENDPOINT}/{material_dimensional_de_prueba.id}", json=update_payload)
        assert response_update.status_code == status.HTTP_200_OK
        data = response_update.json()
        assert data["id"] == material_dimensional_de_prueba.id
        assert data["nombre"] == update_schema.nombre
        assert data["descripcion"] == update_schema.descripcion
        assert Decimal(data["espesor_nominal"]) == update_schema.espesor_nominal
        assert data["sku"] == material_dimensional_de_prueba.sku

        with TestingSessionLocal() as verification_db:
             db_obj_updated = verification_db.get(MaterialDimensional, material_dimensional_de_prueba.id)
             assert db_obj_updated is not None
             assert db_obj_updated.nombre == update_schema.nombre
             assert db_obj_updated.descripcion == update_schema.descripcion
             assert db_obj_updated.espesor_nominal == update_schema.espesor_nominal

    def test_update_material_dimensional_not_found(self, admin_client: TestClient):
        update_payload = MaterialDimensionalUpdate(nombre="Test").model_dump(mode='json', exclude_unset=True)
        response = admin_client.put(f"{MAT_DIM_ENDPOINT}/999999", json=update_payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_material_dimensional_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_dim_payload(suffix)
        response_create = admin_client.post(MAT_DIM_ENDPOINT, json=payload)
        assert response_create.status_code == status.HTTP_201_CREATED
        created_id = response_create.json()["id"]
        response_delete = admin_client.delete(f"{MAT_DIM_ENDPOINT}/{created_id}")
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT

        # --- VERIFICACIÓN REFACTORIZADA ---
        try:
            with TestingSessionLocal() as verification_db:
                logger.debug(f"Test 'test_delete_material_dimensional_success': Verificando ID {created_id} con nueva sesión.")
                deleted_obj = verification_db.get(MaterialDimensional, created_id)
                assert deleted_obj is None, f"MaterialDimensional ID {created_id} aún encontrado en BD post-delete."
                logger.info(f"Test 'test_delete_material_dimensional_success': MaterialDimensional ID {created_id} verificado como eliminado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_delete_material_dimensional_success: {e}")

    def test_delete_material_dimensional_not_found(self, admin_client: TestClient):
        response = admin_client.delete(f"{MAT_DIM_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.skip(reason="PENDIENTE: Implementar cuando StockItemDimensional esté listo y se pueda crear en setup.")
    def test_delete_material_dimensional_conflict(self, admin_client: TestClient, stock_item_dimensional_de_prueba: StockItemDimensional):
        material_id = stock_item_dimensional_de_prueba.material_dimensional_id
        response = admin_client.delete(f"{MAT_DIM_ENDPOINT}/{material_id}")
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_list_materiales_dimensionales_forbidden_operario(self, operario_client: TestClient):
        response = operario_client.get(MAT_DIM_ENDPOINT)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "Permiso insuficiente: Se requiere 'leer:material_definicion'" in response.json()["detail"]


# =====================================================
# --- Tests para Endpoints de Material Consumible ---
# =====================================================
class TestMaterialConsumibleAPI:

    def test_create_material_consumible_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_cons_payload(suffix)
        response = admin_client.post(MAT_CONS_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["sku"] == payload["sku"]
        new_id = data["id"]

        try:
            with TestingSessionLocal() as verification_db:
                db_obj = verification_db.get(MaterialConsumible, new_id)
                assert db_obj is not None, f"MaterialConsumible ID {new_id} no encontrado en BD post-creación."
                assert db_obj.sku == payload["sku"]
                logger.info(f"Test 'test_create_material_consumible_success': MaterialConsumible ID {new_id} verificado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_create_material_consumible_success: {e}")

    def test_create_material_consumible_duplicate_sku(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        payload_schema = MaterialConsumibleCreate(
            sku=material_consumible_de_prueba.sku,
            nombre="Duplicado Cons",
            unidad_medida="kg"
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(MAT_CONS_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_create_material_consumible_invalid_data(self, admin_client: TestClient):
        payload_no_sku = {"nombre": "Test Cons Sin SKU", "unidad_medida": "litro"}
        response_no_sku = admin_client.post(MAT_CONS_ENDPOINT, json=payload_no_sku)
        assert response_no_sku.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        payload_no_unit = {"sku": "TEST-CONS-NOUNIT", "nombre": "Test Cons Sin Unidad"}
        response_no_unit = admin_client.post(MAT_CONS_ENDPOINT, json=payload_no_unit)
        assert response_no_unit.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_material_consumible_forbidden(self, vendedor_client: TestClient):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_cons_payload(suffix)
        response = vendedor_client.post(MAT_CONS_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_materiales_consumibles_success(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        response_list = admin_client.get(MAT_CONS_ENDPOINT)
        assert response_list.status_code == status.HTTP_200_OK
        data = response_list.json()
        assert isinstance(data, list)
        assert any(item["id"] == material_consumible_de_prueba.id for item in data)

    def test_list_materiales_consumibles_permission_vendedor(self, vendedor_client: TestClient):
        response = vendedor_client.get(MAT_CONS_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK

    def test_get_material_consumible_success(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        response_get = admin_client.get(f"{MAT_CONS_ENDPOINT}/{material_consumible_de_prueba.id}")
        assert response_get.status_code == status.HTTP_200_OK
        data = response_get.json()
        assert data["id"] == material_consumible_de_prueba.id
        assert data["sku"] == material_consumible_de_prueba.sku

    def test_get_material_consumible_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{MAT_CONS_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_material_consumible_success(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        update_suffix = uuid.uuid4().hex[:4]
        update_schema = MaterialConsumibleUpdate(
            nombre=f"Consumible ACTUALIZADO {update_suffix}",
            descripcion="Nueva desc",
            stock_minimo=Decimal("25.5")
        )
        update_payload = update_schema.model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{MAT_CONS_ENDPOINT}/{material_consumible_de_prueba.id}", json=update_payload)
        assert response_update.status_code == status.HTTP_200_OK
        data = response_update.json()
        assert data["id"] == material_consumible_de_prueba.id
        assert data["nombre"] == update_schema.nombre
        assert data["descripcion"] == update_schema.descripcion
        assert Decimal(data["stock_minimo"]) == update_schema.stock_minimo

        with TestingSessionLocal() as verification_db:
             db_obj_updated = verification_db.get(MaterialConsumible, material_consumible_de_prueba.id)
             assert db_obj_updated is not None
             assert db_obj_updated.nombre == update_schema.nombre
             assert db_obj_updated.stock_minimo == update_schema.stock_minimo

    def test_update_material_consumible_not_found(self, admin_client: TestClient):
        update_payload = MaterialConsumibleUpdate(nombre="Test").model_dump(mode='json', exclude_unset=True)
        response = admin_client.put(f"{MAT_CONS_ENDPOINT}/999999", json=update_payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_material_consumible_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_cons_payload(suffix)
        response_create = admin_client.post(MAT_CONS_ENDPOINT, json=payload)
        assert response_create.status_code == status.HTTP_201_CREATED
        created_id = response_create.json()["id"]
        response_delete = admin_client.delete(f"{MAT_CONS_ENDPOINT}/{created_id}")
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT
        # --- VERIFICACIÓN REFACTORIZADA ---
        try:
            with TestingSessionLocal() as verification_db:
                deleted_obj = verification_db.get(MaterialConsumible, created_id)
                assert deleted_obj is None, f"MaterialConsumible ID {created_id} aún encontrado en BD post-delete."
                logger.info(f"Test 'test_delete_material_consumible_success': MaterialConsumible ID {created_id} verificado como eliminado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_delete_material_consumible_success: {e}")
        # --- FIN VERIFICACIÓN ---

    def test_delete_material_consumible_not_found(self, admin_client: TestClient):
        response = admin_client.delete(f"{MAT_CONS_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # @pytest.mark.skip(reason="PENDIENTE: Implementar cuando FormulaItem o LineaProformaMaterial use MaterialConsumible.")
    # def test_delete_material_consumible_conflict(self, admin_client: TestClient, ...)

    def test_adjust_stock_consumible_success(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        mat_id = material_consumible_de_prueba.id
        initial_stock = material_consumible_de_prueba.stock_actual or Decimal("0.0") # Default a 0 si es None

        # Añadir stock
        adjust_payload_add_schema = StockAdjustRequest(change_amount=Decimal("50.5"))
        adjust_payload_add_dict = adjust_payload_add_schema.model_dump(mode='json')
        response_add = admin_client.post(f"{MAT_CONS_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload_add_dict)
        assert response_add.status_code == status.HTTP_200_OK
        data_add = response_add.json()
        expected_stock_add = initial_stock + adjust_payload_add_schema.change_amount
        assert Decimal(data_add["stock_actual"]) == pytest.approx(expected_stock_add) # Usar approx por floats

        try:
            with TestingSessionLocal() as verification_db_add:
                db_obj_add = verification_db_add.get(MaterialConsumible, mat_id)
                assert db_obj_add is not None
                assert db_obj_add.stock_actual == pytest.approx(expected_stock_add)
                logger.info(f"Test 'test_adjust_stock_consumible_success' (add): Stock verificado en BD para ID {mat_id}.")
        except Exception as e:
            pytest.fail(f"Error verificación BD (add) en test_adjust_stock_consumible_success: {e}")

        # Quitar stock
        adjust_payload_sub_schema = StockAdjustRequest(change_amount=Decimal("-10.0"))
        adjust_payload_sub_dict = adjust_payload_sub_schema.model_dump(mode='json')
        response_sub = admin_client.post(f"{MAT_CONS_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload_sub_dict)
        assert response_sub.status_code == status.HTTP_200_OK
        data_sub = response_sub.json()
        expected_stock_sub = expected_stock_add + adjust_payload_sub_schema.change_amount
        assert Decimal(data_sub["stock_actual"]) == pytest.approx(expected_stock_sub)

        try:
            with TestingSessionLocal() as verification_db_sub:
                db_obj_sub = verification_db_sub.get(MaterialConsumible, mat_id)
                assert db_obj_sub is not None
                assert db_obj_sub.stock_actual == pytest.approx(expected_stock_sub)
                logger.info(f"Test 'test_adjust_stock_consumible_success' (sub): Stock verificado en BD para ID {mat_id}.")
        except Exception as e:
            pytest.fail(f"Error verificación BD (sub) en test_adjust_stock_consumible_success: {e}")

    def test_adjust_stock_consumible_negative_result(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        mat_id = material_consumible_de_prueba.id
        adjust_payload = StockAdjustRequest(change_amount=Decimal("-10000.0")).model_dump(mode='json')
        response = admin_client.post(f"{MAT_CONS_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_adjust_stock_consumible_forbidden(self, vendedor_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        mat_id = material_consumible_de_prueba.id
        adjust_payload = StockAdjustRequest(change_amount=Decimal("10.0")).model_dump(mode='json')
        response = vendedor_client.post(f"{MAT_CONS_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN


# =====================================================
# --- Tests para Endpoints de Material Simple ---
# =====================================================
class TestMaterialSimpleAPI:
     # --- POST /materiales-simples ---
    def test_create_material_simple_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_simp_payload(suffix)
        response = admin_client.post(MAT_SIMP_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["sku"] == payload["sku"]
        new_id = data["id"]

        try:
            with TestingSessionLocal() as verification_db:
                db_obj = verification_db.get(MaterialSimple, new_id)
                assert db_obj is not None, f"MaterialSimple ID {new_id} no encontrado en BD post-creación."
                assert db_obj.sku == payload["sku"]
                logger.info(f"Test 'test_create_material_simple_success': MaterialSimple ID {new_id} verificado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_create_material_simple_success: {e}")

    def test_create_material_simple_duplicate_sku(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        payload_schema = MaterialSimpleCreate(
            sku=material_simple_de_prueba.sku, # Existente
            nombre="Duplicado Simp",
            unidad_medida="par"
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(MAT_SIMP_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_create_material_simple_invalid_data(self, admin_client: TestClient):
        payload_no_sku = {"nombre": "Test Simp Sin SKU", "unidad_medida": "pqt"}
        response_no_sku = admin_client.post(MAT_SIMP_ENDPOINT, json=payload_no_sku)
        assert response_no_sku.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_material_simple_forbidden(self, vendedor_client: TestClient):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_simp_payload(suffix)
        response = vendedor_client.post(MAT_SIMP_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_materiales_simples_success(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        response_list = admin_client.get(MAT_SIMP_ENDPOINT)
        assert response_list.status_code == status.HTTP_200_OK
        data = response_list.json()
        assert isinstance(data, list)
        assert any(item["id"] == material_simple_de_prueba.id for item in data)

    def test_list_materiales_simples_permission_vendedor(self, vendedor_client: TestClient):
        response = vendedor_client.get(MAT_SIMP_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK # Vendedor puede leer

    def test_get_material_simple_success(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        response_get = admin_client.get(f"{MAT_SIMP_ENDPOINT}/{material_simple_de_prueba.id}")
        assert response_get.status_code == status.HTTP_200_OK
        data = response_get.json()
        assert data["id"] == material_simple_de_prueba.id

    def test_get_material_simple_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{MAT_SIMP_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_material_simple_success(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        update_suffix = uuid.uuid4().hex[:4]
        update_schema = MaterialSimpleUpdate(
            nombre=f"Simple ACTUALIZADO {update_suffix}",
            ubicacion="Caja-Z9"
        )
        update_payload = update_schema.model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{MAT_SIMP_ENDPOINT}/{material_simple_de_prueba.id}", json=update_payload)
        assert response_update.status_code == status.HTTP_200_OK
        data = response_update.json()
        assert data["nombre"] == update_schema.nombre
        assert data["ubicacion"] == update_schema.ubicacion

        with TestingSessionLocal() as verification_db:
             db_obj_updated = verification_db.get(MaterialSimple, material_simple_de_prueba.id)
             assert db_obj_updated is not None
             assert db_obj_updated.nombre == update_schema.nombre

    def test_update_material_simple_not_found(self, admin_client: TestClient):
        update_payload = MaterialSimpleUpdate(nombre="Test").model_dump(mode='json', exclude_unset=True)
        response = admin_client.put(f"{MAT_SIMP_ENDPOINT}/999999", json=update_payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_material_simple_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_simp_payload(suffix)
        response_create = admin_client.post(MAT_SIMP_ENDPOINT, json=payload)
        assert response_create.status_code == status.HTTP_201_CREATED
        created_id = response_create.json()["id"]
        response_delete = admin_client.delete(f"{MAT_SIMP_ENDPOINT}/{created_id}")
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT

        try:
            with TestingSessionLocal() as verification_db:
                deleted_obj = verification_db.get(MaterialSimple, created_id)
                assert deleted_obj is None, f"MaterialSimple ID {created_id} aún encontrado en BD post-delete."
                logger.info(f"Test 'test_delete_material_simple_success': MaterialSimple ID {created_id} verificado como eliminado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_delete_material_simple_success: {e}")

    def test_delete_material_simple_not_found(self, admin_client: TestClient):
        response = admin_client.delete(f"{MAT_SIMP_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # @pytest.mark.skip(reason="PENDIENTE: Implementar cuando FormulaItem o LineaProformaMaterial use MaterialSimple.")
    # def test_delete_material_simple_conflict(self, admin_client: TestClient, ...)

    def test_adjust_stock_simple_success(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        mat_id = material_simple_de_prueba.id
        initial_stock = material_simple_de_prueba.stock_actual or Decimal("0.0")
        adjust_payload_add_schema = StockAdjustRequest(change_amount=Decimal("250"))
        adjust_payload_add_dict = adjust_payload_add_schema.model_dump(mode='json')
        response_add = admin_client.post(f"{MAT_SIMP_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload_add_dict)
        assert response_add.status_code == status.HTTP_200_OK
        expected_stock_add = initial_stock + adjust_payload_add_schema.change_amount
        assert Decimal(response_add.json()["stock_actual"]) == expected_stock_add

        try:
            with TestingSessionLocal() as verification_db_add:
                db_obj_add = verification_db_add.get(MaterialSimple, mat_id)
                assert db_obj_add is not None
                assert db_obj_add.stock_actual == pytest.approx(expected_stock_add)
                logger.info(f"Test 'test_adjust_stock_simple_success' (add): Stock verificado en BD para ID {mat_id}.")
        except Exception as e:
            pytest.fail(f"Error verificación BD (add) en test_adjust_stock_simple_success: {e}")

    def test_adjust_stock_simple_negative_result(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        mat_id = material_simple_de_prueba.id
        adjust_payload = StockAdjustRequest(change_amount=Decimal("-100000")).model_dump(mode='json')
        response = admin_client.post(f"{MAT_SIMP_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_adjust_stock_simple_forbidden(self, vendedor_client: TestClient, material_simple_de_prueba: MaterialSimple):
        mat_id = material_simple_de_prueba.id
        adjust_payload = StockAdjustRequest(change_amount=Decimal("10")).model_dump(mode='json')
        response = vendedor_client.post(f"{MAT_SIMP_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN


# ==============================================================
# --- Tests para Endpoints de Stock Item Dimensional (Base) ---
# ==============================================================
class TestStockItemDimensionalAPI:

    def test_create_stock_item_success(self, admin_client: TestClient, db_session: Session, material_dimensional_de_prueba: MaterialDimensional):
        payload_schema = StockItemDimensionalCreate(
            material_dimensional_id=material_dimensional_de_prueba.id,
            longitud_actual=Decimal("3000.0"),
            ancho_actual=Decimal("1500.0"),
            ubicacion="Rack-A1"
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["material_dimensional_id"] == material_dimensional_de_prueba.id
        assert Decimal(data["longitud_actual"]) == payload_schema.longitud_actual
        assert data["estado"] == "DISPONIBLE"
        item_id = data["id"]

        db_session.close()
        with TestingSessionLocal() as verification_db:
            db_obj = verification_db.get(StockItemDimensional, item_id)
            assert db_obj is not None
            assert db_obj.material_dimensional_id == payload_schema.material_dimensional_id
            assert db_obj.longitud_actual == payload_schema.longitud_actual


    def test_create_stock_item_invalid_foreign_key(self, admin_client: TestClient):
        payload_schema = StockItemDimensionalCreate(
            material_dimensional_id=999999,
            longitud_actual=Decimal("1000"),
            ancho_actual=Decimal("500")
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_404_NOT_FOUND # El servicio valida FK

    def test_list_stock_items_success(self, admin_client: TestClient, stock_item_dimensional_de_prueba: StockItemDimensional):
        response = admin_client.get(STOCK_ITEM_DIM_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert any(item["id"] == stock_item_dimensional_de_prueba.id for item in data)

    def test_list_stock_items_filtered(self, admin_client: TestClient, db_session: Session, material_dimensional_de_prueba: MaterialDimensional):
        # Crear items
        item1_schema = StockItemDimensionalCreate(material_dimensional_id=material_dimensional_de_prueba.id, longitud_actual=1000, ancho_actual=100, estado="DISPONIBLE")
        item2_schema = StockItemDimensionalCreate(material_dimensional_id=material_dimensional_de_prueba.id, longitud_actual=2000, ancho_actual=200, estado="RESERVADO")
        item3_schema = StockItemDimensionalCreate(material_dimensional_id=material_dimensional_de_prueba.id, longitud_actual=3000, ancho_actual=300, estado="DISPONIBLE")
        resp1 = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=item1_schema.model_dump(mode='json'))
        resp2 = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=item2_schema.model_dump(mode='json'))
        resp3 = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=item3_schema.model_dump(mode='json'))
        assert resp1.status_code == status.HTTP_201_CREATED
        assert resp2.status_code == status.HTTP_201_CREATED
        assert resp3.status_code == status.HTTP_201_CREATED
        id1 = resp1.json()["id"]; id3 = resp3.json()["id"]
        # Filtrar
        params = {"material_dimensional_id": material_dimensional_de_prueba.id, "estado": "DISPONIBLE"}
        response = admin_client.get(STOCK_ITEM_DIM_ENDPOINT, params=params)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        ids_respuesta = {item["id"] for item in data}
        assert id1 in ids_respuesta
        assert id3 in ids_respuesta
        assert all(item["estado"] == "DISPONIBLE" for item in data)

    def test_get_stock_item_success(self, admin_client: TestClient, stock_item_dimensional_de_prueba: StockItemDimensional):
        item_id = stock_item_dimensional_de_prueba.id
        response = admin_client.get(f"{STOCK_ITEM_DIM_ENDPOINT}/{item_id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == item_id
        assert data["material_dimensional_id"] == stock_item_dimensional_de_prueba.material_dimensional_id

    def test_get_stock_item_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{STOCK_ITEM_DIM_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_material_dimensional_conflict(self, admin_client: TestClient, stock_item_dimensional_de_prueba: StockItemDimensional):
        """Prueba eliminar un MaterialDimensional con StockItems asociados (409)."""
        material_id = stock_item_dimensional_de_prueba.material_dimensional_id
        logger.info(f"Intentando borrar MaterialDimensional ID {material_id} que tiene StockItem ID {stock_item_dimensional_de_prueba.id} asociado.")
        response = admin_client.delete(f"{MAT_DIM_ENDPOINT}/{material_id}")
        assert response.status_code == status.HTTP_409_CONFLICT
        assert "está en uso (stock existente)" in response.json()["detail"]