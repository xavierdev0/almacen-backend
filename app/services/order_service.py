# app/services/order_service.py

import datetime
import logging
from typing import Optional, Sequence, Tuple# Sequence es preferible para listas de retorno
from sqlmodel import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError # Para capturar errores del repo

# Importar Repositorios
from app.repositories import order_repository, cliente_repository # Necesitamos cliente_repo para validar

# Importar Modelos y Schemas
from app.models.order_models import PedidoCliente, Proforma
from app.schemas.order_schema import PedidoClienteCreate, PedidoClienteRead, ProformaUpdate # Usamos Create para entrada

logger = logging.getLogger(__name__)

# =======================================
# Funciones del Servicio para PedidoCliente
# =======================================

def create_pedido_service(
    db: Session, *, pedido_in: PedidoClienteCreate, vendedor_id: int
) -> PedidoCliente:
    """
    Crea un nuevo PedidoCliente, validando la existencia del cliente
    y asignando el vendedor autenticado.

    Args:
        db: La sesión de base de datos activa.
        pedido_in: Datos de entrada validados por el schema PedidoClienteCreate.
                   Solo contiene cliente_id.
        vendedor_id: ID del usuario (vendedor) autenticado que crea el pedido.

    Returns:
        El objeto PedidoCliente recién creado.

    Raises:
        HTTPException 404: Si el cliente_id proporcionado no existe.
        HTTPException 409: Si ocurre un conflicto inesperado al guardar (ej. FK vendedor inválida).
        HTTPException 500: Para otros errores internos inesperados.
    """
    logger.info(f"Servicio: Intentando crear PedidoCliente para Cliente ID: {pedido_in.cliente_id} por Vendedor ID: {vendedor_id}")

    # 1. Validar que el cliente existe
    cliente = cliente_repository.get_cliente_by_id(db=db, cliente_id=pedido_in.cliente_id)
    if not cliente:
        logger.warning(f"Cliente con ID {pedido_in.cliente_id} no encontrado al intentar crear pedido.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {pedido_in.cliente_id} no encontrado."
        )
    logger.debug(f"Cliente ID {pedido_in.cliente_id} validado: {cliente.nombre}")

    # 2. Preparar el objeto del modelo PedidoCliente
    #    Se asigna el vendedor_id y el estado inicial.
    pedido_data_dict = pedido_in.model_dump() # Obtener dict del schema de entrada
    pedido_model_instance = PedidoCliente(
        **pedido_data_dict, # Pasa cliente_id
        usuario_id_vendedor=vendedor_id,
        estado="NUEVO" # Estado inicial por defecto
        # fecha_creacion y fecha_ultima_actualizacion son manejadas por el modelo/DB
    )

    # 3. Intentar crear usando el repositorio
    try:
        nuevo_pedido = order_repository.create_pedido(db=db, pedido_data=pedido_model_instance)
        # Opcional: Cargar relaciones para devolver más info (si PedidoClienteRead lo requiere)
        # db.refresh(nuevo_pedido, attribute_names=["cliente", "vendedor"])
        try:
            logger.info(f"Creando proformas iniciales para Pedido ID: {nuevo_pedido.id}")
            create_initial_proformas_for_pedido(db=db, pedido_id=nuevo_pedido.id, creador_id=vendedor_id)
            # Refrescar el pedido para cargar la relación proformas recién creada
            db.refresh(nuevo_pedido, attribute_names=["proformas"])
            logger.info(f"Proformas iniciales creadas y pedido refrescado para Pedido ID: {nuevo_pedido.id}")
        except Exception as proforma_exc:
             # Si falla la creación de proformas, idealmente se debería hacer rollback de la creación del pedido,
             # pero por simplicidad aquí solo loggeamos el error y continuamos.
             # En un sistema real, se requeriría una transacción más robusta o manejo compensatorio.
            logger.error(f"Error al crear proformas iniciales para Pedido ID {nuevo_pedido.id}: {proforma_exc}", exc_info=True)
            # No relanzar la excepción aquí para que la creación del pedido no falle si solo fallan las proformas (decisión de diseño)
        # --- FIN: Crear Proformas Iniciales ---
        return nuevo_pedido
    
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al crear pedido para cliente {pedido_in.cliente_id}: {e}", exc_info=True)
        # Podría ser un problema con vendedor_id si no se validó antes (aunque viene del token)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se pudo crear el pedido debido a un conflicto de datos (verifique cliente y vendedor)."
        )
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de DB al crear pedido para cliente {pedido_in.cliente_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el pedido [DB]."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al crear pedido para cliente {pedido_in.cliente_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el pedido [General]."
        )


