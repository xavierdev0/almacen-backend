# app/repositories/order_repository.py

import logging
from typing import Optional, Sequence, List, Dict, Any
from sqlmodel import Session, select, SQLModel
from sqlalchemy.orm import selectinload # Para carga eager opcional
from sqlalchemy.exc import IntegrityError, SQLAlchemyError # Capturar errores específicos

from decimal import Decimal 


# Importar el modelo principal
from app.models.order_models import (
    PedidoCliente, Proforma, LineaProformaMaterial,
    LineaProformaServicio, OrdenProduccion, AsignacionTareaOrden # Añadir OrdenProduccion y AsignacionTareaOrden
)
from app.models.client_model import Cliente
from app.models.user_models import Usuario, Rol

logger = logging.getLogger(__name__)

# =======================================
# Funciones CRUD para PedidoCliente
# =======================================

def create_pedido(db: Session, *, pedido_data: PedidoCliente) -> PedidoCliente:
    """
    Crea un nuevo registro de PedidoCliente en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        pedido_data: Un objeto PedidoCliente (previamente validado y preparado por el servicio).

    Returns:
        El objeto PedidoCliente recién creado y refrescado desde la base de datos.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: FK inválida).
                       La capa de servicio debería manejar esto (ej: 404/400).
        SQLAlchemyError: Para otros errores relacionados con la base de datos.
        Exception: Para errores inesperados no específicos de SQLAlchemy.
    """
    db_pedido = pedido_data # Asumimos que ya es una instancia del modelo
    logger.debug(f"Repositorio: Intentando crear PedidoCliente para Cliente ID: {db_pedido.cliente_id}")
    try:
        db.add(db_pedido)
        db.commit()
        db.refresh(db_pedido) # Carga ID, fecha_creacion, etc. desde la BD
        logger.info(f"PedidoCliente creado con éxito: ID={db_pedido.id}")
        return db_pedido
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al crear PedidoCliente: {e}", exc_info=True)
        # Relanzar para que el servicio maneje (probablemente indica un ID de cliente/vendedor inválido)
        raise e
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de base de datos (SQLAlchemy) al crear PedidoCliente: {e}", exc_info=True)
        raise e # Relanzar para manejo genérico (probablemente 500 en API)
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al crear PedidoCliente: {e}", exc_info=True)
        raise e # Relanzar

