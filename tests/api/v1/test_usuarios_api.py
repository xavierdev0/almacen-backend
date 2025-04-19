# app/tests/api/v1/test_usuarios_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.core.security import verify_password
from app.core.config import settings
# Schemas necesarios
from app.schemas.usuario_schema import UsuarioCreate, UsuarioRead
# Modelos y repositorios para verificaciones en BD
from app.models import Usuario, Rol
from app.repositories import usuario_repository, rol_repository
from typing import Callable

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
USUARIOS_ENDPOINT = f"{API_V1_STR}/usuarios"

# --- Tests para Crear Usuarios (POST /usuarios) ---

def test_create_user_success_admin(
    admin_client: TestClient, # Usa el cliente admin refactorizado
    db_session: Session,
    operario_role_id: int # Fixture para ID del rol Operario
):
    """Prueba la creación exitosa de un usuario (Operario) por un admin."""
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

    # Verificar respuesta HTTP 201
    assert response.status_code == status.HTTP_201_CREATED

    # Verificar contenido de la respuesta (UsuarioRead)
    data = response.json()
    assert data["username"] == username
    assert data["email"] == email
    assert data["nombre_completo"] == "Test Operario Nuevo"
    assert data["esta_activo"] is True
    assert "id" in data
    new_user_id = data["id"]

    # Verificar que el rol asignado está en la respuesta
    assert "roles" in data
    assert isinstance(data["roles"], list)
    role_ids_in_response = {role["id"] for role in data["roles"]}
    assert operario_role_id in role_ids_in_response
    # Opcional: Verificar nombre del rol
    operario_role_name = next((r["nombre"] for r in data["roles"] if r["id"] == operario_role_id), None)
    assert operario_role_name == "Operario"

    # Verificar en la BD
    db_user = usuario_repository.get_usuario(db=db_session, user_id=new_user_id)
    assert db_user is not None
    assert db_user.username == username
    assert db_user.email == email
    # Verificar roles asignados en BD
    db_user_roles = {rol.id for rol in db_user.roles}
    assert operario_role_id in db_user_roles

def test_create_user_duplicate_username_admin(admin_client: TestClient, db_session: Session, admin_user: Usuario):
    """Prueba que crear usuario con username duplicado falle (400)."""
    # Usamos el username del admin_user que ya existe por las fixtures
    existing_username = admin_user.username
    unique_suffix = uuid.uuid4().hex[:6]
    email = f"otroemail_{unique_suffix}@example.com" # Email diferente
    password = "password123"

    user_data = UsuarioCreate(
        username=existing_username, # <-- Username duplicado
        email=email,
        password=password,
        nombre_completo="Usuario Duplicado Test"
        # No asignamos roles para simplificar
    )

    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())

    # Verificar respuesta HTTP 400 (según servicio)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = response.json()
    assert "detail" in data
    assert "nombre de usuario no está disponible" in data["detail"].lower()

def test_create_user_duplicate_email_admin(admin_client: TestClient, db_session: Session, admin_user: Usuario):
    """Prueba que crear usuario con email duplicado falle (400)."""
    # Usamos el email del admin_user que ya existe
    existing_email = admin_user.email
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"otrousername_{unique_suffix}" # Username diferente
    password = "password123"

    user_data = UsuarioCreate(
        username=username,
        email=existing_email, # <-- Email duplicado
        password=password,
        nombre_completo="Usuario Duplicado Email Test"
    )

    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())

    # Verificar respuesta HTTP 400 (según servicio)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = response.json()
    assert "detail" in data
    assert "correo electrónico ya está registrado" in data["detail"].lower()