def get_pedido_service(db: Session, *, pedido_id: int, load_related: bool = True) -> PedidoCliente:
    """
    Obtiene un PedidoCliente por su ID, cargando relaciones por defecto.

    Args:
        db: La sesión de base de datos activa.
        pedido_id: El ID del pedido a buscar.
        load_related: Si cargar relaciones (cliente, vendedor, proformas). True por defecto.

    Returns:
        El objeto PedidoCliente encontrado.

    Raises:
        HTTPException 404: Si el pedido no se encuentra.
        HTTPException 500: Para otros errores internos inesperados.
    """
    logger.debug(f"Servicio: Buscando PedidoCliente ID: {pedido_id}")
    try:
        pedido = order_repository.get_pedido_by_id(db=db, pedido_id=pedido_id, load_related=load_related)
        if not pedido:
            logger.warning(f"PedidoCliente con ID {pedido_id} no encontrado.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pedido con ID {pedido_id} no encontrado."
            )
        logger.info(f"PedidoCliente ID {pedido_id} encontrado.")
        return pedido
    except HTTPException: # Re-lanzar 404
        raise
    except SQLAlchemyError as e:
         logger.error(f"Error de DB al buscar PedidoCliente ID {pedido_id}: {e}", exc_info=True)
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Error interno del servidor al buscar el pedido [DB]."
         )
    except Exception as e:
        logger.error(f"Error inesperado al buscar PedidoCliente ID {pedido_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al buscar el pedido [General]."
        )

def list_pedidos_service(
    db: Session, *,
    skip: int = 0,
    limit: int = 100,
    cliente_id: Optional[int] = None,
    vendedor_id: Optional[int] = None,
    estado: Optional[str] = None,
    load_related: bool = True # Cargar cliente/vendedor por defecto para listas
) -> Sequence[PedidoCliente]:
    """
    Lista PedidoCliente con filtros y paginación, cargando relaciones por defecto.

    Args:
        db: Sesión de BD.
        skip: Registros a saltar.
        limit: Máximo de registros.
        cliente_id: Filtrar por cliente (opcional).
        vendedor_id: Filtrar por vendedor (opcional).
        estado: Filtrar por estado (opcional).
        load_related: Si cargar cliente/vendedor (True por defecto).

    Returns:
        Una secuencia de objetos PedidoCliente.

    Raises:
        HTTPException 500: Error interno.
    """
    logger.debug(f"Servicio: Listando PedidoCliente - skip:{skip}, limit:{limit}, cliente:{cliente_id}, vendedor:{vendedor_id}, estado:{estado}, related:{load_related}")
    try:
        pedidos = order_repository.list_pedidos(
            db=db,
            skip=skip,
            limit=limit,
            cliente_id=cliente_id,
            vendedor_id=vendedor_id,
            estado=estado,
            load_related=load_related
        )
        return pedidos
    except SQLAlchemyError as e:
         logger.error(f"Error de DB al listar PedidoCliente: {e}", exc_info=True)
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Error interno del servidor al listar pedidos [DB]."
         )
    except Exception as e:
        logger.error(f"Error inesperado al listar PedidoCliente: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al listar pedidos [General]."
        )


# (Aquí añadiremos funciones para Proformas, Líneas, Ordenes en fases posteriores)



# =======================================
# Funciones del Servicio para Proforma (NUEVAS)
# =======================================

def _link_proformas(db: Session, *, proforma1: Proforma, proforma2: Proforma) -> None:
    """
    Función helper interna para vincular dos proformas entre sí.
    Actualiza el campo proforma_vinculada_id en ambos registros.
    """
    logger.debug(f"Servicio: Vinculando Proforma ID {proforma1.id} y Proforma ID {proforma2.id}")
    try:
        # Actualizar proforma1 para que apunte a proforma2
        order_repository.update_proforma(
            db=db,
            db_proforma=proforma1,
            update_data={"proforma_vinculada_id": proforma2.id}
        )
        # Actualizar proforma2 para que apunte a proforma1
        order_repository.update_proforma(
            db=db,
            db_proforma=proforma2,
            update_data={"proforma_vinculada_id": proforma1.id}
        )
        logger.info(f"Proformas ID {proforma1.id} y ID {proforma2.id} vinculadas exitosamente.")
    except Exception as e:
        # Si falla la vinculación, las proformas quedan creadas pero desvinculadas.
        # Podríamos intentar rollback aquí, pero la creación ya hizo commit.
        # Loggear el error es importante.
        logger.error(f"Error al intentar vincular proformas {proforma1.id} y {proforma2.id}: {e}", exc_info=True)
        # Relanzar para que la función llamadora lo sepa, aunque no haremos rollback completo aquí.
        raise e