def get_pedido_by_id(db: Session, *, pedido_id: int, load_related: bool = False) -> Optional[PedidoCliente]:
    """
    Obtiene un PedidoCliente específico por su ID.

    Permite opcionalmente cargar relaciones comunes (cliente, vendedor, proformas)
    de forma eager para evitar consultas N+1 posteriores.

    Args:
        db: La sesión de base de datos activa.
        pedido_id: El ID del pedido a buscar.
        load_related: Si es True, carga eager las relaciones cliente, vendedor y proformas.

    Returns:
        El objeto PedidoCliente si se encuentra, None en caso contrario.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Buscando PedidoCliente por ID: {pedido_id}, Cargar relacionados: {load_related}")
    try:
        query = select(PedidoCliente).where(PedidoCliente.id == pedido_id)
        if load_related:
            # Carga Eager: Trae los datos relacionados en la misma consulta inicial.
            # Es más eficiente si sabes que vas a necesitar estos datos después.
            query = query.options(
                selectinload(PedidoCliente.cliente), # Cargar Cliente
                selectinload(PedidoCliente.vendedor), # Cargar Usuario (Vendedor)
                selectinload(PedidoCliente.proformas) # Cargar la lista de Proformas asociadas
                # Añadir selectinload(PedidoCliente.orden_produccion) si se necesita
            )
        pedido = db.exec(query).first()
        if pedido:
            logger.debug(f"PedidoCliente ID {pedido_id} encontrado.")
        else:
            logger.debug(f"PedidoCliente ID {pedido_id} no encontrado.")
        return pedido
    except SQLAlchemyError as e:
        logger.error(f"Error de base de datos (SQLAlchemy) al buscar PedidoCliente ID {pedido_id}: {e}", exc_info=True)
        raise e
    except Exception as e:
        logger.error(f"Error inesperado al buscar PedidoCliente ID {pedido_id}: {e}", exc_info=True)
        raise e

def list_pedidos(
    db: Session, *,
    skip: int = 0,
    limit: int = 100,
    cliente_id: Optional[int] = None,
    vendedor_id: Optional[int] = None,
    estado: Optional[str] = None,
    load_related: bool = False # Opción para cargar relaciones en la lista
) -> Sequence[PedidoCliente]:
    """
    Obtiene una lista paginada y filtrada de PedidoCliente.

    Permite filtrar por cliente_id, vendedor_id y estado.
    Permite opcionalmente cargar relaciones comunes para cada pedido en la lista.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de registros a saltar.
        limit: Número máximo de registros a devolver.
        cliente_id: Filtrar por ID de cliente (opcional).
        vendedor_id: Filtrar por ID de vendedor (opcional).
        estado: Filtrar por estado exacto (opcional).
        load_related: Si es True, carga eager cliente y vendedor para cada pedido.

    Returns:
        Una secuencia (lista) de objetos PedidoCliente que coinciden.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Listando PedidoCliente con filtros - skip:{skip}, limit:{limit}, cliente:{cliente_id}, vendedor:{vendedor_id}, estado:{estado}, related:{load_related}")
    try:
        query = select(PedidoCliente)

        # Aplicar filtros
        if cliente_id is not None:
            query = query.where(PedidoCliente.cliente_id == cliente_id)
        if vendedor_id is not None:
            query = query.where(PedidoCliente.usuario_id_vendedor == vendedor_id)
        if estado is not None:
            query = query.where(PedidoCliente.estado == estado)

        # Aplicar carga eager si se solicita
        if load_related:
            query = query.options(
                selectinload(PedidoCliente.cliente),
                selectinload(PedidoCliente.vendedor)
                # Considerar NO cargar proformas aquí por defecto, podría ser pesado para una lista.
            )

        # Aplicar ordenamiento (ej: por fecha de creación descendente) y paginación
        query = query.order_by(PedidoCliente.fecha_creacion.desc()).offset(skip).limit(limit)

        pedidos = db.exec(query).all()
        logger.debug(f"Se encontraron {len(pedidos)} PedidoCliente.")
        return pedidos
    except SQLAlchemyError as e:
        logger.error(f"Error de base de datos (SQLAlchemy) al listar PedidoCliente: {e}", exc_info=True)
        raise e
    except Exception as e:
        logger.error(f"Error inesperado al listar PedidoCliente: {e}", exc_info=True)
        raise e

