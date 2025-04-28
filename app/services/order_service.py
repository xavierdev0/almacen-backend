# app/services/order_service.py

import datetime
from decimal import Decimal, ROUND_HALF_UP # Asegurar Decimal
import logging
from typing import Any, Optional, Sequence, Tuple, List # Sequence es preferible para listas de retorno
from sqlmodel import Session, select
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError # Para capturar errores del repo
from sqlalchemy.orm import selectinload # Para cargar relaciones anidadas

# Importar Repositorios
from app.models.inventory_models import MaterialConsumible, MaterialDimensional, MaterialSimple, StockItemDimensional
from app.repositories import order_repository,rol_repository, cliente_repository, inventory_repository, service_repository# Necesitamos cliente_repo para validar

# Importar Modelos y Schemas
from app.models.order_models import (
    PedidoCliente, Proforma, LineaProformaMaterial,
      LineaProformaServicio, OrdenProduccion, AsignacionTareaOrden,
 )

from app.schemas.order_schema import PedidoClienteCreate, PedidoClienteRead, ProformaUpdate, LineaProformaMaterialCreate, LineaProformaServicioCreate # Usamos Create para entrada
from app.models.service_models import ServicioDefinicion

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




# ========================================================
# Funciones del Servicio para Líneas de Proforma 
# ========================================================

