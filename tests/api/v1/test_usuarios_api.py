# app/tests/api/v1/test_usuarios_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
import logging # Asegurar import

# Importar configuraciones y utilidades
from app.core.security import verify_password # Necesario para test de contraseña
from app.core.config import settings
# Importar schemas necesarios
from app.schemas.usuario_schema import UsuarioCreate, UsuarioRead
# Importar modelos y repositorios para verificaciones en BD
from app.models import Usuario, Rol
from app.repositories import usuario_repository # Necesario para verificaciones
# Importar TestingSessionLocal desde conftest
from tests.conftest import TestingSessionLocal

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
USUARIOS_ENDPOINT = f"{API_V1_STR}/usuarios"
logger = logging.getLogger(__name__) # Añadir logger

# --- Tests para Crear Usuarios (POST /usuarios) ---

def test_create_user_success_admin(
    admin_client: TestClient, # Usa el cliente admin refactorizado
    db_session: Session, # db_session original (no se usará para verificación post-API)
    operario_role_id: int # Fixture para ID del rol Operario
):
    """Prueba la creación exitosa de un usuario (Operario) por un admin (Refactorizado)."""
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"testoperario_{unique_suffix}"
    email = f"testoperario_{unique_suffix}@example.com"
    password = "password123"

    user_data = UsuarioCreate(
        username=username,
        email=email,
        password=password,
        nombre_completo="Test Operario Nuevo",
        rol_ids=[operario_role_id] # Asignar rol de Operario
    )

    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["username"] == username
    assert data["email"] == email
    assert data["nombre_completo"] == "Test Operario Nuevo"
    assert data["esta_activo"] is True
    assert "id" in data
    new_user_id = data["id"]
    role_ids_in_response = {role["id"] for role in data.get("roles", [])}
    assert operario_role_id in role_ids_in_response

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_create_user_success_admin': Verificando usuario ID {new_user_id} con nueva sesión.")
            # Usar load_related=True implícito en get_usuario o especificarlo si es necesario
            db_user = usuario_repository.get_usuario(db=verification_db, user_id=new_user_id)
            assert db_user is not None, f"Usuario ID {new_user_id} no encontrado en BD post-creación."
            assert db_user.username == username
            assert db_user.email == email
            # Verificar roles asignados en BD
            db_user_roles = {rol.id for rol in db_user.roles}
            assert operario_role_id in db_user_roles
            logger.info(f"Test 'test_create_user_success_admin': Usuario ID {new_user_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_create_user_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests create duplicate, invalid, non-existent role, forbidden sin cambios) ...
def test_create_user_duplicate_username_admin(admin_client: TestClient, db_session: Session, admin_user: Usuario):
    """Prueba que crear usuario con username duplicado falle (400)."""
    existing_username = admin_user.username
    unique_suffix = uuid.uuid4().hex[:6]
    email = f"otroemail_{unique_suffix}@example.com"
    password = "password123"
    user_data = UsuarioCreate(username=existing_username, email=email, password=password, nombre_completo="Usuario Duplicado Test")
    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "nombre de usuario no está disponible" in response.json()["detail"].lower()

def test_create_user_duplicate_email_admin(admin_client: TestClient, db_session: Session, admin_user: Usuario):
    """Prueba que crear usuario con email duplicado falle (400)."""
    existing_email = admin_user.email
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"otrousername_{unique_suffix}"
    password = "password123"
    user_data = UsuarioCreate(username=username, email=existing_email, password=password, nombre_completo="Usuario Duplicado Email Test")
    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "correo electrónico ya está registrado" in response.json()["detail"].lower()

def test_create_user_invalid_data_admin(admin_client: TestClient):
    """Prueba crear usuario con datos inválidos (422)."""
    unique_suffix = uuid.uuid4().hex[:6]
    invalid_email_payload = {"username": f"invalidemail_{unique_suffix}","email": "esto-no-es-un-email","password": "password123","nombre_completo": "Invalido Email"}
    response_email = admin_client.post(USUARIOS_ENDPOINT, json=invalid_email_payload)
    assert response_email.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("email" in error.get("loc", []) for error in response_email.json().get("detail", []))
    invalid_pass_payload = {"username": f"shortpass_{unique_suffix}","email": f"shortpass_{unique_suffix}@example.com","password": "123","nombre_completo": "Pass Corta"}
    response_pass = admin_client.post(USUARIOS_ENDPOINT, json=invalid_pass_payload)
    assert response_pass.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("password" in error.get("loc", []) for error in response_pass.json().get("detail", []))
    invalid_username_payload = {"username": "us","email": f"shortuser_{unique_suffix}@example.com","password": "password123","nombre_completo": "User Corto"}
    response_user = admin_client.post(USUARIOS_ENDPOINT, json=invalid_username_payload)
    assert response_user.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("username" in error.get("loc", []) for error in response_user.json().get("detail", []))

def test_create_user_non_existent_role_id_admin(admin_client: TestClient):
    """Prueba crear usuario asignando un rol_id inexistente (404)."""
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"badrole_{unique_suffix}"
    email = f"badrole_{unique_suffix}@example.com"
    password = "password123"
    non_existent_role_id = 99999
    user_data = UsuarioCreate(username=username,email=email,password=password,nombre_completo="Rol Malo Test",rol_ids=[non_existent_role_id])
    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "ids de rol proporcionados no existen" in response.json()["detail"].lower()

def test_create_user_forbidden_non_admin(vendedor_client: TestClient):
    """Prueba que un no-admin (Vendedor) no puede crear usuarios (403)."""
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"forbidden_{unique_suffix}"
    email = f"forbidden_{unique_suffix}@example.com"
    password = "password123"
    user_data = UsuarioCreate(username=username,email=email,password=password,nombre_completo="No Deberia Crear")
    response = vendedor_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'crear:usuario'" in response.json()["detail"]

# --- GET /me ---
# (Sin cambios, no modifican DB)
def test_read_me_success(vendedor_client: TestClient, vendedor_user: Usuario):
    """Prueba obtener los datos propios con un usuario Vendedor."""
    response = vendedor_client.get(f"{USUARIOS_ENDPOINT}/me")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == vendedor_user.id
    assert data["username"] == vendedor_user.username
    assert data["email"] == vendedor_user.email
    assert data["nombre_completo"] == vendedor_user.nombre_completo
    assert data["esta_activo"] == vendedor_user.esta_activo
    assert "roles" in data
    expected_role_ids = {role.id for role in vendedor_user.roles}
    response_role_ids = {role["id"] for role in data["roles"]}
    assert response_role_ids == expected_role_ids

def test_read_me_unauthenticated(base_client: TestClient):
    """Prueba que obtener /me sin autenticación falle (401)."""
    response = base_client.get(f"{USUARIOS_ENDPOINT}/me")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# =========================
# --- PATCH /me ---
# =========================

def test_update_me_success(vendedor_client: TestClient, db_session: Session, vendedor_user: Usuario):
    """Prueba que un usuario puede actualizar su propio nombre_completo y email (Refactorizado)."""
    unique_suffix = uuid.uuid4().hex[:6]
    new_fullname = f"Nombre Vendedor Actualizado {unique_suffix}"
    new_email = f"vendedor_actualizado_{unique_suffix}@example.com"

    update_payload = {
        "nombre_completo": new_fullname,
        "email": new_email
    }

    response = vendedor_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == vendedor_user.id
    assert data["nombre_completo"] == new_fullname
    assert data["email"] == new_email

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_update_me_success': Verificando usuario ID {vendedor_user.id} con nueva sesión.")
             updated_user_in_db = usuario_repository.get_usuario(db=verification_db, user_id=vendedor_user.id)
             assert updated_user_in_db is not None, "No se encontró el usuario en la BD después del update."
             assert updated_user_in_db.nombre_completo == new_fullname
             assert updated_user_in_db.email == new_email
             logger.info(f"Test 'test_update_me_success': Usuario ID {vendedor_user.id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_update_me_success: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests update me duplicate, invalid, unauthenticated sin cambios) ...
def test_update_me_duplicate_email(vendedor_client: TestClient, admin_user: Usuario):
    """Prueba que actualizar 'me' con un email duplicado falle (400)."""
    update_payload = {"email": admin_user.email}
    response = vendedor_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email ya en uso" in response.json()["detail"].lower() # Mensaje del servicio

def test_update_me_invalid_email(vendedor_client: TestClient):
    """Prueba que actualizar 'me' con email inválido falle (422)."""
    update_payload = {"email": "email-invalido"}
    response = vendedor_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_me_unauthenticated(base_client: TestClient):
    """Prueba que actualizar /me sin autenticación falle (401)."""
    update_payload = {"nombre_completo": "No debería funcionar"}
    response = base_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- PUT /me/password ---

def test_update_my_password_success(
    vendedor_client: TestClient,
    db_session: Session, # No se usará directamente para verificación
    vendedor_user: Usuario,
):
    """Prueba el cambio exitoso de la contraseña propia verificando el hash (Refactorizado)."""
    old_password = "password123" # Contraseña inicial de las fixtures
    new_password = f"new_password_{uuid.uuid4().hex[:6]}"
    user_id = vendedor_user.id # Guardar ID para verificación

    password_payload = {
        "old_password": old_password,
        "new_password": new_password,
        "confirm_password": new_password
    }

    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_update_my_password_success': Verificando usuario ID {user_id} con nueva sesión.")
            updated_user_in_db = usuario_repository.get_usuario(db=verification_db, user_id=user_id)
            assert updated_user_in_db is not None, f"Usuario ID {user_id} no encontrado en BD para verificar hash."
            # Obtener el hash original antes de la modificación para comparar
            # (vendedor_user puede tener estado obsoleto si la sesión del test no se refrescó)
            # Es más seguro verificar que el nuevo hash coincide con la nueva contraseña
            assert verify_password(new_password, updated_user_in_db.contrasena_hash), \
                "El hash en la BD no coincide con la nueva contraseña."
            assert not verify_password(old_password, updated_user_in_db.contrasena_hash), \
                "El hash en la BD todavía coincide con la contraseña antigua."
            logger.info(f"Test 'test_update_my_password_success': Contraseña verificada para Usuario ID {user_id}.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_update_my_password_success: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests update password wrong old, mismatch, short, unauthenticated sin cambios) ...
def test_update_my_password_wrong_old(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'old_password' incorrecta (400)."""
    new_password = "cualquiercosa"
    password_payload = {"old_password": "password_incorrecto","new_password": new_password,"confirm_password": new_password}
    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "contraseña actual incorrecta" in response.json()["detail"].lower()

def test_update_my_password_mismatch_new(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'new_password' y 'confirm_password' distintos (422)."""
    password_payload = {"old_password": "password123","new_password": "nueva_pass_1","confirm_password": "nueva_pass_2"}
    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("confirm_password" in error.get("loc", []) for error in response.json().get("detail", []))

def test_update_my_password_short_new(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'new_password' demasiado corta (422)."""
    password_payload = {"old_password": "password123","new_password": "corta","confirm_password": "corta"}
    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("new_password" in error.get("loc", []) for error in response.json().get("detail", []))

def test_update_my_password_unauthenticated(base_client: TestClient):
    """Prueba cambiar contraseña sin autenticación (401)."""
    password_payload = {"old_password": "password123","new_password": "new_password","confirm_password": "new_password"}
    response = base_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- GET /usuarios/{user_id} ---
# (Sin cambios, no modifican DB)
def test_read_user_success_admin(
    admin_client: TestClient,
    db_session: Session,
    vendedor_user: Usuario
):
    """Prueba obtener datos de otro usuario (Vendedor) como admin, verificando contra la BD."""
    user_id_to_get = vendedor_user.id
    response = admin_client.get(f"{USUARIOS_ENDPOINT}/{user_id_to_get}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == user_id_to_get
    assert data["username"] == vendedor_user.username
    # Usar nueva sesión para obtener estado actual es buena práctica incluso aquí
    with TestingSessionLocal() as verification_db:
        current_db_user = usuario_repository.get_usuario(db=verification_db, user_id=user_id_to_get)
        assert current_db_user is not None, "No se pudo obtener el usuario actual de la BD para comparación."
        assert data["email"] == current_db_user.email
        assert data["nombre_completo"] == current_db_user.nombre_completo
        assert data["esta_activo"] == current_db_user.esta_activo
        assert "roles" in data
        current_db_role_ids = {r.id for r in current_db_user.roles}
        response_role_ids = {r["id"] for r in data["roles"]}
        assert response_role_ids == current_db_role_ids, "Los roles en la respuesta no coinciden con los de la BD."

def test_read_user_not_found_admin(admin_client: TestClient):
    """Prueba obtener un usuario inexistente por ID (404)."""
    non_existent_user_id = 99998
    response = admin_client.get(f"{USUARIOS_ENDPOINT}/{non_existent_user_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Usuario no encontrado" in response.json()["detail"]

def test_read_user_forbidden_non_admin(vendedor_client: TestClient, admin_user: Usuario):
    """Prueba que un Vendedor no puede obtener datos de otro usuario (Admin) (403)."""
    user_id_to_get = admin_user.id # Intentar obtener datos del admin
    response = vendedor_client.get(f"{USUARIOS_ENDPOINT}/{user_id_to_get}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:usuario'" in response.json()["detail"]

# --- POST /usuarios/{user_id}/roles/{rol_id} ---

def test_assign_role_to_user_success_admin(
    admin_client: TestClient,
    db_session: Session, # No se usará para verificación post-API
    vendedor_user: Usuario,
    dibujante_role_id: int # Usar el rol Dibujante
):
    """Prueba asignar un rol (Dibujante) a otro usuario (Vendedor) como admin (Refactorizado)."""
    user_id = vendedor_user.id
    role_id_to_assign = dibujante_role_id
    vendedor_role_id = vendedor_user.roles[0].id # Asume 1 rol inicial

    # Asegurarse que el rol Dibujante no esté asignado inicialmente (usando nueva sesión)
    with TestingSessionLocal() as pre_check_db:
        user_before = usuario_repository.get_usuario(db=pre_check_db, user_id=user_id)
        assert user_before is not None
        vendedor_roles_before = {r.id for r in user_before.roles}
        assert role_id_to_assign not in vendedor_roles_before, "El rol Dibujante ya estaba asignado inesperadamente."

    # Asignar el rol
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_assign}")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == user_id
    response_role_ids = {role["id"] for role in data.get("roles", [])}
    assert vendedor_role_id in response_role_ids
    assert role_id_to_assign in response_role_ids
    assert len(response_role_ids) == len(vendedor_roles_before) + 1

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_assign_role_to_user_success_admin': Verificando usuario ID {user_id} con nueva sesión.")
            updated_user_in_db = usuario_repository.get_usuario(db=verification_db, user_id=user_id)
            assert updated_user_in_db is not None, "No se encontró el usuario en BD para verificar roles."
            final_db_user_roles = {r.id for r in updated_user_in_db.roles}
            assert role_id_to_assign in final_db_user_roles, "El rol asignado no se encontró en la BD."
            assert len(final_db_user_roles) == len(vendedor_roles_before) + 1, "El número de roles en BD no es correcto."
            logger.info(f"Test 'test_assign_role_to_user_success_admin': Roles verificados para Usuario ID {user_id}.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_assign_role_to_user_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests asignar rol ya asignado, user not found, role not found, forbidden sin cambios) ...
def test_assign_role_already_assigned_admin(
    admin_client: TestClient,
    vendedor_user: Usuario,
    vendedor_role_id: int # Usar el rol que ya tiene
):
    """Prueba asignar un rol que el usuario ya tiene (debería ser idempotente, 200 OK)."""
    user_id = vendedor_user.id
    role_id_to_assign = vendedor_role_id # El rol que ya tiene
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_assign}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    response_role_ids = {role["id"] for role in data["roles"]}
    assert role_id_to_assign in response_role_ids

def test_assign_role_user_not_found_admin(admin_client: TestClient, vendedor_role_id: int):
    """Prueba asignar rol a un usuario inexistente (404)."""
    non_existent_user_id = 99998
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{non_existent_user_id}/roles/{vendedor_role_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Usuario no encontrado" in response.json()["detail"]

def test_assign_role_role_not_found_admin(admin_client: TestClient, vendedor_user: Usuario):
    """Prueba asignar un rol inexistente a un usuario válido (404)."""
    user_id = vendedor_user.id
    non_existent_role_id = 99999
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{non_existent_role_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Rol con ID 99999 no encontrado" in response.json()["detail"] # El servicio de rol busca el rol

def test_assign_role_forbidden_non_admin(
    vendedor_client: TestClient,
    admin_user: Usuario, # Intentar modificar al admin
    operario_role_id: int
):
    """Prueba que un Vendedor no puede asignar roles a otro usuario (Admin) (403)."""
    user_id_to_modify = admin_user.id
    role_id_to_assign = operario_role_id
    response = vendedor_client.post(f"{USUARIOS_ENDPOINT}/{user_id_to_modify}/roles/{role_id_to_assign}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'asignar:rol_usuario'" in response.json()["detail"]

# --- DELETE /usuarios/{user_id}/roles/{rol_id} ---

def test_remove_role_from_user_success_admin(
    admin_client: TestClient,
    db_session: Session, # No se usará para verificación post-API
    vendedor_user: Usuario,
    dibujante_role_id: int # Usaremos el rol Dibujante para añadir y quitar
):
    """Prueba quitar un rol (Dibujante) de otro usuario (Vendedor) como admin (Refactorizado)."""
    user_id = vendedor_user.id
    role_id_to_remove = dibujante_role_id
    vendedor_role_id = vendedor_user.roles[0].id # Asume 1 rol inicial

    # 1. Asignar el rol Dibujante primero
    assign_resp = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")
    assert assign_resp.status_code == status.HTTP_200_OK, "Fallo al asignar rol Dibujante previamente"

    # 2. Quitar el rol
    response_delete = admin_client.delete(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")
    assert response_delete.status_code == status.HTTP_204_NO_CONTENT

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_remove_role_from_user_success_admin': Verificando usuario ID {user_id} con nueva sesión.")
             updated_user_in_db = usuario_repository.get_usuario(db=verification_db, user_id=user_id)
             assert updated_user_in_db is not None, "No se encontró el usuario en BD para verificar roles."
             final_db_user_roles = {r.id for r in updated_user_in_db.roles}
             assert role_id_to_remove not in final_db_user_roles, "El rol quitado todavía se encontró en la BD."
             assert vendedor_role_id in final_db_user_roles, "El rol original 'Vendedor' desapareció de la BD."
             logger.info(f"Test 'test_remove_role_from_user_success_admin': Roles verificados para Usuario ID {user_id}.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_remove_role_from_user_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests quitar rol no asignado, user not found, role not found, forbidden sin cambios) ...
def test_remove_role_not_assigned_admin(
    admin_client: TestClient,
    vendedor_user: Usuario,
    operario_role_id: int # Usar un rol que Vendedor no tiene
):
    """Prueba quitar un rol no asignado (debería ser idempotente, 204)."""
    user_id = vendedor_user.id
    role_id_to_remove = operario_role_id # Rol que no está asignado
    response = admin_client.delete(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_remove_role_user_not_found_admin(admin_client: TestClient, vendedor_role_id: int):
    """Prueba quitar rol de un usuario inexistente (404)."""
    non_existent_user_id = 99998
    response = admin_client.delete(f"{USUARIOS_ENDPOINT}/{non_existent_user_id}/roles/{vendedor_role_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Usuario no encontrado" in response.json()["detail"]

def test_remove_role_role_not_found_admin(admin_client: TestClient, vendedor_user: Usuario):
    """Prueba quitar un rol inexistente de un usuario válido (404)."""
    user_id = vendedor_user.id
    non_existent_role_id = 99999
    response = admin_client.delete(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{non_existent_role_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Rol con ID 99999 no encontrado" in response.json()["detail"]

def test_remove_role_forbidden_non_admin(
    vendedor_client: TestClient,
    admin_user: Usuario, # Intentar modificar al admin
    vendedor_role_id: int # Intentar quitar el rol Vendedor (aunque no lo tenga el admin)
):
    """Prueba que un Vendedor no puede quitar roles a otro usuario (Admin) (403)."""
    user_id_to_modify = admin_user.id
    role_id_to_remove = vendedor_role_id
    response = vendedor_client.delete(f"{USUARIOS_ENDPOINT}/{user_id_to_modify}/roles/{role_id_to_remove}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'remover:rol_usuario'" in response.json()["detail"]