def update_pedido(db: Session, *, db_pedido: PedidoCliente, update_data: dict) -> PedidoCliente:
    """
    Actualiza un registro de PedidoCliente existente en la base de datos.
    Principalmente útil para cambiar el estado.

    Args:
        db: La sesión de base de datos activa.
        db_pedido: El objeto PedidoCliente existente obtenido de la BD.
        update_data: Un diccionario con los campos a actualizar (ya filtrados).

    Returns:
        El objeto PedidoCliente actualizado y refrescado.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Intentando actualizar PedidoCliente ID: {db_pedido.id} con datos: {update_data.keys()}")
    try:
        if not update_data:
            logger.warning(f"No se proporcionaron datos para actualizar PedidoCliente ID {db_pedido.id}.")
            return db_pedido # No hay nada que hacer

        # Aplicar los cambios usando sqlmodel_update
        db_pedido.sqlmodel_update(update_data)

        db.add(db_pedido) # Marcar como modificado
        db.commit()
        db.refresh(db_pedido) # Obtener estado actualizado de la BD
        logger.info(f"PedidoCliente ID {db_pedido.id} actualizado con éxito.")
        return db_pedido
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de base de datos (SQLAlchemy) al actualizar PedidoCliente ID {db_pedido.id}: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al actualizar PedidoCliente ID {db_pedido.id}: {e}", exc_info=True)
        raise e

# Nota: La función delete_pedido no se implementa aquí inicialmente, ya que eliminar
# un pedido probablemente requeriría eliminar en cascada o verificar muchas dependencias
# (Proformas, Orden, Facturas). Es más común marcarlo como 'CANCELADO' o 'ARCHIVADO'.
# Si se necesita eliminar, se añadiría aquí con manejo cuidadoso de IntegrityError.

# --- Funciones adicionales que podríamos necesitar más adelante ---
# def get_proforma_by_id(db: Session, proforma_id: int) -> Optional[Proforma]: ...
# def create_proforma(db: Session, proforma_data: Proforma) -> Proforma: ...
# def add_linea_material(db: Session, linea_data: LineaProformaMaterial) -> LineaProformaMaterial: ...
# def update_proforma_totals(db: Session, proforma_id: int) -> Proforma: ...
# ... y así sucesivamente para las otras entidades relacionadas con el pedido ...




# =======================================
# Funciones CRUD para Proforma (NUEVAS)
# =======================================

def create_proforma(db: Session, *, proforma_data: Proforma) -> Proforma:
    """
    Crea un nuevo registro de Proforma en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        proforma_data: Una instancia del modelo Proforma con los datos a crear.

    Returns:
        El objeto Proforma recién creado y refrescado.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: FK inválida).
        SQLAlchemyError: Para otros errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    db_proforma = proforma_data
    logger.debug(f"Repositorio: Intentando añadir Proforma Tipo: {db_proforma.tipo} para Pedido ID: {db_proforma.pedido_cliente_id}")
    try:
        db.add(db_proforma)
        db.commit()
        db.refresh(db_proforma)
        logger.info(f"Proforma creada con éxito: ID={db_proforma.id}, Tipo={db_proforma.tipo}, PedidoID={db_proforma.pedido_cliente_id}")
        return db_proforma
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al crear Proforma: {e}", exc_info=True)
        raise e
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de base de datos (SQLAlchemy) al crear Proforma: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al crear Proforma: {e}", exc_info=True)
        raise e

def get_proforma_by_id(db: Session, *, proforma_id: int, load_related: bool = False) -> Optional[Proforma]:
    """
    Obtiene una Proforma específica por su ID.

    Permite opcionalmente cargar relaciones comunes (pedido, creador, líneas).

    Args:
        db: La sesión de base de datos activa.
        proforma_id: El ID de la proforma a buscar.
        load_related: Si es True, carga eager las relaciones especificadas.

    Returns:
        El objeto Proforma si se encuentra, None en caso contrario.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Buscando Proforma por ID: {proforma_id}, Cargar relacionados: {load_related}")
    try:
        query = select(Proforma).where(Proforma.id == proforma_id)
        if load_related:
            query = query.options(
                selectinload(Proforma.pedido),
                selectinload(Proforma.creador),
                selectinload(Proforma.lineas_material), # Cargar líneas de material
                selectinload(Proforma.lineas_servicio) # Cargar líneas de servicio
                # selectinload(Proforma.proforma_vinculada) # Cargar vinculada si se necesita
            )
        proforma = db.exec(query).first()
        logger.debug(f"Proforma ID {proforma_id} {'encontrada' if proforma else 'no encontrada'}.")
        return proforma
    except SQLAlchemyError as e:
        logger.error(f"Error de base de datos (SQLAlchemy) al buscar Proforma ID {proforma_id}: {e}", exc_info=True); raise e
    except Exception as e:
        logger.error(f"Error inesperado al buscar Proforma ID {proforma_id}: {e}", exc_info=True); raise e

def list_proformas_by_pedido(db: Session, *, pedido_id: int, skip: int = 0, limit: int = 10) -> Sequence[Proforma]:
    """
    Obtiene las proformas asociadas a un PedidoCliente específico.

    Args:
        db: La sesión de base de datos activa.
        pedido_id: El ID del PedidoCliente cuyas proformas se listarán.
        skip: Número de registros a saltar.
        limit: Número máximo de registros a devolver (usualmente 2).

    Returns:
        Una secuencia (lista) de objetos Proforma asociados al pedido.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Listando Proformas para Pedido ID: {pedido_id}")
    try:
        query = select(Proforma).where(Proforma.pedido_cliente_id == pedido_id)
        # Ordenar por tipo podría ser útil (ej: PRODUCTO primero)
        query = query.order_by(Proforma.tipo).offset(skip).limit(limit)
        proformas = db.exec(query).all()
        logger.debug(f"Se encontraron {len(proformas)} Proformas para Pedido ID {pedido_id}.")
        return proformas
    except SQLAlchemyError as e:
        logger.error(f"Error de base de datos (SQLAlchemy) al listar Proformas para Pedido ID {pedido_id}: {e}", exc_info=True); raise e
    except Exception as e:
        logger.error(f"Error inesperado al listar Proformas para Pedido ID {pedido_id}: {e}", exc_info=True); raise e

