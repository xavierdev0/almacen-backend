"""Seed inicial para roles y permisos (solo tablas base)

Revision ID: cb1b951beef5
Revises: fa155d6b27e2
Create Date: 2025-04-17 22:50:44.828761

"""
from typing import Sequence, Union, Dict, List, Tuple, Set

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column, select

# Importar datos iniciales
try:
    from app.initial_data import initial_roles, initial_permissions
except ImportError:
    import sys
    import os
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from app.initial_data import initial_roles, initial_permissions

# revision identifiers, used by Alembic.
revision: str = 'cb1b951beef5'
down_revision: Union[str, None] = 'fa155d6b27e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# --- Definiciones de Tablas ---
rol_table = sa.Table(
    'rol', sa.MetaData(),
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('nombre', sa.String(100), nullable=False, unique=True),
    sa.Column('descripcion', sa.Text, nullable=True),
)
permiso_table = sa.Table(
    'permiso', sa.MetaData(),
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('nombre_accion', sa.String(100), nullable=False),
    sa.Column('nombre_recurso', sa.String(100), nullable=False),
    sa.Column('descripcion', sa.Text, nullable=True),
    sa.UniqueConstraint('nombre_accion', 'nombre_recurso', name='uq_permiso_accion_recurso')
)

# --- Función auxiliar (simplificada, solo para check) ---
def _get_existing_keys_bind(bind, table, key_cols: List[str]) -> Set[Union[str, Tuple]]:
    """Obtiene un set de claves existentes usando el bind de Alembic."""
    existing_keys = set()
    columns_to_select = [table.c[col] for col in key_cols]
    query = select(*columns_to_select)
    results = bind.execute(query).fetchall()
    for result in results:
        if len(key_cols) == 1:
            existing_keys.add(result[0])
        else:
            existing_keys.add(tuple(result))
    return existing_keys

def upgrade() -> None:
    bind = op.get_bind()

    # --- Insertar Roles Base (Idempotente) ---
    print("(Migration cb1b - simplified) Verificando y poblando roles iniciales...")
    existing_roles_names = _get_existing_keys_bind(bind, rol_table, ['nombre'])
    roles_to_insert = [r for r in initial_roles if r['nombre'] not in existing_roles_names]
    if roles_to_insert:
        op.bulk_insert(rol_table, roles_to_insert)
        print(f"(Migration cb1b - simplified) Se insertaron {len(roles_to_insert)} nuevos roles.")
    else:
        print("(Migration cb1b - simplified) Todos los roles iniciales ya existen.")

    # --- Insertar Permisos Base (Idempotente) ---
    print("(Migration cb1b - simplified) Verificando y poblando permisos iniciales...")
    existing_perms_keys = _get_existing_keys_bind(bind, permiso_table, ['nombre_accion', 'nombre_recurso'])
    permissions_to_insert = [
        p for p in initial_permissions
        if (p['nombre_accion'], p['nombre_recurso']) not in existing_perms_keys
    ]
    if permissions_to_insert:
        op.bulk_insert(permiso_table, permissions_to_insert)
        print(f"(Migration cb1b - simplified) Se insertaron {len(permissions_to_insert)} nuevos permisos.")
    else:
        print("(Migration cb1b - simplified) Todos los permisos iniciales ya existen.")

    print("(Migration cb1b - simplified) Upgrade completado (solo roles y permisos base).")


def downgrade() -> None:
    bind = op.get_bind()

    try:
        print("(Migration cb1b - simplified) Ejecutando downgrade: eliminando permisos y roles iniciales...")

        # Obtener nombres/claves para identificar qué eliminar
        role_names_to_delete = [r['nombre'] for r in initial_roles]
        perm_keys_to_delete = [f"{p['nombre_accion']}:{p['nombre_recurso']}" for p in initial_permissions]

        # Obtener los IDs actuales
        # Reutilizamos la función _get_id_map_bind definida localmente para este downgrade
        def _get_id_map_bind_local(bind, table, key_cols: List[str]) -> Dict[Union[str, Tuple], int]:
             id_map = {}
             columns_to_select = [table.c.id] + [table.c[col] for col in key_cols]
             query = select(*columns_to_select)
             results = bind.execute(query).fetchall()
             for result in results:
                 item_id = result[0]; key = tuple(result[1:]) if len(key_cols) > 1 else result[1]
                 id_map[key] = item_id
             return id_map

        role_id_map = _get_id_map_bind_local(bind, rol_table, ['nombre'])
        perm_id_map = _get_id_map_bind_local(bind, permiso_table, ['nombre_accion', 'nombre_recurso'])

        role_ids_to_delete = [role_id_map[name] for name in role_names_to_delete if name in role_id_map]
        permission_ids_to_delete = [perm_id_map[key] for key in perm_keys_to_delete if key in perm_id_map]

        # NO eliminamos de rol_permiso aquí, ya que esta migración no los creó.
        # La nueva migración se encargará de su propio downgrade.

        # Eliminar permisos
        if permission_ids_to_delete:
            delete_stmt = permiso_table.delete().where(permiso_table.c.id.in_(permission_ids_to_delete))
            bind.execute(delete_stmt)
            print(f"(Downgrade cb1b - simplified) Se intentó eliminar permisos base.")

        # Eliminar roles
        if role_ids_to_delete:
             delete_stmt = rol_table.delete().where(rol_table.c.id.in_(role_ids_to_delete))
             bind.execute(delete_stmt)
             print(f"(Downgrade cb1b - simplified) Se intentó eliminar roles base.")

        print("(Migration cb1b - simplified) Downgrade completado.")

    except Exception as e:
        print(f"ERROR durante el downgrade (cb1b - simplified): {e}")
        raise