def create_initial_proformas_for_pedido(
    db: Session, *, pedido_id: int, creador_id: int
) -> Tuple[Proforma, Proforma]:
    """
    Crea el par inicial de proformas (PRODUCTO y SERVICIO) para un pedido dado
    y las vincula entre sí.

    Args:
        db: La sesión de base de datos activa.
        pedido_id: ID del PedidoCliente al que asociar las proformas.
        creador_id: ID del Usuario (Vendedor/Admin) que crea las proformas.

    Returns:
        Una tupla conteniendo las dos proformas creadas: (proforma_producto, proforma_servicio).

    Raises:
        HTTPException 404: Si el pedido_id no existe.
        HTTPException 409: Si ya existen proformas para ese pedido_id.
        HTTPException 500: Para otros errores internos.
    """
    logger.info(f"Servicio: Intentando crear proformas iniciales para Pedido ID: {pedido_id} por Creador ID: {creador_id}")

    # 1. Validar que el pedido existe (reutilizamos get_pedido_service)
    #    No necesitamos cargar relaciones aquí, solo confirmar existencia.
    get_pedido_service(db=db, pedido_id=pedido_id, load_related=False)

    # 2. Verificar si ya existen proformas para este pedido
    existing_proformas = order_repository.list_proformas_by_pedido(db=db, pedido_id=pedido_id)
    if existing_proformas:
        logger.warning(f"Intento de crear proformas iniciales para Pedido ID {pedido_id}, pero ya existen {len(existing_proformas)}.")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El pedido con ID {pedido_id} ya tiene proformas asociadas."
        )

    try:
        # 3. Crear proforma de Productos
        proforma_prod_data = Proforma(
            pedido_cliente_id=pedido_id,
            tipo="PRODUCTO",
            usuario_id_creador=creador_id,
            estado="BORRADOR"
            # El resto de campos toman defaults del modelo
        )
        proforma_prod = order_repository.create_proforma(db=db, proforma_data=proforma_prod_data)

        # 4. Crear proforma de Servicios
        proforma_serv_data = Proforma(
            pedido_cliente_id=pedido_id,
            tipo="SERVICIO",
            usuario_id_creador=creador_id,
            estado="BORRADOR"
        )
        proforma_serv = order_repository.create_proforma(db=db, proforma_data=proforma_serv_data)

        # 5. Vincular ambas proformas
        _link_proformas(db=db, proforma1=proforma_prod, proforma2=proforma_serv)

        logger.info(f"Proformas iniciales creadas y vinculadas para Pedido ID {pedido_id}: ProdID={proforma_prod.id}, ServID={proforma_serv.id}")
        return proforma_prod, proforma_serv

    except Exception as e:
        # Si algo falla después de crear alguna proforma pero antes de terminar,
        # el rollback aquí podría no ser efectivo si create_proforma hizo commit.
        # Esto resalta la necesidad de gestionar transacciones de forma más explícita
        # si se requiere atomicidad completa para este proceso.
        db.rollback() # Intentar rollback de la sesión actual
        logger.error(f"Error al crear/vincular proformas iniciales para Pedido ID {pedido_id}: {e}", exc_info=True)
        # Determinar el código de error apropiado (podría ser 500 o uno más específico si se conoce la causa)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear las proformas iniciales."
        )


def get_proforma_service(db: Session, *, proforma_id: int, load_related: bool = True) -> Proforma:
    """
    Obtiene una Proforma por su ID, cargando relaciones por defecto.

    Args:
        db: La sesión de base de datos activa.
        proforma_id: El ID de la proforma a buscar.
        load_related: Si cargar relaciones (pedido, creador, lineas). True por defecto.

    Returns:
        El objeto Proforma encontrado.

    Raises:
        HTTPException 404: Si la proforma no se encuentra.
        HTTPException 500: Para otros errores internos inesperados.
    """
    logger.debug(f"Servicio: Buscando Proforma ID: {proforma_id}")
    try:
        proforma = order_repository.get_proforma_by_id(db=db, proforma_id=proforma_id, load_related=load_related)
        if not proforma:
            logger.warning(f"Proforma con ID {proforma_id} no encontrada.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Proforma con ID {proforma_id} no encontrada."
            )
        logger.info(f"Proforma ID {proforma_id} encontrada.")
        return proforma
    except HTTPException: # Re-lanzar 404
        raise
    except SQLAlchemyError as e:
         logger.error(f"Error de DB al buscar Proforma ID {proforma_id}: {e}", exc_info=True)
         raise HTTPException(status_code=500, detail="Error DB [GPSF]") # noqa
    except Exception as e:
        logger.error(f"Error inesperado al buscar Proforma ID {proforma_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error General [GPSF]") # noqa


