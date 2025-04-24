# app/api/v1/endpoints/proformas.py

import logging
from typing import List, Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path
from sqlmodel import Session

# Importar dependencias necesarias
from app.api.deps import get_current_active_user, get_db, require_permission
# Importar el servicio correspondiente
from app.models.user_models import Usuario
from app.services import order_service
# Importar los schemas necesarios
from app.schemas.order_schema import ProformaRead, ProformaUpdate
# Importar el modelo Usuario (si se necesitara para current_user en otros endpoints)
# from app.models import Usuario

logger = logging.getLogger(__name__)

# Crear el router específico para proformas
router = APIRouter(
    prefix="/proformas", # Prefijo para todas las rutas de este router
    tags=["Proformas"],  # Etiqueta para agrupar en la documentación OpenAPI
    responses={ # Respuestas comunes
        404: {"description": "Proforma no encontrada"},
        403: {"description": "Permiso insuficiente"},
        401: {"description": "No autenticado"},
        400: {"description": "Solicitud inválida (ej: transición de estado no permitida)"},
        409: {"description": "Conflicto de datos"},
    }
)

# --- Endpoint para Obtener una Proforma por ID ---
@router.get(
    "/{proforma_id}", # Ruta: GET /api/v1/proformas/{proforma_id}
    response_model=ProformaRead,
    summary="Obtener Proforma por ID",
    description="Recupera los detalles de una proforma específica.",
    dependencies=[Depends(require_permission("leer:proforma"))] # Permiso requerido
)
def get_proforma_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    proforma_id: int = Path(..., description="ID de la Proforma a obtener", gt=0)
):
    """
    Endpoint para obtener los detalles de una Proforma específica.

    - Requiere permiso: `leer:proforma`.
    """
    logger.info(f"API: Solicitud para obtener Proforma ID: {proforma_id}")
    try:
        # Llama al servicio para obtener la proforma
        # El servicio maneja el 404 si no se encuentra
        # Pasamos load_related=True (valor por defecto) para que ProformaRead funcione
        proforma = order_service.get_proforma_service(db=db, proforma_id=proforma_id, load_related=True)
        return proforma
    except HTTPException as http_exc:
        logger.warning(f"HTTPException al obtener proforma ID {proforma_id}: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en endpoint get_proforma: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al obtener la proforma."
        )


@router.patch(
    "/{proforma_id}", # Ruta: PATCH /api/v1/proformas/{proforma_id}
    response_model=ProformaRead,
    summary="Actualizar Proforma (Parcial)",
    description="Actualiza parcialmente una proforma existente (ej: cambiar estado, añadir notas). Solo se modifican los campos incluidos en la solicitud.",
    # Definir un permiso genérico para actualizar proformas por ahora
    dependencies=[Depends(require_permission({
            "actualizar:proforma_propia",
            "actualizar:proforma_asignada",
            "actualizar:proforma_global"
            # Podríamos añadir 'cancelar:proforma', 'enviar:proforma', 'posponer:proforma' aquí
            # si queremos que este endpoint maneje esos cambios de estado también.
            # O crear endpoints separados para esas acciones semánticas.
        }))] # Permisos requeridos
)


def update_proforma_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    proforma_id: int = Path(..., description="ID de la Proforma a actualizar", gt=0),
    proforma_in: ProformaUpdate, # Cuerpo de la solicitud con campos opcionales
    current_user: Annotated[Usuario, Depends(get_current_active_user)] # Inyectar usuario actual
):
    """
    Endpoint PATCH para actualizar parcialmente una Proforma existente.

    - Requiere al menos uno de los siguientes permisos:
        - `actualizar:proforma_propia`
        - `actualizar:proforma_asignada`
        - `actualizar:proforma_global`
    - La lógica específica sobre qué campos puede modificar cada rol/permiso
      residiría idealmente en la capa de servicio.
    """
    logger.info(f"API: Solicitud PATCH para Proforma ID: {proforma_id} por Usuario ID: {current_user.id}")
    try:
        # Pasar current_user al servicio podría ser útil para lógica de negocio más fina
        # (ej: verificar si es el creador para 'proforma_propia')
        # Por ahora, el servicio update_proforma_service no lo usa, pero podría extenderse.
        updated_proforma = order_service.update_proforma_service(
            db=db,
            proforma_id=proforma_id,
            proforma_in=proforma_in
            # , current_user=current_user # Pasar si el servicio lo necesita
        )
        return updated_proforma
    except HTTPException as http_exc:
        logger.warning(f"HTTPException al actualizar proforma ID {proforma_id}: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en endpoint update_proforma: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al actualizar la proforma."
        )


# --- Endpoints Futuros para Proforma ---
# Aquí podríamos añadir endpoints como:
# PUT /proformas/{proforma_id} (para actualizar estado, notas) - Requerirá permiso 'actualizar:proforma_propia' o 'actualizar:proforma_asignada'
# POST /proformas/{proforma_id}/lineas-material (para añadir líneas)
# POST /proformas/{proforma_id}/lineas-servicio (para añadir líneas)
# DELETE /proformas/{proforma_id}/lineas-material/{linea_id} (para quitar líneas)
# ... etc ...