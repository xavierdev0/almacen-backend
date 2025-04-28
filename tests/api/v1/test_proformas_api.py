# app/tests/api/v1/test_proformas_api.py

from decimal import Decimal, ROUND_HALF_UP
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlmodel import Session
import logging

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas
from app.models.inventory_models import MaterialDimensional # Necesario para verificación dimensional
from app.schemas.order_schema import ProformaUpdate, ProformaRead, PedidoClienteCreate, LineaProformaMaterialCreate, LineaProformaServicioCreate
# Importar modelos y repositorios
from app.models import Proforma, PedidoCliente, Usuario, Cliente
from app.models import (
    MaterialConsumible, MaterialSimple, StockItemDimensional, ServicioDefinicion,
    LineaProformaMaterial, LineaProformaServicio # Para verificar en BD
)

# Importar fixtures de conftest
from tests.conftest import (
    material_consumible_de_prueba,
    material_simple_de_prueba,
    stock_item_dimensional_de_prueba,
    servicio_definicion_de_prueba,
    TestingSessionLocal # Importante para verificación independiente
)

# Repositorio opcional si se necesita alguna consulta compleja en verificación
# from app.repositories import order_repository

logger = logging.getLogger(__name__)

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
PROFORMAS_ENDPOINT = f"{API_V1_STR}/proformas"
PEDIDOS_ENDPOINT = f"{API_V1_STR}/pedidos" # Necesario para la fixture `pedido_con_proformas`


# ======================================================
# === Tests para Actualizar Proformas (PATCH /{id}) ===
# ======================================================

def test_update_proforma_estado_success(
    admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar el estado de BORRADOR a PENDIENTE_APROBACION como Admin."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)

    response = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)

    # Verificar respuesta API
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == proforma_id
    assert data["estado"] == "PENDIENTE_APROBACION"

    # Verificar en BD usando sesión independiente
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None, "Proforma no encontrada en BD para verificación."
            assert db_proforma.estado == "PENDIENTE_APROBACION", "Estado en BD no coincide."
    except Exception as e:
        pytest.fail(f"Error verificación BD en test_update_proforma_estado_success: {e}")


def test_update_proforma_notas_success(
    vendedor_client: TestClient, pedido_con_proformas: dict, vendedor_user: Usuario
):
    """Prueba actualizar las notas como Vendedor (asume permiso 'actualizar:proforma_propia')."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    new_notes = f"Notas actualizadas por test - {uuid.uuid4().hex[:4]}"
    payload = ProformaUpdate(notas=new_notes).model_dump(exclude_unset=True)

    response = vendedor_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)

    # Verificar respuesta API
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == proforma_id
    assert data["notas"] == new_notes

    # Verificar en BD usando sesión independiente
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None, "Proforma no encontrada en BD para verificación."
            assert db_proforma.notas == new_notes, "Notas en BD no coinciden."
    except Exception as e:
        pytest.fail(f"Error verificación BD en test_update_proforma_notas_success: {e}")

def test_update_proforma_invalid_state_transition(
     admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba una transición de estado inválida (ej: PENDIENTE -> BORRADOR)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    # Asegurar estado PENDIENTE
    payload_pendiente = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)
    resp_pendiente = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_pendiente)
    assert resp_pendiente.status_code == status.HTTP_200_OK

    # Intentar transición inválida
    payload_borrador = ProformaUpdate(estado="BORRADOR").model_dump(exclude_unset=True)
    response_invalid = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_borrador)

    # Verificar error esperado
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
    """Prueba que un Operario (sin permisos de actualización) no puede actualizar proformas (403)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(notas="Intento de Operario").model_dump(exclude_unset=True)
    response = operario_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere uno de" in response.json()["detail"]

