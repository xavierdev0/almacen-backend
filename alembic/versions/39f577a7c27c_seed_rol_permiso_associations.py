"""Seed rol_permiso associations

Revision ID: xxxx_seed_associations # Cambia xxxx por el ID real generado
Revises: cb1b951beef5
Create Date: YYYY-MM-DD HH:MM:SS.ffffff # Fecha de creación

"""
from typing import Sequence, Union, Dict, List, Tuple, Set

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column, select

# Importar datos iniciales (ajustar ruta si es necesario)
try:
    from app.initial_data import role_permission_mapping
except ImportError:
    import sys
    import os
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from app.initial_data import role_permission_mapping


# revision identifiers, used by Alembic.
revision: str = '39f577a7c27c'
down_revision: Union[str, None] = 'cb1b951beef5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# --- Definiciones de Tablas ---
rol_table = sa.Table('rol', sa.MetaData(), sa.Column('id', sa.Integer, primary_key=True), sa.Column('nombre', sa.String(100)))
permiso_table = sa.Table('permiso', sa.MetaData(), sa.Column('id', sa.Integer, primary_key=True), sa.Column('nombre_accion', sa.String(100)), sa.Column('nombre_recurso', sa.String(100)))
rol_permiso_table = sa.Table('rol_permiso', sa.MetaData(), sa.Column('rol_id', sa.Integer, primary_key=True), sa.Column('permiso_id', sa.Integer, primary_key=True))

# --- Funciones auxiliares (copiadas de la versión anterior de cb1b) ---
def _get_id_map_bind(bind, table, key_cols: List[str]) -> Dict[Union[str, Tuple, str], int]: # Permitir str como key
    """Obtiene un mapeo de clave a ID usando el bind de Alembic. CORREGIDO para Permisos."""
    id_map = {}
    # Seleccionar ID y columnas clave
    columns_to_select = [table.c.id] + [table.c[col] for col in key_cols]
    query = select(*columns_to_select)
    results = bind.execute(query).fetchall()
    for result in results:
        item_id = result[0]
        if len(key_cols) == 1: 
            key = result[1] 
        else: 
            action = result[1] 
            resource = result[2] 
            key = f"{action}:{resource}" 
        id_map[key] = item_id
    return id_map
def upgrade() -> None:
    bind = op.get_bind()
    print(f"(Migration {revision}) Verificando y poblando asociaciones rol-permiso...")

    try:
        # Obtener mapeos de IDs (ahora deberían existir por la migración anterior)
        role_id_map = _get_id_map_bind(bind, rol_table, ['nombre'])
        perm_key_to_id_map = _get_id_map_bind(bind, permiso_table, ['nombre_accion', 'nombre_recurso'])

        if not role_id_map or not perm_key_to_id_map:
            print(f"ERROR (Migration {revision}): No se pudieron obtener los IDs de roles/permisos base.")
            raise Exception("Faltan roles/permisos base para crear asociaciones.")

        # Obtener links existentes
        existing_links_stmt = select(rol_permiso_table.c.rol_id, rol_permiso_table.c.permiso_id)
        existing_links_db = bind.execute(existing_links_stmt).fetchall()
        existing_links_set = set((link[0], link[1]) for link in existing_links_db)
        print(f"(Migration {revision}) Encontrados {len(existing_links_set)} links rol-permiso existentes.")

        # Calcular e insertar links faltantes
        links_to_insert: List[Dict[str, int]] = []
        warnings_found = False
        for role_name, perm_keys in role_permission_mapping.items():
            role_id = role_id_map.get(role_name)
            if not role_id:
                print(f"  WARNING (Migration {revision}): Rol '{role_name}' del mapeo no encontrado en BD.")
                warnings_found = True
                continue
            for perm_key in perm_keys:
                perm_id = perm_key_to_id_map.get(perm_key)
                if not perm_id:
                    print(f"  WARNING (Migration {revision}): Permiso '{perm_key}' del mapeo no encontrado en BD.")
                    warnings_found = True
                    continue

                if (role_id, perm_id) not in existing_links_set:
                    links_to_insert.append({'rol_id': role_id, 'permiso_id': perm_id})
                    existing_links_set.add((role_id, perm_id))

        if warnings_found:
             print(f"!! ADVERTENCIA (Migration {revision}): No se pudieron encontrar todos los Roles/Permisos. Las asociaciones pueden estar incompletas. !!")

        if links_to_insert:
            print(f"(Migration {revision}) Insertando {len(links_to_insert)} nuevas asociaciones rol-permiso...")
            op.bulk_insert(rol_permiso_table, links_to_insert)
            print(f"(Migration {revision}) Nuevas asociaciones insertadas.")
        else:
             if not warnings_found:
                print(f"(Migration {revision}) No se encontraron nuevas asociaciones rol-permiso para insertar (ya existen todas).")
             else:
                print(f"(Migration {revision}) No se insertaron asociaciones debido a warnings previos.")

        print(f"(Migration {revision}) Upgrade completado.")

    except Exception as e:
        print(f"ERROR durante la migración de seeding de asociaciones ({revision}): {e}")
        raise # Permitir que Alembic maneje el rollback

def downgrade() -> None:
    bind = op.get_bind()
    print(f"(Migration {revision}) Ejecutando downgrade: eliminando asociaciones rol-permiso iniciales...")

    try:
        # Obtener mapeos de IDs para determinar qué borrar
        role_id_map = _get_id_map_bind(bind, rol_table, ['nombre'])
        perm_id_map = _get_id_map_bind(bind, permiso_table, ['nombre_accion', 'nombre_recurso'])

        # Calcular los IDs específicos que esta migración habría insertado
        role_ids_in_mapping = [role_id_map[name] for name in role_permission_mapping.keys() if name in role_id_map]
        perm_ids_in_mapping = set()
        for perm_keys in role_permission_mapping.values():
            for key in perm_keys:
                if key in perm_id_map:
                    perm_ids_in_mapping.add(perm_id_map[key])

        print(f"(Downgrade {revision}) Se intentará eliminar asociaciones para {len(role_ids_in_mapping)} roles y {len(perm_ids_in_mapping)} permisos del mapeo inicial.")

        # Eliminar solo las asociaciones relacionadas con los roles/permisos del mapeo inicial
        if role_ids_in_mapping or perm_ids_in_mapping:
            conditions = []
            if role_ids_in_mapping: conditions.append(rol_permiso_table.c.rol_id.in_(role_ids_in_mapping))
            # Ser más específico: eliminar solo si ambos IDs son del mapeo podría ser más seguro,
            # pero eliminar si CUALQUIERA de los dos es del mapeo es más simple y consistente con el upgrade.
            if perm_ids_in_mapping: conditions.append(rol_permiso_table.c.permiso_id.in_(list(perm_ids_in_mapping)))

            if conditions:
                delete_stmt = rol_permiso_table.delete().where(sa.or_(*conditions))
                bind.execute(delete_stmt)
                print(f"(Downgrade {revision}) Se intentó eliminar asociaciones rol-permiso.")
        else:
             print(f"(Downgrade {revision}) No se encontraron IDs en el mapeo para eliminar asociaciones.")

        print(f"(Migration {revision}) Downgrade completado.")

    except Exception as e:
        print(f"ERROR durante el downgrade ({revision}): {e}")
        raise