def update_proforma(db: Session, *, db_proforma: Proforma, update_data: Dict[str, Any]) -> Proforma:
    """
    Actualiza un registro de Proforma existente en la base de datos.
    Útil para cambiar estado, notas, o vincular proformas.

    Args:
        db: La sesión de base de datos activa.
        db_proforma: El objeto Proforma existente obtenido de la BD.
        update_data: Un diccionario con los campos a actualizar (ej: {"estado": "APROBADA"},
                     {"proforma_vinculada_id": X}).

    Returns:
        El objeto Proforma actualizado y refrescado.

    Raises:
        IntegrityError: Si la actualización viola alguna restricción (ej: FK a proforma_vinculada_id inválida).
        SQLAlchemyError: Para otros errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    proforma_id = db_proforma.id
    logger.debug(f"Repositorio: Intentando actualizar Proforma ID: {proforma_id} con datos: {list(update_data.keys())}")
    try:
        if not update_data:
            logger.warning(f"No se proporcionaron datos para actualizar Proforma ID {proforma_id}.")
            return db_proforma

        # Aplicar los cambios usando sqlmodel_update
        db_proforma.sqlmodel_update(update_data)

        db.add(db_proforma) # Marcar como modificado
        db.commit()
        db.refresh(db_proforma) # Obtener estado actualizado de la BD
        logger.info(f"Proforma ID {proforma_id} actualizada con éxito.")
        return db_proforma
    except IntegrityError as e:
         db.rollback()
         logger.error(f"Error de integridad al actualizar Proforma ID {proforma_id}: {e}", exc_info=True)
         raise e # Relanzar para que el servicio maneje (ej: 400/404 si FK es inválida)
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de base de datos (SQLAlchemy) al actualizar Proforma ID {proforma_id}: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al actualizar Proforma ID {proforma_id}: {e}", exc_info=True)
        raise e



# ========================================================
# Funciones CRUD para Líneas de Proforma (NUEVAS)
# ========================================================

def add_linea_material(db: Session, *, linea_data: LineaProformaMaterial) -> LineaProformaMaterial:
    """
    Añade una nueva línea de material a una proforma en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        linea_data: Una instancia del modelo LineaProformaMaterial con los datos a crear
                    (preparada por el servicio, incluyendo el total_linea calculado).

    Returns:
        El objeto LineaProformaMaterial recién creado y refrescado.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: FK de proforma_id inválida).
        SQLAlchemyError: Para otros errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    db_linea = linea_data
    logger.debug(f"Repositorio: Intentando añadir LineaProformaMaterial a Proforma ID: {db_linea.proforma_id}")
    try:
        db.add(db_linea)
        db.commit()
        db.refresh(db_linea)
        logger.info(f"LineaProformaMaterial añadida con éxito: ID={db_linea.id} a Proforma ID={db_linea.proforma_id}")
        return db_linea
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al añadir LineaProformaMaterial: {e}", exc_info=True)
        raise e # Relanzar para que el servicio maneje (ej: 404 proforma no encontrada)
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error DB al añadir LineaProformaMaterial: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al añadir LineaProformaMaterial: {e}", exc_info=True)
        raise e

