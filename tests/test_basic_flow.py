import pytest
from fastapi.testclient import TestClient
from fastapi import status
from sqlmodel import Session # Importar Session, aunque la fixture la maneja

from app.core.config import settings # Para construir las URLs de API

# --- Datos para el nuevo usuario ---
# Usa un username que cumpla las reglas (minúsculas, números, _)
test_username = "usuario_test"
test_email = "usuario_test@test.com"
test_password = "a_simple_password123"

def test_create_and_login_flow(client: TestClient, db_session: Session):
    """
    Verifica la creación de un usuario y el login exitoso posterior.
    """
    # 1. Crear el Usuario
    user_data = {
        "email": test_email,
        "username": test_username,
        "password": test_password,
        "nombre_completo": "Basic User Test",
    }
    create_response = client.post(
        f"{settings.API_V1_STR}/usuarios", # URL para crear usuario
        json=user_data
    )

    # Verificar Creación Exitosa
    assert create_response.status_code == status.HTTP_201_CREATED
    created_user_data = create_response.json()
    assert created_user_data["email"] == test_email
    assert created_user_data["username"] == test_username
    assert "id" in created_user_data # Asegurar que se asignó un ID
    print(f"Usuario creado con ID: {created_user_data['id']}") # Log simple para consola

    # 2. Intentar Login con el usuario creado
    login_data = {
        "username": test_username, # Usa el username creado
        "password": test_password, # Usa la contraseña correcta
    }
    login_response = client.post(
        f"{settings.API_V1_STR}/auth/token", # URL para obtener token
        data=login_data # FastAPI espera form data para OAuth2PasswordRequestForm
    )

    # Verificar Login Exitoso
    assert login_response.status_code == status.HTTP_200_OK
    token_data = login_response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
    print("Login exitoso con el nuevo usuario.")

def test_login_failure_wrong_password(client: TestClient, db_session: Session):
    """
    Verifica que el login falle con contraseña incorrecta.
    (Asume que el usuario del test anterior ya existe o crea uno nuevo)
    """
    # Asegurémonos de que el usuario existe (podría crearlo aquí si los tests no corren en orden)
    # Este test es más robusto si crea su propio usuario, pero para simplicidad
    # asumimos que el test anterior se ejecutó o que el usuario ya existe
    # desde una ejecución previa si la BD no se limpia entre tests individuales.
    # ¡Para tests reales, es mejor aislar creando el usuario aquí!

    login_data = {
        "username": test_username, # Usa el username del usuario que debería existir
        "password": "this_is_wrong_password", # Contraseña INCORRECTA
    }
    response = client.post(
        f"{settings.API_V1_STR}/auth/token",
        data=login_data
    )

    # Verificar Falla de Login
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    error_data = response.json()
    # Verifica que el detalle del error sea el esperado (puede variar ligeramente)
    assert "Credenciales inválidas" in error_data.get("detail", "")
    print("Fallo de login con contraseña incorrecta verificado.")