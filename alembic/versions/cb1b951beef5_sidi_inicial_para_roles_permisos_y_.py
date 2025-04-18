"""Seed inicial para roles, permisos y asociaciones

Revision ID: cb1b951beef5
Revises: fa155d6b27e2
Create Date: 2025-04-17 22:50:44.828761

"""
from typing import Sequence, Union, Dict, List, Tuple, Set

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column,  select
from sqlalchemy import String, Integer, Text, Boolean, tuple_

# Importar datos iniciales desde el archivo centralizado
from app.initial_data import initial_roles, initial_permissions


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
        # --- Insertar Roles y Permisos (SE MANTIENE) ---
        print("(Migration) Verificando y poblando roles iniciales...")
        existing_roles_names = _get_existing_data(session, rol_table, ['nombre'])
        roles_to_insert = [r for r in initial_roles if r['nombre'] not in existing_roles_names]
        if roles_to_insert:
            op.bulk_insert(rol_table, roles_to_insert)
            print(f"(Migration) Se insertaron {len(roles_to_insert)} nuevos roles.")
        else:
            print("(Migration) Todos los roles iniciales ya existen.")

        print("(Migration) Verificando y poblando permisos iniciales...")
        existing_perms_keys = _get_existing_data(session, permiso_table, ['nombre_accion', 'nombre_recurso'])
        permissions_to_insert = [p for p in initial_permissions if (p['nombre_accion'], p['nombre_recurso']) not in existing_perms_keys]
        if permissions_to_insert:
            op.bulk_insert(permiso_table, permissions_to_insert)
            print(f"(Migration) Se insertaron {len(permissions_to_insert)} nuevos permisos.")
        else:
            print("(Migration) Todos los permisos iniciales ya existen.")

        session.commit() # Commit después de insertar roles/permisos base

        # --- Insertar Asociaciones RolPermiso (ELIMINADO de la migración) ---
        print("(Migration) Seeding de roles/permisos base completado. Las asociaciones se crearán en conftest.")

    except Exception as e:
        session.rollback()
        print(f"ERROR durante migración de seeding (roles/permisos base): {e}")
        raise
    finally:
        session.close()

def downgrade() -> None:
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    try:
        print("(Migration) Ejecutando downgrade de roles y permisos base...")

        # Obtener nombres/claves para identificar qué eliminar (solo roles y permisos)
        role_names_to_delete = [r['nombre'] for r in initial_roles]
        perm_keys_to_delete = [f"{p['nombre_accion']}:{p['nombre_recurso']}" for p in initial_permissions]

        # Obtener IDs actuales de la DB
        roles_db = session.execute(
            select(rol_table.c.id).where(rol_table.c.nombre.in_(role_names_to_delete))
        ).fetchall()
        role_ids_to_delete = [r.id for r in roles_db]

        permissions_db = session.execute(
            select(permiso_table.c.id, permiso_table.c.nombre_accion, permiso_table.c.nombre_recurso)
        ).fetchall()
        permission_ids_to_delete = [
            p.id for p in permissions_db
            if f"{p.nombre_accion}:{p.nombre_recurso}" in perm_keys_to_delete
        ]

        # --- Eliminar de rol_permiso (ELIMINADO de downgrade) ---
        # Ya no es necesario porque upgrade no los crea y la BD usa CASCADE
        # if role_ids_to_delete or permission_ids_to_delete:
        #    print("Saltando eliminación de rol_permiso (manejado por CASCADE o no creado aquí)")
        #    # delete_stmt = rol_permiso_table.delete().where(...)
        #    # session.execute(delete_stmt)

        # --- Eliminar permisos ---
        if permission_ids_to_delete:
            print(f"Eliminando {len(permission_ids_to_delete)} permisos base...")
            delete_stmt = permiso_table.delete().where(permiso_table.c.id.in_(permission_ids_to_delete))
            result = session.execute(delete_stmt)
            print(f"Permisos eliminados: {result.rowcount}")
        else:
            print("No se encontraron permisos base para eliminar.")

        # --- Eliminar roles ---
        if role_ids_to_delete:
             print(f"Eliminando {len(role_ids_to_delete)} roles base...")
             # Antes de eliminar roles, las FK en usuario_rol y rol_permiso con ON DELETE CASCADE
             # deberían eliminar las filas asociadas automáticamente si la BD está bien configurada.
             delete_stmt = rol_table.delete().where(rol_table.c.id.in_(role_ids_to_delete))
             result = session.execute(delete_stmt)
             print(f"Roles eliminados: {result.rowcount}")
        else:
            print("No se encontraron roles base para eliminar.")

        session.commit()
        print("(Migration) Downgrade de roles/permisos base completado.")

    except Exception as e:
        session.rollback()
        print(f"ERROR durante downgrade de roles/permisos base: {e}")
        raise
    finally:
        session.close()
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