def add_linea_servicio(db: Session, *, linea_data: LineaProformaServicio) -> LineaProformaServicio:
    """
    Añade una nueva línea de servicio a una proforma en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        linea_data: Una instancia del modelo LineaProformaServicio con los datos a crear
                    (preparada por el servicio, incluyendo el total_linea calculado).

    Returns:
        El objeto LineaProformaServicio recién creado y refrescado.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: FK de proforma_id inválida).
        SQLAlchemyError: Para otros errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    db_linea = linea_data
    logger.debug(f"Repositorio: Intentando añadir LineaProformaServicio a Proforma ID: {db_linea.proforma_id}")
    try:
        db.add(db_linea)
        db.commit()
        db.refresh(db_linea)
        logger.info(f"LineaProformaServicio añadida con éxito: ID={db_linea.id} a Proforma ID={db_linea.proforma_id}")
        return db_linea
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al añadir LineaProformaServicio: {e}", exc_info=True)
        raise e
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error DB al añadir LineaProformaServicio: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al añadir LineaProformaServicio: {e}", exc_info=True)
        raise e

def update_proforma_totals(db: Session, *, proforma_id: int) -> Optional[Proforma]:
    """
    Recalcula y actualiza los campos subtotal, impuestos y total de una Proforma
    basándose en la suma de los 'total_linea' de sus líneas asociadas.

    Args:
        db: La sesión de base de datos activa.
        proforma_id: El ID de la proforma cuyos totales se actualizarán.

    Returns:
        El objeto Proforma actualizado si se encontró y actualizó, None si no se encontró.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos al leer o guardar.
        Exception: Para errores inesperados.
    """
    logger.info(f"Repositorio: Recalculando totales para Proforma ID: {proforma_id}")
    try:
        # 1. Obtener la proforma CON sus líneas (material Y servicio) cargadas
        #    Es crucial usar selectinload aquí para evitar N+1 queries al sumar totales.
        query = (
            select(Proforma)
            .where(Proforma.id == proforma_id)
            .options(
                selectinload(Proforma.lineas_material),
                selectinload(Proforma.lineas_servicio)
            )
        )
        db_proforma = db.exec(query).first()

        if not db_proforma:
            logger.warning(f"Proforma ID {proforma_id} no encontrada para actualizar totales.")
            return None # O lanzar excepción si se prefiere

        # 2. Calcular nuevo subtotal sumando los totales de todas las líneas
        new_subtotal = Decimal("0.00")
        if db_proforma.lineas_material:
            new_subtotal += sum(linea.total_linea for linea in db_proforma.lineas_material if linea.total_linea is not None)
        if db_proforma.lineas_servicio:
            new_subtotal += sum(linea.total_linea for linea in db_proforma.lineas_servicio if linea.total_linea is not None)

        # 3. Calcular impuestos (Ejemplo: IVA 12% sobre subtotal)
        # TODO: Implementar lógica de impuestos real. ¿Depende del tipo de producto/servicio? ¿Cliente?
        # Por ahora, un ejemplo simple o 0.
        tasa_iva = Decimal("0.12") # Ejemplo 12%
        new_impuestos = (new_subtotal * tasa_iva).quantize(Decimal("0.01")) # Redondear a 2 decimales
        # new_impuestos = Decimal("0.00") # O simplemente 0 por ahora

        # 4. Calcular nuevo total
        new_total = new_subtotal + new_impuestos

        logger.debug(f"Proforma ID {proforma_id}: Nuevo Subtotal={new_subtotal}, Impuestos={new_impuestos}, Total={new_total}")

        # 5. Actualizar los campos en el objeto Proforma
        update_data = {
            "subtotal": new_subtotal,
            "impuestos": new_impuestos,
            "total": new_total
        }
        db_proforma.sqlmodel_update(update_data)

        # 6. Guardar los cambios
        db.add(db_proforma)
        db.commit()
        db.refresh(db_proforma) # Refrescar para obtener los valores guardados

        logger.info(f"Totales actualizados exitosamente para Proforma ID: {proforma_id}")
        return db_proforma

    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error DB al actualizar totales de Proforma ID {proforma_id}: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al actualizar totales de Proforma ID {proforma_id}: {e}", exc_info=True)
        raise e

# (Aquí añadiríamos funciones para eliminar/actualizar líneas si fueran necesarias)



# =======================================
# Funciones CRUD para PedidoCliente (Existentes)
# =======================================
# ... (tus funciones existentes para PedidoCliente, Proforma, Líneas...) ...


# =====================================================
# === Funciones CRUD para OrdenProduccion (NUEVAS) ===
# =====================================================

def create_orden_produccion(db: Session, *, orden_data: OrdenProduccion) -> OrdenProduccion:
    """
    Crea un nuevo registro de OrdenProduccion en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        orden_data: Una instancia del modelo OrdenProduccion con los datos a crear.

    Returns:
        El objeto OrdenProduccion recién creado y refrescado.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: FK pedido_cliente_id duplicada/inválida).
        SQLAlchemyError: Para otros errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    db_orden = orden_data
    logger.debug(f"Repositorio: Intentando crear OrdenProduccion para Pedido ID: {db_orden.pedido_cliente_id}")
    try:
        db.add(db_orden)
        db.commit()
        db.refresh(db_orden)
        logger.info(f"OrdenProduccion creada con éxito: ID={db_orden.id} para Pedido ID={db_orden.pedido_cliente_id}")
        return db_orden
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al crear OrdenProduccion para Pedido ID {db_orden.pedido_cliente_id}: {e}", exc_info=True)
        raise e # Relanzar para que el servicio maneje (probablemente 409)
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de DB (SQLAlchemy) al crear OrdenProduccion: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al crear OrdenProduccion: {e}", exc_info=True)
        raise e

