# tests/api/v1/test_roles_api.py
import pytest # Necesario para decoradores y runner
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session

# Importar settings para prefijo API
from app.core.config import settings
# Importar schemas para crear payloads y validar respuestas
from app.schemas.rol_permiso_schema import RolCreate, RolRead, RolUpdate, RolReadWithPermissions
# Importar modelo para interactuar con la BD si es necesario verificar
from app.models import Rol, Usuario
from app.repositories import rol_repository, usuario_repository # Para verificaciones directas en BD
import uuid
# --- Constantes ---
API_V1_STR = settings.API_V1_STR
ROLES_ENDPOINT = f"{API_V1_STR}/roles" # Ruta base para roles

# --- Tests para Listar Roles (GET /roles) ---

def test_list_roles_unauthenticated(client: TestClient):
    """Prueba que listar roles sin autenticación falle (401)."""
    response = client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    # No es necesario verificar el body en 401

def test_list_roles_forbidden_non_admin(vendedor_client: TestClient):
    """
    Prueba que listar roles como usuario no-admin (ej: Vendedor) falle (403)
    debido a falta del permiso 'leer:rol'.
    """
    response = vendedor_client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    # Verificar el detalle del error si la dependencia require_permission lo proporciona
    data = response.json()
    assert "detail" in data
    assert "Permiso insuficiente: Se requiere 'leer:rol'." in data["detail"]

def test_list_roles_success_admin(admin_client: TestClient, db_session: Session):
    """
    Prueba que listar roles como admin funcione (200) y devuelva los roles iniciales.
    Asume que la BD de prueba fue poblada con los 5 roles iniciales por las migraciones.
    """
    response = admin_client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    # Verificar que existan al menos los 5 roles iniciales
    assert len(data) >= 5
    role_names = {role["nombre"] for role in data}
    assert "Administrador" in role_names
    assert "Vendedor" in role_names
    assert "Supervisor" in role_names
    assert "Dibujante" in role_names
    assert "Operario" in role_names
    # Verificar que la estructura de cada elemento coincide con RolRead
    for role in data:
        assert "id" in role
        assert "nombre" in role
        assert "descripcion" in role
        # Timestamps son opcionales en el schema, pueden estar o no
        # assert "fecha_creacion" in role
        # assert "fecha_ultima_actualizacion" in role


# --- Tests para Crear Roles (POST /roles) ---