def test_create_user_invalid_data_admin(admin_client: TestClient):
    """Prueba crear usuario con datos inválidos (422)."""
    unique_suffix = uuid.uuid4().hex[:6]

    # Caso 1: Email inválido
    # Enviar directamente el diccionario con datos inválidos
    invalid_email_payload = {
        "username": f"invalidemail_{unique_suffix}",
        "email": "esto-no-es-un-email", # Inválido
        "password": "password123",
        "nombre_completo": "Invalido Email"
    }
    response_email = admin_client.post(USUARIOS_ENDPOINT, json=invalid_email_payload) # Enviar dict
    assert response_email.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    # Verificar (opcional) el detalle del error específico para 'email'
    assert any("email" in error.get("loc", []) for error in response_email.json().get("detail", [])), \
        "El detalle del error 422 no especificó un problema con el campo 'email'."


    # Caso 2: Contraseña corta
    # Enviar directamente el diccionario con datos inválidos
    invalid_pass_payload = {
        "username": f"shortpass_{unique_suffix}",
        "email": f"shortpass_{unique_suffix}@example.com",
        "password": "123", # Demasiado corta
        "nombre_completo": "Pass Corta"
    }
    response_pass = admin_client.post(USUARIOS_ENDPOINT, json=invalid_pass_payload) # Enviar dict
    assert response_pass.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    # Verificar (opcional) el detalle del error específico para 'password'
    assert any("password" in error.get("loc", []) for error in response_pass.json().get("detail", [])), \
        "El detalle del error 422 no especificó un problema con el campo 'password'."

    # Caso 3: Username corto (si tienes min_length en el schema)
    invalid_username_payload = {
        "username": "us", # Demasiado corto (asumiendo min_length=3)
        "email": f"shortuser_{unique_suffix}@example.com",
        "password": "password123",
        "nombre_completo": "User Corto"
    }
    response_user = admin_client.post(USUARIOS_ENDPOINT, json=invalid_username_payload) # Enviar dict
    assert response_user.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("username" in error.get("loc", []) for error in response_user.json().get("detail", [])), \
        "El detalle del error 422 no especificó un problema con el campo 'username'."


def test_create_user_non_existent_role_id_admin(admin_client: TestClient):
    """Prueba crear usuario asignando un rol_id inexistente (404)."""
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"badrole_{unique_suffix}"
    email = f"badrole_{unique_suffix}@example.com"
    password = "password123"
    non_existent_role_id = 99999

    user_data = UsuarioCreate(
        username=username,
        email=email,
        password=password,
        nombre_completo="Rol Malo Test",
        rol_ids=[non_existent_role_id] # <-- ID de rol que no existe
    )

    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())

    # Verificar respuesta HTTP 404 (según servicio usuario_service)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    data = response.json()
    assert "detail" in data
    assert "ids de rol proporcionados no existen" in data["detail"].lower()
    assert str(non_existent_role_id) in data["detail"] # Verificar que menciona el ID problemático

def test_create_user_forbidden_non_admin(vendedor_client: TestClient):
    """Prueba que un no-admin (Vendedor) no puede crear usuarios (403)."""
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"forbidden_{unique_suffix}"
    email = f"forbidden_{unique_suffix}@example.com"
    password = "password123"

    user_data = UsuarioCreate(
        username=username,
        email=email,
        password=password,
        nombre_completo="No Deberia Crear"
    )

    response = vendedor_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())

    # Verificar respuesta HTTP 403
    assert response.status_code == status.HTTP_403_FORBIDDEN
    data = response.json()
    assert "detail" in data
    assert "Permiso insuficiente: Se requiere 'crear:usuario'" in data["detail"]

# --- GET /me ---

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
    # Verificar que los roles coincidan (comparando IDs o nombres)
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
    """Prueba que un usuario puede actualizar su propio nombre_completo y email."""
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

    # Verificar en BD
    updated_user_in_db = usuario_repository.get_usuario(db=db_session, user_id=vendedor_user.id)
    assert updated_user_in_db is not None, "No se encontró el usuario en la BD después del update."
    assert updated_user_in_db.nombre_completo == new_fullname
    assert updated_user_in_db.email == new_email

