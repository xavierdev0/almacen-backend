"""Seed inicial para roles, permisos y asociaciones

Revision ID: cb1b951beef5
Revises: fa155d6b27e2
Create Date: 2025-04-17 22:50:44.828761

"""
from typing import Sequence, Union, Dict, List, Tuple, Set

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Text, Boolean, select, tuple_

# revision identifiers, used by Alembic.
revision: str = 'cb1b951beef5'
down_revision: Union[str, None] = 'fa155d6b27e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



# --- Definiciones de Tablas para Operaciones de Datos ---
rol_table = sa.Table(
    'rol',
    sa.MetaData(),
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('nombre', sa.String(100), nullable=False, unique=True),
    sa.Column('descripcion', sa.Text, nullable=True),
)

permiso_table = sa.Table(
    'permiso',
    sa.MetaData(),
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('nombre_accion', sa.String(100), nullable=False),
    sa.Column('nombre_recurso', sa.String(100), nullable=False),
    sa.Column('descripcion', sa.Text, nullable=True),
)

rol_permiso_table = sa.Table(
    'rol_permiso',
    sa.MetaData(),
    sa.Column('rol_id', sa.Integer, primary_key=True),
    sa.Column('permiso_id', sa.Integer, primary_key=True),
)

# --- Datos Iniciales (Basados en nuestra definición) ---

# 1. Roles
initial_roles = [
    {'nombre': 'Administrador', 'descripcion': 'Acceso total al sistema.'},
    {'nombre': 'Vendedor', 'descripcion': 'Gestión de ventas y clientes.'},
    {'nombre': 'Supervisor', 'descripcion': 'Supervisión de producción y operarios.'},
    {'nombre': 'Dibujante', 'descripcion': 'Cotización y preparación de trabajos CNC.'},
    {'nombre': 'Operario', 'descripcion': 'Ejecución de tareas de producción.'},
]