def add_material_line_to_proforma(
    db: Session, *, proforma_id: int, linea_in: LineaProformaMaterialCreate
) -> Proforma:
    """
    Añade una línea de material a una proforma existente y recalcula totales.
    Utiliza los precios base definidos en los modelos de material.
    Calcula el precio para items dimensionales basado en su área y el precio/unidad base.

    Args:
        db: La sesión de base de datos activa.
        proforma_id: ID de la proforma (debe ser de tipo 'PRODUCTO').
        linea_in: Datos de la línea a añadir (schema LineaProformaMaterialCreate).

    Returns:
        La Proforma actualizada con la nueva línea y totales recalculados.

    Raises:
        HTTPException 404: Si la proforma o el material de origen no existen.
        HTTPException 400/409: Si la proforma no es de tipo 'PRODUCTO' o no está en estado 'BORRADOR'.
        HTTPException 500: Para otros errores internos.
    """
    logger.info(f"Servicio: Intentando añadir línea de material a Proforma ID: {proforma_id}")

    # 1. Obtener la proforma y validar tipo/estado (sin cambios)
    db_proforma = get_proforma_service(db=db, proforma_id=proforma_id, load_related=False)
    if db_proforma.tipo != "PRODUCTO":
        logger.warning(f"Intento de añadir línea de material a proforma tipo '{db_proforma.tipo}' (ID: {proforma_id})")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Solo se pueden añadir líneas de material a proformas de tipo 'PRODUCTO'.")
    if db_proforma.estado != "BORRADOR":
        logger.warning(f"Intento de añadir línea a proforma ID {proforma_id} en estado '{db_proforma.estado}'.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se pueden añadir líneas a una proforma en estado '{db_proforma.estado}'. Debe estar en 'BORRADOR'.")

    # 2. Inicializar variables para la línea
    material_origen: Any = None
    precio_unitario = Decimal("0.00")
    unidad = ""
    descripcion_item = ""

    try:
        # --- Determinar precio, unidad y descripción según el tipo de material ---
        if linea_in.tipo_material_origen == "STOCK_DIMENSIONAL" and linea_in.stock_item_dimensional_id:
            # Obtener el item de stock específico, asegurando cargar la definición del material relacionada
            # Nota: Asumimos que get_stock_item_dimensional_by_id puede cargar 'definicion_material'
            # Si no, se necesitaría cargarlo explícitamente después o ajustar el repositorio.
            # *** IMPORTANTE: El código original del repo no mostraba cómo cargar la relación,
            #     asegúrate de que `material_origen.definicion_material` esté disponible. ***
            #     Podrías necesitar un db.refresh(material_origen, attribute_names=["definicion_material"])
            #     si la carga no es eager por defecto.
            material_origen: Optional[StockItemDimensional] = inventory_repository.get_stock_item_by_id(
                db=db, item_id=linea_in.stock_item_dimensional_id
            )
            # --- Verificación de carga de relación (Ejemplo) ---
            if material_origen and material_origen.definicion_material is None:
                 # Forzar carga si no vino por defecto (requiere que la sesión no se cierre)
                 logger.debug(f"Refrescando definicion_material para StockItemDimensional ID {material_origen.id}")
                 db.refresh(material_origen, attribute_names=["definicion_material"])
            # --- Fin Verificación ---

            if not material_origen or not material_origen.definicion_material:
                 raise HTTPException(status_code=404, detail=f"Stock Item Dimensional ID {linea_in.stock_item_dimensional_id} o su definición no encontrado.") # noqa

            definicion: MaterialDimensional = material_origen.definicion_material
            precio_base_por_unidad_venta = definicion.precio_venta_base_unidad
            unidad_precio_venta = definicion.unidad_precio_venta.lower() # ej: "m2"
            unidad_dimension_fisica = definicion.unidad_dimension.lower() # ej: "mm"
            longitud_actual = material_origen.longitud_actual
            ancho_actual = material_origen.ancho_actual

            # --- Cálculo de Precio por Área (con conversión de unidades) ---
            factor_conversion = Decimal("1.0")
            if unidad_dimension_fisica == "mm" and unidad_precio_venta == "m2":
                factor_conversion = Decimal("1000.0")
            elif unidad_dimension_fisica == "cm" and unidad_precio_venta == "m2":
                factor_conversion = Decimal("100.0")
            # Añadir más conversiones si son necesarias (ej: pulgadas a m2, mm a m lineal, etc.)

            if factor_conversion == Decimal("1.0") and unidad_dimension_fisica != unidad_precio_venta:
                 logger.warning(f"No se definió factor de conversión de '{unidad_dimension_fisica}' a '{unidad_precio_venta}'. Asumiendo 1.0.")
                 # Podría ser un error si las unidades no coinciden y no hay conversión

            # Calcular dimensiones en la unidad base del precio
            longitud_base = longitud_actual / factor_conversion
            ancho_base = ancho_actual / factor_conversion

            # Calcular área u otra medida según unidad_precio_venta
            valor_calculado_base = Decimal("0.0")
            if unidad_precio_venta == "m2":
                valor_calculado_base = longitud_base * ancho_base
            elif unidad_precio_venta == "m_lineal": # Ejemplo si se vendiera por metro lineal
                 # Aquí la lógica dependería de qué dimensión usar (¿longitud?)
                 valor_calculado_base = longitud_base # O ancho_base, o max(l,a), etc.
            # Añadir más lógicas para otras unidades de precio (ej: 'unidad' para piezas fijas)
            else:
                 # Si es 'unidad' o algo no basado en dimensiones, usar el precio base directamente?
                 # O lanzar error si no se sabe cómo calcular? Por ahora, usamos el precio base.
                 logger.warning(f"Unidad de precio '{unidad_precio_venta}' no reconocida para cálculo basado en dimensiones. Usando precio base directamente.")
                 valor_calculado_base = Decimal("1.0") # Para que precio_unitario = precio_base

            # --- Aplicar Descuento por Merma (Ejemplo: 10% de descuento) ---
            # TODO: Definir la regla de descuento real (¿configuración global? ¿por tipo de material?)
            DESCUENTO_MERMA = Decimal("0.10") # 10%
            factor_descuento = (Decimal("1.0") - DESCUENTO_MERMA) if material_origen.es_merma else Decimal("1.0")

            # Calcular precio unitario para esta pieza específica
            precio_unitario_calculado = (valor_calculado_base * precio_base_por_unidad_venta * factor_descuento)
            # Redondear a 4 decimales (o los que se necesiten internamente) antes de usar en total_linea
            precio_unitario = precio_unitario_calculado.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)

            # Unidad en la línea de proforma: Usualmente 'pieza' o 'unidad' al vender un stock item específico
            unidad = "pieza"
            descripcion_item = f"{definicion.nombre} ({longitud_actual}x{ancho_actual} {definicion.unidad_dimension}) {'[Merma]' if material_origen.es_merma else ''}"

        elif linea_in.tipo_material_origen == "CONSUMIBLE" and linea_in.material_consumible_id:
            material_origen: Optional[MaterialConsumible] = inventory_repository.get_material_consumible_by_id(db=db, mat_cons_id=linea_in.material_consumible_id)
            if not material_origen:
                raise HTTPException(status_code=404, detail=f"Material Consumible ID {linea_in.material_consumible_id} no encontrado.")
            # Obtener precio directamente del modelo
            precio_unitario = material_origen.precio_venta_base_unidad
            unidad = material_origen.unidad_medida
            descripcion_item = material_origen.nombre

        elif linea_in.tipo_material_origen == "SIMPLE" and linea_in.material_simple_id:
            material_origen: Optional[MaterialSimple] = inventory_repository.get_material_simple_by_id(db=db, mat_simp_id=linea_in.material_simple_id)
            if not material_origen:
                raise HTTPException(status_code=404, detail=f"Material Simple ID {linea_in.material_simple_id} no encontrado.")
            # Obtener precio directamente del modelo
            precio_unitario = material_origen.precio_venta_base_unidad
            unidad = material_origen.unidad_medida
            descripcion_item = material_origen.nombre
        else:
            # Si llega aquí, hubo un problema con la validación del schema o lógica interna
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tipo de material origen o ID no válido o inconsistente.")

    except HTTPException as http_exc:
        # Relanzar excepciones HTTP (404, 400) ya generadas
        raise http_exc
    except Exception as e:
         logger.error(f"Error buscando/procesando material de origen para línea proforma: {e}", exc_info=True)
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al procesar material de origen.")

    # 3. Calcular total de la línea
    # Para dimensional, cantidad usualmente será 1 (la pieza). Para otros, es la cantidad pedida.
    # Asegurar que precio_unitario (calculado o directo) no sea None.
    if precio_unitario is None:
         logger.error(f"Error: precio_unitario es None para Proforma ID {proforma_id}, Línea: {linea_in}")
         raise HTTPException(status_code=500, detail="Error interno calculando precio de línea.")

    # Redondeamos el total final a 2 decimales para moneda
    total_linea = (linea_in.cantidad * precio_unitario).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # 4. Crear la instancia del modelo LineaProformaMaterial
    linea_db_instance = LineaProformaMaterial(
        proforma_id=proforma_id,
        tipo_material_origen=linea_in.tipo_material_origen,
        stock_item_dimensional_id=linea_in.stock_item_dimensional_id,
        material_consumible_id=linea_in.material_consumible_id,
        material_simple_id=linea_in.material_simple_id,
        cantidad=linea_in.cantidad,
        detalles_corte_solicitado=linea_in.detalles_corte_solicitado,
        # Datos obtenidos/calculados
        descripcion_item=descripcion_item,
        unidad=unidad,
        precio_unitario=precio_unitario.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), # Guardar con 2 decimales también
        total_linea=total_linea
    )

    # 5. Añadir la línea a la BD y actualizar totales de la proforma
    try:
        # Añadir la nueva línea
        _ = order_repository.add_linea_material(db=db, linea_data=linea_db_instance)
        # Recalcular y guardar los totales de la proforma completa
        updated_proforma = order_repository.update_proforma_totals(db=db, proforma_id=proforma_id)

        if updated_proforma is None:
            # Esto indicaría que la proforma desapareció entre la lectura inicial y aquí, muy raro.
            raise HTTPException(status_code=404, detail="Proforma no encontrada durante la actualización final de totales.") # noqa

        logger.info(f"Línea de material añadida (Tipo: {linea_in.tipo_material_origen}) y totales actualizados para Proforma ID {proforma_id}")
        # Devolver la proforma actualizada (preferiblemente recargada para incluir la nueva línea)
        return get_proforma_service(db=db, proforma_id=proforma_id, load_related=True)

    # Manejo de errores específicos y genéricos durante la escritura/actualización
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al añadir línea material a proforma ID {proforma_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto al guardar la línea de material.")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de base de datos al añadir línea material a proforma ID {proforma_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error de base de datos al añadir la línea de material.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al añadir línea material a proforma ID {proforma_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno general al añadir la línea de material.")




