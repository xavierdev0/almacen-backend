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
def test_list_roles_unauthenticated(base_client: TestClient):
    """Prueba que listar roles sin autenticación falle (401)."""
    response = base_client.get(ROLES_ENDPOINT)
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



# --- Tests para Actualizar Roles (PUT /roles/{rol_id}) ---

def test_update_role_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la actualización exitosa de un rol como admin."""
    # 1. Crear un rol temporal para actualizar
    rol_original = RolCreate(nombre=f"RolParaActualizar_{uuid.uuid4()}", descripcion="Descripción Original")
    response_create = admin_client.post(ROLES_ENDPOINT, json=rol_original.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    role_id_to_update = response_create.json()["id"]

    # 2. Preparar los datos de actualización
    update_data = RolUpdate(nombre="Rol Actualizado Test", descripcion="Nueva Descripción")

    # 3. Ejecutar la petición PUT
    response_update = admin_client.put(
        f"{ROLES_ENDPOINT}/{role_id_to_update}",
        json=update_data.model_dump(exclude_unset=True) # Enviar solo campos modificados
    )

    # 4. Verificar respuesta HTTP (200 OK para PUT/PATCH exitoso)
    assert response_update.status_code == status.HTTP_200_OK

    # 5. Verificar contenido de la respuesta (debe coincidir con RolRead y datos actualizados)
    data = response_update.json()
    assert data["id"] == role_id_to_update
    assert data["nombre"] == update_data.nombre
    assert data["descripcion"] == update_data.descripcion

    # 6. Verificar en la BD (opcional pero recomendado)
    db_rol = rol_repository.get_rol(db=db_session, rol_id=role_id_to_update)
    assert db_rol is not None
    assert db_rol.nombre == update_data.nombre
    assert db_rol.descripcion == update_data.descripcion

def test_update_role_conflict_name_admin(admin_client: TestClient, db_session: Session, vendedor_role_id: int):
    """Prueba que actualizar a un nombre de rol existente falle (409)."""
    # 1. Crear un rol temporal
    rol_original = RolCreate(nombre=f"RolConflicto_{uuid.uuid4()}", descripcion="Original")
    response_create = admin_client.post(ROLES_ENDPOINT, json=rol_original.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    role_id_to_update = response_create.json()["id"]

    # 2. Intentar actualizarlo al nombre de un rol existente ('Vendedor')
    update_data = RolUpdate(nombre="Vendedor") # Nombre que ya existe (del fixture)

    # 3. Ejecutar la petición PUT
    response_update = admin_client.put(
        f"{ROLES_ENDPOINT}/{role_id_to_update}",
        json=update_data.model_dump(exclude_unset=True)
    )

    # 4. Verificar respuesta HTTP 409
    assert response_update.status_code == status.HTTP_409_CONFLICT
    data = response_update.json()
    assert "detail" in data
    # El mensaje exacto puede variar, pero debe indicar el conflicto
    assert "conflicto" in data["detail"].lower() or "ya está en uso" in data["detail"].lower() # <-- LÍNEA MODIFICADA


    # 5. Verificar que el rol original no cambió en la BD
    db_rol = rol_repository.get_rol(db=db_session, rol_id=role_id_to_update)
    assert db_rol is not None
    assert db_rol.nombre == rol_original.nombre # Sigue siendo el nombre original

def test_update_role_not_found_admin(admin_client: TestClient):
    """Prueba actualizar un rol con ID inexistente (404)."""
    non_existent_id = 99997 # Otro ID que no debería existir
    update_data = RolUpdate(nombre="Nombre No Importa")

    response = admin_client.put(
        f"{ROLES_ENDPOINT}/{non_existent_id}",
        json=update_data.model_dump(exclude_unset=True)
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Rol con ID {non_existent_id} no encontrado" in response.json()["detail"]

def test_update_role_invalid_data_admin(admin_client: TestClient, db_session: Session):
    """Prueba actualizar un rol con datos inválidos (ej: nombre muy largo) falle (422)."""
    # 1. Crear rol temporal
    rol_original = RolCreate(nombre=f"RolValidacion_{uuid.uuid4()}", descripcion="Valido")
    response_create = admin_client.post(ROLES_ENDPOINT, json=rol_original.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    role_id_to_update = response_create.json()["id"]

    # 2. Intentar actualizar con nombre inválido
    invalid_update_data = {"nombre": "a" * 150} # Asumiendo max_length=100

    # 3. Ejecutar PUT
    response = admin_client.put(
        f"{ROLES_ENDPOINT}/{role_id_to_update}",
        json=invalid_update_data
    )

    # 4. Verificar 422
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_role_forbidden_non_admin(vendedor_client: TestClient, vendedor_role_id: int):
    """Prueba que actualizar un rol como no-admin falle (403)."""
    update_data = RolUpdate(descripcion="Intento No Autorizado")

    response = vendedor_client.put(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}", # Intentar actualizar el rol Vendedor
        json=update_data.model_dump(exclude_unset=True)
    )

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'actualizar:rol'" in response.json()["detail"]




# --- Tests para Asignar Permisos a Roles (POST /roles/{rol_id}/permisos/{permiso_id}) ---

def test_assign_permission_to_role_success_admin(
    admin_client: TestClient,
    db_session: Session,
    permiso_leer_cliente_id: int # Usamos un permiso existente
):
    """
    Prueba asignar exitosamente un permiso a un NUEVO rol como admin,
    asegurando que la asignación no existía previamente.
    """
    # 1. Crear un rol temporal SIN permisos iniciales
    temp_role_data = RolCreate(nombre=f"RolTempPermiso_{uuid.uuid4()}", descripcion="Rol para test de asignación")
    response_create = admin_client.post(ROLES_ENDPOINT, json=temp_role_data.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED, "Fallo al crear rol temporal"
    new_role_id = response_create.json()["id"]
    # Verificar que el rol creado inicialmente no tiene el permiso
    assert not any(p["id"] == permiso_leer_cliente_id for p in response_create.json().get("permisos", [])), "El rol temporal ya tenía el permiso inesperadamente."


    # 2. Ejecutar la petición POST para asignar el permiso al NUEVO rol
    response_assign = admin_client.post(
        f"{ROLES_ENDPOINT}/{new_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    # 3. Verificar respuesta HTTP (200 OK según el endpoint)
    assert response_assign.status_code == status.HTTP_200_OK

    # 4. Verificar contenido de la respuesta (RolReadWithPermissions)
    data = response_assign.json()
    assert data["id"] == new_role_id
    assert "permisos" in data
    assert isinstance(data["permisos"], list)

    # 5. Buscar el permiso asignado en la lista de permisos de la respuesta
    permiso_asignado_encontrado = False
    for perm in data["permisos"]:
        if perm["id"] == permiso_leer_cliente_id:
            assert perm["nombre_accion"] == "leer"
            assert perm["nombre_recurso"] == "cliente"
            permiso_asignado_encontrado = True
            break
    assert permiso_asignado_encontrado, f"El permiso ID {permiso_leer_cliente_id} no se encontró en la respuesta."

    # 6. Verificar en la BD (opcional pero recomendado)
    # Forzar refresh para asegurar que se lee de nuevo
    db_session.commit() # Commit por si acaso
    db_session.expire_all()
    db_rol = rol_repository.get_rol_with_permissions(db=db_session, rol_id=new_role_id)
    assert db_rol is not None, "El rol temporal no se encontró en la BD para verificación."
    permiso_ids_en_db = {p.id for p in db_rol.permisos}
    assert permiso_leer_cliente_id in permiso_ids_en_db, "El permiso no se encontró en la relación del rol en la BD."

def test_assign_permission_already_assigned_admin(
    admin_client: TestClient,
    db_session: Session,
    vendedor_role_id: int,
    permiso_leer_cliente_id: int # Asumimos que fue asignado en el test anterior o en seeding
):
    """Prueba que asignar un permiso ya asignado falle (409)."""
    # Asegurarse que el permiso ya está asignado (por si el test anterior falló o se corre aislado)
    # Podríamos llamar al endpoint una vez aquí para asegurar, o confiar en el estado del test anterior
    # Vamos a asignarlo explícitamente primero para aislar el test:
    assign_response = admin_client.post(
         f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )
    # Permitimos 200 OK (si no estaba) o 409 (si ya estaba)
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT]

    # Intentar asignar de nuevo
    response = admin_client.post(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    # Verificar respuesta HTTP 409
    assert response.status_code == status.HTTP_409_CONFLICT
    data = response.json()
    assert "detail" in data
    assert "ya está asignado" in data["detail"]

def test_assign_permission_role_not_found_admin(
    admin_client: TestClient,
    permiso_leer_cliente_id: int
):
    """Prueba asignar permiso a un rol inexistente (404)."""
    non_existent_role_id = 99996

    response = admin_client.post(
        f"{ROLES_ENDPOINT}/{non_existent_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Rol con ID {non_existent_role_id} no encontrado" in response.json()["detail"]

def test_assign_permission_permission_not_found_admin(
    admin_client: TestClient,
    vendedor_role_id: int
):
    """Prueba asignar un permiso inexistente a un rol válido (404)."""
    non_existent_perm_id = 99995

    response = admin_client.post(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{non_existent_perm_id}"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Permiso con ID {non_existent_perm_id} no encontrado" in response.json()["detail"]

def test_assign_permission_forbidden_non_admin(
    vendedor_client: TestClient, # Cliente no admin
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba que un no-admin no puede asignar permisos (403)."""
    response = vendedor_client.post(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'asignar:permiso_rol'" in response.json()["detail"]





# --- Tests para Quitar Permisos de Roles (DELETE /roles/{rol_id}/permisos/{permiso_id}) ---

def test_remove_permission_from_role_success_admin(
    admin_client: TestClient,
    db_session: Session,
    vendedor_role_id: int,
    permiso_leer_cliente_id: int # Usaremos el permiso que asignamos/existe por defecto
):
    """Prueba quitar exitosamente un permiso asignado a un rol como admin."""
    # 1. Asegurarse de que el permiso está asignado (ya sea por seeding o test anterior)
    #    Para aislar el test, lo asignamos explícitamente aquí.
    assign_response = admin_client.post(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT], "Fallo al asegurar asignación previa"

    # 2. Ejecutar la petición DELETE para quitar la asignación
    response_delete = admin_client.delete(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    # 3. Verificar respuesta HTTP (204 No Content para DELETE exitoso)
    assert response_delete.status_code == status.HTTP_204_NO_CONTENT
    # El cuerpo de la respuesta 204 está vacío

    # 4. Verificar en la BD que la asignación ya no existe (opcional pero recomendado)
    db_session.commit() # Asegurar commit de la operación DELETE
    db_session.expire_all()
    db_rol = rol_repository.get_rol_with_permissions(db=db_session, rol_id=vendedor_role_id)
    assert db_rol is not None
    permiso_ids_en_db = {p.id for p in db_rol.permisos}
    assert permiso_leer_cliente_id not in permiso_ids_en_db, "El permiso todavía se encontró en la relación del rol en la BD."

def test_remove_permission_not_assigned_admin(
    admin_client: TestClient,
    vendedor_role_id: int,
    permiso_gestionar_usuario_id: int # Fixture para permiso que Vendedor no tiene
):
    """Prueba que quitar un permiso no asignado falle (404)."""
    # Asegurarnos que 'gestionar:usuario' no está asignado a Vendedor
    # (lo cual es el caso por defecto según initial_data.py)

    # Intentar quitar la asignación (que no existe)
    response = admin_client.delete(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_gestionar_usuario_id}"
    )

    # Verificar respuesta HTTP 404
    assert response.status_code == status.HTTP_404_NOT_FOUND
    data = response.json()
    assert "detail" in data
    assert "no está asignado al rol" in data["detail"]

def test_remove_permission_role_not_found_admin(
    admin_client: TestClient,
    permiso_leer_cliente_id: int
):
    """Prueba quitar permiso desde un rol inexistente (404)."""
    non_existent_role_id = 99996

    response = admin_client.delete(
        f"{ROLES_ENDPOINT}/{non_existent_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    # El servicio primero busca el rol, así que el error será de rol no encontrado
    assert f"Rol con ID {non_existent_role_id} no encontrado" in response.json()["detail"]

def test_remove_permission_permission_not_found_admin(
    admin_client: TestClient,
    vendedor_role_id: int
):
    """Prueba quitar un permiso inexistente de un rol válido (404)."""
    non_existent_perm_id = 99995

    response = admin_client.delete(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{non_existent_perm_id}"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    # El servicio también busca el permiso, así que el error será de permiso no encontrado
    assert f"Permiso con ID {non_existent_perm_id} no encontrado" in response.json()["detail"]

def test_remove_permission_forbidden_non_admin(
    admin_client: TestClient,      # Fixture admin (ahora gestiona su header)
    vendedor_client: TestClient,   # Fixture vendedor (ahora gestiona su header)
    # Ya no necesitamos admin_token ni vendedor_token aquí
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba que un no-admin no puede quitar permisos (403)."""
    # 1. Asegurarse que el permiso está asignado usando el admin_client
    #    (la fixture admin_client ahora asegura el header correcto)
    assign_response = admin_client.post( # <-- Usa admin_client, la fixture pone el header
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT], \
        "Fallo al asegurar la asignación previa con admin_client"

    # 2. Intentar quitar con el cliente Vendedor
    #    (la fixture vendedor_client ahora asegura el header correcto)
    response = vendedor_client.delete( # <-- Usa vendedor_client, la fixture pone el header
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    # 3. Verificar 403 Forbidden y el mensaje de permiso específico
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'remover:permiso_rol'" in response.json()["detail"]