def get_orden_by_id(db: Session, *, orden_id: int, load_related: bool = True) -> Optional[OrdenProduccion]:
    """
    Obtiene una OrdenProduccion específica por su ID.

    Permite opcionalmente cargar relaciones comunes (pedido, supervisor, tareas)
    de forma eager.

    Args:
        db: La sesión de base de datos activa.
        orden_id: El ID de la orden a buscar.
        load_related: Si es True, carga eager las relaciones.

    Returns:
        El objeto OrdenProduccion si se encuentra, None en caso contrario.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Buscando OrdenProduccion por ID: {orden_id}, Cargar relacionados: {load_related}")
    try:
        query = select(OrdenProduccion).where(OrdenProduccion.id == orden_id)
        if load_related:
            query = query.options(
                selectinload(OrdenProduccion.pedido).selectinload(PedidoCliente.cliente), # Cargar Pedido y Cliente
                selectinload(OrdenProduccion.supervisor), # Cargar Supervisor (Usuario)
                selectinload(OrdenProduccion.asignaciones_tareas).selectinload(AsignacionTareaOrden.usuario_asignado), # Cargar Tareas y Usuario Asignado
                selectinload(OrdenProduccion.asignaciones_tareas).selectinload(AsignacionTareaOrden.rol_contexto) # Cargar Tareas y Rol Contexto
                # Considerar si cargar linea_servicio/linea_material dentro de tareas es necesario aquí
            )
        orden = db.exec(query).first()
        logger.debug(f"OrdenProduccion ID {orden_id} {'encontrada' if orden else 'no encontrada'}.")
        return orden
    except SQLAlchemyError as e:
        logger.error(f"Error DB (SQLAlchemy) al buscar OrdenProduccion ID {orden_id}: {e}", exc_info=True); raise e
    except Exception as e:
        logger.error(f"Error inesperado al buscar OrdenProduccion ID {orden_id}: {e}", exc_info=True); raise e

def list_ordenes_by_estado(
    db: Session, *,
    estados: List[str],
    skip: int = 0,
    limit: int = 100,
    load_related: bool = False # Por defecto False para listas puede ser más eficiente
) -> Sequence[OrdenProduccion]:
    """
    Obtiene una lista paginada de OrdenProduccion filtrada por uno o más estados.
    Ordena por prioridad descendente y luego por fecha de inicio de espera ascendente.

    Args:
        db: La sesión de base de datos activa.
        estados: Lista de strings con los estados a buscar (ej: ['PENDIENTE_ASIGNACION']).
        skip: Número de registros a saltar.
        limit: Número máximo de registros a devolver.
        load_related: Si es True, carga relaciones básicas (ej: pedido, supervisor).

    Returns:
        Una secuencia (lista) de objetos OrdenProduccion que coinciden.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Listando OrdenProduccion por Estados: {estados}, skip:{skip}, limit:{limit}, related:{load_related}")
    if not estados: # Si la lista de estados está vacía, no devolver nada
        return []
    try:
        query = select(OrdenProduccion).where(OrdenProduccion.estado.in_(estados))

        if load_related:
             query = query.options(
                 selectinload(OrdenProduccion.pedido).selectinload(PedidoCliente.cliente), # Cargar Pedido y Cliente
                 selectinload(OrdenProduccion.supervisor) # Cargar Supervisor
                 # Evitar cargar tareas por defecto en listas grandes
             )

        # Ordenar según índice idx_orden_prod_estado_prioridad (estado ya filtra, usar prioridad y fecha)
        query = query.order_by(OrdenProduccion.prioridad.desc(), OrdenProduccion.fecha_inicio_espera.asc())
        query = query.offset(skip).limit(limit)

        ordenes = db.exec(query).all()
        logger.debug(f"Se encontraron {len(ordenes)} OrdenProduccion para estados {estados}.")
        return ordenes
    except SQLAlchemyError as e:
        logger.error(f"Error DB (SQLAlchemy) al listar OrdenProduccion por estados {estados}: {e}", exc_info=True); raise e
    except Exception as e:
        logger.error(f"Error inesperado al listar OrdenProduccion por estados {estados}: {e}", exc_info=True); raise e

