# app/api/v1/api.py
from fastapi import APIRouter
from app.api.v1.endpoints import auth, usuarios

api_router_v1 = APIRouter()

# Incluye todos los routers de endpoints con metadatos
api_router_v1.include_router(
    auth.router,
    prefix="/auth",
    tags=["Autenticación"],
    responses={401: {"description": "Credenciales inválidas"}}
)

api_router_v1.include_router(
    usuarios.router,
    prefix="/usuarios",
    tags=["Usuarios"],
    responses={
        403: {"description": "Permisos insuficientes"},
        404: {"description": "Usuario no encontrado"}
    }
)