# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.api.v1.api import api_router_v1
from app.core.database import engine
from sqlmodel import SQLModel
import logging

# Configuración inicial de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    #description=settings.PROJECT_DESCRIPTION,
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    # contact={"name": settings.CONTACT_NAME,"email": settings.CONTACT_EMAIL},
    # license_info={ "name": settings.LICENSE_NAME}
)

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Total-Count"]  # Útil para paginación
)

# Eventos del ciclo de vida
@app.on_event("startup")
async def startup_event():
    logger.info("Iniciando aplicación...")
    SQLModel.metadata.create_all(engine)
    logger.info("Base de datos inicializada")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Apagando aplicación...")

# Endpoints principales
app.include_router(
    api_router_v1,
    prefix=settings.API_V1_STR,
    responses={
        500: {"description": "Error interno del servidor"}
    }
)

# Servir archivos estáticos (si es necesario)
# app.mount( f"{settings.API_V1_STR}/static",StaticFiles(directory="static"),name="static")

# Endpoint raíz
@app.get(
    "/",
    include_in_schema=False,
    summary="Endpoint de bienvenida"
)
def root():
    return {
        "message": "Bienvenido a la API de Gestión de Almacén",
        "version": "1.0.0",
        "documentation": {
            "swagger": f"{settings.API_V1_STR}/docs",
            "redoc": f"{settings.API_V1_STR}/redoc"
        }
    }

# Health Check
@app.get(
    "/health",
    tags=["Sistema"],
    summary="Verificar estado del servicio",
    response_description="Estado del servicio"
)
def health_check():
    return {"status": "ok", "details": "Servicio operativo"}