def update_proforma_service(
    db: Session, *, proforma_id: int, proforma_in: ProformaUpdate
) -> Proforma:
    """
    Actualiza campos específicos de una Proforma (ej: estado, notas).

    Args:
        db: La sesión de base de datos activa.
        proforma_id: ID de la proforma a actualizar.
        proforma_in: Objeto ProformaUpdate con los campos a actualizar.

    Returns:
        El objeto Proforma actualizado.

    Raises:
        HTTPException 404: Si la proforma no se encuentra.
        HTTPException 400: Si la transición de estado no es válida (TODO).
        HTTPException 500: Para otros errores internos.
    """
    logger.info(f"Servicio: Intentando actualizar Proforma ID: {proforma_id}")

    # 1. Obtener la proforma existente (maneja 404 si no existe)
    #    No necesitamos cargar todas las relaciones para una simple actualización de estado/notas.
    db_proforma = get_proforma_service(db=db, proforma_id=proforma_id, load_related=False)

    # 2. Preparar los datos de actualización (solo campos enviados)
    update_data = proforma_in.model_dump(exclude_unset=True)

    if not update_data:
        logger.warning(f"No se proporcionaron datos para actualizar Proforma ID {proforma_id}. No se realiza ninguna acción.")
        return db_proforma # Devolver sin cambios si no hay nada que actualizar

    # 3. Validación de Lógica de Negocio (Ej: Transición de Estados)
    #    Si se está cambiando el estado, validar si la transición es permitida.
    new_estado = update_data.get("estado")
    if new_estado and new_estado != db_proforma.estado:
        logger.info(f"Intentando cambiar estado de Proforma ID {proforma_id} de '{db_proforma.estado}' a '{new_estado}'")
        # --- INICIO: Lógica de Transición (Simplificada) ---
        # TODO: Implementar reglas de transición de estado más robustas según el flujo definido.
        # Ejemplo básico: Solo permitir pasar de BORRADOR a PENDIENTE_APROBACION por ahora.
        allowed_transitions = {
            "BORRADOR": ["PENDIENTE_APROBACION", "CANCELADA"],
            "PENDIENTE_APROBACION": ["APROBADA", "RECHAZADA", "CANCELADA", "POSPUESTA"],
            "POSPUESTA": ["PENDIENTE_APROBACION", "CANCELADA", "EXPIRADA"] # Expirada podría ser un proceso automático
            # Añadir más transiciones permitidas...
        }
        if db_proforma.estado not in allowed_transitions or new_estado not in allowed_transitions.get(db_proforma.estado, []):
             logger.warning(f"Transición de estado inválida para Proforma ID {proforma_id}: de '{db_proforma.estado}' a '{new_estado}'.")
             raise HTTPException(
                 status_code=status.HTTP_400_BAD_REQUEST, # 400 Bad Request o 409 Conflict son opciones
                 detail=f"No se puede cambiar el estado de la proforma de '{db_proforma.estado}' a '{new_estado}'."
             )
        # Si el nuevo estado es APROBADA, actualizar fecha_aprobacion
        if new_estado == "APROBADA":
            update_data['fecha_aprobacion'] = datetime.utcnow() # O usar datetime.now(timezone.utc)
        # --- FIN: Lógica de Transición ---

    # 4. Llamar al repositorio para actualizar
    try:
        updated_proforma = order_repository.update_proforma(
            db=db, db_proforma=db_proforma, update_data=update_data
        )
        return updated_proforma
    except IntegrityError as e: # Poco probable aquí a menos que FK proforma_vinculada_id sea inválido
        db.rollback(); logger.error(f"Error de integridad al actualizar proforma ID {proforma_id}: {e}", exc_info=True); raise HTTPException(status_code=409, detail="Conflicto datos [USP]") # noqa
    except SQLAlchemyError as e:
        db.rollback(); logger.error(f"Error DB al actualizar proforma ID {proforma_id}: {e}", exc_info=True); raise HTTPException(status_code=500, detail="Error DB [USP]") # noqa
    except Exception as e:
        db.rollback(); logger.error(f"Error inesperado al actualizar proforma ID {proforma_id}: {e}", exc_info=True); raise HTTPException(status_code=500, detail="Error General [USP]") # noqa

# (Aquí añadiríamos funciones para añadir/quitar líneas, etc.)