# 2. Permisos (Lista refinada)
initial_permissions = [
    # Gestión Acceso y Sistema
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'usuario', 'descripcion': 'CRUD completo de usuarios (implica leer, crear, actualizar, eliminar).'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'rol', 'descripcion': 'CRUD completo de roles (implica leer, crear, actualizar, eliminar).'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'usuario', 'descripcion': 'Ver información de usuarios.'},
    {'nombre_accion': 'crear', 'nombre_recurso': 'usuario', 'descripcion': 'Registrar nuevos usuarios.'},
    {'nombre_accion': 'actualizar', 'nombre_recurso': 'usuario', 'descripcion': 'Modificar cualquier usuario.'},
    {'nombre_accion': 'eliminar', 'nombre_recurso': 'usuario', 'descripcion': 'Eliminar usuarios.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'rol', 'descripcion': 'Ver roles definidos.'},
    {'nombre_accion': 'crear', 'nombre_recurso': 'rol', 'descripcion': 'Crear nuevos roles.'},
    {'nombre_accion': 'actualizar', 'nombre_recurso': 'rol', 'descripcion': 'Modificar roles existentes.'},
    {'nombre_accion': 'eliminar', 'nombre_recurso': 'rol', 'descripcion': 'Eliminar roles.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'permiso', 'descripcion': 'Ver permisos definidos.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'permiso', 'descripcion': 'CRUD completo sobre permisos.'},
    {'nombre_accion': 'asignar', 'nombre_recurso': 'rol_usuario', 'descripcion': 'Conceder rol a usuario.'},
    {'nombre_accion': 'remover', 'nombre_recurso': 'rol_usuario', 'descripcion': 'Quitar rol a usuario.'},
    {'nombre_accion': 'asignar', 'nombre_recurso': 'permiso_rol', 'descripcion': 'Conceder permiso a rol.'},
    {'nombre_accion': 'remover', 'nombre_recurso': 'permiso_rol', 'descripcion': 'Quitar permiso a rol.'},
    {'nombre_accion': 'anular', 'nombre_recurso': 'venta_factura', 'descripcion': 'Anular una venta/factura completa.'},
    {'nombre_accion': 'ver', 'nombre_recurso': 'panel_admin', 'descripcion': 'Acceso a interfaz de administración.'},
    # Clientes
    {'nombre_accion': 'leer', 'nombre_recurso': 'cliente', 'descripcion': 'Ver clientes existentes.'},
    {'nombre_accion': 'crear', 'nombre_recurso': 'cliente', 'descripcion': 'Registrar nuevos clientes.'},
    {'nombre_accion': 'actualizar', 'nombre_recurso': 'cliente', 'descripcion': 'Modificar datos de clientes.'},
    {'nombre_accion': 'eliminar', 'nombre_recurso': 'cliente', 'descripcion': 'Eliminar clientes.'},
    # Proformas
    {'nombre_accion': 'leer', 'nombre_recurso': 'proforma', 'descripcion': 'Ver detalles de proformas.'},
    {'nombre_accion': 'crear', 'nombre_recurso': 'proforma', 'descripcion': 'Iniciar una nueva proforma.'},
    {'nombre_accion': 'actualizar', 'nombre_recurso': 'proforma_propia', 'descripcion': 'Modificar proforma propia (borrador).'},
    {'nombre_accion': 'actualizar', 'nombre_recurso': 'proforma_asignada', 'descripcion': 'Modificar proforma asignada (Dibujante).'},
    {'nombre_accion': 'actualizar', 'nombre_recurso': 'proforma_global', 'descripcion': 'Modificar cualquier proforma (Admin).'},
    {'nombre_accion': 'cancelar', 'nombre_recurso': 'proforma', 'descripcion': 'Cancelar una proforma.'},
    {'nombre_accion': 'enviar', 'nombre_recurso': 'proforma', 'descripcion': 'Marcar proforma como lista.'},
    {'nombre_accion': 'posponer', 'nombre_recurso': 'proforma', 'descripcion': 'Guardar proforma para después.'},
    {'nombre_accion': 'adjuntar', 'nombre_recurso': 'archivo_proforma', 'descripcion': 'Subir archivos a proforma (ej: CNC).'},
    # Pedidos y Órdenes
    {'nombre_accion': 'leer', 'nombre_recurso': 'pedido_cliente', 'descripcion': 'Ver estado general del pedido.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'orden_produccion', 'descripcion': 'Ver detalles de orden de producción.'},
    {'nombre_accion': 'tomar', 'nombre_recurso': 'tarea_orden', 'descripcion': 'Asignarse/Tomar tarea de una orden.'},
    {'nombre_accion': 'actualizar', 'nombre_recurso': 'tarea_orden', 'descripcion': 'Registrar avance/completar tarea.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'orden_produccion', 'descripcion': 'Gestionar estado/supervisor de orden.'},
    {'nombre_accion': 'adjuntar', 'nombre_recurso': 'archivo_orden', 'descripcion': 'Subir archivo/foto resultado final.'},
    # Inventario
    {'nombre_accion': 'leer', 'nombre_recurso': 'material_definicion', 'descripcion': 'Ver tipos de materiales.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'material_definicion', 'descripcion': 'CRUD sobre tipos de material.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'stock', 'descripcion': 'Ver niveles y detalles de stock.'},
    {'nombre_accion': 'ajustar', 'nombre_recurso': 'stock', 'descripcion': 'Realizar ajustes manuales de stock.'},
    {'nombre_accion': 'ver', 'nombre_recurso': 'merma', 'descripcion': 'Consultar stock marcado como merma.'},
    # Infraestructura
    {'nombre_accion': 'leer', 'nombre_recurso': 'area_trabajo', 'descripcion': 'Ver áreas de trabajo.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'area_trabajo', 'descripcion': 'CRUD sobre áreas de trabajo.'},
    {'nombre_accion': 'asignar', 'nombre_recurso': 'usuario_area', 'descripcion': 'Vincular usuario a área.'},
    {'nombre_accion': 'remover', 'nombre_recurso': 'usuario_area', 'descripcion': 'Desvincular usuario de área.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'maquina', 'descripcion': 'Ver información de máquinas.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'maquina', 'descripcion': 'CRUD sobre máquinas.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'herramienta', 'descripcion': 'Ver información de herramientas.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'herramienta', 'descripcion': 'CRUD sobre herramientas.'},
    {'nombre_accion': 'asignar', 'nombre_recurso': 'maquina_herramienta', 'descripcion': 'Vincular herramienta a máquina.'},
    {'nombre_accion': 'remover', 'nombre_recurso': 'maquina_herramienta', 'descripcion': 'Desvincular herramienta de máquina.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'registro_mantenimiento', 'descripcion': 'Ver historial de mantenimiento.'},
    {'nombre_accion': 'crear', 'nombre_recurso': 'registro_mantenimiento', 'descripcion': 'Registrar mantenimiento.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'reporte_error_maquina', 'descripcion': 'Ver errores reportados.'},
    {'nombre_accion': 'crear', 'nombre_recurso': 'reporte_error_maquina', 'descripcion': 'Reportar nuevo error/avería.'},
    {'nombre_accion': 'resolver', 'nombre_recurso': 'reporte_error_maquina', 'descripcion': 'Marcar error como resuelto.'},
    # Servicios y Fórmulas
    {'nombre_accion': 'leer', 'nombre_recurso': 'servicio_definicion', 'descripcion': 'Ver los servicios ofrecidos.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'servicio_definicion', 'descripcion': 'CRUD sobre definiciones de servicios.'},
    {'nombre_accion': 'leer', 'nombre_recurso': 'formula', 'descripcion': 'Ver fórmulas asociadas a servicios.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'formula', 'descripcion': 'CRUD sobre fórmulas.'},
    # Facturación y Pagos
    {'nombre_accion': 'leer', 'nombre_recurso': 'venta_factura', 'descripcion': 'Ver información de facturas.'},
    {'nombre_accion': 'actualizar', 'nombre_recurso': 'estado_pago', 'descripcion': 'Marcar factura como pagada.'},
    # Acciones Personales
    {'nombre_accion': 'leer', 'nombre_recurso': 'periodo_indisponibilidad', 'descripcion': 'Ver reportes de indisponibilidad.'},
    {'nombre_accion': 'registrar', 'nombre_recurso': 'mi_indisponibilidad', 'descripcion': 'Registrar periodo de indisponibilidad propio.'},
]

# 3. Mapeo Rol -> Lista de Permisos (accion:recurso)
role_permission_mapping: Dict[str, List[str]] = {
    'Administrador': [
        'gestionar:usuario', 'gestionar:rol', 'gestionar:permiso', 'asignar:rol_usuario',
        'remover:rol_usuario', 'asignar:permiso_rol', 'remover:permiso_rol',
        'anular:venta_factura', 'ver:panel_admin', 'leer:cliente', 'crear:cliente',
        'actualizar:cliente', 'eliminar:cliente', 'leer:proforma', 'crear:proforma',
        'actualizar:proforma_global', 'cancelar:proforma', 'enviar:proforma',
        'posponer:proforma', 'adjuntar:archivo_proforma', 'leer:pedido_cliente',
        'leer:orden_produccion', 'gestionar:orden_produccion', 'adjuntar:archivo_orden',
        'leer:material_definicion', 'gestionar:material_definicion', 'leer:stock',
        'ajustar:stock', 'ver:merma', 'leer:area_trabajo', 'gestionar:area_trabajo',
        'asignar:usuario_area', 'remover:usuario_area', 'leer:maquina', 'gestionar:maquina',
        'leer:herramienta', 'gestionar:herramienta', 'asignar:maquina_herramienta',
        'remover:maquina_herramienta', 'leer:registro_mantenimiento',
        'crear:registro_mantenimiento', 'leer:reporte_error_maquina',
        'crear:reporte_error_maquina', 'resolver:reporte_error_maquina',
        'leer:servicio_definicion', 'gestionar:servicio_definicion', 'leer:formula',
        'gestionar:formula', 'leer:venta_factura', 'actualizar:estado_pago',
        'leer:periodo_indisponibilidad', 'registrar:mi_indisponibilidad'
    ],
    'Vendedor': [
        'leer:cliente', 'crear:cliente', 'actualizar:cliente', 'leer:proforma',
        'crear:proforma', 'actualizar:proforma_propia', 'cancelar:proforma',
        'enviar:proforma', 'posponer:proforma', 'adjuntar:archivo_proforma',
        'leer:pedido_cliente', 'leer:orden_produccion', 'leer:material_definicion',
        'leer:stock', 'leer:servicio_definicion', 'leer:venta_factura',
        'actualizar:estado_pago', 'registrar:mi_indisponibilidad'
    ],
    'Supervisor': [
        'leer:cliente', 'leer:proforma', 'leer:pedido_cliente', 'leer:orden_produccion',
        'gestionar:orden_produccion', 'adjuntar:archivo_orden', 'leer:material_definicion',
        'leer:stock', 'ajustar:stock', 'ver:merma', 'leer:area_trabajo',
        'asignar:usuario_area', 'remover:usuario_area', 'leer:maquina', 'leer:herramienta',
        'asignar:maquina_herramienta', 'remover:maquina_herramienta',
        'leer:registro_mantenimiento', 'crear:registro_mantenimiento',
        'leer:reporte_error_maquina', 'crear:reporte_error_maquina',
        'resolver:reporte_error_maquina', 'leer:periodo_indisponibilidad',
        'registrar:mi_indisponibilidad'
    ],
    'Dibujante': [
        'leer:cliente', 'leer:proforma', 'actualizar:proforma_asignada',
        'adjuntar:archivo_proforma', 'leer:pedido_cliente', 'leer:orden_produccion',
        'tomar:tarea_orden', 'actualizar:tarea_orden', 'leer:material_definicion',
        'leer:stock', 'leer:maquina', 'leer:herramienta', 'leer:servicio_definicion',
        'leer:formula', 'crear:reporte_error_maquina', 'registrar:mi_indisponibilidad'
    ],
    'Operario': [
        'leer:orden_produccion', 'tomar:tarea_orden', 'actualizar:tarea_orden',
        'leer:stock', 'leer:maquina', 'leer:herramienta',
        'crear:reporte_error_maquina', 'registrar:mi_indisponibilidad'
    ]
}


def _get_existing_data(session, table, key_cols: List[str]) -> Set[Union[str, Tuple]]:
    """Obtiene un set de claves existentes (nombre o tupla accion/recurso) de una tabla."""
    existing_keys = set()
    query = select(*[table.c[col] for col in key_cols])
    results = session.execute(query).fetchall()
    for result in results:
        if len(key_cols) == 1:
            existing_keys.add(result[0])
        else:
            existing_keys.add(tuple(result))
    return existing_keys

def _get_id_map(session, table, key_cols: List[str]) -> Dict[Union[str, Tuple], int]:
    """Obtiene un mapeo de clave(nombre o tupla) a ID."""
    id_map = {}
    query = select(table.c.id, *[table.c[col] for col in key_cols])
    results = session.execute(query).fetchall()
    for result in results:
        item_id = result[0]
        if len(key_cols) == 1:
            key = result[1]
        else:
            key = tuple(result[1:])
        id_map[key] = item_id
    return id_map

def upgrade() -> None:
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    try:
        # --- 1. Insertar Roles (si no existen) ---
        print("Verificando y poblando roles iniciales...")
        existing_roles_names = _get_existing_data(session, rol_table, ['nombre'])
        roles_to_insert = [
            role for role in initial_roles
            if role['nombre'] not in existing_roles_names
        ]
        if roles_to_insert:
            op.bulk_insert(rol_table, roles_to_insert)
            print(f"Se insertaron {len(roles_to_insert)} nuevos roles.")
            # Forzar flush para asegurar que los datos se envíen a la DB antes de consultar IDs
            session.flush()
        else:
            print("Todos los roles iniciales ya existen.")

        # --- 2. Insertar Permisos (si no existen) ---
        print("Verificando y poblando permisos iniciales...")
        existing_perms_keys = _get_existing_data(session, permiso_table, ['nombre_accion', 'nombre_recurso'])
        permissions_to_insert = [
            perm for perm in initial_permissions
            if (perm['nombre_accion'], perm['nombre_recurso']) not in existing_perms_keys
        ]
        if permissions_to_insert:
            op.bulk_insert(permiso_table, permissions_to_insert)
            print(f"Se insertaron {len(permissions_to_insert)} nuevos permisos.")
            # Forzar flush
            session.flush()
        else:
            print("Todos los permisos iniciales ya existen.")

        # --- 3. Obtener IDs y Mapear (Incluye existentes y nuevos) ---
        print("Obteniendo IDs actualizados para roles y permisos...")
        role_id_map = _get_id_map(session, rol_table, ['nombre'])
        # --- DEBUGGING ROLES ---
        print(f"  DEBUG: Mapeo Rol->ID obtenido: {role_id_map}")
        if len(role_id_map) < len(initial_roles):
            print(f"  WARNING: No se pudieron obtener todos los IDs de Roles. Esperados: {len(initial_roles)}, Obtenidos: {len(role_id_map)}")
        # --- FIN DEBUGGING ---

        permission_id_map = _get_id_map(session, permiso_table, ['nombre_accion', 'nombre_recurso'])
        # --- DEBUGGING PERMISSIONS ---
        print(f"  DEBUG: Mapeo Permiso(accion, recurso)->ID obtenido (Tuplas): {permission_id_map}") # Mostrar mapa original
        if len(permission_id_map) < len(initial_permissions):
            print(f"  WARNING: No se pudieron obtener todos los IDs de Permisos. Esperados: {len(initial_permissions)}, Obtenidos: {len(permission_id_map)}")
        # Revisar explícitamente si las tuplas clave existen en el mapa obtenido
        if ('gestionar', 'usuario') not in permission_id_map:
            print("  DEBUG: La tupla ('gestionar', 'usuario') NO FUE ENCONTRADA en permission_id_map.")
        else:
             print(f"  DEBUG: La tupla ('gestionar', 'usuario') SÍ FUE ENCONTRADA. ID: {permission_id_map.get(('gestionar', 'usuario'))}")
        if ('gestionar', 'rol') not in permission_id_map:
            print("  DEBUG: La tupla ('gestionar', 'rol') NO FUE ENCONTRADA en permission_id_map.")
        else:
             print(f"  DEBUG: La tupla ('gestionar', 'rol') SÍ FUE ENCONTRADA. ID: {permission_id_map.get(('gestionar', 'rol'))}")
        # --- FIN DEBUGGING ---

        # Crear clave 'accion:recurso' para mapeo fácil
        permission_key_to_id_map = {
            f"{action}:{resource}": perm_id
            for (action, resource), perm_id in permission_id_map.items()
        }
        # --- DEBUGGING PERMISSIONS STR KEY ---
        print(f"  DEBUG: Mapeo Permiso str(accion:recurso)->ID creado: {permission_key_to_id_map}")
        if 'gestionar:usuario' not in permission_key_to_id_map:
             print("  DEBUG: La clave 'gestionar:usuario' NO ESTÁ en permission_key_to_id_map.")
        if 'gestionar:rol' not in permission_key_to_id_map:
             print("  DEBUG: La clave 'gestionar:rol' NO ESTÁ en permission_key_to_id_map.")
        # --- FIN DEBUGGING ---

        # --- 4. Crear y Insertar Asociaciones RolPermiso (si no existen) ---
        print("Verificando y creando asociaciones rol-permiso...")
        # (El resto de la lógica de asociación sigue igual que antes)
        existing_links_query = select(rol_permiso_table.c.rol_id, rol_permiso_table.c.permiso_id)
        existing_links_results = session.execute(existing_links_query).fetchall()
        existing_links_set = set(existing_links_results)

        rol_permiso_entries_to_insert = []
        missing_roles_count = 0
        missing_perms_count = 0
        skipped_existing_links = 0

        for role_name, permission_keys in role_permission_mapping.items():
            role_id = role_id_map.get(role_name)
            if not role_id:
                print(f"  CRITICAL WARNING: Rol '{role_name}' no tiene ID, omitiendo sus permisos.")
                missing_roles_count += 1
                continue

            for perm_key in permission_keys:
                permission_id = permission_key_to_id_map.get(perm_key) # Usa el mapa con clave string
                if not permission_id:
                    # Este es el warning que viste
                    print(f"  CRITICAL WARNING: Permiso '{perm_key}' no tiene ID para rol '{role_name}', omitiendo.")
                    missing_perms_count += 1
                    continue

                if (role_id, permission_id) not in existing_links_set:
                    rol_permiso_entries_to_insert.append({'rol_id': role_id, 'permiso_id': permission_id})
                else:
                    skipped_existing_links += 1

        if missing_roles_count > 0 or missing_perms_count > 0:
            print(f"Resumen de WARNINGS CRÍTICOS: {missing_roles_count} roles sin ID, {missing_perms_count} permisos sin ID.")

        if skipped_existing_links > 0:
            print(f"Se omitieron {skipped_existing_links} asociaciones rol-permiso que ya existían.")

        if rol_permiso_entries_to_insert:
            print(f"Insertando {len(rol_permiso_entries_to_insert)} nuevas asociaciones rol-permiso...")
            op.bulk_insert(rol_permiso_table, rol_permiso_entries_to_insert)
            print("Nuevas asociaciones insertadas.")
        else:
            print("No hay nuevas asociaciones rol-permiso para insertar.")

        session.commit()
        print("Poblado inicial (seeding) idempotente completado exitosamente.")

    except Exception as e:
        session.rollback()
        print(f"ERROR durante el poblado inicial (seeding): {e}")
        raise
    finally:
        session.close()



def downgrade() -> None:
    # El downgrade sigue siendo el mismo, ya que elimina específicamente
    # los roles/permisos/asociaciones definidos en esta migración,
    # independientemente de si ya existían antes o fueron creados aquí.
    # Si quieres un downgrade más seguro que solo elimine lo que *esta*
    # migración creó, sería más complejo y generalmente no es necesario
    # para migraciones de seeding.
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    try:
        print("Eliminando asociaciones rol-permiso, permisos y roles iniciales...")

        # (Mismo código de downgrade que la versión anterior)
        # Obtener nombres/claves para identificar qué eliminar
        role_names_to_delete = [r['nombre'] for r in initial_roles]
        perm_keys_to_delete = [f"{p['nombre_accion']}:{p['nombre_recurso']}" for p in initial_permissions]

        # Obtener los IDs actuales de la DB correspondientes a esos nombres/claves
        roles_db = session.execute(
            select(rol_table.c.id).where(rol_table.c.nombre.in_(role_names_to_delete))
        ).fetchall()
        role_ids_to_delete = [r.id for r in roles_db]
        print(f"Se identificaron {len(role_ids_to_delete)} IDs de roles para eliminar.")

        permissions_db = session.execute(
            select(permiso_table.c.id, permiso_table.c.nombre_accion, permiso_table.c.nombre_recurso)
        ).fetchall()
        permission_ids_to_delete = [
            p.id for p in permissions_db
            if f"{p.nombre_accion}:{p.nombre_recurso}" in perm_keys_to_delete
        ]
        print(f"Se identificaron {len(permission_ids_to_delete)} IDs de permisos para eliminar.")


        # 1. Eliminar de rol_permiso
        if role_ids_to_delete or permission_ids_to_delete:
            delete_stmt = rol_permiso_table.delete().where(
                sa.or_(
                    rol_permiso_table.c.rol_id.in_(role_ids_to_delete),
                    rol_permiso_table.c.permiso_id.in_(permission_ids_to_delete)
                )
            )
            result = session.execute(delete_stmt)
            print(f"Se eliminaron {result.rowcount} asociaciones rol-permiso.")
        else:
            print("No se encontraron IDs de roles o permisos para eliminar asociaciones.")

        # 2. Eliminar permisos
        if permission_ids_to_delete:
            delete_stmt = permiso_table.delete().where(permiso_table.c.id.in_(permission_ids_to_delete))
            result = session.execute(delete_stmt)
            print(f"Se eliminaron {result.rowcount} permisos.")
        else:
            print("No se encontraron IDs de permisos para eliminar.")

        # 3. Eliminar roles
        if role_ids_to_delete:
             delete_stmt = rol_table.delete().where(rol_table.c.id.in_(role_ids_to_delete))
             result = session.execute(delete_stmt)
             print(f"Se eliminaron {result.rowcount} roles.")
        else:
            print("No se encontraron IDs de roles para eliminar.")

        session.commit()
        print("Downgrade completado exitosamente.")

    except Exception as e:
        session.rollback()
        print(f"ERROR durante el downgrade: {e}")
        raise
    finally:
        session.close()