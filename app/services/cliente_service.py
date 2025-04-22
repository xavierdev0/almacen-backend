# app/services/cliente_service.py
import logging
from typing import Optional, Sequence

from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError # Para capturar errores del repo

# Importar Repositorio, Modelo y Schemas
from app.repositories import cliente_repository
from app.models.client_model import Cliente
from app.schemas.client_schema import ClienteCreate, ClienteUpdate

logger = logging.getLogger(__name__)

# =======================================
#  Funciones del Servicio para Clientes
# =======================================

def create_cliente_service(db: Session, *, cliente_in: ClienteCreate) -> Cliente:
    """
    Crea un nuevo cliente, realizando validaciones previas.

    Args:
        db: Sesión de base de datos.
        cliente_in: Datos del cliente a crear (Schema ClienteCreate).

    Returns:
        El objeto Cliente creado.

    Raises:
        HTTPException 409: Si el email o la identificación fiscal ya existen.
        HTTPException 500: Para otros errores inesperados.
    """
    logger.info(f"Servicio: Intentando crear cliente: Nombre='{cliente_in.nombre}'")

    # --- Validación de Duplicados (ANTES de llamar al repositorio) ---
    if cliente_in.identificacion_fiscal:
        existing_by_id = cliente_repository.get_cliente_by_identificacion(
            db, identificacion=cliente_in.identificacion_fiscal
        )
        if existing_by_id:
            logger.warning(f"Conflicto: Identificación fiscal '{cliente_in.identificacion_fiscal}' ya existe.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"La identificación fiscal '{cliente_in.identificacion_fiscal}' ya está registrada."
            )

    if cliente_in.email:
        existing_by_email = cliente_repository.get_cliente_by_email(db, email=cliente_in.email)
        if existing_by_email:
            logger.warning(f"Conflicto: Email '{cliente_in.email}' ya existe.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"El correo electrónico '{cliente_in.email}' ya está registrado."
            )
    # --- Fin Validación Duplicados ---

    try:
        # Convertir schema a modelo para el repositorio
        # model_dump() es de Pydantic v2, usar .dict() si es v1
        cliente_data = Cliente.model_validate(cliente_in) 

        # Llamar al repositorio para crear
        new_cliente = cliente_repository.create_cliente(db=db, cliente_data=cliente_data)
        return new_cliente

    except IntegrityError as e: # Por si acaso hay una race condition o error no capturado antes
        db.rollback()
        logger.error(f"Error de Integridad (inesperado) al crear cliente '{cliente_in.nombre}': {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conflicto de datos al intentar guardar el cliente. Verifique identificación y email."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al crear cliente '{cliente_in.nombre}': {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el cliente."
        )


def get_cliente_by_id_service(db: Session, *, cliente_id: int) -> Cliente:
    """
    Obtiene un cliente por su ID.

    Args:
        db: Sesión de base de datos.
        cliente_id: ID del cliente a buscar.

    Returns:
        El objeto Cliente encontrado.

    Raises:
        HTTPException 404: Si el cliente no se encuentra.
        HTTPException 500: Para otros errores inesperados.
    """
    logger.debug(f"Servicio: Buscando cliente con ID: {cliente_id}")
    try:
        cliente = cliente_repository.get_cliente_by_id(db=db, cliente_id=cliente_id)
        if not cliente:
            logger.warning(f"Servicio: Cliente con ID {cliente_id} no encontrado.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cliente con ID {cliente_id} no encontrado."
            )
        return cliente
    except HTTPException: # Re-lanzar 404
        raise
    except Exception as e:
        logger.error(f"Error inesperado en servicio al buscar cliente ID {cliente_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al buscar el cliente."
        )

def get_clientes_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[Cliente]:
    """
    Obtiene una lista paginada de clientes.

    Args:
        db: Sesión de base de datos.
        skip: Número de clientes a saltar.
        limit: Número máximo de clientes a devolver.

    Returns:
        Una secuencia (lista) de objetos Cliente.

    Raises:
        HTTPException 500: Para errores inesperados.
    """
    logger.debug(f"Servicio: Listando clientes con skip={skip}, limit={limit}")
    try:
        clientes = cliente_repository.list_clientes(db=db, skip=skip, limit=limit)
        return clientes
    except Exception as e:
        logger.error(f"Error inesperado en servicio al listar clientes: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al listar clientes."
        )

def update_cliente_service(db: Session, *, cliente_id: int, cliente_in: ClienteUpdate) -> Cliente:
    """
    Actualiza un cliente existente, realizando validaciones previas.

    Args:
        db: Sesión de base de datos.
        cliente_id: ID del cliente a actualizar.
        cliente_in: Datos con los campos a actualizar (Schema ClienteUpdate).

    Returns:
        El objeto Cliente actualizado.

    Raises:
        HTTPException 404: Si el cliente original no se encuentra.
        HTTPException 409: Si la actualización causa conflicto de email o identificación.
        HTTPException 500: Para otros errores inesperados.
    """
    logger.info(f"Servicio: Intentando actualizar cliente ID: {cliente_id}")

    # 1. Obtener el cliente existente
    db_cliente = get_cliente_by_id_service(db=db, cliente_id=cliente_id) # Reutiliza la función que maneja 404

    # 2. Preparar datos y validar conflictos si cambian campos UNIQUE
    # model_dump con exclude_unset=True es de Pydantic v2
    # usar .dict(exclude_unset=True) si es Pydantic v1
    update_data = cliente_in.model_dump(exclude_unset=True)

    if not update_data:
         logger.warning(f"Servicio: No se proporcionaron datos para actualizar cliente ID {cliente_id}.")
         # No es un error, simplemente no hay nada que hacer.
         # Se podría devolver el cliente sin cambios o lanzar 400 Bad Request.
         # Devolver sin cambios parece razonable.
         return db_cliente

    # Validar conflicto de identificación si se intenta cambiar
    new_identificacion = update_data.get("identificacion_fiscal")
    if new_identificacion is not None and new_identificacion != db_cliente.identificacion_fiscal:
        existing_by_id = cliente_repository.get_cliente_by_identificacion(db, identificacion=new_identificacion)
        # Si existe OTRO cliente con esa identificación
        if existing_by_id and existing_by_id.id != cliente_id:
            logger.warning(f"Conflicto al actualizar: Nueva identificación '{new_identificacion}' ya pertenece a cliente ID {existing_by_id.id}.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"La identificación fiscal '{new_identificacion}' ya está registrada por otro cliente."
            )

    # Validar conflicto de email si se intenta cambiar
    new_email = update_data.get("email")
    if new_email is not None and new_email != db_cliente.email:
        existing_by_email = cliente_repository.get_cliente_by_email(db, email=new_email)
         # Si existe OTRO cliente con ese email
        if existing_by_email and existing_by_email.id != cliente_id:
            logger.warning(f"Conflicto al actualizar: Nuevo email '{new_email}' ya pertenece a cliente ID {existing_by_email.id}.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"El correo electrónico '{new_email}' ya está registrado por otro cliente."
            )

    # 3. Llamar al repositorio para actualizar
    try:
        updated_cliente = cliente_repository.update_cliente(
            db=db, db_cliente=db_cliente, update_data=update_data
        )
        return updated_cliente
    except IntegrityError as e: # Por si acaso hay una race condition o error no capturado antes
        db.rollback()
        logger.error(f"Error de Integridad (inesperado) al actualizar cliente ID {cliente_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conflicto de datos al intentar guardar la actualización del cliente."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al actualizar cliente ID {cliente_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al actualizar el cliente."
        )


def delete_cliente_service(db: Session, *, cliente_id: int) -> Cliente:
    """
    Elimina un cliente por su ID, manejando posibles errores de dependencia.

    Args:
        db: Sesión de base de datos.
        cliente_id: ID del cliente a eliminar.

    Returns:
        El objeto Cliente que fue eliminado.

    Raises:
        HTTPException 404: Si el cliente no se encuentra.
        HTTPException 409: Si el cliente no puede ser eliminado debido a
                           dependencias (pedidos, facturas).
        HTTPException 500: Para otros errores inesperados.
    """
    logger.info(f"Servicio: Intentando eliminar cliente ID: {cliente_id}")

    # 1. Asegurarse que el cliente existe (get_cliente_by_id_service ya maneja 404)
    cliente_to_delete = get_cliente_by_id_service(db=db, cliente_id=cliente_id)

    # 2. Intentar eliminar usando el repositorio
    try:
        deleted_cliente = cliente_repository.delete_cliente(db=db, cliente_id=cliente_id)
        # El repositorio devuelve None si no lo encontró, pero ya lo verificamos antes.
        # Sin embargo, es bueno tener un check por si acaso.
        if deleted_cliente is None:
             # Esto no debería ocurrir si get_cliente_by_id_service funcionó
             logger.error(f"Inconsistencia: Cliente ID {cliente_id} encontrado pero delete_cliente devolvió None.")
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno inconsistente al eliminar cliente.")
        return deleted_cliente # Devolver el objeto eliminado
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"No se pudo eliminar cliente ID {cliente_id} debido a dependencias (ON DELETE RESTRICT): {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"No se puede eliminar el cliente ID {cliente_id} porque tiene pedidos o facturas asociadas."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al eliminar cliente ID {cliente_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al eliminar el cliente."
        )