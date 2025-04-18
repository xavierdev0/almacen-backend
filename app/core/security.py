# app/core/security.py
from datetime import datetime, timedelta, timezone
from typing import Optional, Any
import logging

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

# --- Configuración de logging ---
logger = logging.getLogger(__name__)

# --- Configuración de Hashing de Contraseñas ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Validación de configuración ---
if not settings.SECRET_KEY or settings.SECRET_KEY == "secret-key":
    logger.error("SECRET_KEY no está configurada correctamente")
    raise ValueError("Falta configuración de SECRET_KEY")

# --- Configuración de JWT ---
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

# --- Esquema OAuth2 ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

# --- Funciones de Contraseña ---
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# --- Funciones de JWT ---
def create_access_token(subject: str | Any, expires_delta: Optional[timedelta] = None) -> str:
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {
        "exp": expire,
        "iat": now,  # Tiempo de emisión
        "sub": str(subject),
        # Puedes añadir más claims aquí (ej: roles, iss, aud)
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def decode_access_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Validación adicional de claims
        if not all(key in payload for key in ["exp", "iat", "sub"]):
            logger.warning("Token con claims incompletos")
            return None
            
        subject: str = payload.get("sub")
        return subject
    except JWTError as e:
        logger.error(f"Error de JWT: {str(e)}")
        return None