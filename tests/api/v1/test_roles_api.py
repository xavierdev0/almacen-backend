# tests/api/v1/test_roles_api.py
import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
import logging # Asegurar import
import uuid

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas
from app.schemas.rol_permiso_schema import RolCreate, RolRead, RolUpdate, RolReadWithPermissions
# Importar modelos y repositorios
from app.models import Rol, Usuario, Permiso # Importar Permiso
from app.repositories import rol_repository, usuario_repository # Necesario para verificaciones
# Importar TestingSessionLocal
from tests.conftest import TestingSessionLocal

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
ROLES_ENDPOINT = f"{API_V1_STR}/roles"
logger = logging.getLogger(__name__) # Añadir logger

# --- Tests para Listar Roles (GET /roles) ---
# (Sin cambios, no modifican DB)
def test_list_roles_unauthenticated(base_client: TestClient):
    response = base_client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_list_roles_forbidden_non_admin(vendedor_client: TestClient):
    response = vendedor_client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:rol'." in response.json()["detail"]

def test_list_roles_success_admin(admin_client: TestClient, db_session: Session):
    response = admin_client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 5
    role_names = {role["nombre"] for role in data}
    assert "Administrador" in role_names
    assert "Vendedor" in role_names
    for role in data:
        assert "id" in role
        assert "nombre" in role