def add_servicio_line_to_proforma(
    db: Session, *, proforma_id: int, linea_in: LineaProformaServicioCreate
) -> Proforma:
    """
    Añade una línea de servicio a una proforma existente y recalcula totales.
    (CORREGIDO para manejar errores 500 y placeholders de precio).

    Args:
        db: La sesión de base de datos activa.
        proforma_id: ID de la proforma (debe ser de tipo 'SERVICIO').
        linea_in: Datos de la línea a añadir (schema LineaProformaServicioCreate).

    Returns:
        La Proforma actualizada con la nueva línea y totales recalculados.

    Raises:
        HTTPException 404: Si la proforma, servicio o línea de material asociada no existen.
        HTTPException 400/409: Si la proforma no es de tipo 'SERVICIO' o no está en 'BORRADOR',
                               o si se provee linea_proforma_material_id inválida.
        HTTPException 500: Para otros errores internos.
    """
    logger.info(f"Servicio: Intentando añadir línea de servicio a Proforma ID: {proforma_id}")

    # 1. Obtener la proforma y realizar validaciones iniciales
    try:
        db_proforma = get_proforma_service(db=db, proforma_id=proforma_id, load_related=False) # Maneja 404 si proforma no existe
    except HTTPException as e:
        raise e # Relanzar 404
    except Exception as e:
         logger.error(f"Error inesperado obteniendo Proforma ID {proforma_id} en add_servicio_line: {e}", exc_info=True)
         raise HTTPException(status_code=500, detail="Error interno al obtener proforma [GASL]")

    if db_proforma.tipo != "SERVICIO":
        logger.warning(f"Intento de añadir línea de servicio a proforma tipo '{db_proforma.tipo}' (ID: {proforma_id})")
        # Lanzar 400 - esta validación parece correcta y no debería causar 500
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Solo se pueden añadir líneas de servicio a proformas de tipo 'SERVICIO'.")
    if db_proforma.estado != "BORRADOR":
        logger.warning(f"Intento de añadir línea a proforma ID {proforma_id} en estado '{db_proforma.estado}'.")
        # Lanzar 409 - esta validación parece correcta y no debería causar 500
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se pueden añadir líneas a una proforma en estado '{db_proforma.estado}'. Debe estar en 'BORRADOR'.")

    # 2. Obtener detalles de la definición del servicio
    servicio_def: Optional[ServicioDefinicion] = None
    try:
        servicio_def = service_repository.get_servicio_by_id(db=db, servicio_id=linea_in.servicio_definicion_id)
        if not servicio_def:
             logger.warning(f"ServicioDefinicion ID {linea_in.servicio_definicion_id} no encontrado.")
             # Lanzar 404 - esta validación parece correcta y no debería causar 500
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La definición del servicio con ID {linea_in.servicio_definicion_id} no fue encontrada.")

    except HTTPException as e:
        raise e # Relanzar 404
    except Exception as e:
        logger.error(f"Error buscando servicio definición ID {linea_in.servicio_definicion_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno buscando definición servicio [GASD]")

    # 3. Validar linea_proforma_material_id si se proporcionó
    if linea_in.linea_proforma_material_id is not None:
        try:
            if not db_proforma.proforma_vinculada_id:
                 logger.warning(f"Intento de vincular línea de servicio a material en proforma no vinculada (ID: {proforma_id})")
                 # Lanzar 400 - esta validación parece correcta y no debería causar 500
                 raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se puede asociar línea de servicio a material si la proforma de servicio no está vinculada a una de producto.")

            # Obtener la línea de material (usar db.get es simple y eficiente)
            linea_material_db = db.get(LineaProformaMaterial, linea_in.linea_proforma_material_id)

            if not linea_material_db:
                 logger.warning(f"Línea de material asociada ID {linea_in.linea_proforma_material_id} no encontrada.")
                 # Lanzar 404 - esta validación parece correcta y no debería causar 500
                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La línea de material asociada con ID {linea_in.linea_proforma_material_id} no fue encontrada.")

            # Verificar que pertenece a la proforma vinculada
            if linea_material_db.proforma_id != db_proforma.proforma_vinculada_id:
                 logger.warning(f"Línea material ID {linea_in.linea_proforma_material_id} no pertenece a proforma producto vinculada ID {db_proforma.proforma_vinculada_id}.")
                 # Lanzar 400 - esta validación parece correcta y no debería causar 500
                 raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La línea de material asociada no pertenece a la proforma de producto vinculada.")

        except HTTPException as e:
            raise e # Relanzar 404 o 400
        except Exception as e:
            logger.error(f"Error validando linea material ID {linea_in.linea_proforma_material_id}: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Error interno validando línea material [GVLM]")

    # 4. Calcular Precio Unitario y Total (Lógica Placeholder Mejorada)
    precio_unitario = Decimal("0.00") # Inicializar a 0 para evitar None
    descripcion_servicio = servicio_def.nombre # Usar nombre de la definición

    # --- INICIO: Lógica de Cálculo de Precio (¡REEMPLAZAR CON LÓGICA REAL!) ---
    # Esta sección necesita la lógica definitiva basada en tus reglas de negocio.
    # Prioridad ejemplo: costo_por_unidad > costo_por_minuto (si se pudiera calcular tiempo) > default 0
    if servicio_def.costo_por_unidad is not None:
        precio_unitario = servicio_def.costo_por_unidad
        logger.debug(f"Usando costo_por_unidad ({precio_unitario}) para servicio ID {servicio_def.id}")
    elif servicio_def.costo_por_minuto is not None:
        # !!! ADVERTENCIA: Falta la lógica para obtener/calcular el TIEMPO !!!
        # El schema LineaProformaServicioCreate NO tiene campo para tiempo estimado.
        # Necesitas:
        #   1. Añadir campo `tiempo_estimado_minutos: Optional[Decimal]` a LineaProformaServicioCreate.
        #   2. O Calcular el tiempo aquí basado en `servicio_def.tiempo_setup_min`,
        #      `servicio_def.tiempo_preparado_min_por_unidad` y `linea_in.cantidad`.
        #   3. Implementar la fórmula: precio = tiempo_total * costo_por_minuto.
        # Por AHORA, como no podemos calcularlo, asignamos 0 y loggeamos warning.
        logger.warning(f"Servicio ID {servicio_def.id} tiene costo_por_minuto pero falta lógica/dato de tiempo. Precio unitario será 0.")
        precio_unitario = Decimal("0.00") # Default seguro para evitar error NOT NULL
    else:
        # Si no hay costo por unidad ni por minuto, ¿cuál es el precio?
        # Podría ser un servicio gratuito, un error de configuración, o requerir cotización manual (Dibujante).
        # Por ahora, default a 0.
        logger.warning(f"Servicio ID {servicio_def.id} no tiene costo_por_unidad ni costo_por_minuto definidos. Precio unitario será 0.")
        precio_unitario = Decimal("0.00")

    # Considerar Factores IH/ST/M si aplican a tu cálculo final
    # precio_unitario = precio_unitario * (servicio_def.factor_ih or Decimal('1.0')) ... etc.

    # --- FIN: Lógica de Cálculo de Precio (Placeholder) ---

    # Calcular total línea redondeando a 2 decimales
    total_linea = (linea_in.cantidad * precio_unitario).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # 5. Crear la instancia del modelo LineaProformaServicio
    # Asegurarse que precio_unitario y total_linea son Decimal válidos (no None)
    linea_db_instance = LineaProformaServicio(
        proforma_id=proforma_id,
        servicio_definicion_id=linea_in.servicio_definicion_id,
        cantidad=linea_in.cantidad,
        linea_proforma_material_id=linea_in.linea_proforma_material_id,
        ruta_imagen_cnc=linea_in.ruta_imagen_cnc,
        detalles_adicionales=linea_in.detalles_adicionales,
        # Datos obtenidos/calculados
        descripcion_servicio=descripcion_servicio,
        precio_unitario=precio_unitario.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), # Guardar redondeado
        total_linea=total_linea
    )

    # 6. Añadir la línea a la BD y actualizar totales
    try:
        # Añadir la nueva línea
        _ = order_repository.add_linea_servicio(db=db, linea_data=linea_db_instance)
        # Recalcular y guardar los totales de la proforma completa
        updated_proforma = order_repository.update_proforma_totals(db=db, proforma_id=proforma_id)

        if updated_proforma is None:
            # Raro si la proforma existía antes, pero posible race condition?
            logger.error(f"Proforma ID {proforma_id} no encontrada después de añadir línea servicio.")
            raise HTTPException(status_code=404, detail="Proforma no encontrada durante actualización de totales.") # noqa

        logger.info(f"Línea de servicio añadida (Servicio ID: {servicio_def.id}) y totales actualizados para Proforma ID {proforma_id}")
        # Devolver la proforma actualizada, recargada para incluir la nueva línea
        return get_proforma_service(db=db, proforma_id=proforma_id, load_related=True)

    # Manejo de errores durante la escritura/actualización
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error integridad al añadir línea servicio a proforma ID {proforma_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto al guardar la línea de servicio.")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error DB al añadir línea servicio a proforma ID {proforma_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error de base de datos al añadir la línea de servicio.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al añadir línea servicio a proforma ID {proforma_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno general al añadir la línea de servicio.")
    