def test_update_me_duplicate_email(vendedor_client: TestClient, admin_user: Usuario):
    """Prueba que actualizar 'me' con un email duplicado falle (400)."""
    # Intentar cambiar el email del vendedor al email del admin (que ya existe)
    update_payload = {"email": admin_user.email}

    response = vendedor_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = response.json()
    assert "detail" in data
    assert "email ya en uso" in data["detail"].lower() # Mensaje del servicio

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
    db_session: Session,
    vendedor_user: Usuario,
):
    """Prueba el cambio exitoso de la contraseña propia verificando el hash."""
    old_password = "password123" # Contraseña inicial de las fixtures
    new_password = f"new_password_{uuid.uuid4().hex[:6]}"

    password_payload = {
        "old_password": old_password,
        "new_password": new_password,
        "confirm_password": new_password
    }

    # Realizar la petición para cambiar la contraseña
    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)

    # Verificar 204 No Content (la petición fue aceptada)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verificar directamente en la BD que el hash cambió y coincide con la nueva contraseña
    # db_session.commit() # No debería ser necesario hacer commit aquí, el endpoint ya lo hizo
    # Volver a obtener el usuario desde la sesión de prueba actual para ver los cambios
    updated_user_in_db = usuario_repository.get_usuario(db=db_session, user_id=vendedor_user.id)
    assert updated_user_in_db is not None, "Usuario no encontrado en BD para verificar hash."
    assert updated_user_in_db.contrasena_hash != vendedor_user.contrasena_hash, \
        "El hash de la contraseña no cambió en la base de datos."

    # Verificar que la nueva contraseña coincide con el nuevo hash
    assert verify_password(new_password, updated_user_in_db.contrasena_hash), \
        "El hash en la BD no coincide con la nueva contraseña."
    # Verificar que la contraseña antigua YA NO coincide con el nuevo hash
    assert not verify_password(old_password, updated_user_in_db.contrasena_hash), \
        "El hash en la BD todavía coincide con la contraseña antigua."