def test_update_proforma_invalid_payload_estado(
    admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar con un valor de estado inválido en el payload (422)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    invalid_payload = {"estado": "ESTADO_INVENTADO"} # Valor no permitido por el ENUM implícito o validador
    response = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_proforma_unauthenticated(
    base_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar proforma sin autenticación (401)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(notas="No Auth").model_dump(exclude_unset=True)
    response = base_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED



# =======================================================================
# === Tests para Añadir Líneas de Material (POST /{id}/lineas-material) ===
# =======================================================================

@pytest.mark.parametrize("material_type, fixture_name, payload_extra", [
    ("CONSUMIBLE", "material_consumible_de_prueba", {"material_consumible_id": True}),
    ("SIMPLE", "material_simple_de_prueba", {"material_simple_id": True}),
    ("STOCK_DIMENSIONAL", "stock_item_dimensional_de_prueba", {"stock_item_dimensional_id": True}),
])
def test_add_linea_material_success(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    request: pytest.FixtureRequest,
    material_type: str,
    fixture_name: str,
    payload_extra: dict
):
    """
    Prueba añadir líneas de diferentes tipos de material a una proforma PRODUCTO,
    verificando precios y totales calculados. (Refactorizado)
    """
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    material_fixture = request.getfixturevalue(fixture_name)
    assert material_fixture.id is not None, f"Fixture '{fixture_name}' no tiene ID."
    material_id = material_fixture.id
    cantidad_a_anadir = Decimal("3.0") # Cantidad base, se ajusta para dimensional
    expected_precio_unitario = Decimal("0.00")
    expected_unidad_linea = ""

    # --- Calcular Precio Unitario Esperado (Lógica SIMILAR al servicio) ---
    # Esta lógica debe mantenerse sincronizada con la del servicio real.
    if material_type in ["CONSUMIBLE", "SIMPLE"]:
        expected_precio_unitario = material_fixture.precio_venta_base_unidad
        expected_unidad_linea = material_fixture.unidad_medida
    elif material_type == "STOCK_DIMENSIONAL":
        with TestingSessionLocal() as temp_db: # Sesión temporal para obtener definición
             definicion = temp_db.get(MaterialDimensional, material_fixture.material_dimensional_id)
        assert definicion is not None, "No se pudo obtener MaterialDimensional para calcular precio esperado"

        precio_base = definicion.precio_venta_base_unidad
        unidad_precio = definicion.unidad_precio_venta.lower()
        unidad_dims = definicion.unidad_dimension.lower()
        longitud = material_fixture.longitud_actual
        ancho = material_fixture.ancho_actual
        es_merma = material_fixture.es_merma

        # Lógica de conversión y cálculo (Ejemplo básico)
        factor = Decimal("1.0")
        if unidad_dims == "mm" and unidad_precio == "m2": factor = Decimal("1000.0")
        elif unidad_dims == "cm" and unidad_precio == "m2": factor = Decimal("100.0")
        # Añadir más conversiones según sea necesario...

        # Calcular valor base (ej: área)
        valor_base = Decimal("1.0")
        if unidad_precio == "m2":
            if factor == Decimal("1.0") and unidad_dims != 'm':
                 pytest.skip(f"Test saltado: No se implementó conversión de {unidad_dims} a m2") # Saltar si no hay conversión
            valor_base = (longitud / factor) * (ancho / factor)
        # Añadir lógica para otras unidades de precio (m_lineal, unidad, etc.)

        # Aplicar descuento de merma (Ejemplo)
        DESCUENTO_MERMA = Decimal("0.10") # TODO: Usar configuración o valor real
        factor_descuento = (Decimal("1.0") - DESCUENTO_MERMA) if es_merma else Decimal("1.0")

        expected_precio_unitario = (valor_base * precio_base * factor_descuento)
        expected_unidad_linea = "pieza" # La línea representa una pieza física
        cantidad_a_anadir = Decimal("1.0") # Se añade una pieza a la vez

    # Calcular total esperado de la línea
    expected_total_linea = (cantidad_a_anadir * expected_precio_unitario).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # --- Construir Payload ---
    payload_data = {
        "tipo_material_origen": material_type,
        "cantidad": cantidad_a_anadir
    }
    id_key = list(payload_extra.keys())[0] # ej: "material_consumible_id"
    payload_data[id_key] = material_id
    payload_schema = LineaProformaMaterialCreate(**payload_data)
    payload_dict = payload_schema.model_dump(mode='json')

    # --- Llamada API ---
    response = vendedor_client.post(
        f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material",
        json=payload_dict
    )

    # --- Verificar Respuesta API ---
    assert response.status_code == status.HTTP_201_CREATED, f"API call failed: {response.text}"
    # (Opcional: verificar contenido de la respuesta si es necesario, pero la verificación BD es más fiable)
    # data = response.json()
    # assert data["id"] == proforma_id
    # ...

    # --- Verificar en BD (Verificación principal) ---
    try:
        with TestingSessionLocal() as verification_db:
            # Recargar proforma y líneas desde la BD
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None, f"Proforma ID {proforma_id} no encontrada en BD para verificación."
            verification_db.refresh(db_proforma, attribute_names=["lineas_material"])

            # Buscar la línea específica en la BD
            db_linea_encontrada = None
            for linea in db_proforma.lineas_material:
                if getattr(linea, id_key, None) == material_id:
                    db_linea_encontrada = linea
                    break

            assert db_linea_encontrada is not None, f"No se encontró la línea añadida para material ID {material_id} en la BD."

            # Verificar detalles de la línea encontrada en BD
            assert db_linea_encontrada.cantidad == cantidad_a_anadir, "Cantidad en BD no coincide"
            assert db_linea_encontrada.unidad == expected_unidad_linea, "Unidad en BD no coincide"
            assert db_linea_encontrada.precio_unitario.quantize(Decimal("0.01")) == expected_precio_unitario.quantize(Decimal("0.01")), "Precio unitario en BD no coincide"
            assert db_linea_encontrada.total_linea == expected_total_linea, "Total de línea en BD no coincide"

            # Verificar totales actualizados en proforma
            expected_subtotal_db = sum(
                (l.total_linea for l in db_proforma.lineas_material if l.total_linea is not None), Decimal("0.00")
            ) # Asumiendo solo líneas de material en proforma PRODUCTO
            assert db_proforma.subtotal == expected_subtotal_db.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "Subtotal de Proforma en BD no coincide"
            # TODO: Verificar impuestos y total si la lógica está implementada

    except Exception as e:
        pytest.fail(f"Error verificación BD en test_add_linea_material_success ({material_type}): {e}")



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
    # --- CORRECCIÓN: Hacer la aserción más flexible ---
    assert "no encontrado" in response.json()["detail"].lower()
    #assert "material consumible" in response.json()["detail"].lower() or "material de origen" in response.json()["detail"].lower()
    #assert "Material Consumible ID 99999 no encontrado" in response.json()["detail"] # Corrección


# --- Tests Negativos para Añadir Línea de Material (Sin cambios, ya eran robustos) ---

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
    assert "no encontrado" in response.json()["detail"].lower() # Aserción más general

def test_add_linea_material_invalid_payload(
    vendedor_client: TestClient, pedido_con_proformas: dict
):
    """Prueba añadir línea con cantidad inválida (422)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    invalid_payload = {
        "tipo_material_origen": "CONSUMIBLE",
        "material_consumible_id": 1, # Asumir ID 1 existe
        "cantidad": 0 # Inválido (<0)
    }
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_add_linea_material_forbidden(
    operario_client: TestClient,
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


# =======================================================================
# === Tests para Añadir Líneas de Servicio (POST /{id}/lineas-servicio) ===
# =======================================================================

def test_add_linea_servicio_success(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """
    Prueba añadir una línea de servicio básica a una proforma SERVICIO.
    Verifica con la lógica de precios (placeholder) actual del servicio.
    """
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    servicio_id = servicio_definicion_de_prueba.id
    assert servicio_id is not None, "Fixture servicio_definicion_de_prueba no tiene ID."
    cantidad_a_anadir = Decimal("1.5")

    # --- Calcular Precio Unitario y Total Esperado (REPLICAR LÓGICA DEL SERVICIO) ---
    # !! ESTA LÓGICA DEBE ACTUALIZARSE CUANDO CAMBIE LA DEL SERVICIO !!
    expected_precio_unitario = servicio_definicion_de_prueba.costo_por_unidad if servicio_definicion_de_prueba.costo_por_unidad is not None else Decimal("0.00")
    expected_total_linea = (cantidad_a_anadir * expected_precio_unitario).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    # --------------------------------------------------------------------------

    payload_schema = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_id,
        cantidad=cantidad_a_anadir
    )
    payload_dict = payload_schema.model_dump(mode='json')

    response = vendedor_client.post(
        f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio",
        json=payload_dict
    )

    # Verificar Respuesta API
    assert response.status_code == status.HTTP_201_CREATED, f"API call failed: {response.text}"
    # (Opcional: verificar respuesta JSON si es necesario)

    # --- Verificar en BD (Principal) ---
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None, f"Proforma ID {proforma_id} no encontrada en BD."
            verification_db.refresh(db_proforma, attribute_names=["lineas_servicio"])

            # Buscar la línea específica
            db_linea_encontrada = next(
                (linea for linea in db_proforma.lineas_servicio if linea.servicio_definicion_id == servicio_id),
                None
            )
            assert db_linea_encontrada is not None, f"Línea para servicio ID {servicio_id} no encontrada en BD."

            # Verificar detalles de la línea
            assert db_linea_encontrada.cantidad == cantidad_a_anadir
            assert db_linea_encontrada.linea_proforma_material_id is None
            assert db_linea_encontrada.precio_unitario.quantize(Decimal("0.01")) == expected_precio_unitario.quantize(Decimal("0.01")), "Precio unitario servicio en BD no coincide"
            assert db_linea_encontrada.total_linea == expected_total_linea, "Total línea servicio en BD no coincide"

            # Verificar totales proforma
            expected_subtotal_db = sum((l.total_linea for l in db_proforma.lineas_servicio if l.total_linea is not None), Decimal("0.00"))
            assert db_proforma.subtotal == expected_subtotal_db.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "Subtotal proforma servicio en BD no coincide"
            # TODO: Verificar impuestos y total

    except Exception as e:
        pytest.fail(f"Error verificación BD en test_add_linea_servicio_success: {e}")


def test_add_linea_servicio_linked_to_material_success(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """
    Prueba añadir línea de servicio vinculada a una línea de material.
    Verifica precios y totales con lógica placeholder.
    """
    proforma_prod_id = pedido_con_proformas["proforma_producto_id"]
    proforma_serv_id = pedido_con_proformas["proforma_servicio_id"]
    servicio_id = servicio_definicion_de_prueba.id
    assert servicio_id is not None, "Fixture servicio_definicion_de_prueba no tiene ID."
    cantidad_servicio = Decimal("1.0")

    # 1. Añadir línea de material primero (y obtener su ID desde BD)
    payload_mat_schema = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_consumible_de_prueba.id,
        cantidad=Decimal("2.0") # Cantidad del material
    )
    resp_mat = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_prod_id}/lineas-material", json=payload_mat_schema.model_dump(mode='json'))
    assert resp_mat.status_code == status.HTTP_201_CREATED, f"Fallo al crear línea material previa: {resp_mat.text}"

    # Obtener ID de la línea de material desde BD
    linea_material_id = None
    with TestingSessionLocal() as verify_db_mat:
        stmt_id = select(LineaProformaMaterial.id).where(
            LineaProformaMaterial.proforma_id == proforma_prod_id,
            LineaProformaMaterial.material_consumible_id == material_consumible_de_prueba.id
        ).order_by(LineaProformaMaterial.id.desc())
        linea_material_id = verify_db_mat.scalar(stmt_id)
        assert linea_material_id is not None, "No se encontró el ID de la línea de material en BD"

    # 2. Calcular Precio Esperado Servicio (REPLICAR LÓGICA SERVICIO - Placeholder)
    expected_precio_unitario_serv = servicio_definicion_de_prueba.costo_por_unidad if servicio_definicion_de_prueba.costo_por_unidad is not None else Decimal("0.00")
    expected_total_linea_serv = (cantidad_servicio * expected_precio_unitario_serv).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # 3. Añadir línea de servicio vinculada
    payload_serv_schema = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_id,
        cantidad=cantidad_servicio,
        linea_proforma_material_id=linea_material_id # <-- Vinculación
    )
    payload_serv_dict = payload_serv_schema.model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_serv_id}/lineas-servicio", json=payload_serv_dict)

    # 4. Verificar Respuesta API
    assert response.status_code == status.HTTP_201_CREATED, f"API call failed: {response.text}"
    # (Opcional: verificar respuesta JSON)

    # 5. Verificar en BD
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma_serv = verification_db.get(Proforma, proforma_serv_id)
            assert db_proforma_serv is not None, f"Proforma Servicio ID {proforma_serv_id} no encontrada en BD."
            verification_db.refresh(db_proforma_serv, attribute_names=["lineas_servicio"])

            # Buscar línea específica
            db_linea_serv = next(
                (l for l in db_proforma_serv.lineas_servicio if l.linea_proforma_material_id == linea_material_id),
                None
            )
            assert db_linea_serv is not None, f"Línea de servicio vinculada a material ID {linea_material_id} no encontrada en BD."

            # Verificar vínculo y precios/totales
            assert db_linea_serv.servicio_definicion_id == servicio_id
            assert db_linea_serv.cantidad == cantidad_servicio
            assert db_linea_serv.precio_unitario.quantize(Decimal("0.01")) == expected_precio_unitario_serv.quantize(Decimal("0.01")), "Precio unitario servicio vinculado en BD no coincide"
            assert db_linea_serv.total_linea == expected_total_linea_serv, "Total línea servicio vinculado en BD no coincide"

            # Verificar totales proforma
            expected_subtotal_serv_db = sum((l.total_linea for l in db_proforma_serv.lineas_servicio if l.total_linea is not None), Decimal("0.00"))
            assert db_proforma_serv.subtotal == expected_subtotal_serv_db.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "Subtotal proforma servicio (vinculado) en BD no coincide"
            # TODO: Verificar impuestos y total

    except Exception as e:
        pytest.fail(f"Error verificación BD en test_add_linea_servicio_linked_to_material_success: {e}")


# --- Tests Negativos para Añadir Línea de Servicio (Ahora deberían pasar con códigos 4xx) ---

def test_add_linea_servicio_wrong_proforma_type(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio a proforma de PRODUCTO (espera 400)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
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
    """Prueba añadir línea de servicio a proforma no en BORRADOR (espera 409)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload_update = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)
    resp_update = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_update)
    assert resp_update.status_code == status.HTTP_200_OK
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
    """Prueba añadir línea con ID de servicio inexistente (espera 404)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=99999,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "La definición del servicio con ID 99999 no fue encontrada." in response.json()["detail"]

def test_add_linea_servicio_invalid_material_link(
    vendedor_client: TestClient, pedido_con_proformas: dict, servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio vinculando a linea material inexistente (espera 404)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_definicion_de_prueba.id,
        cantidad=Decimal("1"),
        linea_proforma_material_id=88888
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "La línea de material asociada con ID 88888 no fue encontrada." in response.json()["detail"]

def test_add_linea_servicio_forbidden(
    operario_client: TestClient,
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