# ==========================================================
# === Servicios para Ordenes de Producción y Tareas      ===
# ==========================================================

def crear_orden_para_pedido_aprobado(db: Session, *, pedido_id: int) -> OrdenProduccion:
    """
    Crea una Orden de Producción y sus tareas iniciales cuando se aprueba un PedidoCliente.
    (Lógica de creación de tareas REFINADA)
    """
    logger.info(f"Servicio: Intentando crear Orden de Producción para Pedido ID: {pedido_id}")

    # 1. Obtener Pedido y validar estado (con carga de relaciones anidadas)
    try:
        query = (
            select(PedidoCliente)
            .where(PedidoCliente.id == pedido_id)
            .options(
                selectinload(PedidoCliente.proformas)
                .selectinload(Proforma.lineas_material), # Cargar Líneas Material dentro de Proformas
                selectinload(PedidoCliente.proformas)
                .selectinload(Proforma.lineas_servicio) # Cargar Líneas Servicio dentro de Proformas
                .selectinload(LineaProformaServicio.servicio_definicion) # Cargar Definición dentro de Línea Servicio
                # Añadir más selectinload si son necesarios
            )
        )
        pedido = db.exec(query).first()

        if not pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pedido ID {pedido_id} no encontrado.")

        # Verificar estado y existencia de orden previa (igual que antes)
        if pedido.estado != "APROBADA":
             raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El pedido debe estar en estado 'APROBADA' para generar la orden.") # noqa
        if order_repository.get_orden_by_pedido_id(db=db, pedido_id=pedido.id): # Necesitarás añadir esta función al repo
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El pedido {pedido_id} ya tiene una orden generada.") # noqa

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error obteniendo o validando Pedido ID {pedido_id} y sus relaciones: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al verificar el pedido y sus líneas.")

    # 2. Crear la Orden de Producción (igual que antes)
    try:
        orden_data = OrdenProduccion(
            pedido_cliente_id=pedido_id, estado="PENDIENTE_ASIGNACION", prioridad=0,
            fecha_inicio_espera=datetime.utcnow()
        )
        db_orden = order_repository.create_orden_produccion(db=db, orden_data=orden_data)
    except Exception as e:
        logger.error(f"Error creando OrdenProduccion para Pedido ID {pedido_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al crear la orden de producción.")

    # 3. Crear Tareas Iniciales (Lógica Refinada)
    tareas_creadas_info = [] # Para loggear o devolver info
    try:
        # --- INICIO: Lógica Refinada para Crear Tareas ---

        # Flags para determinar qué tipos de tareas generales se necesitan
        necesita_dibujo = False
        necesita_corte = False
        necesita_maquinado = False
        tiene_solo_productos_simples = True # Asumir True inicialmente

        # Obtener IDs de roles necesarios
        rol_dibujante = rol_repository.get_rol_by_name(db=db, nombre="Dibujante")
        rol_operario = rol_repository.get_rol_by_name(db=db, nombre="Operario")
        if not rol_dibujante or not rol_operario:
             raise ValueError("Roles base 'Dibujante' u 'Operario' no encontrados en la BD.") # Error de config

        # Analizar líneas de servicio
        for proforma in pedido.proformas:
            if proforma.tipo == "SERVICIO":
                tiene_solo_productos_simples = False # Si hay servicios, no es solo despacho simple
                for linea_serv in proforma.lineas_servicio:
                    # Acceder a servicio_definicion (ya debería estar cargado por selectinload)
                    if linea_serv.servicio_definicion:
                        definicion = linea_serv.servicio_definicion
                        if definicion.requiere_dibujo_cnc:
                            necesita_dibujo = True
                        # Identificar servicios de corte o maquinado (ajustar palabras clave si es necesario)
                        nombre_servicio_upper = definicion.nombre.upper()
                        if "CORTE" in nombre_servicio_upper:
                            necesita_corte = True
                        if "CNC" in nombre_servicio_upper or "MAQUINADO" in nombre_servicio_upper:
                            # Podríamos diferenciar CNC Router de Laser si fuera necesario
                            necesita_maquinado = True
                    else:
                         logger.warning(f"Línea de servicio ID {linea_serv.id} no tiene servicio_definicion cargado.")


        # Analizar líneas de material
        for proforma in pedido.proformas:
            if proforma.tipo == "PRODUCTO":
                 if not proforma.lineas_material: # Si hay proforma de producto pero sin líneas
                     tiene_solo_productos_simples = False # Marcar que no es solo despacho simple
                 for linea_mat in proforma.lineas_material:
                     # Si hay dimensionales O se pide corte, no es despacho simple
                     if linea_mat.tipo_material_origen == "STOCK_DIMENSIONAL":
                         tiene_solo_productos_simples = False
                     if linea_mat.detalles_corte_solicitado:
                         necesita_corte = True
                         tiene_solo_productos_simples = False
                     # Si hay consumibles o simples, por ahora no cambia las tareas principales,
                     # pero sabemos que no es *solo* dimensional.


        # Crear tareas basado en flags (evitando duplicados si un servicio y material piden lo mismo)
        tipos_tarea_a_crear = set() # Usar un set para evitar duplicar tipos

        if necesita_dibujo:
            tipos_tarea_a_crear.add(("DIBUJO_CNC", rol_dibujante.id))
        if necesita_corte:
            tipos_tarea_a_crear.add(("CORTE_MATERIAL", rol_operario.id))
        if necesita_maquinado:
            tipos_tarea_a_crear.add(("MAQUINADO_CNC", rol_operario.id)) # Asignar a Operario por defecto

        # Si no se necesita ninguna tarea específica de producción, crear una de despacho
        if not tipos_tarea_a_crear:
            # Si tiene_solo_productos_simples es True, podría ser despacho directo.
            # Si es False pero no hay tareas específicas, podría ser preparación/empaque.
            # Vamos a crear una tarea genérica de 'PREPARACION_DESPACHO' para Operario.
            tipos_tarea_a_crear.add(("PREPARACION_DESPACHO", rol_operario.id))


        # Crear las instancias de AsignacionTareaOrden
        for tipo_tarea, rol_id in tipos_tarea_a_crear:
            tarea_data = AsignacionTareaOrden(
                orden_id=db_orden.id,
                rol_id_contexto=rol_id,
                tipo_tarea=tipo_tarea,
                estado_tarea="PENDIENTE",
                usuario_id_asignado=None # Inicialmente no asignada
                # linea_proforma_..._id = None (Por ahora, tareas generales para la orden)
            )
            repo_tarea = order_repository.create_asignacion_tarea(db=db, tarea_data=tarea_data)
            tareas_creadas_info.append({"id": repo_tarea.id, "tipo": repo_tarea.tipo_tarea})
            logger.info(f"Tarea '{repo_tarea.tipo_tarea}' creada (ID: {repo_tarea.id}) para Orden ID {db_orden.id}")

        # --- Fin Lógica Refinada ---

    except ValueError as ve: # Captura error si los roles base no se encuentran
         logger.error(f"Error de configuración obteniendo roles base: {ve}", exc_info=True)
         # Podríamos intentar rollback de la orden creada, pero es complejo
         raise HTTPException(status_code=500, detail=f"Error de configuración interna: {ve}")
    except Exception as e:
         logger.error(f"Error creando tareas iniciales para Orden ID {db_orden.id}: {e}", exc_info=True)
         # Rollback aquí afectaría solo a la creación de tareas, la orden ya está commiteada.
         db.rollback()
         # Es importante indicar que la orden se creó pero las tareas fallaron.
         # Podríamos actualizar el estado de la orden a 'ERROR_CREACION_TAREAS' o similar.
         # Por ahora, lanzamos 500.
         raise HTTPException(status_code=500, detail="Error interno al crear las tareas de la orden.")

    # 4. Actualizar estado del Pedido (igual que antes)
    try:
        order_repository.update_pedido(db=db, db_pedido=pedido, update_data={"estado": "EN_PRODUCCION"})
        logger.info(f"Estado del Pedido ID {pedido_id} actualizado a 'EN_PRODUCCION'.")
    except Exception as e:
        logger.error(f"Error actualizando estado del Pedido ID {pedido_id} a 'EN_PRODUCCION': {e}", exc_info=True)
        # No relanzar, loggear es suficiente.

    # Devolver la orden creada, recargada con sus tareas
    db.refresh(db_orden, attribute_names=["asignaciones_tareas"])
    return db_orden