def test_update_my_password_wrong_old(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'old_password' incorrecta (400)."""
    new_password = "cualquiercosa"
    password_payload = {
        "old_password": "password_incorrecto", # Contraseña antigua errónea
        "new_password": new_password,
        "confirm_password": new_password
    }

    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = response.json()
    assert "detail" in data
    assert "contraseña actual incorrecta" in data["detail"].lower()

def test_update_my_password_mismatch_new(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'new_password' y 'confirm_password' distintos (422)."""
    password_payload = {
        "old_password": "password123",
        "new_password": "nueva_pass_1",
        "confirm_password": "nueva_pass_2" # No coinciden
    }

    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    data = response.json()
    # Verificar que el error está relacionado con la validación del schema
    assert "detail" in data
    assert isinstance(data["detail"], list)
    assert any("confirm_password" in error.get("loc", []) for error in data["detail"]), \
        "El detalle del error 422 no especificó un problema con 'confirm_password'."

def test_update_my_password_short_new(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'new_password' demasiado corta (422)."""
    password_payload = {
        "old_password": "password123",
        "new_password": "corta", # Demasiado corta
        "confirm_password": "corta"
    }

    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    data = response.json()
    assert any("new_password" in error.get("loc", []) for error in data["detail"]), \
        "El detalle del error 422 no especificó un problema con 'new_password'."


def test_update_my_password_unauthenticated(base_client: TestClient):
    """Prueba cambiar contraseña sin autenticación (401)."""
    password_payload = {
        "old_password": "password123",
        "new_password": "new_password",
        "confirm_password": "new_password"
    }
    response = base_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED




# --- GET /usuarios/{user_id} ---

def test_read_user_success_admin(
    admin_client: TestClient,
    db_session: Session, # Usar la sesión del test para obtener el estado actual
    vendedor_user: Usuario # Aún usamos la fixture para obtener el ID
):
    """Prueba obtener datos de otro usuario (Vendedor) como admin, verificando contra la BD."""
    user_id_to_get = vendedor_user.id
    response = admin_client.get(f"{USUARIOS_ENDPOINT}/{user_id_to_get}")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == user_id_to_get
    assert data["username"] == vendedor_user.username # Username no debería cambiar

    # --- OBTENER ESTADO ACTUAL DE LA BD ---
    # Volver a obtener el usuario desde la sesión actual del test
    current_db_user = usuario_repository.get_usuario(db=db_session, user_id=user_id_to_get)
    assert current_db_user is not None, "No se pudo obtener el usuario actual de la BD para comparación."
    # --- FIN OBTENER ESTADO ACTUAL ---

    # Ahora comparar la respuesta de la API contra el estado actual de la BD
    assert data["email"] == current_db_user.email
    assert data["nombre_completo"] == current_db_user.nombre_completo
    assert data["esta_activo"] == current_db_user.esta_activo

    assert "roles" in data
    # Comparar IDs de roles es suficiente y más simple que nombres
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
    db_session: Session,
    vendedor_user: Usuario,
    dibujante_role_id: int # Usar el rol Dibujante
):
    """Prueba asignar un rol (Dibujante) a otro usuario (Vendedor) como admin."""
    user_id = vendedor_user.id
    role_id_to_assign = dibujante_role_id

    # Asegurarse que el rol Dibujante no esté asignado inicialmente
    vendedor_roles_before = {r.id for r in vendedor_user.roles}
    assert role_id_to_assign not in vendedor_roles_before, "El rol Dibujante ya estaba asignado inesperadamente."

    # Asignar el rol
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_assign}")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == user_id
    # Verificar que ambos roles (Vendedor y Dibujante) están ahora en la respuesta
    response_role_ids = {role["id"] for role in data["roles"]}
    assert vendedor_user.roles[0].id in response_role_ids # Asume que vendedor solo tiene 1 rol inicial
    assert role_id_to_assign in response_role_ids
    assert len(response_role_ids) == len(vendedor_roles_before) + 1

    # Verificar en BD
    updated_user_in_db = usuario_repository.get_usuario(db=db_session, user_id=vendedor_user.id)
    assert updated_user_in_db is not None, "No se encontró el usuario en BD para verificar roles."
    final_db_user_roles = {r.id for r in updated_user_in_db.roles}
    assert role_id_to_assign in final_db_user_roles, "El rol asignado no se encontró en la BD."
    assert len(final_db_user_roles) == len(vendedor_roles_before) + 1, "El número de roles en BD no es correcto."


def test_assign_role_already_assigned_admin(
    admin_client: TestClient,
    vendedor_user: Usuario,
    vendedor_role_id: int # Usar el rol que ya tiene
):
    """Prueba asignar un rol que el usuario ya tiene (debería ser idempotente, 200 OK)."""
    user_id = vendedor_user.id
    role_id_to_assign = vendedor_role_id # El rol que ya tiene

    # Intentar asignar de nuevo
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_assign}")

    # El repositorio actual no lanza error si ya existe, el servicio devuelve el usuario actualizado
    assert response.status_code == status.HTTP_200_OK
    # Verificar que el rol sigue ahí (y no se duplicó, etc.)
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
    db_session: Session,
    vendedor_user: Usuario,
    dibujante_role_id: int # Usaremos el rol Dibujante para añadir y quitar
):
    """Prueba quitar un rol (Dibujante) de otro usuario (Vendedor) como admin."""
    user_id = vendedor_user.id
    role_id_to_remove = dibujante_role_id

    # 1. Primero, asignar el rol Dibujante para asegurarse de que existe la asignación
    assign_resp = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")
    assert assign_resp.status_code == status.HTTP_200_OK, "Fallo al asignar rol Dibujante previamente"
    roles_after_assign = {r["id"] for r in assign_resp.json()["roles"]}
    assert role_id_to_remove in roles_after_assign

    # 2. Quitar el rol
    response_delete = admin_client.delete(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")

    # Verificar 204 No Content
    assert response_delete.status_code == status.HTTP_204_NO_CONTENT

    # 3. Verificar en BD que el rol Dibujante ya no está volviendo a consultar
    # db_session.commit() # Opcional: asegurar visibilidad en la sesión del test
    updated_user_in_db = usuario_repository.get_usuario(db=db_session, user_id=vendedor_user.id)
    assert updated_user_in_db is not None, "No se encontró el usuario en BD para verificar roles."
    final_db_user_roles = {r.id for r in updated_user_in_db.roles}
    assert role_id_to_remove not in final_db_user_roles, "El rol quitado todavía se encontró en la BD."
    # Asegurar que el rol original (Vendedor) sí sigue ahí
    vendedor_role_id = next((r.id for r in vendedor_user.roles if r.nombre == "Vendedor"), None) # Obtener ID de Vendedor original
    assert vendedor_role_id in final_db_user_roles, "El rol original 'Vendedor' desapareció de la BD."

def test_remove_role_not_assigned_admin(
    admin_client: TestClient,
    vendedor_user: Usuario,
    operario_role_id: int # Usar un rol que Vendedor no tiene
):
    """Prueba quitar un rol no asignado (debería ser idempotente, 204)."""
    user_id = vendedor_user.id
    role_id_to_remove = operario_role_id # Rol que no está asignado

    response = admin_client.delete(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")

    # El repositorio actual no lanza error si no existe, devuelve 204
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
    # El ID del rol a quitar no importa tanto como el hecho de que la acción está prohibida
    role_id_to_remove = vendedor_role_id
    response = vendedor_client.delete(f"{USUARIOS_ENDPOINT}/{user_id_to_modify}/roles/{role_id_to_remove}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'remover:rol_usuario'" in response.json()["detail"]