def update_orden_produccion(db: Session, *, db_orden: OrdenProduccion, update_data: Dict[str, Any]) -> OrdenProduccion:
    """
    Actualiza un registro de OrdenProduccion existente.

    Args:
        db: La sesión de base de datos activa.
        db_orden: El objeto OrdenProduccion existente obtenido de la BD.
        update_data: Un diccionario con los campos a actualizar.

    Returns:
        El objeto OrdenProduccion actualizado y refrescado.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    orden_id = db_orden.id
    logger.debug(f"Repositorio: Intentando actualizar OrdenProduccion ID: {orden_id} con datos: {list(update_data.keys())}")
    try:
        if not update_data:
            logger.warning(f"No se proporcionaron datos para actualizar OrdenProduccion ID {orden_id}.")
            return db_orden

        db_orden.sqlmodel_update(update_data)
        db.add(db_orden)
        db.commit()
        db.refresh(db_orden)
        logger.info(f"OrdenProduccion ID {orden_id} actualizada con éxito.")
        return db_orden
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error DB (SQLAlchemy) al actualizar OrdenProduccion ID {orden_id}: {e}", exc_info=True); raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al actualizar OrdenProduccion ID {orden_id}: {e}", exc_info=True); raise e


# =========================================================
# === Funciones CRUD para AsignacionTareaOrden (NUEVAS) ===
# =========================================================

def create_asignacion_tarea(db: Session, *, tarea_data: AsignacionTareaOrden) -> AsignacionTareaOrden:
    """
    Crea un nuevo registro de AsignacionTareaOrden en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        tarea_data: Una instancia del modelo AsignacionTareaOrden con los datos a crear.

    Returns:
        El objeto AsignacionTareaOrden recién creado y refrescado.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: FKs inválidas).
        SQLAlchemyError: Para otros errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    db_tarea = tarea_data
    logger.debug(f"Repositorio: Intentando crear AsignacionTareaOrden para Orden ID: {db_tarea.orden_id}, Tipo: {db_tarea.tipo_tarea}")
    try:
        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        logger.info(f"AsignacionTareaOrden creada con éxito: ID={db_tarea.id} para Orden ID={db_tarea.orden_id}")
        return db_tarea
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al crear AsignacionTareaOrden: {e}", exc_info=True)
        raise e
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error de DB (SQLAlchemy) al crear AsignacionTareaOrden: {e}", exc_info=True)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al crear AsignacionTareaOrden: {e}", exc_info=True)
        raise e