# ... (resto de funciones de servicio: get_orden_details_service, get_pending_orders_stack_service) ...

# --- Funciones auxiliares del repositorio que podrían necesitarse ---
# Añadir a order_repository.py:
# def get_orden_by_pedido_id(db: Session, *, pedido_id: int) -> Optional[OrdenProduccion]:
#     logger.debug(f"Repositorio: Buscando OrdenProduccion por Pedido ID: {pedido_id}")
#     try:
#         statement = select(OrdenProduccion).where(OrdenProduccion.pedido_cliente_id == pedido_id)
#         return db.exec(statement).first()
#     except Exception as e:
#         logger.error(f"Error buscando OrdenProduccion por Pedido ID {pedido_id}: {e}", exc_info=True)
#         raise e

def get_orden_details_service(db: Session, *, orden_id: int) -> OrdenProduccion:
    """
    Obtiene los detalles completos de una Orden de Producción por ID.

    Args:
        db: Sesión de base de datos activa.
        orden_id: ID de la orden a buscar.

    Returns:
        El objeto OrdenProduccion con relaciones cargadas.

    Raises:
        HTTPException 404: Si la orden no se encuentra.
        HTTPException 500: Para otros errores internos.
    """
    logger.debug(f"Servicio: Buscando detalles de OrdenProduccion ID: {orden_id}")
    try:
        # Pedir al repositorio que cargue las relaciones necesarias
        orden = order_repository.get_orden_by_id(db=db, orden_id=orden_id, load_related=True)
        if not orden:
            logger.warning(f"OrdenProduccion con ID {orden_id} no encontrada.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Orden de producción con ID {orden_id} no encontrada."
            )
        logger.info(f"OrdenProduccion ID {orden_id} encontrada con detalles.")
        return orden
    except HTTPException:
        raise # Relanzar 404
    except Exception as e:
        logger.error(f"Error inesperado buscando OrdenProduccion ID {orden_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al buscar la orden.")


