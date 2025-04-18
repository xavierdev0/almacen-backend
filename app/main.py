# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.api.v1.api import api_router_v1
from app.core.database import engine
from sqlmodel import SQLModel
import logging

from app.api.v1.api import api_router_v1 # Importa el router de la v1
from app.core.config import settings    # Importa la configuración

app = FastAPI(
    title=settings.PROJECT_NAME,
    #description=settings.PROJECT_DESCRIPTION,
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)




app.include_router(api_router_v1, prefix=settings.API_V1_STR)