def get_tarea_by_id(db: Session, *, tarea_id: int, load_related: bool = False) -> Optional[AsignacionTareaOrden]:
    """
    Obtiene una AsignacionTareaOrden específica por su ID.

    Args:
        db: La sesión de base de datos activa.
        tarea_id: El ID de la tarea a buscar.
        load_related: Si es True, carga relaciones (orden, usuario, rol).

    Returns:
        El objeto AsignacionTareaOrden si se encuentra, None en caso contrario.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Buscando AsignacionTareaOrden por ID: {tarea_id}, Cargar relacionados: {load_related}")
    try:
        query = select(AsignacionTareaOrden).where(AsignacionTareaOrden.id == tarea_id)
        if load_related:
             query = query.options(
                 selectinload(AsignacionTareaOrden.orden),
                 selectinload(AsignacionTareaOrden.usuario_asignado),
                 selectinload(AsignacionTareaOrden.rol_contexto)
                 # Cargar linea_servicio / linea_material opcionalmente
             )
        tarea = db.exec(query).first()
        logger.debug(f"AsignacionTareaOrden ID {tarea_id} {'encontrada' if tarea else 'no encontrada'}.")
        return tarea
    except SQLAlchemyError as e:
        logger.error(f"Error DB (SQLAlchemy) al buscar Tarea ID {tarea_id}: {e}", exc_info=True); raise e
    except Exception as e:
        logger.error(f"Error inesperado al buscar Tarea ID {tarea_id}: {e}", exc_info=True); raise e

def list_tareas_by_orden(db: Session, *, orden_id: int, load_related: bool = True) -> Sequence[AsignacionTareaOrden]:
    """
    Obtiene todas las tareas asociadas a una Orden de Producción específica.

    Args:
        db: La sesión de base de datos activa.
        orden_id: El ID de la orden cuyas tareas se listarán.
        load_related: Si es True, carga relaciones de cada tarea (usuario, rol).

    Returns:
        Una secuencia (lista) de objetos AsignacionTareaOrden asociados a la orden.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    logger.debug(f"Repositorio: Listando Tareas para Orden ID: {orden_id}, Cargar relacionados: {load_related}")
    try:
        query = select(AsignacionTareaOrden).where(AsignacionTareaOrden.orden_id == orden_id)
        if load_related:
            query = query.options(
                 selectinload(AsignacionTareaOrden.usuario_asignado),
                 selectinload(AsignacionTareaOrden.rol_contexto)
            )
        # Ordenar quizás por ID o tipo de tarea
        query = query.order_by(AsignacionTareaOrden.id)
        tareas = db.exec(query).all()
        logger.debug(f"Se encontraron {len(tareas)} Tareas para Orden ID {orden_id}.")
        return tareas
    except SQLAlchemyError as e:
        logger.error(f"Error DB (SQLAlchemy) al listar Tareas para Orden ID {orden_id}: {e}", exc_info=True); raise e
    except Exception as e:
        logger.error(f"Error inesperado al listar Tareas para Orden ID {orden_id}: {e}", exc_info=True); raise e


def update_asignacion_tarea(db: Session, *, db_tarea: AsignacionTareaOrden, update_data: Dict[str, Any]) -> AsignacionTareaOrden:
    """
    Actualiza un registro de AsignacionTareaOrden existente.

    Args:
        db: La sesión de base de datos activa.
        db_tarea: El objeto AsignacionTareaOrden existente obtenido de la BD.
        update_data: Un diccionario con los campos a actualizar.

    Returns:
        El objeto AsignacionTareaOrden actualizado y refrescado.

    Raises:
        SQLAlchemyError: Para errores relacionados con la base de datos.
        Exception: Para errores inesperados.
    """
    tarea_id = db_tarea.id
    logger.debug(f"Repositorio: Intentando actualizar Tarea ID: {tarea_id} con datos: {list(update_data.keys())}")
    try:
        if not update_data:
            logger.warning(f"No se proporcionaron datos para actualizar Tarea ID {tarea_id}.")
            return db_tarea

        db_tarea.sqlmodel_update(update_data)
        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        logger.info(f"AsignacionTareaOrden ID {tarea_id} actualizada con éxito.")
        return db_tarea
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error DB (SQLAlchemy) al actualizar Tarea ID {tarea_id}: {e}", exc_info=True); raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado al actualizar Tarea ID {tarea_id}: {e}", exc_info=True); raise e