def test_create_role_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la creación exitosa de un rol como admin."""
    role_data = RolCreate(nombre="RolCreadoEnTest", descripcion="Descripción test")
    response = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())

    # Verificar respuesta HTTP
    assert response.status_code == status.HTTP_201_CREATED

    # Verificar contenido de la respuesta (debe coincidir con RolRead)
    data = response.json()
    assert data["nombre"] == role_data.nombre
    assert data["descripcion"] == role_data.descripcion
    assert "id" in data
    new_role_id = data["id"]

    # Verificar en la BD (opcional pero recomendado)
    db_rol = rol_repository.get_rol(db=db_session, rol_id=new_role_id)
    assert db_rol is not None
    assert db_rol.nombre == role_data.nombre
    assert db_rol.descripcion == role_data.descripcion

def test_create_role_duplicate_name(admin_client: TestClient, db_session: Session):
    """Prueba que crear un rol con nombre duplicado falle (409)."""
    # Crear el primer rol
    role_data = RolCreate(nombre="RolDuplicadoParaTest", descripcion="Test 409")
    response1 = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response1.status_code == status.HTTP_201_CREATED

    # Intentar crear de nuevo con el mismo nombre
    response2 = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response2.status_code == status.HTTP_409_CONFLICT
    data = response2.json()
    assert "detail" in data
    assert f"El rol '{role_data.nombre}' ya existe" in data["detail"]

def test_create_role_invalid_data(admin_client: TestClient):
    """Prueba que crear un rol con datos inválidos (ej: nombre muy largo) falle (422)."""
    invalid_role_data = {"nombre": "a" * 150, "descripcion": "Test"} # Asumiendo max_length=100 para nombre
    response = admin_client.post(ROLES_ENDPOINT, json=invalid_role_data)
    # FastAPI/Pydantic deberían devolver 422 Unprocessable Entity
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_create_role_forbidden_non_admin(vendedor_client: TestClient):
    """Prueba que crear un rol como no-admin falle (403)."""
    role_data = RolCreate(nombre="RolNoAdminTest", descripcion="No debería crearse")
    response = vendedor_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'crear:rol'" in response.json()["detail"]

# --- Tests para Obtener Rol por ID (GET /roles/{rol_id}) ---
def test_get_role_by_id_success(admin_client: TestClient, vendedor_role_id: int):
    """Prueba obtener un rol existente por ID como admin."""
    response = admin_client.get(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == vendedor_role_id
    assert data["nombre"] == "Vendedor"
    assert "permisos" in data # Verificar que viene con permisos (RolReadWithPermissions)
    assert isinstance(data["permisos"], list)
    # Podríamos verificar algunos permisos esperados para Vendedor si quisiéramos
    perm_keys = {f"{p['nombre_accion']}:{p['nombre_recurso']}" for p in data["permisos"]}
    assert "leer:cliente" in perm_keys
    assert "crear:proforma" in perm_keys


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
    """Prueba la eliminación exitosa de un rol NO ASIGNADO como admin."""
    # 1. Crear un rol temporal que NO esté asignado a nadie
    role_name_to_delete = f"RolParaBorrar_{uuid.uuid4()}"
    temp_role_data = RolCreate(nombre=role_name_to_delete, descripcion="Se eliminará")
    # Usar repositorio para crearlo directamente en la sesión de prueba
    db_rol = rol_repository.create_rol(db=db_session, rol_in=temp_role_data)
    role_id_to_delete = db_rol.id

    # 2. Ejecutar la petición DELETE
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{role_id_to_delete}")

    # 3. Verificar respuesta HTTP (204 No Content para DELETE exitoso)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # 4. Verificar en la BD que el rol ya no existe
    # Forzar commit/refresh para asegurar visibilidad si fuera necesario, aunque get debería funcionar
    db_session.commit()
    db_session.expire_all() # Para asegurar que se lee de nuevo de la BD
    deleted_rol = rol_repository.get_rol(db=db_session, rol_id=role_id_to_delete)
    assert deleted_rol is None

def test_delete_role_not_found_admin(admin_client: TestClient):
    """Prueba eliminar un rol con ID inexistente (404)."""
    non_existent_id = 99998 # Usar otro ID inexistente por si acaso
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{non_existent_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Rol con ID {non_existent_id} no encontrado" in response.json()["detail"]

def test_delete_role_conflict_assigned_admin(
    admin_client: TestClient, db_session: Session, vendedor_role_id: int, vendedor_user: Usuario
):
    """Prueba eliminar un rol ASIGNADO a un usuario (409 Conflict)."""
    # El rol 'Vendedor' (ID de la fixture) está asignado al 'vendedor_user'
    # Asegurarnos que la asignación existe en esta sesión por si acaso
    # (Aunque las fixtures de módulo deberían asegurarlo)
    user_in_db = usuario_repository.get_usuario(db=db_session, user_id=vendedor_user.id)
    assert user_in_db is not None
    roles_usuario = {rol.id for rol in user_in_db.roles}
    assert vendedor_role_id in roles_usuario

    # Intentar eliminar el rol Vendedor
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}")

    # Verificar respuesta HTTP 409
    assert response.status_code == status.HTTP_409_CONFLICT
    data = response.json()
    assert "detail" in data
    # El mensaje exacto puede variar según la implementación del repo/servicio
    assert "No se puede eliminar el rol" in data["detail"]
    assert "porque está asignado a" in data["detail"]

def test_delete_role_forbidden_non_admin(
    vendedor_client: TestClient, vendedor_role_id: int # Usamos vendedor_role_id aunque no se debería poder borrar
):
    """Prueba que eliminar un rol como no-admin falle (403)."""
    response = vendedor_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}")

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'eliminar:rol'" in response.json()["detail"]

# --- PRÓXIMOS PASOS ---
# 1. Implementar el resto de fixtures en conftest.py (si no están ya).
# 2. Añadir más tests aquí para:
#    - PUT /roles/{rol_id} (éxito, not found, conflicto de nombre, forbidden)
#    - DELETE /roles/{rol_id} (éxito, not found, conflicto si está en uso, forbidden)
#    - POST /roles/{rol_id}/permisos/{permiso_id} (éxito, not found rol/perm, conflicto si ya existe, forbidden)
#    - DELETE /roles/{rol_id}/permisos/{permiso_id} (éxito, not found rol/perm/asignación, forbidden)