def get_pending_orders_stack_service(db: Session, *, skip: int = 0, limit: int = 50) -> Sequence[OrdenProduccion]:
    """
    Obtiene la lista ("stack") de órdenes pendientes de asignación.

    Args:
        db: Sesión de base de datos activa.
        skip: Número de órdenes a saltar.
        limit: Número máximo de órdenes a devolver.

    Returns:
        Una secuencia de objetos OrdenProduccion en estado 'PENDIENTE_ASIGNACION'.

    Raises:
        HTTPException 500: Para errores internos.
    """
    logger.debug(f"Servicio: Obteniendo stack de órdenes pendientes (skip={skip}, limit={limit})")
    try:
        # Llama al repositorio filtrando por el estado adecuado
        ordenes_pendientes = order_repository.list_ordenes_by_estado(
            db=db,
            estados=["PENDIENTE_ASIGNACION"], # Estado específico
            skip=skip,
            limit=limit,
            load_related=True # Cargar detalles básicos para mostrar en el stack
        )
        return ordenes_pendientes
    except Exception as e:
        logger.error(f"Error inesperado obteniendo stack de órdenes pendientes: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al obtener órdenes pendientes.")

# --- Punto de Integración ---
# Debes asegurarte de llamar a `crear_orden_para_pedido_aprobado`
# desde la lógica que maneja la aprobación de un PedidoCliente.
# Por ejemplo, en `order_service.py`, dentro de una función `approve_pedido_service`
# o modificando `update_proforma_service` para que lo detecte cuando ambas proformas
# (o la única relevante) lleguen al estado 'APROBADA'.

