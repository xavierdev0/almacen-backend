# app/api/v1/api.py
from fastapi import APIRouter
# Importar los routers existentes y los nuevos
from app.api.v1.endpoints import auth, usuarios, roles, permisos, clientes, inventario, service

api_router_v1 = APIRouter()

# --- Autenticación ---
api_router_v1.include_router(
    auth.router,
    responses={401: {"description": "Credenciales inválidas"}}
)

# --- Usuarios ---
api_router_v1.include_router(
    usuarios.router,
    responses={
        403: {"description": "Permisos insuficientes"},
        404: {"description": "Usuario no encontrado"}
    }
)


# --- Clientes --- # <--- 2. AÑADIR ESTA SECCIÓN
api_router_v1.include_router(
    clientes.router 
)

# --- Roles (Admin) ---
# Incluimos el router definido en endpoints/roles.py
api_router_v1.include_router(
    roles.router,
)


# --- Servicios --- # <--- 
api_router_v1.include_router(
    service.router # Incluir el router que definimos en servicios.py
)



# --- Permisos (Admin) ---
# Incluimos el router definido en endpoints/permisos.py
api_router_v1.include_router(
    permisos.router
)

api_router_v1.include_router(
    inventario.router 
)