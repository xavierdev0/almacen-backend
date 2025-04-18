# app/api/v1/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from datetime import timedelta
import logging
from typing import Annotated

from app.core.database import get_db
from app.core.security import create_access_token
from app.core.config import settings
from app.services import auth_service
from app.schemas.token_schema import Token

router = APIRouter(prefix="/auth",tags=["Autenticación"]) 
logger = logging.getLogger(__name__)

@router.post("/token", response_model=Token)
async def login_for_access_token(
    request: Request,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)]
):
    """Endpoint de autenticación con JWT."""
    try:
        # Log seguro y trazabilidad
        client_ip = request.client.host if request.client else "unknown"
        logger.info(
            f"Intento de login desde {client_ip}. Usuario: {form_data.username[:3]}***"
        )

        # Autenticación
        user = auth_service.authenticate_user(db, form_data.username, form_data.password)
        if not user:
            logger.warning(f"Fallo de autenticación desde {client_ip}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Generación de token con UUID como subject
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            subject=str(user.id),  
            expires_delta=access_token_expires
        )

        logger.info(f"Login exitoso para usuario ID: {user.id}")
        return {"access_token": access_token, "token_type": "bearer"}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en autenticación: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno durante la autenticación"
        )