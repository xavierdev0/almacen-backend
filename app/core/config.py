# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    PROJECT_NAME: str
    API_V1_STR: str
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:8000", "http://localhost:3000"]  # Valores predeterminados
    model_config = SettingsConfigDict(env_file=".env")  # Carga variables desde .env

settings = Settings() # Crea una instancia de la clase Settings