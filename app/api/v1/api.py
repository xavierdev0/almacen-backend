# app/api/v1/api.py
from fastapi import APIRouter
# Importar los routers existentes y los nuevos
from app.api.v1.endpoints import auth, usuarios, roles, permisos, clientes

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
    responses={ # Respuestas comunes para este grupo de endpoints
        403: {"description": "Acceso restringido (Requiere rol Admin por ahora)"},
        404: {"description": "Rol no encontrado"},
        409: {"description": "Conflicto de datos (ej: nombre duplicado, rol en uso)"}
    }
    # No necesitamos añadir la dependencia de seguridad aquí,
    # porque ya la aplicamos a nivel del router en roles.py
)

# --- Permisos (Admin) ---
# Incluimos el router definido en endpoints/permisos.py
api_router_v1.include_router(
    permisos.router,
    responses={ # Respuestas comunes para este grupo
        403: {"description": "Acceso restringido (Requiere rol Admin por ahora)"},
        404: {"description": "Permiso no encontrado"},
        409: {"description": "Conflicto de datos (ej: acción/recurso duplicado)"}
    }

)