# --- Tests para Crear Roles (POST /roles) ---
def test_create_role_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la creación exitosa de un rol como admin (Refactorizado)."""
    role_name = f"RolCreadoEnTest_{uuid.uuid4().hex[:6]}"
    role_data = RolCreate(nombre=role_name, descripcion="Descripción test")
    response = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["nombre"] == role_data.nombre
    assert data["descripcion"] == role_data.descripcion
    assert "id" in data
    new_role_id = data["id"]

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_create_role_success_admin': Verificando rol ID {new_role_id} con nueva sesión.")
             db_rol = rol_repository.get_rol(db=verification_db, rol_id=new_role_id)
             assert db_rol is not None, f"Rol ID {new_role_id} no encontrado en BD post-creación."
             assert db_rol.nombre == role_data.nombre
             assert db_rol.descripcion == role_data.descripcion
             logger.info(f"Test 'test_create_role_success_admin': Rol ID {new_role_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_create_role_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests create duplicate, invalid, forbidden sin cambios) ...
def test_create_role_duplicate_name(admin_client: TestClient, db_session: Session):
    """Prueba que crear un rol con nombre duplicado falle (409)."""
    role_data = RolCreate(nombre="RolDuplicadoParaTest", descripcion="Test 409")
    response1 = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response1.status_code == status.HTTP_201_CREATED
    response2 = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response2.status_code == status.HTTP_409_CONFLICT
    assert f"El rol '{role_data.nombre}' ya existe" in response2.json()["detail"]

def test_create_role_invalid_data(admin_client: TestClient):
    """Prueba que crear un rol con datos inválidos (ej: nombre muy largo) falle (422)."""
    invalid_role_data = {"nombre": "a" * 150, "descripcion": "Test"} # Asumiendo max_length=100 para nombre
    response = admin_client.post(ROLES_ENDPOINT, json=invalid_role_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_create_role_forbidden_non_admin(vendedor_client: TestClient):
    """Prueba que crear un rol como no-admin falle (403)."""
    role_data = RolCreate(nombre="RolNoAdminTest", descripcion="No debería crearse")
    response = vendedor_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'crear:rol'" in response.json()["detail"]

# --- Tests para Obtener Rol por ID (GET /roles/{rol_id}) ---
# (Sin cambios)
def test_get_role_by_id_success(admin_client: TestClient, vendedor_role_id: int):
    """Prueba obtener un rol existente por ID como admin."""
    response = admin_client.get(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == vendedor_role_id
    assert data["nombre"] == "Vendedor"
    assert "permisos" in data
    assert isinstance(data["permisos"], list)
    perm_keys = {f"{p['nombre_accion']}:{p['nombre_recurso']}" for p in data["permisos"]}
    assert "leer:cliente" in perm_keys

def test_get_role_not_found(admin_client: TestClient):
    """Prueba obtener un rol con ID inexistente (404)."""
    response = admin_client.get(f"{ROLES_ENDPOINT}/99999") # ID que no existe
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_get_role_forbidden_non_admin(vendedor_client: TestClient, vendedor_role_id: int):
    """Prueba que obtener un rol por ID como no-admin falle (403)."""
    response = vendedor_client.get(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:rol'" in response.json()["detail"]


# --- Tests para Eliminar Roles (DELETE /roles/{rol_id}) ---

def test_delete_role_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la eliminación exitosa de un rol NO ASIGNADO como admin (Refactorizado)."""
    role_name_to_delete = f"RolParaBorrar_{uuid.uuid4()}"
    temp_role_data = RolCreate(nombre=role_name_to_delete, descripcion="Se eliminará")
    # Crear rol directamente en BD para este test, asegurando que no esté asignado
    db_rol = rol_repository.create_rol(db=db_session, rol_in=temp_role_data)
    role_id_to_delete = db_rol.id
    db_session.commit() # Asegurar que la creación esté confirmada

    response = admin_client.delete(f"{ROLES_ENDPOINT}/{role_id_to_delete}")

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_delete_role_success_admin': Verificando rol ID {role_id_to_delete} con nueva sesión.")
            deleted_rol = rol_repository.get_rol(db=verification_db, rol_id=role_id_to_delete)
            assert deleted_rol is None, f"Rol ID {role_id_to_delete} aún encontrado en BD post-delete."
            logger.info(f"Test 'test_delete_role_success_admin': Rol ID {role_id_to_delete} verificado como eliminado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_delete_role_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests delete not_found, conflict, forbidden sin cambios) ...
def test_delete_role_not_found_admin(admin_client: TestClient):
    """Prueba eliminar un rol con ID inexistente (404)."""
    non_existent_id = 99998
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{non_existent_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_role_conflict_assigned_admin(
    admin_client: TestClient, db_session: Session, vendedor_role_id: int, vendedor_user: Usuario
):
    """Prueba eliminar un rol ASIGNADO a un usuario (409 Conflict)."""
    user_in_db = usuario_repository.get_usuario(db=db_session, user_id=vendedor_user.id)
    assert user_in_db is not None
    roles_usuario = {rol.id for rol in user_in_db.roles}
    assert vendedor_role_id in roles_usuario
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "No se puede eliminar el rol" in response.json()["detail"]

def test_delete_role_forbidden_non_admin(
    vendedor_client: TestClient, vendedor_role_id: int
):
    """Prueba que eliminar un rol como no-admin falle (403)."""
    response = vendedor_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'eliminar:rol'" in response.json()["detail"]


# --- Tests para Actualizar Roles (PUT /roles/{rol_id}) ---

def test_update_role_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la actualización exitosa de un rol como admin (Refactorizado)."""
    rol_original = RolCreate(nombre=f"RolParaActualizar_{uuid.uuid4().hex[:6]}", descripcion="Descripción Original")
    # Crear directamente en DB para asegurar que existe
    db_rol_original = rol_repository.create_rol(db=db_session, rol_in=rol_original)
    role_id_to_update = db_rol_original.id
    db_session.commit()

    update_data = RolUpdate(nombre="Rol Actualizado Test", descripcion="Nueva Descripción")

    response_update = admin_client.put(
        f"{ROLES_ENDPOINT}/{role_id_to_update}",
        json=update_data.model_dump(exclude_unset=True)
    )

    assert response_update.status_code == status.HTTP_200_OK
    data = response_update.json()
    assert data["id"] == role_id_to_update
    assert data["nombre"] == update_data.nombre
    assert data["descripcion"] == update_data.descripcion

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_update_role_success_admin': Verificando rol ID {role_id_to_update} con nueva sesión.")
             db_rol = rol_repository.get_rol(db=verification_db, rol_id=role_id_to_update)
             assert db_rol is not None, f"Rol ID {role_id_to_update} no encontrado en BD post-update."
             assert db_rol.nombre == update_data.nombre
             assert db_rol.descripcion == update_data.descripcion
             logger.info(f"Test 'test_update_role_success_admin': Rol ID {role_id_to_update} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_update_role_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests update conflict, not_found, invalid, forbidden sin cambios) ...
def test_update_role_conflict_name_admin(admin_client: TestClient, db_session: Session, vendedor_role_id: int):
    """Prueba que actualizar a un nombre de rol existente falle (409)."""
    rol_original = RolCreate(nombre=f"RolConflicto_{uuid.uuid4().hex[:6]}", descripcion="Original")
    response_create = admin_client.post(ROLES_ENDPOINT, json=rol_original.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    role_id_to_update = response_create.json()["id"]
    update_data = RolUpdate(nombre="Vendedor")
    response_update = admin_client.put(f"{ROLES_ENDPOINT}/{role_id_to_update}",json=update_data.model_dump(exclude_unset=True))
    assert response_update.status_code == status.HTTP_409_CONFLICT
    assert "conflicto" in response_update.json()["detail"].lower() or "ya está en uso" in response_update.json()["detail"].lower()
    # Verificar que no cambió
    with TestingSessionLocal() as vdb:
        db_rol = vdb.get(Rol, role_id_to_update)
        assert db_rol is not None
        assert db_rol.nombre == rol_original.nombre


def test_update_role_not_found_admin(admin_client: TestClient):
    """Prueba actualizar un rol con ID inexistente (404)."""
    non_existent_id = 99997
    update_data = RolUpdate(nombre="Nombre No Importa")
    response = admin_client.put(f"{ROLES_ENDPOINT}/{non_existent_id}",json=update_data.model_dump(exclude_unset=True))
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_role_invalid_data_admin(admin_client: TestClient, db_session: Session):
    """Prueba actualizar un rol con datos inválidos (ej: nombre muy largo) falle (422)."""
    rol_original = RolCreate(nombre=f"RolValidacion_{uuid.uuid4().hex[:6]}", descripcion="Valido")
    response_create = admin_client.post(ROLES_ENDPOINT, json=rol_original.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    role_id_to_update = response_create.json()["id"]
    invalid_update_data = {"nombre": "a" * 150}
    response = admin_client.put(f"{ROLES_ENDPOINT}/{role_id_to_update}",json=invalid_update_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_role_forbidden_non_admin(vendedor_client: TestClient, vendedor_role_id: int):
    """Prueba que actualizar un rol como no-admin falle (403)."""
    update_data = RolUpdate(descripcion="Intento No Autorizado")
    response = vendedor_client.put(f"{ROLES_ENDPOINT}/{vendedor_role_id}",json=update_data.model_dump(exclude_unset=True))
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'actualizar:rol'" in response.json()["detail"]


# --- Tests para Asignar Permisos a Roles (POST /roles/{rol_id}/permisos/{permiso_id}) ---

def test_assign_permission_to_role_success_admin(
    admin_client: TestClient,
    db_session: Session, # No se usará para verificación post-API
    permiso_leer_cliente_id: int
):
    """
    Prueba asignar exitosamente un permiso a un NUEVO rol como admin (Refactorizado).
    """
    temp_role_data = RolCreate(nombre=f"RolTempPermiso_{uuid.uuid4().hex[:6]}", descripcion="Rol para test de asignación")
    response_create = admin_client.post(ROLES_ENDPOINT, json=temp_role_data.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    new_role_id = response_create.json()["id"]

    response_assign = admin_client.post(
        f"{ROLES_ENDPOINT}/{new_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    assert response_assign.status_code == status.HTTP_200_OK
    data = response_assign.json()
    assert data["id"] == new_role_id
    permiso_asignado_encontrado = any(p["id"] == permiso_leer_cliente_id for p in data.get("permisos", []))
    assert permiso_asignado_encontrado, f"El permiso ID {permiso_leer_cliente_id} no se encontró en la respuesta."

    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_assign_permission_to_role_success_admin': Verificando rol ID {new_role_id} con nueva sesión.")
             # Usar get_rol_with_permissions para cargar la relación
             db_rol = rol_repository.get_rol_with_permissions(db=verification_db, rol_id=new_role_id)
             assert db_rol is not None, "El rol temporal no se encontró en la BD para verificación."
             permiso_ids_en_db = {p.id for p in db_rol.permisos}
             assert permiso_leer_cliente_id in permiso_ids_en_db, "El permiso no se encontró en la relación del rol en la BD."
             logger.info(f"Test 'test_assign_permission_to_role_success_admin': Permiso asignado a rol ID {new_role_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_assign_permission_to_role_success_admin: {e}")


# ... (tests asignar permiso ya asignado, rol no encontrado, permiso no encontrado, forbidden sin cambios) ...
def test_assign_permission_already_assigned_admin(
    admin_client: TestClient,
    db_session: Session,
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba que asignar un permiso ya asignado falle (409)."""
    assign_response = admin_client.post( f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT]
    response = admin_client.post(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "ya está asignado" in response.json()["detail"]

def test_assign_permission_role_not_found_admin(
    admin_client: TestClient,
    permiso_leer_cliente_id: int
):
    """Prueba asignar permiso a un rol inexistente (404)."""
    non_existent_role_id = 99996
    response = admin_client.post(f"{ROLES_ENDPOINT}/{non_existent_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_assign_permission_permission_not_found_admin(
    admin_client: TestClient,
    vendedor_role_id: int
):
    """Prueba asignar un permiso inexistente a un rol válido (404)."""
    non_existent_perm_id = 99995
    response = admin_client.post(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{non_existent_perm_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_assign_permission_forbidden_non_admin(
    vendedor_client: TestClient,
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba que un no-admin no puede asignar permisos (403)."""
    response = vendedor_client.post(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'asignar:permiso_rol'" in response.json()["detail"]


# --- Tests para Quitar Permisos de Roles (DELETE /roles/{rol_id}/permisos/{permiso_id}) ---

def test_remove_permission_from_role_success_admin(
    admin_client: TestClient,
    db_session: Session, # No se usará para verificación post-API
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba quitar exitosamente un permiso asignado a un rol como admin (Refactorizado)."""
    # 1. Asegurar que el permiso está asignado
    assign_response = admin_client.post(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT], "Fallo al asegurar asignación previa"

    # 2. Ejecutar la petición DELETE para quitar la asignación
    response_delete = admin_client.delete(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    assert response_delete.status_code == status.HTTP_204_NO_CONTENT

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_remove_permission_from_role_success_admin': Verificando rol ID {vendedor_role_id} con nueva sesión.")
             db_rol = rol_repository.get_rol_with_permissions(db=verification_db, rol_id=vendedor_role_id)
             assert db_rol is not None
             permiso_ids_en_db = {p.id for p in db_rol.permisos}
             assert permiso_leer_cliente_id not in permiso_ids_en_db, "El permiso todavía se encontró en la relación del rol en la BD."
             logger.info(f"Test 'test_remove_permission_from_role_success_admin': Permiso quitado de rol ID {vendedor_role_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_remove_permission_from_role_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests quitar permiso no asignado, rol no encontrado, permiso no encontrado, forbidden sin cambios) ...
def test_remove_permission_not_assigned_admin(
    admin_client: TestClient,
    vendedor_role_id: int,
    permiso_gestionar_usuario_id: int
):
    """Prueba que quitar un permiso no asignado falle (404)."""
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_gestionar_usuario_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "no está asignado al rol" in response.json()["detail"]

def test_remove_permission_role_not_found_admin(
    admin_client: TestClient,
    permiso_leer_cliente_id: int
):
    """Prueba quitar permiso desde un rol inexistente (404)."""
    non_existent_role_id = 99996
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{non_existent_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_remove_permission_permission_not_found_admin(
    admin_client: TestClient,
    vendedor_role_id: int
):
    """Prueba quitar un permiso inexistente de un rol válido (404)."""
    non_existent_perm_id = 99995
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{non_existent_perm_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_remove_permission_forbidden_non_admin(
    admin_client: TestClient,
    vendedor_client: TestClient,
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba que un no-admin no puede quitar permisos (403)."""
    assign_response = admin_client.post(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT]
    response = vendedor_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'remover:permiso_rol'" in response.json()["detail"]