# Ejemplo de cómo podría ser la modificación en `update_proforma_service` (EXISTENTE):
#
# def update_proforma_service(db: Session, *, proforma_id: int, proforma_in: ProformaUpdate) -> Proforma:
#     # ... (obtener db_proforma, validar transición, etc.) ...
#     new_estado = update_data.get("estado")
#     estado_anterior = db_proforma.estado
#
#     # ... (validación de transición) ...
#
#     updated_proforma = order_repository.update_proforma(...)
#
#     # --- NUEVO: Verificar si se debe crear Orden de Producción ---
#     if new_estado == "APROBADA" and estado_anterior != "APROBADA":
#          # Verificar si la proforma vinculada (si existe) también está aprobada
#          pedido_listo_para_orden = False
#          if updated_proforma.proforma_vinculada_id:
#              proforma_vinculada = order_repository.get_proforma_by_id(db, proforma_id=updated_proforma.proforma_vinculada_id)
#              if proforma_vinculada and proforma_vinculada.estado == "APROBADA":
#                  pedido_listo_para_orden = True
#          else:
#              # Si no hay proforma vinculada, la aprobación de esta es suficiente
#              pedido_listo_para_orden = True
#
#          if pedido_listo_para_orden:
#              try:
#                  # Llamar a la función del nuevo servicio (o de este mismo archivo)
#                  _ = crear_orden_para_pedido_aprobado(db=db, pedido_id=updated_proforma.pedido_cliente_id)
#              except HTTPException as orden_exc:
#                   # Decidir qué hacer si falla la creación de la orden (loggear, ¿revertir aprobación?)
#                   logger.error(f"Error al crear orden de producción para pedido {updated_proforma.pedido_cliente_id} tras aprobación de proforma {proforma_id}: {orden_exc.detail}")
#                   # Podríamos relanzar o solo loggear dependiendo de la criticidad
#
#     return updated_proforma

