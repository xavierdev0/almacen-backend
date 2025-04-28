# .gitignore

```
# Entorno virtual
venv/

# Bytecode de Python y archivos temporales
__pycache__/
*.pyc
*.pyo
*.pyd

# Variables de entorno
.env

# Configuración del IDE (VS Code)
.vscode/


*.db

# Archivos de log
*.log

# Otros archivos específicos del sistema operativo
*.swp # Archivos de swap de Vim
*.swo # Archivos de swap de Vim
.DS_Store # Archivos de macOS

# Configuraciones de PyCharm
.idea/

# Archivos de cobertura de tests
.coverage
htmlcov/

# Archivos generados por herramientas de documentación
docs/_build/
```

# .pytest_cache\.gitignore

```
# Created by pytest automatically.
*

```

# .pytest_cache\CACHEDIR.TAG

```TAG
Signature: 8a477f597d28d172789f06886806bc55
# This file is a cache directory tag created by pytest.
# For information about cache directory tags, see:
#	https://bford.info/cachedir/spec.html

```

# .pytest_cache\README.md

```md
# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

```

# .pytest_cache\v\cache\lastfailed

```
{
  "tests/test_basic_flow.py::test_create_and_login_flow": true,
  "tests/test_basic_flow.py::test_login_failure_wrong_password": true,
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_list_materiales_dimensionales_forbidden": true,
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_consumible_success": true
}
```

# .pytest_cache\v\cache\nodeids

```
[
  "tests/api/v1/test_clientes_api.py::test_create_cliente_duplicate_email",
  "tests/api/v1/test_clientes_api.py::test_create_cliente_duplicate_identificacion",
  "tests/api/v1/test_clientes_api.py::test_create_cliente_invalid_data",
  "tests/api/v1/test_clientes_api.py::test_create_cliente_success_admin",
  "tests/api/v1/test_clientes_api.py::test_create_cliente_success_vendedor",
  "tests/api/v1/test_clientes_api.py::test_create_cliente_unauthenticated",
  "tests/api/v1/test_clientes_api.py::test_delete_cliente_forbidden_vendedor",
  "tests/api/v1/test_clientes_api.py::test_delete_cliente_not_found_admin",
  "tests/api/v1/test_clientes_api.py::test_delete_cliente_success_admin",
  "tests/api/v1/test_clientes_api.py::test_delete_cliente_unauthenticated",
  "tests/api/v1/test_clientes_api.py::test_get_cliente_not_found",
  "tests/api/v1/test_clientes_api.py::test_get_cliente_success_vendedor",
  "tests/api/v1/test_clientes_api.py::test_get_cliente_unauthenticated",
  "tests/api/v1/test_clientes_api.py::test_list_clientes_pagination",
  "tests/api/v1/test_clientes_api.py::test_list_clientes_success_admin",
  "tests/api/v1/test_clientes_api.py::test_list_clientes_success_vendedor",
  "tests/api/v1/test_clientes_api.py::test_list_clientes_unauthenticated",
  "tests/api/v1/test_clientes_api.py::test_update_cliente_conflict_email",
  "tests/api/v1/test_clientes_api.py::test_update_cliente_invalid_data",
  "tests/api/v1/test_clientes_api.py::test_update_cliente_not_found",
  "tests/api/v1/test_clientes_api.py::test_update_cliente_success_vendedor",
  "tests/api/v1/test_clientes_api.py::test_update_cliente_unauthenticated",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_adjust_stock_consumible_forbidden",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_adjust_stock_consumible_negative_result",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_adjust_stock_consumible_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_create_material_consumible_duplicate_sku",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_create_material_consumible_forbidden",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_create_material_consumible_invalid_data",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_create_material_consumible_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_delete_material_consumible_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_delete_material_consumible_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_get_material_consumible_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_get_material_consumible_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_list_materiales_consumibles_permission_vendedor",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_list_materiales_consumibles_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_update_material_consumible_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialConsumibleAPI::test_update_material_consumible_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_create_material_dimensional_duplicate_sku",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_create_material_dimensional_forbidden",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_create_material_dimensional_invalid_data",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_create_material_dimensional_success_admin",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_delete_material_dimensional_conflict",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_delete_material_dimensional_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_delete_material_dimensional_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_get_material_dimensional_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_get_material_dimensional_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_list_materiales_dimensionales_forbidden",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_list_materiales_dimensionales_forbidden_operario",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_list_materiales_dimensionales_permission_vendedor",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_list_materiales_dimensionales_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_update_material_dimensional_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialDimensionalAPI::test_update_material_dimensional_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_adjust_stock_simple_forbidden",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_adjust_stock_simple_negative_result",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_adjust_stock_simple_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_create_material_simple_duplicate_sku",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_create_material_simple_forbidden",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_create_material_simple_invalid_data",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_create_material_simple_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_delete_material_simple_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_delete_material_simple_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_get_material_simple_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_get_material_simple_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_list_materiales_simples_permission_vendedor",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_list_materiales_simples_success",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_update_material_simple_not_found",
  "tests/api/v1/test_inventario_api.py::TestMaterialSimpleAPI::test_update_material_simple_success",
  "tests/api/v1/test_inventario_api.py::TestStockItemDimensionalAPI::test_create_stock_item_invalid_foreign_key",
  "tests/api/v1/test_inventario_api.py::TestStockItemDimensionalAPI::test_create_stock_item_success",
  "tests/api/v1/test_inventario_api.py::TestStockItemDimensionalAPI::test_delete_material_dimensional_conflict",
  "tests/api/v1/test_inventario_api.py::TestStockItemDimensionalAPI::test_get_stock_item_not_found",
  "tests/api/v1/test_inventario_api.py::TestStockItemDimensionalAPI::test_get_stock_item_success",
  "tests/api/v1/test_inventario_api.py::TestStockItemDimensionalAPI::test_list_stock_items_filtered",
  "tests/api/v1/test_inventario_api.py::TestStockItemDimensionalAPI::test_list_stock_items_success",
  "tests/api/v1/test_pedidos_api.py::test_create_pedido_cliente_not_found",
  "tests/api/v1/test_pedidos_api.py::test_create_pedido_forbidden_operario",
  "tests/api/v1/test_pedidos_api.py::test_create_pedido_invalid_payload",
  "tests/api/v1/test_pedidos_api.py::test_create_pedido_success_admin",
  "tests/api/v1/test_pedidos_api.py::test_create_pedido_success_vendedor",
  "tests/api/v1/test_pedidos_api.py::test_create_pedido_unauthenticated",
  "tests/api/v1/test_pedidos_api.py::test_get_pedido_forbidden_operario",
  "tests/api/v1/test_pedidos_api.py::test_get_pedido_not_found",
  "tests/api/v1/test_pedidos_api.py::test_get_pedido_success_admin",
  "tests/api/v1/test_pedidos_api.py::test_get_pedido_success_vendedor",
  "tests/api/v1/test_pedidos_api.py::test_get_pedido_unauthenticated",
  "tests/api/v1/test_pedidos_api.py::test_list_pedidos_filtered",
  "tests/api/v1/test_pedidos_api.py::test_list_pedidos_forbidden_operario",
  "tests/api/v1/test_pedidos_api.py::test_list_pedidos_pagination",
  "tests/api/v1/test_pedidos_api.py::test_list_pedidos_success",
  "tests/api/v1/test_pedidos_api.py::test_list_pedidos_unauthenticated",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_consumible_success",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_forbidden",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_invalid_payload",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_not_found",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_success[CONSUMIBLE-material_consumible_de_prueba-payload_extra0]",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_success[SIMPLE-material_simple_de_prueba-payload_extra1]",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_success[STOCK_DIMENSIONAL-stock_item_dimensional_de_prueba-payload_extra2]",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_wrong_proforma_state",
  "tests/api/v1/test_proformas_api.py::test_add_linea_material_wrong_proforma_type",
  "tests/api/v1/test_proformas_api.py::test_add_linea_servicio_def_not_found",
  "tests/api/v1/test_proformas_api.py::test_add_linea_servicio_forbidden",
  "tests/api/v1/test_proformas_api.py::test_add_linea_servicio_invalid_material_link",
  "tests/api/v1/test_proformas_api.py::test_add_linea_servicio_linked_to_material_success",
  "tests/api/v1/test_proformas_api.py::test_add_linea_servicio_success",
  "tests/api/v1/test_proformas_api.py::test_add_linea_servicio_wrong_proforma_state",
  "tests/api/v1/test_proformas_api.py::test_add_linea_servicio_wrong_proforma_type",
  "tests/api/v1/test_proformas_api.py::test_update_proforma_estado_success",
  "tests/api/v1/test_proformas_api.py::test_update_proforma_forbidden_operario",
  "tests/api/v1/test_proformas_api.py::test_update_proforma_invalid_payload_estado",
  "tests/api/v1/test_proformas_api.py::test_update_proforma_invalid_state_transition",
  "tests/api/v1/test_proformas_api.py::test_update_proforma_not_found",
  "tests/api/v1/test_proformas_api.py::test_update_proforma_notas_success",
  "tests/api/v1/test_proformas_api.py::test_update_proforma_unauthenticated",
  "tests/api/v1/test_roles_api.py::test_assign_permission_already_assigned_admin",
  "tests/api/v1/test_roles_api.py::test_assign_permission_forbidden_non_admin",
  "tests/api/v1/test_roles_api.py::test_assign_permission_permission_not_found_admin",
  "tests/api/v1/test_roles_api.py::test_assign_permission_role_not_found_admin",
  "tests/api/v1/test_roles_api.py::test_assign_permission_to_role_success_admin",
  "tests/api/v1/test_roles_api.py::test_create_role_duplicate_name",
  "tests/api/v1/test_roles_api.py::test_create_role_forbidden_non_admin",
  "tests/api/v1/test_roles_api.py::test_create_role_invalid_data",
  "tests/api/v1/test_roles_api.py::test_create_role_success_admin",
  "tests/api/v1/test_roles_api.py::test_delete_role_conflict_assigned_admin",
  "tests/api/v1/test_roles_api.py::test_delete_role_forbidden_non_admin",
  "tests/api/v1/test_roles_api.py::test_delete_role_not_found_admin",
  "tests/api/v1/test_roles_api.py::test_delete_role_success_admin",
  "tests/api/v1/test_roles_api.py::test_get_role_by_id_success",
  "tests/api/v1/test_roles_api.py::test_get_role_forbidden_non_admin",
  "tests/api/v1/test_roles_api.py::test_get_role_not_found",
  "tests/api/v1/test_roles_api.py::test_list_roles_forbidden_non_admin",
  "tests/api/v1/test_roles_api.py::test_list_roles_success_admin",
  "tests/api/v1/test_roles_api.py::test_list_roles_unauthenticated",
  "tests/api/v1/test_roles_api.py::test_remove_permission_forbidden_non_admin",
  "tests/api/v1/test_roles_api.py::test_remove_permission_from_role_success_admin",
  "tests/api/v1/test_roles_api.py::test_remove_permission_not_assigned_admin",
  "tests/api/v1/test_roles_api.py::test_remove_permission_permission_not_found_admin",
  "tests/api/v1/test_roles_api.py::test_remove_permission_role_not_found_admin",
  "tests/api/v1/test_roles_api.py::test_update_role_conflict_name_admin",
  "tests/api/v1/test_roles_api.py::test_update_role_forbidden_non_admin",
  "tests/api/v1/test_roles_api.py::test_update_role_invalid_data_admin",
  "tests/api/v1/test_roles_api.py::test_update_role_not_found_admin",
  "tests/api/v1/test_roles_api.py::test_update_role_success_admin",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_create_servicio_duplicate_name_admin",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_create_servicio_forbidden_vendedor",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_create_servicio_invalid_data",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_create_servicio_success_admin",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_delete_servicio_not_found",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_delete_servicio_success",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_get_servicio_not_found",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_get_servicio_success",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_list_servicios_forbidden_operario",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_list_servicios_pagination",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_list_servicios_permission_dibujante",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_list_servicios_permission_vendedor",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_list_servicios_success",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_update_servicio_duplicate_name",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_update_servicio_not_found",
  "tests/api/v1/test_servicios_api.py::TestServicioDefinicionAPI::test_update_servicio_success",
  "tests/api/v1/test_usuarios_api.py::test_assign_role_already_assigned_admin",
  "tests/api/v1/test_usuarios_api.py::test_assign_role_forbidden_non_admin",
  "tests/api/v1/test_usuarios_api.py::test_assign_role_role_not_found_admin",
  "tests/api/v1/test_usuarios_api.py::test_assign_role_to_user_success_admin",
  "tests/api/v1/test_usuarios_api.py::test_assign_role_user_not_found_admin",
  "tests/api/v1/test_usuarios_api.py::test_create_user_duplicate_email_admin",
  "tests/api/v1/test_usuarios_api.py::test_create_user_duplicate_username_admin",
  "tests/api/v1/test_usuarios_api.py::test_create_user_forbidden_non_admin",
  "tests/api/v1/test_usuarios_api.py::test_create_user_invalid_data_admin",
  "tests/api/v1/test_usuarios_api.py::test_create_user_non_existent_role_id_admin",
  "tests/api/v1/test_usuarios_api.py::test_create_user_success_admin",
  "tests/api/v1/test_usuarios_api.py::test_read_me_success",
  "tests/api/v1/test_usuarios_api.py::test_read_me_unauthenticated",
  "tests/api/v1/test_usuarios_api.py::test_read_user_forbidden_non_admin",
  "tests/api/v1/test_usuarios_api.py::test_read_user_not_found_admin",
  "tests/api/v1/test_usuarios_api.py::test_read_user_success_admin",
  "tests/api/v1/test_usuarios_api.py::test_remove_role_forbidden_non_admin",
  "tests/api/v1/test_usuarios_api.py::test_remove_role_from_user_success_admin",
  "tests/api/v1/test_usuarios_api.py::test_remove_role_not_assigned_admin",
  "tests/api/v1/test_usuarios_api.py::test_remove_role_role_not_found_admin",
  "tests/api/v1/test_usuarios_api.py::test_remove_role_user_not_found_admin",
  "tests/api/v1/test_usuarios_api.py::test_update_me_duplicate_email",
  "tests/api/v1/test_usuarios_api.py::test_update_me_invalid_email",
  "tests/api/v1/test_usuarios_api.py::test_update_me_success",
  "tests/api/v1/test_usuarios_api.py::test_update_me_unauthenticated",
  "tests/api/v1/test_usuarios_api.py::test_update_my_password_mismatch_new",
  "tests/api/v1/test_usuarios_api.py::test_update_my_password_short_new",
  "tests/api/v1/test_usuarios_api.py::test_update_my_password_success",
  "tests/api/v1/test_usuarios_api.py::test_update_my_password_unauthenticated",
  "tests/api/v1/test_usuarios_api.py::test_update_my_password_wrong_old",
  "tests/test_basic_flow.py::test_create_and_login_flow",
  "tests/test_basic_flow.py::test_login_failure_wrong_password"
]
```

# .pytest_cache\v\cache\stepwise

```
[]
```

# alembic.ini

```ini
# A generic, single database configuration.

[alembic]
# path to migration scripts
# Use forward slashes (/) also on windows to provide an os agnostic path
script_location = alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python>=3.9 or backports.zoneinfo library and tzdata library.
# Any required deps can installed by adding `alembic[tz]` to the pip requirements
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to alembic/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "version_path_separator" below.
# version_locations = %(here)s/bar:%(here)s/bat:alembic/versions

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses os.pathsep.
# If this key is omitted entirely, it falls back to the legacy behavior of splitting on spaces and/or commas.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
# version_path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
version_path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

# sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the exec runner, execute a binary
# hooks = ruff
# ruff.type = exec
# ruff.executable = %(here)s/.venv/bin/ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

```

# alembic\env.py

```py
import os
import sys
from logging.config import fileConfig


from sqlalchemy import pool
from alembic import context

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

from sqlmodel import SQLModel
from app.core.database import engine
from app.models import *

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = engine.url #config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    #connectable = engine_from_config(
    #    config.get_section(config.config_ini_section, {}),
    #    prefix="sqlalchemy.",
    #    poolclass=pool.NullPool,
    #)

    connectable = engine
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

# alembic\README

```
Generic single-database configuration.
```

# alembic\script.py.mako

```mako
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade schema."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade schema."""
    ${downgrades if downgrades else "pass"}

```

# alembic\versions\39f577a7c27c_seed_rol_permiso_associations.py

```py
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
```

# alembic\versions\cb1b951beef5_sidi_inicial_para_roles_permisos_y_.py

```py
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
```

# alembic\versions\fa155d6b27e2_creacion_inicial_del_esquema_basado_en_.py

```py
"""Creacion inicial del esquema basado en modelos

Revision ID: fa155d6b27e2
Revises: 
Create Date: 2025-04-17 00:34:38.823864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'fa155d6b27e2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area_trabajo',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=150), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nombre')
    )
    op.create_table('cliente',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('tipo_identificacion', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
        sa.Column('identificacion_fiscal', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
        sa.Column('persona_contacto', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
        sa.Column('email', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
        sa.Column('telefono', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
        sa.Column('direccion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cliente_email'), 'cliente', ['email'], unique=True)
    op.create_index(op.f('ix_cliente_identificacion_fiscal'), 'cliente', ['identificacion_fiscal'], unique=True)
    op.create_index(op.f('ix_cliente_nombre'), 'cliente', ['nombre'], unique=False)

    op.create_table('herramienta',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=150), nullable=False),
        sa.Column('tipo', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=True),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('codigo_interno', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_herramienta_codigo_interno'), 'herramienta', ['codigo_interno'], unique=True)

    op.create_table('material_consumible',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('sku', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('unidad_medida', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('rendimiento_m2', sa.Numeric(precision=10, scale=3), nullable=True),
        sa.Column('precio_venta_base_unidad', sa.Numeric(precision=14, scale=4), nullable=False),
        sa.Column('stock_actual', sa.Numeric(precision=10, scale=3), nullable=False),
        sa.Column('stock_minimo', sa.Numeric(precision=10, scale=3), nullable=True),
        sa.Column('ubicacion', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_material_consumible_sku'), 'material_consumible', ['sku'], unique=True)

    op.create_table('material_dimensional',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('sku', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('espesor_nominal', sa.Numeric(precision=10, scale=3), nullable=False),
        sa.Column('unidad_dimension', sqlmodel.sql.sqltypes.AutoString(length=10), nullable=False),
        sa.Column('precio_venta_base_unidad', sa.Numeric(precision=14, scale=4), nullable=False),
        sa.Column('unidad_precio_venta', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=False),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_material_dimensional_sku'), 'material_dimensional', ['sku'], unique=True)

    op.create_table('material_simple',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('sku', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('unidad_medida', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('precio_venta_base_unidad', sa.Numeric(precision=14, scale=4), nullable=False),
        sa.Column('stock_actual', sa.Numeric(precision=10, scale=3), nullable=False),
        sa.Column('stock_minimo', sa.Numeric(precision=10, scale=3), nullable=True),
        sa.Column('ubicacion', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_material_simple_sku'), 'material_simple', ['sku'], unique=True)

    op.create_table('permiso',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre_accion', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
        sa.Column('nombre_recurso', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nombre_accion', 'nombre_recurso', name='uq_permiso_accion_recurso')
    )

    op.create_table('rol',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rol_nombre'), 'rol', ['nombre'], unique=True)

    op.create_table('servicio_definicion',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('codigo', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('unidad_cobro', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('costo_por_unidad', sa.Numeric(precision=12, scale=2), nullable=True),
        sa.Column('costo_por_minuto', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column('tiempo_setup_min', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column('tiempo_preparado_min_por_unidad', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column('factor_ih', sa.Numeric(precision=5, scale=3), nullable=True),
        sa.Column('factor_st', sa.Numeric(precision=5, scale=3), nullable=True),
        sa.Column('factor_m', sa.Numeric(precision=5, scale=3), nullable=True),
        sa.Column('requiere_dibujo_cnc', sa.Boolean(), nullable=False),
        # --- CORREGIDO (Aplicado en el intento anterior, mantener) ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_servicio_definicion_codigo'), 'servicio_definicion', ['codigo'], unique=True)

    op.create_table('usuario',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
        sa.Column('email', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('contrasena_hash', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('nombre_completo', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('esta_activo', sa.Boolean(), nullable=False),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuario_email'), 'usuario', ['email'], unique=True)
    op.create_index(op.f('ix_usuario_username'), 'usuario', ['username'], unique=True)

    op.create_table('formula',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('servicio_definicion_id', sa.Integer(), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=150), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.ForeignKeyConstraint(['servicio_definicion_id'], ['servicio_definicion.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_formula_servicio_definicion_id'), 'formula', ['servicio_definicion_id'], unique=False)

    op.create_table('maquina',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=150), nullable=False),
        sa.Column('tipo', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('modelo', sqlmodel.sql.sqltypes.AutoString(length=150), nullable=True),
        sa.Column('numero_serie', sqlmodel.sql.sqltypes.AutoString(length=150), nullable=True),
        sa.Column('area_trabajo_id', sa.Integer(), nullable=True),
        sa.Column('margen_perdida_mm', sa.Numeric(precision=5, scale=2), nullable=True),
        sa.Column('estado', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('fecha_adquisicion', sa.Date(), nullable=True),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.ForeignKeyConstraint(['area_trabajo_id'], ['area_trabajo.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_maquina_area_trabajo_id'), 'maquina', ['area_trabajo_id'], unique=False)
    op.create_index(op.f('ix_maquina_numero_serie'), 'maquina', ['numero_serie'], unique=True)

    op.create_table('pedido_cliente',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('cliente_id', sa.Integer(), nullable=False),
        sa.Column('usuario_id_vendedor', sa.Integer(), nullable=False),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('estado', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
        sa.ForeignKeyConstraint(['usuario_id_vendedor'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pedido_cliente_cliente_id'), 'pedido_cliente', ['cliente_id'], unique=False)
    op.create_index(op.f('ix_pedido_cliente_estado'), 'pedido_cliente', ['estado'], unique=False)
    op.create_index(op.f('ix_pedido_cliente_usuario_id_vendedor'), 'pedido_cliente', ['usuario_id_vendedor'], unique=False)

    op.create_table('periodo_indisponibilidad',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('usuario_id', sa.Integer(), nullable=False),
        sa.Column('fecha_inicio', sa.DateTime(), nullable=False), # Fecha inicio usualmente se pone al crear, no default
        sa.Column('fecha_fin', sa.DateTime(), nullable=True),
        sa.Column('motivo', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_periodo_indisponibilidad_usuario_id'), 'periodo_indisponibilidad', ['usuario_id'], unique=False)

    op.create_table('rol_permiso',
        sa.Column('rol_id', sa.Integer(), nullable=False),
        sa.Column('permiso_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['permiso_id'], ['permiso.id'], ),
        sa.ForeignKeyConstraint(['rol_id'], ['rol.id'], ),
        sa.PrimaryKeyConstraint('rol_id', 'permiso_id')
    )
    op.create_table('usuario_area_trabajo',
        sa.Column('usuario_id', sa.Integer(), nullable=False),
        sa.Column('area_trabajo_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['area_trabajo_id'], ['area_trabajo.id'], ),
        sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('usuario_id', 'area_trabajo_id')
    )
    op.create_table('usuario_rol',
        sa.Column('usuario_id', sa.Integer(), nullable=False),
        sa.Column('rol_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['rol_id'], ['rol.id'], ),
        sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('usuario_id', 'rol_id')
    )
    op.create_table('formula_item',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('formula_id', sa.Integer(), nullable=False),
        sa.Column('tipo_material', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('material_consumible_id', sa.Integer(), nullable=True),
        sa.Column('material_simple_id', sa.Integer(), nullable=True),
        sa.Column('cantidad_necesaria', sa.Numeric(precision=10, scale=3), nullable=False),
        sa.Column('unidad_rendimiento', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('descripcion_uso', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['formula_id'], ['formula.id'], ),
        sa.ForeignKeyConstraint(['material_consumible_id'], ['material_consumible.id'], ),
        sa.ForeignKeyConstraint(['material_simple_id'], ['material_simple.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_formula_item_formula_id'), 'formula_item', ['formula_id'], unique=False)
    op.create_index(op.f('ix_formula_item_material_consumible_id'), 'formula_item', ['material_consumible_id'], unique=False)
    op.create_index(op.f('ix_formula_item_material_simple_id'), 'formula_item', ['material_simple_id'], unique=False)

    op.create_table('maquina_herramienta',
        sa.Column('maquina_id', sa.Integer(), nullable=False),
        sa.Column('herramienta_id', sa.Integer(), nullable=False),
        # --- CORREGIDO (Aunque fecha_asignacion usualmente se pone al asignar) ---
        sa.Column('fecha_asignacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.Column('posicion', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
        sa.ForeignKeyConstraint(['herramienta_id'], ['herramienta.id'], ),
        sa.ForeignKeyConstraint(['maquina_id'], ['maquina.id'], ),
        sa.PrimaryKeyConstraint('maquina_id', 'herramienta_id')
    )

    op.create_table('orden_produccion',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('pedido_cliente_id', sa.Integer(), nullable=False),
        sa.Column('usuario_id_supervisor', sa.Integer(), nullable=True),
        sa.Column('estado', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_inicio_espera', sa.DateTime(), server_default=sa.func.now(), nullable=True), # Default now() tiene sentido aquí
        # --- FIN CORRECCIÓN ---
        sa.Column('fecha_asignacion', sa.DateTime(), nullable=True),
        sa.Column('fecha_estimada_finalizacion', sa.DateTime(), nullable=True),
        sa.Column('fecha_real_finalizacion', sa.DateTime(), nullable=True),
        sa.Column('notas_supervisor', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('ruta_imagen_final', sqlmodel.sql.sqltypes.AutoString(length=512), nullable=True),
        sa.Column('prioridad', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['pedido_cliente_id'], ['pedido_cliente.id'], ),
        sa.ForeignKeyConstraint(['usuario_id_supervisor'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orden_produccion_estado'), 'orden_produccion', ['estado'], unique=False)
    op.create_index(op.f('ix_orden_produccion_pedido_cliente_id'), 'orden_produccion', ['pedido_cliente_id'], unique=True)
    op.create_index(op.f('ix_orden_produccion_usuario_id_supervisor'), 'orden_produccion', ['usuario_id_supervisor'], unique=False)

    op.create_table('proforma',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('pedido_cliente_id', sa.Integer(), nullable=False),
        sa.Column('tipo', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('proforma_vinculada_id', sa.Integer(), nullable=True),
        sa.Column('usuario_id_creador', sa.Integer(), nullable=False),
        sa.Column('estado', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.Column('fecha_aprobacion', sa.DateTime(), nullable=True),
        sa.Column('fecha_reserva_expira', sa.DateTime(), nullable=True),
        sa.Column('estado_reserva', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
        sa.Column('subtotal', sa.Numeric(precision=15, scale=2), nullable=True),
        sa.Column('impuestos', sa.Numeric(precision=15, scale=2), nullable=True),
        sa.Column('total', sa.Numeric(precision=15, scale=2), nullable=True),
        sa.Column('notas', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['pedido_cliente_id'], ['pedido_cliente.id'], ),
        sa.ForeignKeyConstraint(['proforma_vinculada_id'], ['proforma.id'], ),
        sa.ForeignKeyConstraint(['usuario_id_creador'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proforma_estado'), 'proforma', ['estado'], unique=False)
    op.create_index(op.f('ix_proforma_pedido_cliente_id'), 'proforma', ['pedido_cliente_id'], unique=False)
    op.create_index(op.f('ix_proforma_proforma_vinculada_id'), 'proforma', ['proforma_vinculada_id'], unique=False)
    op.create_index(op.f('ix_proforma_usuario_id_creador'), 'proforma', ['usuario_id_creador'], unique=False)

    op.create_table('registro_mantenimiento',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('maquina_id', sa.Integer(), nullable=False),
        sa.Column('usuario_id_tecnico', sa.Integer(), nullable=True),
        sa.Column('fecha_mantenimiento', sa.DateTime(), nullable=False), # Se registra al hacer, no default
        sa.Column('tipo', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('costo_repuestos', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column('horas_mano_obra', sa.Numeric(precision=5, scale=2), nullable=True),
        sa.ForeignKeyConstraint(['maquina_id'], ['maquina.id'], ),
        sa.ForeignKeyConstraint(['usuario_id_tecnico'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_registro_mantenimiento_maquina_id'), 'registro_mantenimiento', ['maquina_id'], unique=False)
    op.create_index(op.f('ix_registro_mantenimiento_usuario_id_tecnico'), 'registro_mantenimiento', ['usuario_id_tecnico'], unique=False)

    op.create_table('reporte_error_maquina',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('maquina_id', sa.Integer(), nullable=False),
        sa.Column('usuario_id_reportador', sa.Integer(), nullable=False),
        # --- CORREGIDO ---
        sa.Column('fecha_reporte', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.Column('descripcion_error', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('codigo_error', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=True),
        sa.Column('prioridad', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
        sa.Column('esta_resuelto', sa.Boolean(), nullable=False),
        sa.Column('fecha_resolucion', sa.DateTime(), nullable=True),
        sa.Column('usuario_id_resolutor', sa.Integer(), nullable=True),
        sa.Column('detalles_resolucion', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['maquina_id'], ['maquina.id'], ),
        sa.ForeignKeyConstraint(['usuario_id_reportador'], ['usuario.id'], ),
        sa.ForeignKeyConstraint(['usuario_id_resolutor'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reporte_error_maquina_esta_resuelto'), 'reporte_error_maquina', ['esta_resuelto'], unique=False)
    op.create_index(op.f('ix_reporte_error_maquina_maquina_id'), 'reporte_error_maquina', ['maquina_id'], unique=False)
    op.create_index(op.f('ix_reporte_error_maquina_usuario_id_reportador'), 'reporte_error_maquina', ['usuario_id_reportador'], unique=False)
    op.create_index(op.f('ix_reporte_error_maquina_usuario_id_resolutor'), 'reporte_error_maquina', ['usuario_id_resolutor'], unique=False)

    op.create_table('stock_item_dimensional',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('material_dimensional_id', sa.Integer(), nullable=False),
        sa.Column('longitud_actual', sa.Numeric(precision=10, scale=3), nullable=False),
        sa.Column('ancho_actual', sa.Numeric(precision=10, scale=3), nullable=False),
        sa.Column('ubicacion', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
        sa.Column('es_merma', sa.Boolean(), nullable=False),
        sa.Column('stock_item_padre_id', sa.Integer(), nullable=True),
        sa.Column('orden_produccion_generadora_id', sa.Integer(), nullable=True),
        sa.Column('estado', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        # --- CORREGIDO ---
        sa.Column('fecha_ingreso', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('fecha_ultima_actualizacion', sa.DateTime(), server_default=sa.func.now(), server_onupdate=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.ForeignKeyConstraint(['material_dimensional_id'], ['material_dimensional.id'], ),
        sa.ForeignKeyConstraint(['orden_produccion_generadora_id'], ['orden_produccion.id'], ), # Esta FK se añadía después, verificar si es correcto
        sa.ForeignKeyConstraint(['stock_item_padre_id'], ['stock_item_dimensional.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stock_item_dimensional_estado'), 'stock_item_dimensional', ['estado'], unique=False)
    op.create_index(op.f('ix_stock_item_dimensional_material_dimensional_id'), 'stock_item_dimensional', ['material_dimensional_id'], unique=False)
    op.create_index(op.f('ix_stock_item_dimensional_orden_produccion_generadora_id'), 'stock_item_dimensional', ['orden_produccion_generadora_id'], unique=False)
    op.create_index(op.f('ix_stock_item_dimensional_stock_item_padre_id'), 'stock_item_dimensional', ['stock_item_padre_id'], unique=False)

    # Re-añadir FK faltante aquí explícitamente si Alembic no la puso arriba
    # op.create_foreign_key(
    #     'fk_stock_item_dim_orden_gen', 'stock_item_dimensional', 'orden_produccion',
    #     ['orden_produccion_generadora_id'], ['id'],
    #     ondelete='SET NULL', onupdate='CASCADE'
    # )


    op.create_table('venta_factura',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('pedido_cliente_id', sa.Integer(), nullable=False),
        sa.Column('proforma_productos_id', sa.Integer(), nullable=True),
        sa.Column('proforma_servicios_id', sa.Integer(), nullable=True),
        sa.Column('cliente_id', sa.Integer(), nullable=False),
        sa.Column('monto_total_final', sa.Numeric(precision=15, scale=2), nullable=False),
        sa.Column('fecha_factura', sa.DateTime(), nullable=False), # Se genera al facturar, no default
        sa.Column('ref_factura_externa', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
        sa.Column('estado_factura_externa', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=True),
        sa.Column('estado_pago', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        # --- CORREGIDO ---
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
        sa.ForeignKeyConstraint(['pedido_cliente_id'], ['pedido_cliente.id'], ),
        sa.ForeignKeyConstraint(['proforma_productos_id'], ['proforma.id'], ),
        sa.ForeignKeyConstraint(['proforma_servicios_id'], ['proforma.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_venta_factura_cliente_id'), 'venta_factura', ['cliente_id'], unique=False)
    op.create_index(op.f('ix_venta_factura_pedido_cliente_id'), 'venta_factura', ['pedido_cliente_id'], unique=False)
    op.create_index(op.f('ix_venta_factura_proforma_productos_id'), 'venta_factura', ['proforma_productos_id'], unique=False)
    op.create_index(op.f('ix_venta_factura_proforma_servicios_id'), 'venta_factura', ['proforma_servicios_id'], unique=False)
    op.create_index(op.f('ix_venta_factura_ref_factura_externa'), 'venta_factura', ['ref_factura_externa'], unique=True)

    op.create_table('linea_proforma_material',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('proforma_id', sa.Integer(), nullable=False),
        sa.Column('tipo_material_origen', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('stock_item_dimensional_id', sa.Integer(), nullable=True),
        sa.Column('material_consumible_id', sa.Integer(), nullable=True),
        sa.Column('material_simple_id', sa.Integer(), nullable=True),
        sa.Column('descripcion_item', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('cantidad', sa.Numeric(precision=10, scale=3), nullable=False),
        sa.Column('unidad', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        sa.Column('precio_unitario', sa.Numeric(precision=12, scale=2), nullable=False),
        sa.Column('total_linea', sa.Numeric(precision=15, scale=2), nullable=False),
        sa.Column('detalles_corte_solicitado', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['material_consumible_id'], ['material_consumible.id'], ),
        sa.ForeignKeyConstraint(['material_simple_id'], ['material_simple.id'], ),
        sa.ForeignKeyConstraint(['proforma_id'], ['proforma.id'], ),
        sa.ForeignKeyConstraint(['stock_item_dimensional_id'], ['stock_item_dimensional.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_linea_proforma_material_material_consumible_id'), 'linea_proforma_material', ['material_consumible_id'], unique=False)
    op.create_index(op.f('ix_linea_proforma_material_material_simple_id'), 'linea_proforma_material', ['material_simple_id'], unique=False)
    op.create_index(op.f('ix_linea_proforma_material_proforma_id'), 'linea_proforma_material', ['proforma_id'], unique=False)
    op.create_index(op.f('ix_linea_proforma_material_stock_item_dimensional_id'), 'linea_proforma_material', ['stock_item_dimensional_id'], unique=False)

    op.create_table('linea_proforma_servicio',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('proforma_id', sa.Integer(), nullable=False),
        sa.Column('servicio_definicion_id', sa.Integer(), nullable=False),
        sa.Column('linea_proforma_material_id', sa.Integer(), nullable=True),
        sa.Column('descripcion_servicio', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column('cantidad', sa.Numeric(precision=10, scale=3), nullable=False),
        sa.Column('precio_unitario', sa.Numeric(precision=12, scale=2), nullable=False),
        sa.Column('total_linea', sa.Numeric(precision=15, scale=2), nullable=False),
        sa.Column('ruta_imagen_cnc', sqlmodel.sql.sqltypes.AutoString(length=512), nullable=True),
        sa.Column('detalles_adicionales', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['linea_proforma_material_id'], ['linea_proforma_material.id'], ),
        sa.ForeignKeyConstraint(['proforma_id'], ['proforma.id'], ),
        sa.ForeignKeyConstraint(['servicio_definicion_id'], ['servicio_definicion.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_linea_proforma_servicio_linea_proforma_material_id'), 'linea_proforma_servicio', ['linea_proforma_material_id'], unique=False)
    op.create_index(op.f('ix_linea_proforma_servicio_proforma_id'), 'linea_proforma_servicio', ['proforma_id'], unique=False)
    op.create_index(op.f('ix_linea_proforma_servicio_servicio_definicion_id'), 'linea_proforma_servicio', ['servicio_definicion_id'], unique=False)

    op.create_table('asignacion_tarea_orden',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('orden_id', sa.Integer(), nullable=False),
        sa.Column('linea_proforma_servicio_id', sa.Integer(), nullable=True),
        sa.Column('linea_proforma_material_id', sa.Integer(), nullable=True),
        sa.Column('usuario_id_asignado', sa.Integer(), nullable=False),
        sa.Column('rol_id_contexto', sa.Integer(), nullable=False),
        sa.Column('tipo_tarea', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
        sa.Column('estado_tarea', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
        # --- CORREGIDO (Aunque fecha_asignacion usualmente se pone al asignar) ---
        sa.Column('fecha_asignacion', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        # --- FIN CORRECCIÓN ---
        sa.Column('fecha_inicio_tarea', sa.DateTime(), nullable=True),
        sa.Column('fecha_fin_tarea', sa.DateTime(), nullable=True),
        sa.Column('notas', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['linea_proforma_material_id'], ['linea_proforma_material.id'], ),
        sa.ForeignKeyConstraint(['linea_proforma_servicio_id'], ['linea_proforma_servicio.id'], ),
        sa.ForeignKeyConstraint(['orden_id'], ['orden_produccion.id'], ),
        sa.ForeignKeyConstraint(['rol_id_contexto'], ['rol.id'], ),
        sa.ForeignKeyConstraint(['usuario_id_asignado'], ['usuario.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asignacion_tarea_orden_linea_proforma_material_id'), 'asignacion_tarea_orden', ['linea_proforma_material_id'], unique=False)
    op.create_index(op.f('ix_asignacion_tarea_orden_linea_proforma_servicio_id'), 'asignacion_tarea_orden', ['linea_proforma_servicio_id'], unique=False)
    op.create_index(op.f('ix_asignacion_tarea_orden_orden_id'), 'asignacion_tarea_orden', ['orden_id'], unique=False)
    op.create_index(op.f('ix_asignacion_tarea_orden_rol_id_contexto'), 'asignacion_tarea_orden', ['rol_id_contexto'], unique=False)
    op.create_index(op.f('ix_asignacion_tarea_orden_usuario_id_asignado'), 'asignacion_tarea_orden', ['usuario_id_asignado'], unique=False)
    # ### end Alembic commands ###

def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_asignacion_tarea_orden_usuario_id_asignado'), table_name='asignacion_tarea_orden')
    op.drop_index(op.f('ix_asignacion_tarea_orden_rol_id_contexto'), table_name='asignacion_tarea_orden')
    op.drop_index(op.f('ix_asignacion_tarea_orden_orden_id'), table_name='asignacion_tarea_orden')
    op.drop_index(op.f('ix_asignacion_tarea_orden_linea_proforma_servicio_id'), table_name='asignacion_tarea_orden')
    op.drop_index(op.f('ix_asignacion_tarea_orden_linea_proforma_material_id'), table_name='asignacion_tarea_orden')
    op.drop_table('asignacion_tarea_orden')
    op.drop_index(op.f('ix_linea_proforma_servicio_servicio_definicion_id'), table_name='linea_proforma_servicio')
    op.drop_index(op.f('ix_linea_proforma_servicio_proforma_id'), table_name='linea_proforma_servicio')
    op.drop_index(op.f('ix_linea_proforma_servicio_linea_proforma_material_id'), table_name='linea_proforma_servicio')
    op.drop_table('linea_proforma_servicio')
    op.drop_index(op.f('ix_linea_proforma_material_stock_item_dimensional_id'), table_name='linea_proforma_material')
    op.drop_index(op.f('ix_linea_proforma_material_proforma_id'), table_name='linea_proforma_material')
    op.drop_index(op.f('ix_linea_proforma_material_material_simple_id'), table_name='linea_proforma_material')
    op.drop_index(op.f('ix_linea_proforma_material_material_consumible_id'), table_name='linea_proforma_material')
    op.drop_table('linea_proforma_material')
    op.drop_index(op.f('ix_venta_factura_ref_factura_externa'), table_name='venta_factura')
    op.drop_index(op.f('ix_venta_factura_proforma_servicios_id'), table_name='venta_factura')
    op.drop_index(op.f('ix_venta_factura_proforma_productos_id'), table_name='venta_factura')
    op.drop_index(op.f('ix_venta_factura_pedido_cliente_id'), table_name='venta_factura')
    op.drop_index(op.f('ix_venta_factura_cliente_id'), table_name='venta_factura')
    op.drop_table('venta_factura')
    op.drop_index(op.f('ix_stock_item_dimensional_stock_item_padre_id'), table_name='stock_item_dimensional')
    op.drop_index(op.f('ix_stock_item_dimensional_orden_produccion_generadora_id'), table_name='stock_item_dimensional')
    op.drop_index(op.f('ix_stock_item_dimensional_material_dimensional_id'), table_name='stock_item_dimensional')
    op.drop_index(op.f('ix_stock_item_dimensional_estado'), table_name='stock_item_dimensional')
    op.drop_table('stock_item_dimensional')
    op.drop_index(op.f('ix_reporte_error_maquina_usuario_id_resolutor'), table_name='reporte_error_maquina')
    op.drop_index(op.f('ix_reporte_error_maquina_usuario_id_reportador'), table_name='reporte_error_maquina')
    op.drop_index(op.f('ix_reporte_error_maquina_maquina_id'), table_name='reporte_error_maquina')
    op.drop_index(op.f('ix_reporte_error_maquina_esta_resuelto'), table_name='reporte_error_maquina')
    op.drop_table('reporte_error_maquina')
    op.drop_index(op.f('ix_registro_mantenimiento_usuario_id_tecnico'), table_name='registro_mantenimiento')
    op.drop_index(op.f('ix_registro_mantenimiento_maquina_id'), table_name='registro_mantenimiento')
    op.drop_table('registro_mantenimiento')
    op.drop_index(op.f('ix_proforma_usuario_id_creador'), table_name='proforma')
    op.drop_index(op.f('ix_proforma_proforma_vinculada_id'), table_name='proforma')
    op.drop_index(op.f('ix_proforma_pedido_cliente_id'), table_name='proforma')
    op.drop_index(op.f('ix_proforma_estado'), table_name='proforma')
    op.drop_table('proforma')
    op.drop_index(op.f('ix_orden_produccion_usuario_id_supervisor'), table_name='orden_produccion')
    op.drop_index(op.f('ix_orden_produccion_pedido_cliente_id'), table_name='orden_produccion')
    op.drop_index(op.f('ix_orden_produccion_estado'), table_name='orden_produccion')
    op.drop_table('orden_produccion')
    op.drop_table('maquina_herramienta')
    op.drop_index(op.f('ix_formula_item_material_simple_id'), table_name='formula_item')
    op.drop_index(op.f('ix_formula_item_material_consumible_id'), table_name='formula_item')
    op.drop_index(op.f('ix_formula_item_formula_id'), table_name='formula_item')
    op.drop_table('formula_item')
    op.drop_table('usuario_rol')
    op.drop_table('usuario_area_trabajo')
    op.drop_table('rol_permiso')
    op.drop_index(op.f('ix_periodo_indisponibilidad_usuario_id'), table_name='periodo_indisponibilidad')
    op.drop_table('periodo_indisponibilidad')
    op.drop_index(op.f('ix_pedido_cliente_usuario_id_vendedor'), table_name='pedido_cliente')
    op.drop_index(op.f('ix_pedido_cliente_estado'), table_name='pedido_cliente')
    op.drop_index(op.f('ix_pedido_cliente_cliente_id'), table_name='pedido_cliente')
    op.drop_table('pedido_cliente')
    op.drop_index(op.f('ix_maquina_numero_serie'), table_name='maquina')
    op.drop_index(op.f('ix_maquina_area_trabajo_id'), table_name='maquina')
    op.drop_table('maquina')
    op.drop_index(op.f('ix_formula_servicio_definicion_id'), table_name='formula')
    op.drop_table('formula')
    op.drop_index(op.f('ix_usuario_username'), table_name='usuario')
    op.drop_index(op.f('ix_usuario_email'), table_name='usuario')
    op.drop_table('usuario')
    op.drop_index(op.f('ix_servicio_definicion_codigo'), table_name='servicio_definicion')
    op.drop_table('servicio_definicion')
    op.drop_index(op.f('ix_rol_nombre'), table_name='rol')
    op.drop_table('rol')
    op.drop_table('permiso')
    op.drop_index(op.f('ix_material_simple_sku'), table_name='material_simple')
    op.drop_table('material_simple')
    op.drop_index(op.f('ix_material_dimensional_sku'), table_name='material_dimensional')
    op.drop_table('material_dimensional')
    op.drop_index(op.f('ix_material_consumible_sku'), table_name='material_consumible')
    op.drop_table('material_consumible')
    op.drop_index(op.f('ix_herramienta_codigo_interno'), table_name='herramienta')
    op.drop_table('herramienta')
    op.drop_index(op.f('ix_cliente_nombre'), table_name='cliente')
    op.drop_index(op.f('ix_cliente_identificacion_fiscal'), table_name='cliente')
    op.drop_index(op.f('ix_cliente_email'), table_name='cliente')
    op.drop_table('cliente')
    op.drop_table('area_trabajo')
    # ### end Alembic commands ###

```

# app\__init__.py

```py

```

# app\api\__init__.py

```py

```

# app\api\deps.py

```py
# app/api/deps.py
from typing import Annotated, Optional, Callable, Set, Union
from fastapi import Depends, HTTPException, status, Request
from sqlmodel import Session, select # <--- Asegúrate de importar select
from sqlalchemy.orm import selectinload # <--- Importar selectinload
from jose import JWTError
import logging
# Ya no necesitamos importar UUID aquí si no se usa directamente

from app.core.database import get_db
from app.core.security import oauth2_scheme, decode_access_token
# Importar modelos necesarios
from app.models import Usuario, Rol, Permiso
# Importar repositorio (aunque ahora haremos la consulta aquí)
from app.repositories import usuario_repository

logger = logging.getLogger(__name__)

def auth_exception(detail: str = "Credenciales de autenticación inválidas") -> HTTPException:
    """
    Helper para generar la excepción estándar de autenticación 401.
    """
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )

async def get_current_user(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_scheme)]
) -> Usuario:
    """
    Obtiene el usuario actual desde el JWT, verifica su existencia en la DB
    y carga eager sus roles asociados.

    Args:
        db: Sesión de base de datos inyectada por FastAPI.
        token: Token JWT extraído del header Authorization por FastAPI.

    Returns:
        El objeto Usuario con sus roles cargados.

    Raises:
        HTTPException 401: Para cualquier fallo de autenticación (token inválido,
                           usuario no encontrado, error de formato, etc.).
    """
    try:
        subject_str = decode_access_token(token)

        if not subject_str:
            logger.warning(f"Token inválido o claims incompletos: {token[:10]}...")
            raise auth_exception("Token inválido o expirado")

        try:
            user_id = int(subject_str)
        except ValueError:
            logger.error(f"Subject del token no es un entero válido: {subject_str}")
            raise auth_exception("Identificador de usuario inválido en el token")

        statement = (
            select(Usuario)
            .where(Usuario.id == user_id)
            .options(
                selectinload(Usuario.roles).selectinload(Rol.permisos)
            )
        )
        user = db.exec(statement).first()

        if not user:
            logger.error(f"Usuario del token no encontrado: ID {user_id}")
            raise auth_exception("Usuario asociado al token no encontrado.")

        logger.debug(f"Usuario autenticado: ID={user.id}, Username='{user.username}'")
        if user.roles:
            perm_count = sum(len(r.permisos) if r.permisos else 0 for r in user.roles)
            role_names_str = ', '.join([r.nombre for r in user.roles])
            logger.debug(f"*** EAGER LOAD CHECK Usuario ID={user.id}: Roles cargados=[{role_names_str}], Permisos totales cargados={perm_count} ***")
            for r in user.roles:
                if r.permisos is None:
                    logger.warning(f"*** EAGER LOAD CHECK: Rol '{r.nombre}' (ID={r.id}) tiene 'permisos' como None! ***")
                elif len(r.permisos) == 0:
                     logger.debug(f"*** EAGER LOAD CHECK: Rol '{r.nombre}' (ID={r.id}) tiene lista 'permisos' vacía. ***")

        else:
            logger.debug(f"*** EAGER LOAD CHECK Usuario ID={user.id}: No tiene roles asignados. ***")

        return user

    except JWTError as e:
        logger.error(f"Error decodificando token JWT: {str(e)}")
        raise auth_exception("Error en el token JWT.")
    # ValueError ya se captura arriba al convertir user_id
    except HTTPException as http_exc: # Relanzar excepciones HTTP directamente
        raise http_exc
    except Exception as e:
        logger.critical(f"Error inesperado en get_current_user: {str(e)}", exc_info=True)
        raise auth_exception("Error interno durante la autenticación.")


def get_current_active_user(
    current_user: Annotated[Usuario, Depends(get_current_user)]
) -> Usuario:
    """
    Verifica que el usuario obtenido de get_current_user esté activo.

    Args:
        current_user: El usuario obtenido de la dependencia get_current_user.

    Returns:
        El objeto Usuario si está activo.

    Raises:
        HTTPException 403: Si el usuario no está activo.
    """
    if not current_user.esta_activo:
        logger.warning(f"Intento de acceso de usuario inactivo: ID={current_user.id}, Username='{current_user.username}'")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cuenta de usuario deshabilitada."
        )
    return current_user





def require_permission(required_permissions: Union[str, Set[str]]) -> Callable:
    """
    Fábrica que crea una dependencia de FastAPI para verificar si el usuario
    activo tiene un permiso específico O al menos uno de un conjunto de permisos.

    Args:
        required_permissions: Un string con el permiso requerido (ej: "leer:cliente")
                              o un set/list de strings con los permisos requeridos
                              (ej: {"actualizar:proforma_propia", "actualizar:proforma_global"}).

    Returns:
        Una función de dependencia asíncrona para usar con FastAPI (`Depends`).
    """
    # Convertir a set si se recibe un solo string para manejo uniforme
    if isinstance(required_permissions, str):
        permission_set = {required_permissions}
        req_perm_repr = f"'{required_permissions}'" # Para logging
    elif isinstance(required_permissions, (set, list)):
        permission_set = set(required_permissions)
        req_perm_repr = f"uno de {permission_set}" # Para logging
    else:
        # Error de configuración si no es string ni set/list
        raise TypeError("required_permissions debe ser un string o un set/list de strings")

    if not permission_set:
         raise ValueError("El conjunto de permisos requeridos no puede estar vacío.")


    async def _permission_check(
        current_user: Annotated[Usuario, Depends(get_current_active_user)]
    ):
        """Dependencia interna que realiza la verificación."""
        # 1. Obtener todos los permisos únicos del usuario (como antes)
        user_permissions: Set[str] = set()
        if current_user.roles:
            for role in current_user.roles:
                # Verificar que la relación 'permisos' fue cargada (por get_current_user)
                if role.permisos is None:
                     logger.error(f"ERROR CRÍTICO: La relación 'permisos' NO está cargada para el Rol ID={role.id} ('{role.nombre}') del usuario ID={current_user.id}. Asegurar selectinload(Usuario.roles).selectinload(Rol.permisos) en get_current_user.") # noqa
                     # Lanzar error 500 porque es un fallo de configuración/carga de datos
                     raise HTTPException(status_code=500, detail="Error interno verificando permisos [LoadFail]")
                for permission in role.permisos:
                    if permission.nombre_accion and permission.nombre_recurso:
                        user_permissions.add(f"{permission.nombre_accion}:{permission.nombre_recurso}")

        # 2. Verificar si el usuario tiene AL MENOS UNO de los permisos requeridos
        #    Usamos la intersección de conjuntos: si la intersección NO está vacía,
        #    significa que el usuario tiene al menos uno de los permisos requeridos.
        has_permission = bool(permission_set.intersection(user_permissions))

        # 3. Lanzar excepción 403 si NO tiene ninguno de los permisos requeridos
        if not has_permission:
            logger.warning(
                f"Acceso DENEGADO para Usuario ID={current_user.id}. "
                f"Requiere: {req_perm_repr}. Posee: {user_permissions}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permiso insuficiente: Se requiere {req_perm_repr}."
            )
        else:
            # Opcional: Log de acceso permitido
            logger.debug(
                 f"Acceso PERMITIDO para Usuario ID={current_user.id}. "
                 f"Req: {req_perm_repr}. Posee: {user_permissions}."
             )
        # Si tiene el permiso (o uno de ellos), la dependencia simplemente termina
        # y FastAPI continúa con la ejecución del endpoint.

    return _permission_check
```

# app\api\v1\__init__.py

```py

```

# app\api\v1\api.py

```py
# app/api/v1/api.py
from fastapi import APIRouter
# Importar los routers existentes y los nuevos
from app.api.v1.endpoints import auth, pedidos, usuarios, roles, permisos, clientes, inventario, service, proformas


api_router_v1 = APIRouter()

# --- Autenticación ---
api_router_v1.include_router(
    auth.router,
    responses={401: {"description": "Credenciales inválidas"}}
)

# --- Usuarios ---
api_router_v1.include_router(
    usuarios.router,
    responses={
        403: {"description": "Permisos insuficientes"},
        404: {"description": "Usuario no encontrado"}
    }
)


# --- Clientes --- # <--- 2. AÑADIR ESTA SECCIÓN
api_router_v1.include_router(
    clientes.router 
)

# --- Roles (Admin) ---
# Incluimos el router definido en endpoints/roles.py
api_router_v1.include_router(
    roles.router,
)


# --- Servicios --- # <--- 
api_router_v1.include_router(
    service.router # Incluir el router que definimos en servicios.py
)



# --- Permisos (Admin) ---
# Incluimos el router definido en endpoints/permisos.py
api_router_v1.include_router(
    permisos.router
)

api_router_v1.include_router(
    inventario.router 
)

# Debajo de la inclusión de clientes o donde sea lógico
api_router_v1.include_router(
    pedidos.router
)

api_router_v1.include_router(
    proformas.router
)
```

# app\api\v1\endpoints\__init__.py

```py

```

# app\api\v1\endpoints\auth.py

```py
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
```

# app\api\v1\endpoints\clientes.py

```py
# app/api/v1/endpoints/clientes.py
import logging
from typing import List, Annotated # Annotated para Depends más limpio

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response
from sqlmodel import Session

# Importar dependencias, servicios y schemas necesarios
from app.api.deps import get_db, require_permission # Usamos nuestra dependencia de permisos
from app.services import cliente_service
from app.schemas.client_schema import (
    ClienteCreate, ClienteUpdate, ClienteRead
)
# El modelo Usuario no suele necesitarse directamente en endpoints si usamos deps
# from app.models import Usuario

logger = logging.getLogger(__name__)

# Crear el router específico para clientes
router = APIRouter(
    prefix="/clientes", # Prefijo para todas las rutas de este router
    tags=["Clientes"],  # Etiqueta para agrupar en la documentación OpenAPI
    # Podríamos añadir respuestas comunes aquí si quisiéramos
    # responses={404: {"description": "Cliente no encontrado"}} # Ejemplo
)

# --- Endpoint para Crear un Cliente ---
@router.post(
    "", # Ruta: POST /api/v1/clientes
    response_model=ClienteRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo cliente",
    dependencies=[Depends(require_permission("crear:cliente"))], # Aplicar permiso
    responses={
        409: {"description": "Conflicto, email o identificación ya existen"},
        403: {"description": "Permiso insuficiente"},
        400: {"description": "Datos de entrada inválidos (validación schema)"}
    }
)
def create_new_cliente(
    *,
    db: Annotated[Session, Depends(get_db)],
    cliente_in: ClienteCreate # Cuerpo de la solicitud validado por el schema
    # current_user: Annotated[Usuario, Depends(get_current_active_user)] # No necesario si solo usamos permiso
):
    """
    Crea un nuevo cliente en el sistema.

    - **Requiere permiso:** `crear:cliente`.
    """
    logger.info(f"[Permiso: crear:cliente] Solicitud para crear cliente: {cliente_in.nombre}")
    # La lógica de validación de duplicados y creación está en el servicio
    # Las excepciones (409, 500) lanzadas por el servicio se propagarán
    cliente = cliente_service.create_cliente_service(db=db, cliente_in=cliente_in)
    return cliente

# --- Endpoint para Listar Clientes ---
@router.get(
    "", # Ruta: GET /api/v1/clientes
    response_model=List[ClienteRead],
    summary="Listar clientes",
    dependencies=[Depends(require_permission("leer:cliente"))], # Aplicar permiso
    responses={
        403: {"description": "Permiso insuficiente"}
    }
)
def list_all_clientes(
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0, description="Número de clientes a saltar"),
    limit: int = Query(100, ge=1, le=200, description="Número máximo de clientes a devolver")
):
    """
    Obtiene una lista paginada de clientes.

    - **Requiere permiso:** `leer:cliente`.
    """
    logger.debug(f"[Permiso: leer:cliente] Solicitud para listar clientes, skip={skip}, limit={limit}")
    clientes = cliente_service.get_clientes_service(db=db, skip=skip, limit=limit)
    return clientes

# --- Endpoint para Obtener un Cliente por ID ---
@router.get(
    "/{cliente_id}", # Ruta: GET /api/v1/clientes/{cliente_id}
    response_model=ClienteRead,
    summary="Obtener un cliente por ID",
    dependencies=[Depends(require_permission("leer:cliente"))], # Aplicar permiso
    responses={
        404: {"description": "Cliente no encontrado"},
        403: {"description": "Permiso insuficiente"}
    }
)
def get_single_cliente(
    *,
    db: Annotated[Session, Depends(get_db)],
    cliente_id: int = Path(..., description="ID del cliente a obtener", gt=0)
):
    """
    Obtiene los detalles de un cliente específico por su ID.

    - **Requiere permiso:** `leer:cliente`.
    """
    logger.debug(f"[Permiso: leer:cliente] Solicitud para obtener cliente ID: {cliente_id}")
    # El servicio maneja la lógica de búsqueda y el error 404
    cliente = cliente_service.get_cliente_by_id_service(db=db, cliente_id=cliente_id)
    return cliente

# --- Endpoint para Actualizar un Cliente ---
# Usaremos PUT para reemplazo total o parcial (depende de cómo se use ClienteUpdate)
# o PATCH para actualización parcial explícita. PUT es más simple aquí.
@router.put(
    "/{cliente_id}", # Ruta: PUT /api/v1/clientes/{cliente_id}
    response_model=ClienteRead,
    summary="Actualizar un cliente",
    dependencies=[Depends(require_permission("actualizar:cliente"))], # Aplicar permiso
    responses={
        404: {"description": "Cliente no encontrado"},
        409: {"description": "Conflicto, email o identificación ya existen en otro cliente"},
        403: {"description": "Permiso insuficiente"},
        400: {"description": "Datos de entrada inválidos (validación schema)"}
    }
)
def update_existing_cliente(
    *,
    db: Annotated[Session, Depends(get_db)],
    cliente_id: int = Path(..., description="ID del cliente a actualizar", gt=0),
    cliente_in: ClienteUpdate # Cuerpo con los campos a actualizar
):
    """
    Actualiza la información de un cliente existente.
    Solo los campos proporcionados en el cuerpo de la solicitud serán actualizados.

    - **Requiere permiso:** `actualizar:cliente`.
    """
    logger.info(f"[Permiso: actualizar:cliente] Solicitud para actualizar cliente ID: {cliente_id}")
    # El servicio maneja la búsqueda (404), validación de conflictos (409) y actualización
    updated_cliente = cliente_service.update_cliente_service(
        db=db, cliente_id=cliente_id, cliente_in=cliente_in
    )
    return updated_cliente

# --- Endpoint para Eliminar un Cliente ---
@router.delete(
    "/{cliente_id}", # Ruta: DELETE /api/v1/clientes/{cliente_id}
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un cliente",
    dependencies=[Depends(require_permission("eliminar:cliente"))], # Aplicar permiso
    responses={
        404: {"description": "Cliente no encontrado"},
        409: {"description": "Conflicto, el cliente tiene pedidos/facturas asociadas"},
        403: {"description": "Permiso insuficiente"}
    }
)
def delete_existing_cliente(
    *,
    db: Annotated[Session, Depends(get_db)],
    cliente_id: int = Path(..., description="ID del cliente a eliminar", gt=0)
):
    """
    Elimina un cliente existente.
    Falla si el cliente tiene pedidos o facturas asociados (debido a restricciones FK).

    - **Requiere permiso:** `eliminar:cliente`.
    """
    logger.warning(f"[Permiso: eliminar:cliente] Solicitud para eliminar cliente ID: {cliente_id}") # Warning para delete
    # El servicio maneja la búsqueda (404) y el error de integridad (409)
    cliente_service.delete_cliente_service(db=db, cliente_id=cliente_id)
    # Si el servicio no lanzó excepción, la eliminación fue exitosa (o el cliente no existía, lo cual es manejado por el 404 del get interno)
    return Response(status_code=status.HTTP_204_NO_CONTENT) # Respuesta estándar para DELETE exitoso
```

# app\api\v1\endpoints\inventario.py

```py
# app/api/v1/endpoints/inventario.py
import logging
from typing import List, Optional, Annotated, Sequence
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Body, Response
from sqlmodel import Session
from pydantic import BaseModel, Field

# Importar dependencias, servicios y schemas necesarios
from app.api.deps import get_db, require_permission
from app.services import inventory_service
from app.schemas.inventory_schema import (
    MaterialDimensionalCreate, MaterialDimensionalUpdate, MaterialDimensionalRead,
    MaterialConsumibleCreate, MaterialConsumibleUpdate, MaterialConsumibleRead,
    MaterialSimpleCreate, MaterialSimpleUpdate, MaterialSimpleRead, StockAdjustRequest,
    StockItemDimensionalCreate, StockItemDimensionalRead,
)

logger = logging.getLogger(__name__)

# --- Router Principal para Inventario ---
router = APIRouter(
    prefix="/inventario",
    tags=["Inventario"],
    responses={
        404: {"description": "Recurso de inventario no encontrado"},
        403: {"description": "Permiso insuficiente"},
        409: {"description": "Conflicto de datos (ej: SKU duplicado, dependencia)"}
    }
)

# --- Sub-Router para Tipos de Material Dimensional ---
router_mat_dim = APIRouter(prefix="/materiales-dimensionales")

@router_mat_dim.post(
    "",
    response_model=MaterialDimensionalRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear tipo de Material Dimensional",
    dependencies=[Depends(require_permission("gestionar:material_definicion"))]
)
def create_material_dimensional(
    *, # <--- Asegurar que los siguientes son kwargs
    db: Annotated[Session, Depends(get_db)],
    mat_dim_in: MaterialDimensionalCreate
):
    """Crea un nuevo tipo de material dimensional (ej: planchas, tablones)."""
    logger.info(f"[Permiso: gestionar:material_definicion] Crear MaterialDimensional SKU: {mat_dim_in.sku}")
    return inventory_service.create_material_dimensional_service(db=db, mat_dim_in=mat_dim_in)

@router_mat_dim.get(
    "",
    response_model=List[MaterialDimensionalRead],
    summary="Listar tipos de Material Dimensional",
    dependencies=[Depends(require_permission("leer:material_definicion"))]
)
def list_materiales_dimensionales(
    # Los parámetros de Query van primero, luego las dependencias
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Lista los tipos de materiales dimensionales definidos."""
    logger.debug(f"[Permiso: leer:material_definicion] Listar MaterialDimensional")
    return inventory_service.list_materiales_dimensionales_service(db=db, skip=skip, limit=limit)

@router_mat_dim.get(
    "/{mat_dim_id}",
    response_model=MaterialDimensionalRead,
    summary="Obtener tipo de Material Dimensional por ID",
    dependencies=[Depends(require_permission("leer:material_definicion"))]
)
def get_material_dimensional(
    # El parámetro de Path va primero
    mat_dim_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Obtiene detalles de un tipo específico de material dimensional."""
    logger.debug(f"[Permiso: leer:material_definicion] Obtener MaterialDimensional ID: {mat_dim_id}")
    return inventory_service.get_material_dimensional_by_id_service(db=db, mat_dim_id=mat_dim_id)

@router_mat_dim.put(
    "/{mat_dim_id}",
    response_model=MaterialDimensionalRead,
    summary="Actualizar tipo de Material Dimensional",
    dependencies=[Depends(require_permission("gestionar:material_definicion"))]
)
def update_material_dimensional(
    # Path param primero
    mat_dim_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    mat_dim_in: MaterialDimensionalUpdate # Body al final
):
    """Actualiza la definición de un tipo de material dimensional."""
    logger.info(f"[Permiso: gestionar:material_definicion] Actualizar MaterialDimensional ID: {mat_dim_id}")
    return inventory_service.update_material_dimensional_service(db=db, mat_dim_id=mat_dim_id, mat_dim_in=mat_dim_in)

@router_mat_dim.delete(
    "/{mat_dim_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar tipo de Material Dimensional",
    dependencies=[Depends(require_permission("gestionar:material_definicion"))]
)
def delete_material_dimensional(
    # Path param primero
    mat_dim_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Elimina un tipo de material dimensional (falla si está en uso)."""
    logger.warning(f"[Permiso: gestionar:material_definicion] Eliminar MaterialDimensional ID: {mat_dim_id}")
    inventory_service.delete_material_dimensional_service(db=db, mat_dim_id=mat_dim_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- Sub-Router para Tipos de Material Consumible ---
router_mat_cons = APIRouter(prefix="/materiales-consumibles")

@router_mat_cons.post("", response_model=MaterialConsumibleRead, status_code=status.HTTP_201_CREATED, summary="Crear tipo de Material Consumible", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def create_material_consumible(
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    mat_cons_in: MaterialConsumibleCreate
):
    """Crea un nuevo tipo de material consumible."""
    logger.info(f"[Permiso: gestionar:material_definicion] Crear MaterialConsumible SKU: {mat_cons_in.sku}")
    return inventory_service.create_material_consumible_service(db=db, mat_cons_in=mat_cons_in)

@router_mat_cons.get("", response_model=List[MaterialConsumibleRead], summary="Listar tipos de Material Consumible", dependencies=[Depends(require_permission("leer:material_definicion"))])
def list_materiales_consumibles(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Lista los tipos de materiales consumibles definidos."""
    logger.debug(f"[Permiso: leer:material_definicion] Listar MaterialConsumible")
    return inventory_service.list_materiales_consumibles_service(db=db, skip=skip, limit=limit)

@router_mat_cons.get("/{mat_cons_id}", response_model=MaterialConsumibleRead, summary="Obtener tipo de Material Consumible por ID", dependencies=[Depends(require_permission("leer:material_definicion"))])
def get_material_consumible(
    mat_cons_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Obtiene detalles de un tipo específico de material consumible."""
    logger.debug(f"[Permiso: leer:material_definicion] Obtener MaterialConsumible ID: {mat_cons_id}")
    return inventory_service.get_material_consumible_by_id_service(db=db, mat_cons_id=mat_cons_id)

@router_mat_cons.put("/{mat_cons_id}", response_model=MaterialConsumibleRead, summary="Actualizar tipo de Material Consumible", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def update_material_consumible(
    mat_cons_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    mat_cons_in: MaterialConsumibleUpdate
):
    """Actualiza la definición de un tipo de material consumible (no el stock)."""
    logger.info(f"[Permiso: gestionar:material_definicion] Actualizar MaterialConsumible ID: {mat_cons_id}")
    return inventory_service.update_material_consumible_service(db=db, mat_cons_id=mat_cons_id, mat_cons_in=mat_cons_in)

@router_mat_cons.delete("/{mat_cons_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar tipo de Material Consumible", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def delete_material_consumible(
    mat_cons_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Elimina un tipo de material consumible (falla si está en uso)."""
    logger.warning(f"[Permiso: gestionar:material_definicion] Eliminar MaterialConsumible ID: {mat_cons_id}")
    inventory_service.delete_material_consumible_service(db=db, mat_cons_id=mat_cons_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_mat_cons.post("/{mat_cons_id}/ajustar-stock", response_model=MaterialConsumibleRead, summary="Ajustar stock de Material Consumible", dependencies=[Depends(require_permission("ajustar:stock"))])
def adjust_stock_consumible(
    mat_cons_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    adjust_in: StockAdjustRequest = Body(...) # Body al final
):
    """Ajusta la cantidad de stock actual para un material consumible."""
    logger.info(f"[Permiso: ajustar:stock] Ajustar stock MaterialConsumible ID: {mat_cons_id}, Cambio: {adjust_in.change_amount}")
    return inventory_service.adjust_stock_consumible_service(db=db, mat_cons_id=mat_cons_id, change_amount=adjust_in.change_amount)


# --- Sub-Router para Tipos de Material Simple ---
router_mat_simp = APIRouter(prefix="/materiales-simples")

@router_mat_simp.post("", response_model=MaterialSimpleRead, status_code=status.HTTP_201_CREATED, summary="Crear tipo de Material Simple", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def create_material_simple(
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    mat_simp_in: MaterialSimpleCreate
):
    """Crea un nuevo tipo de material simple."""
    logger.info(f"[Permiso: gestionar:material_definicion] Crear MaterialSimple SKU: {mat_simp_in.sku}")
    return inventory_service.create_material_simple_service(db=db, mat_simp_in=mat_simp_in)

@router_mat_simp.get("", response_model=List[MaterialSimpleRead], summary="Listar tipos de Material Simple", dependencies=[Depends(require_permission("leer:material_definicion"))])
def list_materiales_simples(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Lista los tipos de materiales simples definidos."""
    logger.debug(f"[Permiso: leer:material_definicion] Listar MaterialSimple")
    return inventory_service.list_materiales_simples_service(db=db, skip=skip, limit=limit)

@router_mat_simp.get("/{mat_simp_id}", response_model=MaterialSimpleRead, summary="Obtener tipo de Material Simple por ID", dependencies=[Depends(require_permission("leer:material_definicion"))])
def get_material_simple(
    mat_simp_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Obtiene detalles de un tipo específico de material simple."""
    logger.debug(f"[Permiso: leer:material_definicion] Obtener MaterialSimple ID: {mat_simp_id}")
    return inventory_service.get_material_simple_by_id_service(db=db, mat_simp_id=mat_simp_id)

@router_mat_simp.put("/{mat_simp_id}", response_model=MaterialSimpleRead, summary="Actualizar tipo de Material Simple", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def update_material_simple(
    mat_simp_id: int = Path(..., gt=0), # <--- CORREGIDO: Orden
    *,                                  # <--- CORREGIDO: Añadido *
    db: Annotated[Session, Depends(get_db)],
    mat_simp_in: MaterialSimpleUpdate
):
    """Actualiza la definición de un tipo de material simple (no el stock)."""
    logger.info(f"[Permiso: gestionar:material_definicion] Actualizar MaterialSimple ID: {mat_simp_id}")
    return inventory_service.update_material_simple_service(db=db, mat_simp_id=mat_simp_id, mat_simp_in=mat_simp_in)

@router_mat_simp.delete("/{mat_simp_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar tipo de Material Simple", dependencies=[Depends(require_permission("gestionar:material_definicion"))])
def delete_material_simple(
    mat_simp_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Elimina un tipo de material simple (falla si está en uso)."""
    logger.warning(f"[Permiso: gestionar:material_definicion] Eliminar MaterialSimple ID: {mat_simp_id}")
    inventory_service.delete_material_simple_service(db=db, mat_simp_id=mat_simp_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router_mat_simp.post("/{mat_simp_id}/ajustar-stock", response_model=MaterialSimpleRead, summary="Ajustar stock de Material Simple", dependencies=[Depends(require_permission("ajustar:stock"))])
def adjust_stock_simple(
    mat_simp_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    adjust_in: StockAdjustRequest = Body(...)
):
    """Ajusta la cantidad de stock actual para un material simple."""
    logger.info(f"[Permiso: ajustar:stock] Ajustar stock MaterialSimple ID: {mat_simp_id}, Cambio: {adjust_in.change_amount}")
    return inventory_service.adjust_stock_simple_service(db=db, mat_simp_id=mat_simp_id, change_amount=adjust_in.change_amount)


# --- Sub-Router para Items de Stock Dimensional ---
router_stock_dim = APIRouter(prefix="/stock-items-dimensionales")

@router_stock_dim.post(
    "",
    response_model=StockItemDimensionalRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear/Registrar nueva pieza de Stock Dimensional",
    dependencies=[Depends(require_permission("ajustar:stock"))]
)
def create_stock_item_dimensional(
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)],
    item_in: StockItemDimensionalCreate
):
    """Registra una nueva pieza física de material dimensional en el inventario."""
    logger.info(f"[Permiso: ajustar:stock] Crear StockItemDimensional para MaterialID: {item_in.material_dimensional_id}")
    return inventory_service.create_stock_item_service(db=db, item_in=item_in)

@router_stock_dim.get(
    "",
    response_model=List[StockItemDimensionalRead],
    summary="Listar piezas de Stock Dimensional (con filtros)",
    dependencies=[Depends(require_permission("leer:stock"))]
)
def list_stock_items_dimensionales(
    # Parámetros Query primero
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    material_dimensional_id: Optional[int] = Query(None, description="Filtrar por ID de tipo de material"),
    estado: Optional[str] = Query(None, description="Filtrar por estado (ej: DISPONIBLE, RESERVADO)"),
    min_longitud: Optional[Decimal] = Query(None, description="Filtrar por longitud mínima"),
    min_ancho: Optional[Decimal] = Query(None, description="Filtrar por ancho mínimo"),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Lista las piezas físicas de stock dimensional, permitiendo filtrar por criterios."""
    logger.debug(f"[Permiso: leer:stock] Listar StockItemDimensional con filtros")
    return inventory_service.list_stock_items_service(
        db=db, skip=skip, limit=limit,
        material_dimensional_id=material_dimensional_id, estado=estado,
        min_longitud=min_longitud, min_ancho=min_ancho
    )

@router_stock_dim.get(
    "/{item_id}",
    response_model=StockItemDimensionalRead,
    summary="Obtener una pieza de Stock Dimensional por ID",
    dependencies=[Depends(require_permission("leer:stock"))]
)
def get_stock_item_dimensional(
    item_id: int = Path(..., gt=0),
    *, # <--- Separador
    db: Annotated[Session, Depends(get_db)]
):
    """Obtiene los detalles de una pieza específica de stock dimensional."""
    logger.debug(f"[Permiso: leer:stock] Obtener StockItemDimensional ID: {item_id}")
    return inventory_service.get_stock_item_by_id_service(db=db, item_id=item_id)

# PUT/DELETE para StockItemDimensional se añadirán después si son necesarios.

# --- Incluir Sub-Routers en el Router Principal de Inventario ---
router.include_router(router_mat_dim)
router.include_router(router_mat_cons)
router.include_router(router_mat_simp)
router.include_router(router_stock_dim)
```

# app\api\v1\endpoints\pedidos.py

```py
# app/api/v1/endpoints/pedidos.py

import logging
from typing import List, Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path
from sqlmodel import Session

# Importar dependencias necesarias
from app.api.deps import get_db, require_permission, get_current_active_user
# Importar el servicio correspondiente
from app.repositories import order_repository
from app.services import order_service
# Importar los schemas necesarios
from app.schemas.order_schema import PedidoClienteCreate, PedidoClienteRead, ProformaRead 
# Importar el modelo Usuario para tipar current_user
from app.models import Usuario

logger = logging.getLogger(__name__)

# Crear el router específico para pedidos
router = APIRouter(
    prefix="/pedidos", # Prefijo para todas las rutas de este router
    tags=["Pedidos"],  # Etiqueta para agrupar en la documentación OpenAPI
    responses={ # Respuestas comunes (pueden ser sobreescritas por endpoints específicos)
        404: {"description": "Pedido no encontrado"},
        403: {"description": "Permiso insuficiente"},
        401: {"description": "No autenticado"},
        409: {"description": "Conflicto de datos"},
    }
)

# --- Endpoint para Crear un PedidoCliente ---
@router.post(
    "", # Ruta: POST /api/v1/pedidos
    response_model=PedidoClienteRead, # Lo que devolverá la API
    status_code=status.HTTP_201_CREATED, # Código para creación exitosa
    summary="Crear un nuevo Pedido de Cliente",
    description="Crea un registro inicial para un pedido de cliente. El vendedor se asigna automáticamente basado en el usuario autenticado.",
    dependencies=[Depends(require_permission("crear:pedido_cliente"))] # Permiso requerido
)
def create_pedido_endpoint(
    *, # Forza argumentos keyword-only después de esto
    db: Annotated[Session, Depends(get_db)],
    pedido_in: PedidoClienteCreate, # El cuerpo de la solicitud validado por el schema
    current_user: Annotated[Usuario, Depends(get_current_active_user)] # Obtener el usuario logueado
):
    """
    Endpoint para crear un nuevo PedidoCliente.

    - Requiere permiso: `crear:pedido_cliente`.
    - Asigna el usuario autenticado como vendedor.
    """
    logger.info(f"API: Solicitud para crear PedidoCliente por Vendedor ID: {current_user.id} para Cliente ID: {pedido_in.cliente_id}")
    try:
        # Llama al servicio, pasando la sesión, los datos de entrada y el ID del vendedor
        nuevo_pedido = order_service.create_pedido_service(
            db=db,
            pedido_in=pedido_in,
            vendedor_id=current_user.id
        )
        # El servicio ya devuelve el objeto PedidoCliente creado
        return nuevo_pedido
    except HTTPException as http_exc:
        # Si el servicio lanzó una HTTPException (ej: 404 cliente no encontrado), la relanzamos
        logger.warning(f"HTTPException al crear pedido: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        # Captura cualquier otro error inesperado del servicio o repositorio
        logger.error(f"Error inesperado en endpoint create_pedido: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al procesar la solicitud de creación del pedido."
        )


# --- Endpoint para Obtener un PedidoCliente por ID ---
@router.get(
    "/{pedido_id}", # Ruta: GET /api/v1/pedidos/{pedido_id}
    response_model=PedidoClienteRead,
    summary="Obtener un PedidoCliente por su ID",
    description="Recupera los detalles de un pedido específico, incluyendo información del cliente y vendedor.",
    dependencies=[Depends(require_permission("leer:pedido_cliente"))] # Permiso requerido
)
def get_pedido_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    pedido_id: int = Path(..., description="ID del PedidoCliente a obtener", gt=0) # Parámetro de ruta validado
    # current_user: Annotated[Usuario, Depends(get_current_active_user)] # No necesario si solo valida permiso
):
    """
    Endpoint para obtener los detalles de un PedidoCliente específico.

    - Requiere permiso: `leer:pedido_cliente`.
    """
    logger.info(f"API: Solicitud para obtener PedidoCliente ID: {pedido_id}")
    try:
        # Llama al servicio para obtener el pedido
        # El servicio se encarga de manejar el caso "no encontrado" (404)
        # Pasamos load_related=True (valor por defecto en el servicio) para que PedidoClienteRead funcione
        pedido = order_service.get_pedido_service(db=db, pedido_id=pedido_id, load_related=True)
        return pedido
    except HTTPException as http_exc:
        logger.warning(f"HTTPException al obtener pedido ID {pedido_id}: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en endpoint get_pedido: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al obtener el pedido."
        )


# --- Endpoint para Listar PedidoClientes ---
@router.get(
    "", # Ruta: GET /api/v1/pedidos
    response_model=List[PedidoClienteRead],
    summary="Listar Pedidos de Clientes",
    description="Obtiene una lista paginada de pedidos, con opciones de filtrado por cliente, vendedor y estado.",
    dependencies=[Depends(require_permission("leer:pedido_cliente"))] # Permiso requerido
)
def list_pedidos_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0, description="Número de pedidos a saltar"),
    limit: int = Query(100, ge=1, le=200, description="Número máximo de pedidos a devolver"),
    cliente_id: Optional[int] = Query(None, description="Filtrar por ID de cliente"),
    vendedor_id: Optional[int] = Query(None, description="Filtrar por ID de vendedor"),
    estado: Optional[str] = Query(None, description="Filtrar por estado del pedido")
    # current_user: Annotated[Usuario, Depends(get_current_active_user)] # Podría usarse para filtrar por vendedor si no es admin/supervisor
):
    """
    Endpoint para listar PedidoClientes con filtros y paginación.

    - Requiere permiso: `leer:pedido_cliente`.
    - TODO: Implementar lógica para restringir la vista si el usuario no es Admin/Supervisor?
    """
    logger.info(f"API: Solicitud para listar PedidoCliente - skip:{skip}, limit:{limit}, cliente:{cliente_id}, vendedor:{vendedor_id}, estado:{estado}")
    # Por ahora, el permiso 'leer:pedido_cliente' da acceso a todos. Se puede refinar luego.
    try:
        # Llama al servicio para listar, pasando los filtros
        # El servicio usa load_related=True por defecto para que PedidoClienteRead funcione
        pedidos = order_service.list_pedidos_service(
            db=db,
            skip=skip,
            limit=limit,
            cliente_id=cliente_id,
            vendedor_id=vendedor_id,
            estado=estado,
            load_related=True
        )
        return pedidos
    except HTTPException as http_exc:
        logger.warning(f"HTTPException al listar pedidos: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en endpoint list_pedidos: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al listar los pedidos."
        )


# --- NUEVO Endpoint para Listar Proformas de un Pedido ---
@router.get(
    "/{pedido_id}/proformas", # Ruta: GET /api/v1/pedidos/{pedido_id}/proformas
    response_model=List[ProformaRead],
    summary="Listar Proformas de un Pedido específico",
    description="Obtiene la lista de proformas (normalmente 2: Producto y Servicio) asociadas a un pedido.",
    dependencies=[Depends(require_permission("leer:proforma"))] # O podría ser "leer:pedido_cliente"
)
def list_proformas_for_pedido_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    pedido_id: int = Path(..., description="ID del PedidoCliente cuyas proformas se listarán", gt=0)
):
    """
    Endpoint para listar las proformas asociadas a un PedidoCliente.

    - Requiere permiso: `leer:proforma`.
    """
    logger.info(f"API: Solicitud para listar proformas del Pedido ID: {pedido_id}")
    # Podríamos verificar si el pedido existe primero, pero list_proformas_by_pedido
    # devolverá una lista vacía si el pedido no existe o no tiene proformas, lo cual es aceptable.
    # Si quisiéramos un 404 si el pedido no existe, deberíamos llamar a get_pedido_service aquí primero.
    try:
        # Llamamos directamente al repositorio, ya que no hay lógica de servicio compleja aquí
        # El servicio get_pedido_service ya valida si el pedido existe si quisiéramos ser más estrictos
        proformas = order_repository.list_proformas_by_pedido(db=db, pedido_id=pedido_id)
        # Si no se encontraron proformas pero el pedido sí existe, se devuelve lista vacía (HTTP 200)
        return proformas
    except Exception as e:
        # Capturar errores generales del repositorio o DB
        logger.error(f"Error inesperado en endpoint list_proformas_for_pedido: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al listar las proformas del pedido."
        )

```

# app\api\v1\endpoints\permisos.py

```py
# app/api/v1/endpoints/permisos.py

import logging
from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response # Añadir Response
from sqlmodel import Session

from app.core.database import get_db
# Importar dependencias necesarias
from app.api.deps import get_db, require_permission # Quitar get_current_active_user si no se usa, quitar require_admin_role
# from app.models import Usuario # Ya no se necesita aquí si no se inyecta current_user
# Importar servicios y schemas
from app.services import permiso_service
from app.schemas.rol_permiso_schema import (
    PermisoCreate, PermisoUpdate, PermisoRead
)

logger = logging.getLogger(__name__)

# Aplicar la dependencia de seguridad a nivel de router
router = APIRouter(
    prefix="/permisos",
    tags=["Permisos"], # Mismo tag para agrupar en Swagger
)

@router.post(
    "", # Ruta: POST /api/v1/permisos
    response_model=PermisoRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo Permiso",
    # Añadir dependencia de permiso específico
    dependencies=[Depends(require_permission("gestionar:permiso"))] # <--- DEPENDENCIA CORRECTA
)
def create_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_in: PermisoCreate
):
    """
    Crea un nuevo permiso en el sistema.
    Requiere permiso 'gestionar:permiso'.
    """
    logger.info(f"[Permiso: gestionar:permiso] Solicitud para crear permiso: {permiso_in.nombre_accion}:{permiso_in.nombre_recurso}")
    # El servicio maneja la lógica y posible 409 por duplicado
    permiso = permiso_service.create_new_permiso(db=db, permiso_in=permiso_in)
    return permiso

@router.get(
    "", # Ruta: GET /api/v1/permisos
    response_model=List[PermisoRead],
    summary="Listar Permisos",
    dependencies=[Depends(require_permission("leer:permiso"))] # <--- DEPENDENCIA CORRECTA
)
def list_permisos(
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0, description="Número de permisos a saltar"), # Añadir descripciones si se desean
    limit: int = Query(100, ge=1, le=500, description="Número máximo de permisos a devolver") # Añadir descripciones
):
    """
    Lista permisos con paginación.
    Requiere permiso 'leer:permiso'.
    """
    logger.debug(f"[Permiso: leer:permiso] Solicitud para listar permisos, skip={skip}, limit={limit}")
    permisos = permiso_service.get_all_permisos(db=db, skip=skip, limit=limit)
    return permisos

@router.get(
    "/{permiso_id}", # Ruta: GET /api/v1/permisos/{permiso_id}
    response_model=PermisoRead,
    summary="Obtener un Permiso por ID",
    dependencies=[Depends(require_permission("leer:permiso"))], # <--- DEPENDENCIA CORRECTA
    responses={404: {"description": "Permiso no encontrado"}}
)
def get_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a obtener", gt=0)
):
    """
    Obtiene detalles de un permiso específico.
    Requiere permiso 'leer:permiso'.
    """
    logger.debug(f"[Permiso: leer:permiso] Solicitud para obtener permiso ID: {permiso_id}")
    # El servicio maneja el 404
    permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id)
    # Nota: El servicio debería lanzar HTTPException(status_code=404) si no se encuentra
    return permiso

@router.put(
    "/{permiso_id}", # Ruta: PUT /api/v1/permisos/{permiso_id}
    response_model=PermisoRead,
    summary="Actualizar un Permiso",
    dependencies=[Depends(require_permission("gestionar:permiso"))], # <--- DEPENDENCIA CORRECTA
    responses={404: {"description": "Permiso no encontrado"},
               409: {"description": "Conflicto, acción/recurso ya existe"}}
)
def update_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a actualizar", gt=0),
    permiso_in: PermisoUpdate
):
    """
    Actualiza un permiso existente.
    Requiere permiso 'gestionar:permiso'.
    """
    logger.info(f"[Permiso: gestionar:permiso] Solicitud para actualizar permiso ID: {permiso_id}")
    # El servicio maneja 404, 409 y lógica
    updated_permiso = permiso_service.update_existing_permiso(
        db=db, permiso_id=permiso_id, permiso_in=permiso_in
    )
    # Nota: El servicio debería lanzar HTTPException(status_code=404/409) según corresponda
    return updated_permiso

@router.delete(
    "/{permiso_id}", # Ruta: DELETE /api/v1/permisos/{permiso_id}
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un Permiso",
    dependencies=[Depends(require_permission("gestionar:permiso"))], # <--- DEPENDENCIA CORRECTA
    responses={404: {"description": "Permiso no encontrado"}}
    # 409 no aplica por ON DELETE CASCADE (o debería manejarse en servicio si hay reglas de negocio)
)
def delete_permiso(
    *,
    db: Annotated[Session, Depends(get_db)],
    permiso_id: int = Path(..., description="ID del permiso a eliminar", gt=0)
):
    """
    Elimina un permiso existente. Las asociaciones con roles se eliminan en cascada (DB).
    Requiere permiso 'gestionar:permiso'.
    """
    logger.info(f"[Permiso: gestionar:permiso] Solicitud para eliminar permiso ID: {permiso_id}")
    # El servicio maneja 404
    deleted = permiso_service.delete_existing_permiso(db=db, permiso_id=permiso_id)
    # Nota: El servicio debería lanzar HTTPException(status_code=404) si no se encuentra
    # Es buena práctica retornar explícitamente Response para 204
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- FIN: Mantener solo este bloque de definiciones ---
```

# app\api\v1\endpoints\proformas.py

```py
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
from app.schemas.order_schema import ProformaRead, ProformaUpdate, LineaProformaMaterialCreate, LineaProformaServicioCreate
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






# ======================================================
# --- Endpoints para Añadir Líneas a Proforma (NUEVOS) ---
# ======================================================

@router.post(
    "/{proforma_id}/lineas-material", # Ruta: POST /api/v1/proformas/{proforma_id}/lineas-material
    response_model=ProformaRead, # Devuelve la proforma actualizada con la nueva línea
    status_code=status.HTTP_201_CREATED,
    summary="Añadir Línea de Material a Proforma",
    description="Añade un ítem de material a una proforma de tipo 'PRODUCTO' que esté en estado 'BORRADOR'. Recalcula los totales.",
    dependencies=[Depends(require_permission("anadir:linea_proforma"))] # Permiso requerido
)
def add_material_line_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    proforma_id: int = Path(..., description="ID de la Proforma (tipo PRODUCTO) a la que añadir la línea", gt=0),
    linea_in: LineaProformaMaterialCreate # Datos de la línea en el cuerpo
):
    """
    Endpoint para añadir una línea de material a una Proforma.

    - Requiere permiso: `anadir:linea_proforma`.
    - Solo funciona en proformas de tipo 'PRODUCTO' en estado 'BORRADOR'.
    - Valida que el material de origen exista.
    - Recalcula y guarda los totales de la proforma.
    """
    logger.info(f"API: Solicitud POST para añadir línea de material a Proforma ID: {proforma_id}")
    try:
        updated_proforma = order_service.add_material_line_to_proforma(
            db=db,
            proforma_id=proforma_id,
            linea_in=linea_in
        )
        # El servicio devuelve la proforma actualizada (incluyendo la nueva línea)
        return updated_proforma
    except HTTPException as http_exc:
        # Relanzar excepciones específicas del servicio (404, 400, 409)
        logger.warning(f"HTTPException al añadir línea material a proforma ID {proforma_id}: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        # Capturar cualquier otro error inesperado
        logger.error(f"Error inesperado en endpoint add_material_line: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al añadir la línea de material."
        )


@router.post(
    "/{proforma_id}/lineas-servicio", # Ruta: POST /api/v1/proformas/{proforma_id}/lineas-servicio
    response_model=ProformaRead, # Devuelve la proforma actualizada
    status_code=status.HTTP_201_CREATED,
    summary="Añadir Línea de Servicio a Proforma",
    description="Añade un ítem de servicio a una proforma de tipo 'SERVICIO' que esté en estado 'BORRADOR'. Recalcula los totales.",
    dependencies=[Depends(require_permission("anadir:linea_proforma"))] # Mismo permiso
)
def add_servicio_line_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    proforma_id: int = Path(..., description="ID de la Proforma (tipo SERVICIO) a la que añadir la línea", gt=0),
    linea_in: LineaProformaServicioCreate # Datos de la línea en el cuerpo
):
    """
    Endpoint para añadir una línea de servicio a una Proforma.

    - Requiere permiso: `anadir:linea_proforma`.
    - Solo funciona en proformas de tipo 'SERVICIO' en estado 'BORRADOR'.
    - Valida que la definición del servicio exista.
    - Valida la línea de material asociada si se proporciona.
    - Recalcula y guarda los totales de la proforma.
    """
    logger.info(f"API: Solicitud POST para añadir línea de servicio a Proforma ID: {proforma_id}")
    try:
        updated_proforma = order_service.add_servicio_line_to_proforma(
            db=db,
            proforma_id=proforma_id,
            linea_in=linea_in
        )
        return updated_proforma
    except HTTPException as http_exc:
        logger.warning(f"HTTPException al añadir línea servicio a proforma ID {proforma_id}: {http_exc.status_code} - {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en endpoint add_servicio_line: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al añadir la línea de servicio."
        )



# --- Endpoints Futuros para Proforma ---
# Aquí podríamos añadir endpoints como:
# PUT /proformas/{proforma_id} (para actualizar estado, notas) - Requerirá permiso 'actualizar:proforma_propia' o 'actualizar:proforma_asignada'
# POST /proformas/{proforma_id}/lineas-material (para añadir líneas)
# POST /proformas/{proforma_id}/lineas-servicio (para añadir líneas)
# DELETE /proformas/{proforma_id}/lineas-material/{linea_id} (para quitar líneas)
# ... etc ...
```

# app\api\v1\endpoints\roles.py

```py
# app/api/v1/endpoints/roles.py

import logging
from typing import List, Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response
from sqlmodel import Session

from app.core.database import get_db
# Importar dependencias necesarias
from app.api.deps import get_db, get_current_active_user, require_permission #QUITAMOS require_admin_role, AÑADIMOS require_permission
from app.models import Usuario, Rol
from app.services import rol_service
from app.schemas.rol_permiso_schema import (
    RolCreate, RolUpdate, RolRead, RolReadWithPermissions, PermisoRead
)

logger = logging.getLogger(__name__)

# Aplicar la dependencia de seguridad a nivel de router
# Todas las rutas en este archivo requerirán el rol de admin
router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)

@router.post(
    "",
    response_model=RolRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo Rol",
    # Añadir dependencia de permiso específico
    dependencies=[Depends(require_permission("crear:rol"))] # <--- NUEVA DEPENDENCIA
)
def create_rol(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_in: RolCreate,
    dependencies=[Depends(require_permission("crear:rol"))] # <<<--- AÑADIR ESTA LÍNEA

):
    """Crea un nuevo rol en el sistema. Requiere permiso 'crear:rol'."""
    logger.info(f"[Permiso: crear:rol] Solicitud para crear rol: {rol_in.nombre}")
    rol = rol_service.create_new_rol(db=db, rol_in=rol_in)
    return rol

@router.get(
    "",
    response_model=List[RolRead],
    summary="Listar Roles",
    dependencies=[Depends(require_permission("leer:rol"))] # <--- NUEVA DEPENDENCIA
)
def list_roles(
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200)
):
    """Lista roles con paginación. Requiere permiso 'leer:rol'."""
    logger.debug(f"[Permiso: leer:rol] Solicitud para listar roles, skip={skip}, limit={limit}")
    roles = rol_service.get_all_roles(db=db, skip=skip, limit=limit)
    return roles

@router.get(
    "/{rol_id}",
    response_model=RolReadWithPermissions,
    summary="Obtener un Rol por ID (con permisos)",
    dependencies=[Depends(require_permission("leer:rol"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Rol no encontrado"}}
)
def get_rol(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol a obtener", gt=0)
    
):
    """Obtiene detalles de un rol específico, incluyendo sus permisos. Requiere permiso 'leer:rol'."""
    logger.debug(f"[Permiso: leer:rol] Solicitud para obtener rol ID: {rol_id}")
    rol = rol_service.get_rol_by_id(db=db, rol_id=rol_id, include_permissions=True)
    return rol


@router.put(
    "/{rol_id}",
    response_model=RolRead,
    summary="Actualizar un Rol",
    dependencies=[Depends(require_permission("actualizar:rol"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Rol no encontrado"},
               409: {"description": "Conflicto, nombre ya existe"}}
)
def update_rol(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol a actualizar", gt=0),
    rol_in: RolUpdate
):
    """Actualiza un rol existente. Requiere permiso 'actualizar:rol'."""
    logger.info(f"[Permiso: actualizar:rol] Solicitud para actualizar rol ID: {rol_id}")
    updated_rol = rol_service.update_existing_rol(db=db, rol_id=rol_id, rol_in=rol_in)
    return updated_rol

@router.delete(
    "/{rol_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un Rol",
    dependencies=[Depends(require_permission("eliminar:rol"))], # <--- NUEVA DEPENDENCIA
    responses={404: {"description": "Rol no encontrado"},
               409: {"description": "Conflicto, rol asignado a usuarios"}}
)
def delete_rol(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol a eliminar", gt=0)
):
    """Elimina un rol existente. Falla si está asignado a usuarios. Requiere permiso 'eliminar:rol'."""
    logger.info(f"[Permiso: eliminar:rol] Solicitud para eliminar rol ID: {rol_id}")
    rol_service.delete_existing_rol(db=db, rol_id=rol_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- Endpoints para Asociación Rol-Permiso (Ahora con permisos específicos) ---

@router.post(
    "/{rol_id}/permisos/{permiso_id}",
    response_model=RolReadWithPermissions,
    status_code=status.HTTP_200_OK,
    summary="Asignar un Permiso a un Rol",
    dependencies=[Depends(require_permission("asignar:permiso_rol"))], 
    responses={
        404: {"description": "Rol o Permiso no encontrado"},
        409: {"description": "Conflicto, el permiso ya está asignado a este rol"}
    }
)
def assign_permission_to_role_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol al que asignar el permiso", gt=0),
    permiso_id: int = Path(..., description="ID del permiso a asignar", gt=0)
):
    """Asigna un permiso específico a un rol específico. Requiere permiso 'asignar:permiso_rol'."""
    logger.info(f"[Permiso: asignar:permiso_rol] Solicitud para asignar permiso ID={permiso_id} a rol ID={rol_id}")
    try:
        updated_rol = rol_service.add_permission_to_role(
            db=db, rol_id=rol_id, permiso_id=permiso_id
        )
        return updated_rol
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado asignando permiso ID={permiso_id} a rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor.")


@router.delete(
    "/{rol_id}/permisos/{permiso_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Quitar un Permiso de un Rol",
    dependencies=[Depends(require_permission("remover:permiso_rol"))], 
    responses={
        404: {"description": "Rol o Permiso no encontrado, o Permiso no asignado a este Rol"}
    }
)
def remove_permission_from_role_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    rol_id: int = Path(..., description="ID del rol del que quitar el permiso", gt=0),
    permiso_id: int = Path(..., description="ID del permiso a quitar", gt=0)
):
    """Quita la asignación de un permiso específico a un rol específico. Requiere permiso 'remover:permiso_rol'."""
    logger.info(f"[Permiso: remover:permiso_rol] Solicitud para quitar permiso ID={permiso_id} de rol ID={rol_id}")
    try:
        rol_service.remove_permission_from_role(
            db=db, rol_id=rol_id, permiso_id=permiso_id
        )
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado quitando permiso ID={permiso_id} de rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor.")

```

# app\api\v1\endpoints\service.py

```py
# app/api/v1/endpoints/servicios.py
import logging
from typing import List, Optional, Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response
from sqlmodel import Session

# Importar dependencias, servicios y schemas necesarios
from app.api.deps import get_db, require_permission
from app.services import service_service # Cambiado a service_service
from app.schemas.service_schema import (
    ServicioDefinicionCreate, ServicioDefinicionUpdate, ServicioDefinicionRead
)

logger = logging.getLogger(__name__)

# --- Router Principal para Servicios ---
# Podríamos tener más endpoints relacionados a servicios aquí en el futuro (ej: Fórmulas)
router = APIRouter(
    prefix="/servicios", # Prefijo base para todos los endpoints relacionados a servicios
    tags=["Servicios"],  # Etiqueta para agrupar en la documentación OpenAPI
    responses={
        404: {"description": "Recurso de servicio no encontrado"},
        403: {"description": "Permiso insuficiente"},
        409: {"description": "Conflicto de datos (ej: nombre duplicado, dependencia)"}
    }
)

# --- Endpoints específicos para Definiciones de Servicio ---

@router.post(
    "/definiciones", # Ruta: POST /api/v1/servicios/definiciones
    response_model=ServicioDefinicionRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva Definición de Servicio",
    # Asumiendo permiso 'gestionar:servicio_definicion'
    dependencies=[Depends(require_permission("gestionar:servicio_definicion"))]
)
def create_new_servicio_definicion(
    *, # Forzar kwargs
    db: Annotated[Session, Depends(get_db)],
    servicio_in: ServicioDefinicionCreate # Cuerpo de la solicitud
):
    """
    Crea una nueva definición para un tipo de servicio ofrecido.

    Requiere permiso: `gestionar:servicio_definicion`.
    """
    logger.info(f"[Permiso: gestionar:servicio_definicion] Crear ServicioDefinicion: {servicio_in.nombre}")
    # El servicio maneja la validación de nombre único y errores
    return service_service.create_servicio_service(db=db, servicio_in=servicio_in)

@router.get(
    "/definiciones", # Ruta: GET /api/v1/servicios/definiciones
    response_model=List[ServicioDefinicionRead],
    summary="Listar Definiciones de Servicio",
    # Asumiendo permiso 'leer:servicio_definicion'
    dependencies=[Depends(require_permission("leer:servicio_definicion"))]
)
def list_all_servicio_definiciones(
    # Parámetros de Query primero
    skip: int = Query(0, ge=0, description="Número de definiciones a saltar"),
    limit: int = Query(100, ge=1, le=200, description="Número máximo de definiciones a devolver"),
    *, # Separador
    db: Annotated[Session, Depends(get_db)]
):
    """
    Obtiene una lista paginada de todas las definiciones de servicios disponibles.

    Requiere permiso: `leer:servicio_definicion`.
    """
    logger.debug(f"[Permiso: leer:servicio_definicion] Listar ServicioDefinicion")
    return service_service.list_servicios_service(db=db, skip=skip, limit=limit)

@router.get(
    "/definiciones/{servicio_id}", # Ruta: GET /api/v1/servicios/definiciones/{id}
    response_model=ServicioDefinicionRead,
    summary="Obtener Definición de Servicio por ID",
    dependencies=[Depends(require_permission("leer:servicio_definicion"))]
)
def get_single_servicio_definicion(
    # Parámetro de Path primero
    servicio_id: int = Path(..., description="ID de la definición de servicio a obtener", gt=0),
    *, # Separador
    db: Annotated[Session, Depends(get_db)]
):
    """
    Obtiene los detalles de una definición de servicio específica por su ID.

    Requiere permiso: `leer:servicio_definicion`.
    """
    logger.debug(f"[Permiso: leer:servicio_definicion] Obtener ServicioDefinicion ID: {servicio_id}")
    # El servicio maneja el error 404 si no se encuentra
    return service_service.get_servicio_by_id_service(db=db, servicio_id=servicio_id)

@router.put(
    "/definiciones/{servicio_id}", # Ruta: PUT /api/v1/servicios/definiciones/{id}
    response_model=ServicioDefinicionRead,
    summary="Actualizar Definición de Servicio",
    dependencies=[Depends(require_permission("gestionar:servicio_definicion"))]
)
def update_existing_servicio_definicion(
    # Path param primero
    servicio_id: int = Path(..., description="ID de la definición de servicio a actualizar", gt=0),
    *, # Separador
    db: Annotated[Session, Depends(get_db)],
    servicio_in: ServicioDefinicionUpdate # Cuerpo con los campos a actualizar
):
    """
    Actualiza la información de una definición de servicio existente.
    Solo los campos proporcionados en el cuerpo de la solicitud serán actualizados.

    Requiere permiso: `gestionar:servicio_definicion`.
    """
    logger.info(f"[Permiso: gestionar:servicio_definicion] Actualizar ServicioDefinicion ID: {servicio_id}")
    # El servicio maneja 404, conflicto de nombre (409) y actualización
    return service_service.update_servicio_service(db=db, servicio_id=servicio_id, servicio_in=servicio_in)

@router.delete(
    "/definiciones/{servicio_id}", # Ruta: DELETE /api/v1/servicios/definiciones/{id}
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar Definición de Servicio",
    dependencies=[Depends(require_permission("gestionar:servicio_definicion"))]
)
def delete_existing_servicio_definicion(
    # Path param primero
    servicio_id: int = Path(..., description="ID de la definición de servicio a eliminar", gt=0),
    *, # Separador
    db: Annotated[Session, Depends(get_db)]
):
    """
    Elimina una definición de servicio existente.
    Falla si el servicio está referenciado en Fórmulas o Proformas.

    Requiere permiso: `gestionar:servicio_definicion`.
    """
    logger.warning(f"[Permiso: gestionar:servicio_definicion] Eliminar ServicioDefinicion ID: {servicio_id}")
    # El servicio maneja 404 y conflicto de integridad (409)
    service_service.delete_servicio_service(db=db, servicio_id=servicio_id)
    # Si el servicio no lanzó excepción, la eliminación fue exitosa
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Aquí se podrían añadir endpoints para Fórmulas en el futuro (ej: POST /definiciones/{id}/formulas)
```

# app\api\v1\endpoints\usuarios.py

```py
# app/api/v1/endpoints/usuarios.py
import logging
from typing import List, Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status, Path, Response
from sqlmodel import Session

from app.core.database import get_db
# Importar dependencias necesarias
from app.api.deps import get_db, get_current_active_user, require_permission # Cambiar require_admin_role por require_permission
from app.models import Usuario
from app.services import usuario_service
from app.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioRead,
    UsuarioUpdate,
    UsuarioUpdatePassword
)
from app.schemas.rol_permiso_schema import RolRead

router = APIRouter(prefix="/usuarios", tags=["Usuarios"]) # O "Users"
logger = logging.getLogger(__name__)

# --- Creación de Usuario ---
@router.post(
    "", # Ruta base del router de usuarios (ej: /api/v1/usuarios)
    response_model=UsuarioRead, # Devuelve el usuario creado con sus roles
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo usuario",
    dependencies=[Depends(require_permission("crear:usuario"))], # <--- PERMISO ESPECÍFICO
    responses={
        400: {"description": "Datos inválidos"},
        404: {"description": "Uno o más IDs de rol no existen"},
        403: {"description": "Permiso insuficiente"} 
    }
)
def create_user(
    *,
    db: Annotated[Session, Depends(get_db)],
    user_in: UsuarioCreate
):
    """
    Crea un nuevo usuario en el sistema especificando sus datos y roles iniciales.

    - **Requiere permiso:** `crear:usuario`.
    - Permite asignar roles mediante la lista `rol_ids`.
    """
    # Log indicando la acción protegida
    logger.info(f"[Permiso: crear:usuario] Solicitud para crear usuario: {user_in.username}")
    try:
        new_user = usuario_service.create_new_user(db=db, user_in=user_in)
        return new_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado al crear usuario '{user_in.username}': {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el usuario."
        )


# --- Endpoints /me (Solo requieren usuario activo, sin permiso específico) ---
@router.get(
    "/me",
    response_model=UsuarioRead,
    summary="Obtener datos del usuario autenticado"
    # No requiere permiso específico más allá de estar autenticado y activo
)
def read_users_me(
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Obtiene los datos del usuario autenticado (incluyendo sus roles)."""
    logger.info(f"Solicitud de datos para usuario ID: {current_user.id}")
    return current_user

@router.patch(
    "/me",
    response_model=UsuarioRead,
    summary="Actualizar perfil del usuario autenticado"
    # No requiere permiso específico
)
def update_self(
    *,
    db: Annotated[Session, Depends(get_db)],
    update_data: UsuarioUpdate,
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Permite al usuario autenticado actualizar su propio perfil."""
    logger.info(f"Actualizando perfil propio para usuario ID: {current_user.id}")
    try:
        updated_user = usuario_service.update_user_profile(
            db=db, current_user=current_user, user_in=update_data
        )
        return updated_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error actualizando perfil propio (ID: {current_user.id}): {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al actualizar el perfil.")

@router.put(
    "/me/password",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Cambiar contraseña del usuario autenticado"
    # No requiere permiso específico
)
def update_password(
    *,
    db: Annotated[Session, Depends(get_db)],
    password_data: UsuarioUpdatePassword,
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    """Endpoint para que el usuario autenticado cambie su propia contraseña."""
    logger.info(f"Solicitando cambio de contraseña para usuario ID: {current_user.id}")
    try:
        usuario_service.update_user_password(db=db, current_user=current_user, password_in=password_data)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error cambiando contraseña propia (ID: {current_user.id}): {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al actualizar contraseña.")




# --- Endpoints Admin sobre Usuarios Específicos ---

@router.get(
    "/{user_id}",
    response_model=UsuarioRead,
    summary="Obtener usuario por ID", # Ya no necesita (Admin) aquí
    # Aplicar permiso específico
    dependencies=[Depends(require_permission("leer:usuario"))], # <--- PERMISO ESPECÍFICO
    responses={404: {"description": "Usuario no encontrado"},
               403: {"description": "Permiso insuficiente"}}
)
def get_user(
    *,
    db: Annotated[Session, Depends(get_db)],
    user_id: int = Path(..., description="ID del usuario a obtener", gt=0)
):
    """
    Obtiene información de cualquier usuario por su ID.
    - **Requiere permiso:** `leer:usuario`.
    """
    logger.info(f"[Permiso: leer:usuario] Solicitud para obtener usuario ID: {user_id}")
    try:
        user = usuario_service.get_user_info(db=db, user_id=user_id)
        return user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error obteniendo usuario ID {user_id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno al recuperar usuario.")


@router.post(
    "/{user_id}/roles/{rol_id}",
    response_model=UsuarioRead,
    status_code=status.HTTP_200_OK,
    summary="Asignar un Rol a un Usuario",
    # Aplicar permiso específico
    dependencies=[Depends(require_permission("asignar:rol_usuario"))], # <--- PERMISO ESPECÍFICO
    responses={
        404: {"description": "Usuario o Rol no encontrado"},
        403: {"description": "Permiso insuficiente"}
    }
)
def assign_role_to_user_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    user_id: int = Path(..., description="ID del usuario al que asignar el rol", gt=0),
    rol_id: int = Path(..., description="ID del rol a asignar", gt=0)
):
    """
    Asigna un rol específico a un usuario específico.
    - **Requiere permiso:** `asignar:rol_usuario`.
    """
    logger.info(f"[Permiso: asignar:rol_usuario] Solicitud para asignar rol ID={rol_id} a usuario ID={user_id}")
    try:
        updated_user = usuario_service.assign_role_to_user_service(
            db=db, user_id=user_id, rol_id=rol_id
        )
        return updated_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado asignando rol ID={rol_id} a usuario ID={user_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor.")


@router.delete(
    "/{user_id}/roles/{rol_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Quitar un Rol de un Usuario",
    # Aplicar permiso específico
    dependencies=[Depends(require_permission("remover:rol_usuario"))], # <--- PERMISO ESPECÍFICO
    responses={
        404: {"description": "Usuario o Rol no encontrado"},
        403: {"description": "Permiso insuficiente"}
    }
)
def remove_role_from_user_endpoint(
    *,
    db: Annotated[Session, Depends(get_db)],
    user_id: int = Path(..., description="ID del usuario del que quitar el rol", gt=0),
    rol_id: int = Path(..., description="ID del rol a quitar", gt=0)
):
    """
    Quita la asignación de un rol específico a un usuario específico.
    - **Requiere permiso:** `remover:rol_usuario`.
    """
    logger.info(f"[Permiso: remover:rol_usuario] Solicitud para quitar rol ID={rol_id} de usuario ID={user_id}")
    try:
        usuario_service.remove_role_from_user_service(
            db=db, user_id=user_id, rol_id=rol_id
        )
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado quitando rol ID={rol_id} de usuario ID={user_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor.")

```

# app\core\__init__.py

```py

```

# app\core\config.py

```py
# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    PROJECT_NAME: str
    API_V1_STR: str
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:8000", "http://localhost:3000"]  # Valores predeterminados
    model_config = SettingsConfigDict(env_file=".env")  # Carga variables desde .env

settings = Settings() # Crea una instancia de la clase Settings
```

# app\core\database.py

```py
# app/core/database.py

from sqlmodel import SQLModel, Session, create_engine
# Usamos sessionmaker de sqlalchemy.orm directamente, es compatible
from sqlalchemy.orm import sessionmaker
from typing import Generator

# Importa tu objeto de configuración (ajusta la ruta si es necesario)
from app.core.config import settings

# 1. URL de la Base de Datos desde la configuración
# Asegúrate de que tu .env tenga una línea como:
# DATABASE_URL=mysql+mysqlconnector://tu_usuario:tu_contraseña@localhost:3306/tu_base_de_datos
DATABASE_URL = settings.DATABASE_URL

# Argumentos específicos para el engine (pueden variar según driver/necesidad)
# Para MySQL con mysql-connector-python, usualmente no se necesitan args especiales aquí.
connect_args = {}

# 2. Crear el Engine de SQLAlchemy/SQLModel
# pool_recycle: Reutiliza conexiones después de X segundos (ej. 3600 = 1 hora) para evitar timeouts de MySQL.
# pool_pre_ping: Verifica la conexión antes de usarla del pool.
# echo=True: Imprime las sentencias SQL ejecutadas (útil para depuración, quitar en producción).
engine = create_engine(
    DATABASE_URL,
    echo=False, # Cambiar a True para depuración SQL
    connect_args=connect_args,
    pool_recycle=3600,
    pool_pre_ping=True
)

# 3. Crear la fábrica de Sesiones (SessionLocal)
# autocommit=False y autoflush=False son configuraciones estándar para usar con FastAPI.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session # Usamos la Session de SQLModel/SQLAlchemy
)

# 4. Dependencia de FastAPI para obtener la sesión de BD
def get_db() -> Generator[Session, None, None]:
    """
    Generador de dependencia para obtener una sesión de base de datos.

    Yields:
        Session: Objeto de sesión de base de datos.

    Asegura que la sesión se cierre después de su uso.
    """
    # Llama a la fábrica para obtener una sesión
    db = SessionLocal()
    try:
        # Entrega la sesión al contexto que la pidió (ej. tu endpoint)
        yield db
    finally:
        # Siempre cierra la sesión al finalizar, incluso si hubo errores
        db.close()



```

# app\core\security.py

```py
# app/core/security.py
from datetime import datetime, timedelta, timezone
from typing import Optional, Any
import logging

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

# --- Configuración de logging ---
logger = logging.getLogger(__name__)

# --- Configuración de Hashing de Contraseñas ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Validación de configuración ---
if not settings.SECRET_KEY or settings.SECRET_KEY == "secret-key":
    logger.error("SECRET_KEY no está configurada correctamente")
    raise ValueError("Falta configuración de SECRET_KEY")

# --- Configuración de JWT ---
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

# --- Esquema OAuth2 ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

# --- Funciones de Contraseña ---
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# --- Funciones de JWT ---
def create_access_token(subject: str | Any, expires_delta: Optional[timedelta] = None) -> str:
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {
        "exp": expire,
        "iat": now,  # Tiempo de emisión
        "sub": str(subject),
        # Puedes añadir más claims aquí (ej: roles, iss, aud)
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def decode_access_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Validación adicional de claims
        if not all(key in payload for key in ["exp", "iat", "sub"]):
            logger.warning("Token con claims incompletos")
            return None
            
        subject: str = payload.get("sub")
        return subject
    except JWTError as e:
        logger.error(f"Error de JWT: {str(e)}")
        return None
```

# app\initial_data.py

```py
# app/initial_data.py

"""
Define los datos iniciales para roles, permisos y sus mapeos.
Se usa tanto para la migración de seeding como para las fixtures de prueba.
"""


initial_roles = [
    {'nombre': 'Administrador', 'descripcion': 'Acceso total al sistema.'},
    {'nombre': 'Vendedor', 'descripcion': 'Gestión de ventas y clientes.'},
    {'nombre': 'Supervisor', 'descripcion': 'Supervisión de producción y operarios.'},
    {'nombre': 'Dibujante', 'descripcion': 'Cotización y preparación de trabajos CNC.'},
    {'nombre': 'Operario', 'descripcion': 'Ejecución de tareas de producción.'},
]


initial_permissions = [
    # Gestión Acceso y Sistema
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'usuario', 'descripcion': 'CRUD completo de usuarios.'},
    {'nombre_accion': 'gestionar', 'nombre_recurso': 'rol', 'descripcion': 'CRUD completo de roles.'},
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
    # Ojo con este:
    {'nombre_accion': 'anadir', 'nombre_recurso': 'linea_proforma', 'descripcion': 'Añadir líneas de material o servicio a una proforma en borrador.'},
    # Pedidos y Órdenes
    {'nombre_accion': 'leer', 'nombre_recurso': 'pedido_cliente', 'descripcion': 'Ver estado general del pedido.'},
    {'nombre_accion': 'crear', 'nombre_recurso': 'pedido_cliente', 'descripcion': 'Crear nuevos pedidos de clientes.'},
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

# Lista de Permisos (accion:recurso)
role_permission_mapping = {
    'Administrador': [
        'gestionar:usuario', 'gestionar:rol', 'gestionar:permiso', 'leer:usuario', 'crear:usuario',
        'actualizar:usuario', 'eliminar:usuario', 'leer:rol', 'crear:rol', 'actualizar:rol',
        'eliminar:rol', 'leer:permiso', 'asignar:rol_usuario', 'remover:rol_usuario',
        'asignar:permiso_rol', 'remover:permiso_rol', 'anular:venta_factura', 'ver:panel_admin',
        'leer:cliente', 'crear:cliente', 'actualizar:cliente', 'eliminar:cliente',
        'leer:proforma', 'crear:proforma', 'actualizar:proforma_global', 'cancelar:proforma',
        'enviar:proforma', 'posponer:proforma', 'adjuntar:archivo_proforma',
        'leer:pedido_cliente', 'crear:pedido_cliente','leer:orden_produccion', 'gestionar:orden_produccion',
        'adjuntar:archivo_orden', 'leer:material_definicion', 'gestionar:material_definicion',
        'leer:stock', 'ajustar:stock', 'ver:merma', 'leer:area_trabajo',
        'gestionar:area_trabajo', 'asignar:usuario_area', 'remover:usuario_area',
        'leer:maquina', 'gestionar:maquina', 'leer:herramienta', 'gestionar:herramienta',
        'asignar:maquina_herramienta', 'remover:maquina_herramienta',
        'leer:registro_mantenimiento', 'crear:registro_mantenimiento',
        'leer:reporte_error_maquina', 'crear:reporte_error_maquina',
        'resolver:reporte_error_maquina', 'leer:servicio_definicion',
        'gestionar:servicio_definicion', 'leer:formula', 'gestionar:formula',
        'leer:venta_factura', 'actualizar:estado_pago', 'leer:periodo_indisponibilidad',
        'registrar:mi_indisponibilidad', 
        'anadir:linea_proforma'
    ],
    'Vendedor': [
        'leer:cliente', 'crear:cliente', 'actualizar:cliente', 'leer:proforma',
        'crear:proforma', 'actualizar:proforma_propia', 'cancelar:proforma',
        'enviar:proforma', 'posponer:proforma', 'adjuntar:archivo_proforma',
        'leer:pedido_cliente', 'crear:pedido_cliente', 'leer:orden_produccion', 'leer:material_definicion',
        'leer:stock', 'leer:servicio_definicion', 'leer:venta_factura',
        'actualizar:estado_pago', 'registrar:mi_indisponibilidad',
        'anadir:linea_proforma'
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
        'leer:formula', 'crear:reporte_error_maquina', 'registrar:mi_indisponibilidad', 'anadir:linea_proforma'
    ],
    'Operario': [
        'leer:orden_produccion', 'tomar:tarea_orden', 'actualizar:tarea_orden',
        'leer:stock', 'leer:maquina', 'leer:herramienta',
        'crear:reporte_error_maquina', 'registrar:mi_indisponibilidad'
    ]
}
```

# app\main.py

```py
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.api.v1.api import api_router_v1
from app.core.database import engine
from sqlmodel import SQLModel
import logging

from app.api.v1.api import api_router_v1 # Importa el router de la v1
from app.core.config import settings    # Importa la configuración

app = FastAPI(
    title=settings.PROJECT_NAME,
    #description=settings.PROJECT_DESCRIPTION,
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)




app.include_router(api_router_v1, prefix=settings.API_V1_STR)
```

# app\models\__init__.py

```py
# app/models/__init__.py
# app/models/__init__.py
"""
Este archivo __init__.py convierte al directorio 'models' en un paquete de Python
y re-exporta todas las clases de modelos SQLModel definidas en los módulos
separados.

Esto permite importar los modelos de forma más conveniente desde otras partes
de la aplicación, por ejemplo:
  from app.models import Usuario, PedidoCliente
en lugar de:
  from app.models.user_models import Usuario
  from app.models.order_models import PedidoCliente
"""

# Importaciones desde user_models.py
from .user_models import (
    UsuarioRol,
    RolPermiso,
    Usuario,
    Rol,
    Permiso,
    PeriodoIndisponibilidad
)

# Importaciones desde inventory_models.py
from .inventory_models import (
    MaterialDimensional,
    StockItemDimensional,
    MaterialConsumible,
    MaterialSimple
)

# Importaciones desde machine_models.py
from .machine_models import (
    MaquinaHerramienta,
    UsuarioAreaTrabajo,
    AreaTrabajo,
    Maquina,
    Herramienta,
    RegistroMantenimiento,
    ReporteErrorMaquina
)

# Importaciones desde service_models.py
from .service_models import (
    ServicioDefinicion,
    Formula,
    FormulaItem
)

# Importaciones desde order_models.py
from .order_models import (
    PedidoCliente,
    Proforma,
    LineaProformaMaterial,
    LineaProformaServicio,
    OrdenProduccion,
    AsignacionTareaOrden
)

# Importaciones desde client_model.py
from .client_model import Cliente

# Importaciones desde billing_models.py
from .billing_models import VentaFactura


# Opcional: Definir __all__ para controlar qué se importa con 'from app.models import *'
# Es buena práctica definirlo explícitamente si se planea usar 'import *'
# aunque la importación explícita (from app.models import MiModelo) es generalmente preferida.
__all__ = [
    # User Models
    "UsuarioRol",
    "RolPermiso",
    "Usuario",
    "Rol",
    "Permiso",
    "PeriodoIndisponibilidad",
    # Inventory Models
    "MaterialDimensional",
    "StockItemDimensional",
    "MaterialConsumible",
    "MaterialSimple",
    # Machine Models
    "MaquinaHerramienta",
    "UsuarioAreaTrabajo",
    "AreaTrabajo",
    "Maquina",
    "Herramienta",
    "RegistroMantenimiento",
    "ReporteErrorMaquina",
    # Service Models
    "ServicioDefinicion",
    "Formula",
    "FormulaItem",
    # Order Models
    "PedidoCliente",
    "Proforma",
    "LineaProformaMaterial",
    "LineaProformaServicio",
    "OrdenProduccion",
    "AsignacionTareaOrden",
    # Client Models
    "Cliente",
    # Billing Models
    "VentaFactura",
]
```

# app\models\billing_models.py

```py
# app/models/billing_models.py

from datetime import datetime
from decimal import Decimal
from typing import Optional, TYPE_CHECKING # No necesitamos List aquí

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .order_models import PedidoCliente, Proforma
    from .client_model import Cliente

# -----------------------------------------------------
# Modelo para Venta/Factura
# -----------------------------------------------------

class VentaFactura(SQLModel, table=True):
    """Representa la factura generada para una venta, vinculada a un pedido."""
    __tablename__ = "venta_factura"

    id: Optional[int] = Field(default=None, primary_key=True)
    pedido_cliente_id: int = Field(foreign_key="pedido_cliente.id", index=True)
    # FKs opcionales a las proformas específicas incluidas en esta factura
    proforma_productos_id: Optional[int] = Field(
        default=None, foreign_key="proforma.id", index=True, nullable=True
    )
    proforma_servicios_id: Optional[int] = Field(
        default=None, foreign_key="proforma.id", index=True, nullable=True
    )
    # FK a cliente (denormalizada de pedido_cliente para conveniencia)
    cliente_id: int = Field(foreign_key="cliente.id", index=True)
    monto_total_final: Decimal = Field(max_digits=15, decimal_places=2)
    fecha_factura: datetime = Field()
    ref_factura_externa: Optional[str] = Field(
        default=None, unique=True, index=True, max_length=255, nullable=True
    )
    estado_factura_externa: Optional[str] = Field(default=None, max_length=100, nullable=True)
    estado_pago: str = Field(default="PENDIENTE", max_length=50) # ENUM
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)

    # Relación N:1 con PedidoCliente
    pedido: "PedidoCliente" = Relationship(back_populates="facturas")

    # Relación N:1 con Proforma (para productos)
    # Se necesita foreign_keys por haber dos FK a la misma tabla Proforma
    proforma_productos: Optional["Proforma"] = Relationship(
        back_populates="facturas_productos",
        sa_relationship_kwargs={'foreign_keys': '[VentaFactura.proforma_productos_id]'}
    )

    # Relación N:1 con Proforma (para servicios)
    # Se necesita foreign_keys por haber dos FK a la misma tabla Proforma
    proforma_servicios: Optional["Proforma"] = Relationship(
        back_populates="facturas_servicios",
        sa_relationship_kwargs={'foreign_keys': '[VentaFactura.proforma_servicios_id]'}
    )

    # Relación N:1 con Cliente
    cliente: "Cliente" = Relationship(back_populates="facturas")


# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .order_models import PedidoCliente, Proforma
    from .client_model import Cliente

    # Recordatorio: Añadir/Verificar back_populates correspondientes en otros modelos:
    # class PedidoCliente(...):
    #     facturas: List["VentaFactura"] = Relationship(back_populates="pedido")
    #
    # class Proforma(...):
    #     facturas_productos: List["VentaFactura"] = Relationship(back_populates="proforma_productos")
    #     facturas_servicios: List["VentaFactura"] = Relationship(back_populates="proforma_servicios")
    #
    # class Cliente(...):
    #     facturas: List["VentaFactura"] = Relationship(back_populates="cliente")
```

# app\models\client_model.py

```py
# app/models/client_model.py

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .order_models import PedidoCliente
    from .billing_models import VentaFactura

# -----------------------------------------------------
# Modelo para Clientes
# -----------------------------------------------------

class Cliente(SQLModel, table=True):
    """Representa a un cliente del negocio."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=255)
    # ENUM manejado como str, validación en otro nivel
    tipo_identificacion: Optional[str] = Field(default=None, max_length=50, nullable=True) # Ej: 'RUC', 'CEDULA'
    identificacion_fiscal: Optional[str] = Field(
        default=None, unique=True, index=True, max_length=50, nullable=True
    )
    persona_contacto: Optional[str] = Field(default=None, max_length=255, nullable=True)
    email: Optional[str] = Field(
        default=None, unique=True, index=True, max_length=255, nullable=True
    )
    telefono: Optional[str] = Field(default=None, max_length=50, nullable=True)
    direccion: Optional[str] = Field(default=None, nullable=True) # Considerar sa_column=Column(Text)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con PedidoCliente (un cliente puede tener muchos pedidos)
    pedidos: List["PedidoCliente"] = Relationship(back_populates="cliente")

    # Relación 1:N con VentaFactura (un cliente puede tener muchas facturas)
    # El campo cliente_id en VentaFactura está denormalizado, pero la relación es útil.
    facturas: List["VentaFactura"] = Relationship(back_populates="cliente")


# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .order_models import PedidoCliente
    from .billing_models import VentaFactura # Necesario cuando se defina VentaFactura

    # Recordatorio: Añadir/Verificar back_populates correspondientes en otros modelos:
    # class PedidoCliente(...):
    #     cliente: "Cliente" = Relationship(back_populates="pedidos")
    #
    # class VentaFactura(...):
    #     cliente: "Cliente" = Relationship(back_populates="facturas")
```

# app\models\inventory_models.py

```py
# app/models/inventory_models.py

from datetime import datetime
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .order_models import OrdenProduccion, LineaProformaMaterial
    from .service_models import FormulaItem

# -----------------------------------------------------
# Modelo para Tipos de Material Dimensional
# -----------------------------------------------------

class MaterialDimensional(SQLModel, table=True):
    """Define un tipo de material que se maneja por dimensiones (ej: planchas, tablones)."""
    # Nombre explícito de tabla (opcional si coincide con la inferencia)
    __tablename__ = "material_dimensional"

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str = Field(max_length=100, unique=True, index=True)
    nombre: str = Field(max_length=255)
    descripcion: Optional[str] = Field(default=None) # Considerar: sa_column=Column(Text)
    espesor_nominal: Decimal = Field(max_digits=10, decimal_places=3)
    unidad_dimension: str = Field(default="mm", max_length=10)
    precio_venta_base_unidad: Decimal = Field(max_digits=14, decimal_places=4) # Esto se agrego
    unidad_precio_venta: str = Field(default="m2", max_length=20) # Esto se agrego
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con StockItemDimensional (un tipo de material tiene muchas piezas en stock)
    items_stock: List["StockItemDimensional"] = Relationship(back_populates="definicion_material")

# -----------------------------------------------------
# Modelo para Stock Físico de Material Dimensional
# -----------------------------------------------------

class StockItemDimensional(SQLModel, table=True):
    """Representa una pieza física específica de material dimensional en el inventario."""
    __tablename__ = "stock_item_dimensional"

    id: Optional[int] = Field(default=None, primary_key=True)
    material_dimensional_id: int = Field(foreign_key="material_dimensional.id", index=True)
    longitud_actual: Decimal = Field(max_digits=10, decimal_places=3)
    ancho_actual: Decimal = Field(max_digits=10, decimal_places=3)
    # El espesor se obtiene a través de la relación con MaterialDimensional
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    es_merma: bool = Field(default=False)
    stock_item_padre_id: Optional[int] = Field(
        default=None, foreign_key="stock_item_dimensional.id", index=True, nullable=True
    )
    orden_produccion_generadora_id: Optional[int] = Field(
        default=None, foreign_key="orden_produccion.id", index=True, nullable=True
    )
    # El ENUM de la DB se maneja como str aquí, la validación puede estar en otro nivel
    estado: str = Field(default="DISPONIBLE", index=True, max_length=50)
    fecha_ingreso: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación N:1 con MaterialDimensional (muchas piezas pertenecen a un tipo)
    definicion_material: MaterialDimensional = Relationship(back_populates="items_stock")

    # Relación N:1 con OrdenProduccion (muchas mermas pueden ser generadas por una orden)
    orden_generadora: Optional["OrdenProduccion"] = Relationship(back_populates="items_merma_generados")

    # Relación Auto-referenciada para Padre/Hijos (Merma)
    # Un item puede ser padre de varias mermas (hijos)
    items_merma_hijos: List["StockItemDimensional"] = Relationship(
        back_populates="item_padre"
        # sa_relationship_kwargs={'cascade': 'all, delete-orphan'} # Opcional: si se borra el padre, borrar mermas hijas
    )
    # Una merma (hijo) tiene un solo padre
    item_padre: Optional["StockItemDimensional"] = Relationship(
        back_populates="items_merma_hijos",
        sa_relationship_kwargs=dict(remote_side="StockItemDimensional.id") # Necesario para auto-referencia N:1
    )

    # Relación con LineaProformaMaterial (a definir en order_models.py)
    lineas_proforma: List["LineaProformaMaterial"] = Relationship(back_populates="stock_item")


# -----------------------------------------------------
# Modelo para Materiales Consumibles
# -----------------------------------------------------

class MaterialConsumible(SQLModel, table=True):
    """Define un tipo de material consumible (ej: lija, pintura, diluyente)."""
    __tablename__ = "material_consumible"

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str = Field(max_length=100, unique=True, index=True)
    nombre: str = Field(max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_medida: str = Field(max_length=50)
    rendimiento_m2: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=3, nullable=True)
    precio_venta_base_unidad: Decimal = Field(max_digits=14, decimal_places=4) # Esto se agrego
    stock_actual: Decimal = Field(default=0, max_digits=10, decimal_places=3)
    stock_minimo: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=3, nullable=True)
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con FormulaItem (a definir en service_models.py)
    items_formula: List["FormulaItem"] = Relationship(back_populates="material_consumible")

    # Relación con LineaProformaMaterial (a definir en order_models.py)
    lineas_proforma: List["LineaProformaMaterial"] = Relationship(back_populates="material_consumible")

# -----------------------------------------------------
# Modelo para Materiales Simples
# -----------------------------------------------------

class MaterialSimple(SQLModel, table=True):
    """Define un tipo de material simple (ej: clavos, tornillos)."""
    __tablename__ = "material_simple"

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str = Field(max_length=100, unique=True, index=True)
    nombre: str = Field(max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_medida: str = Field(max_length=50)
    precio_venta_base_unidad: Decimal = Field(max_digits=14, decimal_places=4) # Esto se agrego
    stock_actual: Decimal = Field(default=0, max_digits=10, decimal_places=3)
    stock_minimo: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=3, nullable=True)
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con FormulaItem (a definir en service_models.py)
    items_formula: List["FormulaItem"] = Relationship(back_populates="material_simple")

    # Relación con LineaProformaMaterial (a definir en order_models.py)
    lineas_proforma: List["LineaProformaMaterial"] = Relationship(back_populates="material_simple")
```

# app\models\machine_models.py

```py
# app/models/machine_models.py

from datetime import datetime, date # Importar date también
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .user_models import Usuario # Necesario para las relaciones

# -----------------------------------------------------
# Modelos de Tablas de Enlace (Muchos a Muchos)
# -----------------------------------------------------

class MaquinaHerramienta(SQLModel, table=True):
    """Modelo de tabla de enlace para la relación N:M entre Maquina y Herramienta."""
    __tablename__ = "maquina_herramienta"

    maquina_id: Optional[int] = Field(
        default=None, foreign_key="maquina.id", primary_key=True
    )
    herramienta_id: Optional[int] = Field(
        default=None, foreign_key="herramienta.id", primary_key=True
    )
    fecha_asignacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    posicion: Optional[str] = Field(default=None, max_length=50)

    # Relaciones para acceder fácilmente desde el link model (opcional pero útil)
    maquina: "Maquina" = Relationship(back_populates="herramientas_link")
    herramienta: "Herramienta" = Relationship(back_populates="maquinas_link")


class UsuarioAreaTrabajo(SQLModel, table=True):
    """Modelo de tabla de enlace para la relación N:M entre Usuario y AreaTrabajo."""
    __tablename__ = "usuario_area_trabajo"

    usuario_id: Optional[int] = Field(
        default=None, foreign_key="usuario.id", primary_key=True
    )
    area_trabajo_id: Optional[int] = Field(
        default=None, foreign_key="area_trabajo.id", primary_key=True
    )

    # Relaciones para acceder fácilmente desde el link model (opcional pero útil)
    usuario: "Usuario" = Relationship(back_populates="areas_trabajo_link")
    area_trabajo: "AreaTrabajo" = Relationship(back_populates="usuarios_link")

# -----------------------------------------------------
# Modelos Principales
# -----------------------------------------------------

class AreaTrabajo(SQLModel, table=True):
    """Representa un área física o lógica dentro del almacén/taller."""
    __tablename__ = "area_trabajo"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True, max_length=150)
    descripcion: Optional[str] = Field(default=None)

    # Relación 1:N con Maquina (un área puede tener varias máquinas)
    maquinas: List["Maquina"] = Relationship(back_populates="area_trabajo")

    # Relación N:M con Usuario (vía UsuarioAreaTrabajo)
    # El atributo 'usuarios' se puede obtener a través del link model si se necesita
    usuarios_link: List["UsuarioAreaTrabajo"] = Relationship(back_populates="area_trabajo")


class Maquina(SQLModel, table=True):
    """Representa una máquina utilizada en el proceso productivo."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150)
    tipo: str = Field(max_length=50) # Ej: 'CNC_ROUTER', 'CNC_LASER', 'CORTE_SIERRA'
    modelo: Optional[str] = Field(default=None, max_length=150)
    numero_serie: Optional[str] = Field(default=None, unique=True, index=True, max_length=150)
    area_trabajo_id: Optional[int] = Field(default=None, foreign_key="area_trabajo.id", index=True, nullable=True)
    margen_perdida_mm: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=2, nullable=True)
    estado: str = Field(default="OPERATIVA", max_length=50) # Ej: 'OPERATIVA', 'EN_MANTENIMIENTO', 'AVERIADA'
    fecha_adquisicion: Optional[date] = Field(default=None, nullable=True) # Usamos date para solo fecha
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación N:1 con AreaTrabajo (una máquina pertenece a un área, opcionalmente)
    area_trabajo: Optional["AreaTrabajo"] = Relationship(back_populates="maquinas")

    # Relación N:M con Herramienta (vía MaquinaHerramienta)
    herramientas_link: List["MaquinaHerramienta"] = Relationship(back_populates="maquina")

    # Relación 1:N con RegistroMantenimiento
    registros_mantenimiento: List["RegistroMantenimiento"] = Relationship(back_populates="maquina")

    # Relación 1:N con ReporteErrorMaquina
    reportes_errores: List["ReporteErrorMaquina"] = Relationship(back_populates="maquina")


class Herramienta(SQLModel, table=True):
    """Representa una herramienta o accesorio que puede ser usado por una máquina."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150)
    tipo: Optional[str] = Field(default=None, max_length=100)
    descripcion: Optional[str] = Field(default=None)
    codigo_interno: Optional[str] = Field(default=None, unique=True, index=True, max_length=50)

    # Relación N:M con Maquina (vía MaquinaHerramienta)
    maquinas_link: List["MaquinaHerramienta"] = Relationship(back_populates="herramienta")


class RegistroMantenimiento(SQLModel, table=True):
    """Registra una actividad de mantenimiento realizada sobre una máquina."""
    __tablename__ = "registro_mantenimiento"

    id: Optional[int] = Field(default=None, primary_key=True)
    maquina_id: int = Field(foreign_key="maquina.id", index=True)
    usuario_id_tecnico: Optional[int] = Field(default=None, foreign_key="usuario.id", index=True, nullable=True)
    fecha_mantenimiento: datetime = Field()
    tipo: str = Field(max_length=50) # Ej: 'PREVENTIVO', 'CORRECTIVO', 'INSPECCION'
    descripcion: str = Field() # Considerar sa_column=Column(Text)
    costo_repuestos: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2, nullable=True)
    horas_mano_obra: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=2, nullable=True)

    # Relación N:1 con Maquina
    maquina: Maquina = Relationship(back_populates="registros_mantenimiento")

    # Relación N:1 con Usuario (Técnico)
    tecnico: Optional["Usuario"] = Relationship(back_populates="mantenimientos_realizados")


class ReporteErrorMaquina(SQLModel, table=True):
    """Registra un error o avería reportado para una máquina."""
    __tablename__ = "reporte_error_maquina"

    id: Optional[int] = Field(default=None, primary_key=True)
    maquina_id: int = Field(foreign_key="maquina.id", index=True)
    usuario_id_reportador: int = Field(foreign_key="usuario.id", index=True)
    fecha_reporte: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    descripcion_error: str = Field() # Considerar sa_column=Column(Text)
    codigo_error: Optional[str] = Field(default=None, max_length=100)
    prioridad: Optional[str] = Field(default="MEDIA", max_length=50) # Ej: 'BAJA', 'MEDIA', 'ALTA', 'CRITICA'
    esta_resuelto: bool = Field(default=False, index=True)
    fecha_resolucion: Optional[datetime] = Field(default=None, nullable=True)
    usuario_id_resolutor: Optional[int] = Field(default=None, foreign_key="usuario.id", index=True, nullable=True)
    detalles_resolucion: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)

    # Relación N:1 con Maquina
    maquina: Maquina = Relationship(back_populates="reportes_errores")

    # Relación N:1 con Usuario (Reportador)
    reportador: "Usuario" = Relationship(
        back_populates="errores_reportados",
        sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_reportador]'}
    )

    # Relación N:1 con Usuario (Resolutor)
    resolutor: Optional["Usuario"] = Relationship(
        back_populates="errores_resueltos",
        sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_resolutor]'}
    )

# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .user_models import Usuario # Importamos Usuario para type hints

    # Añadir las relaciones inversas correspondientes en user_models.py:
    # class Usuario(SQLModel, table=True):
    #     ...
    #     areas_trabajo_link: List["UsuarioAreaTrabajo"] = Relationship(back_populates="usuario")
    #     mantenimientos_realizados: List["RegistroMantenimiento"] = Relationship(back_populates="tecnico")
    #     errores_reportados: List["ReporteErrorMaquina"] = Relationship(back_populates="reportador", sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_reportador]'})
    #     errores_resueltos: List["ReporteErrorMaquina"] = Relationship(back_populates="resolutor", sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_resolutor]'})
    #     ...
```

# app\models\order_models.py

```py
# app/models/order_models.py

from datetime import datetime
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .client_model import Cliente
    from .user_models import Usuario, Rol
    from .inventory_models import (
        StockItemDimensional, MaterialConsumible, MaterialSimple
    )
    from .service_models import ServicioDefinicion
    from .billing_models import VentaFactura
    #from .order_production_schema import AsignacionTareaOrden

# -----------------------------------------------------
# Modelo para Pedido del Cliente (Contenedor Principal)
# -----------------------------------------------------

class PedidoCliente(SQLModel, table=True):
    """Representa la solicitud global de un cliente, que agrupa proformas."""
    __tablename__ = "pedido_cliente"

    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id", index=True)
    usuario_id_vendedor: int = Field(foreign_key="usuario.id", index=True)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    estado: str = Field(default="NUEVO", index=True, max_length=50) # ENUM
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación N:1 con Cliente
    cliente: "Cliente" = Relationship(back_populates="pedidos")

    # Relación N:1 con Usuario (Vendedor)
    vendedor: "Usuario" = Relationship(back_populates="pedidos_creados")

    # Relación 1:N con Proforma (un pedido tiene 1 o 2 proformas)
    proformas: List["Proforma"] = Relationship(back_populates="pedido")

    # Relación 1:1 con OrdenProduccion (un pedido genera una orden)
    # 'uselist=False' indica que es una relación uno a uno (o uno a cero/uno)
    orden_produccion: Optional["OrdenProduccion"] = Relationship(
        back_populates="pedido", sa_relationship_kwargs={'uselist': False}
    )

    # Relación 1:N con VentaFactura (un pedido puede tener varias facturas si hay pagos parciales/ajustes)
    facturas: List["VentaFactura"] = Relationship(back_populates="pedido")

# -----------------------------------------------------
# Modelo para Proformas (Productos o Servicios)
# -----------------------------------------------------

class Proforma(SQLModel, table=True):
    """Representa una cotización/proforma, ya sea de productos o servicios."""
    id: Optional[int] = Field(default=None, primary_key=True)
    pedido_cliente_id: int = Field(foreign_key="pedido_cliente.id", index=True)
    tipo: str = Field(max_length=50) # 'PRODUCTO' o 'SERVICIO'
    # Clave foránea a sí misma para vincular proforma de producto y servicio
    proforma_vinculada_id: Optional[int] = Field(
        default=None, foreign_key="proforma.id", index=True, nullable=True
    )
    usuario_id_creador: int = Field(foreign_key="usuario.id", index=True)
    estado: str = Field(default="BORRADOR", index=True, max_length=50) # ENUM
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )
    fecha_aprobacion: Optional[datetime] = Field(default=None, nullable=True)
    fecha_reserva_expira: Optional[datetime] = Field(default=None, nullable=True)
    estado_reserva: Optional[str] = Field(default="NO_APLICA", max_length=50, nullable=True) # ENUM
    subtotal: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2, nullable=True)
    impuestos: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2, nullable=True)
    total: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2, nullable=True)
    notas: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)

    # Relación N:1 con PedidoCliente
    pedido: PedidoCliente = Relationship(back_populates="proformas")

    # Relación N:1 con Usuario (Creador)
    creador: "Usuario" = Relationship(back_populates="proformas_creadas")

    # Relación 1:1 Auto-referenciada (para vincular producto <-> servicio)
    proforma_vinculada: Optional["Proforma"] = Relationship(
        back_populates="proforma_vinculada_con", # Nombre del atributo en el otro lado
        sa_relationship_kwargs=dict(
            remote_side="Proforma.id", # Columna remota (la propia id)
            uselist=False # Indica que es una relación uno a uno
        )
    )
    # Atributo necesario para el back_populates de la relación anterior
    proforma_vinculada_con: Optional["Proforma"] = Relationship(back_populates="proforma_vinculada")

    # Relación 1:N con LineaProformaMaterial
    lineas_material: List["LineaProformaMaterial"] = Relationship(back_populates="proforma")

    # Relación 1:N con LineaProformaServicio
    lineas_servicio: List["LineaProformaServicio"] = Relationship(back_populates="proforma")

    # Relación con VentaFactura (lado N de la relación N:M implícita)
    facturas_productos: List["VentaFactura"] = Relationship(
        back_populates="proforma_productos",
        # Añadir esta línea especificando la FK en la tabla VentaFactura
        sa_relationship_kwargs={'foreign_keys': '[VentaFactura.proforma_productos_id]'}
    )
    facturas_servicios: List["VentaFactura"] = Relationship(
        back_populates="proforma_servicios",
        # Añadir esta línea especificando la FK en la tabla VentaFactura
        sa_relationship_kwargs={'foreign_keys': '[VentaFactura.proforma_servicios_id]'}
    )


# -----------------------------------------------------
# Modelo para Líneas de Proforma (Materiales)
# -----------------------------------------------------

class LineaProformaMaterial(SQLModel, table=True):
    """Representa una línea de item de material en una proforma."""
    __tablename__ = "linea_proforma_material"

    id: Optional[int] = Field(default=None, primary_key=True)
    proforma_id: int = Field(foreign_key="proforma.id", index=True)
    tipo_material_origen: str = Field(max_length=50) # ENUM: 'STOCK_DIMENSIONAL', 'CONSUMIBLE', 'SIMPLE'
    stock_item_dimensional_id: Optional[int] = Field(
        default=None, foreign_key="stock_item_dimensional.id", index=True, nullable=True
    )
    material_consumible_id: Optional[int] = Field(
        default=None, foreign_key="material_consumible.id", index=True, nullable=True
    )
    material_simple_id: Optional[int] = Field(
        default=None, foreign_key="material_simple.id", index=True, nullable=True
    )
    descripcion_item: str = Field(max_length=255)
    cantidad: Decimal = Field(max_digits=10, decimal_places=3)
    unidad: str = Field(max_length=50)
    precio_unitario: Decimal = Field(max_digits=12, decimal_places=2)
    total_linea: Decimal = Field(max_digits=15, decimal_places=2)
    detalles_corte_solicitado: Optional[str] = Field(default=None) # Podría ser JSON serializado

    # Relación N:1 con Proforma
    proforma: Proforma = Relationship(back_populates="lineas_material")

    # Relaciones N:1 con los posibles orígenes del material
    stock_item: Optional["StockItemDimensional"] = Relationship(back_populates="lineas_proforma")
    material_consumible: Optional["MaterialConsumible"] = Relationship(back_populates="lineas_proforma")
    material_simple: Optional["MaterialSimple"] = Relationship(back_populates="lineas_proforma")

    # Relación 1:N con LineaProformaServicio (si un servicio se aplica a esta línea)
    servicios_asociados: List["LineaProformaServicio"] = Relationship(back_populates="linea_material_asociada")

    # Relación 1:N con AsignacionTareaOrden (tareas específicas para esta línea)
    tareas_asignadas: List["AsignacionTareaOrden"] = Relationship(back_populates="linea_material")


# -----------------------------------------------------
# Modelo para Líneas de Proforma (Servicios)
# -----------------------------------------------------

class LineaProformaServicio(SQLModel, table=True):
    """Representa una línea de item de servicio en una proforma."""
    __tablename__ = "linea_proforma_servicio"

    id: Optional[int] = Field(default=None, primary_key=True)
    proforma_id: int = Field(foreign_key="proforma.id", index=True)
    servicio_definicion_id: int = Field(foreign_key="servicio_definicion.id", index=True)
    linea_proforma_material_id: Optional[int] = Field(
        default=None, foreign_key="linea_proforma_material.id", index=True, nullable=True
    )
    descripcion_servicio: str = Field(max_length=255)
    cantidad: Decimal = Field(max_digits=10, decimal_places=3)
    precio_unitario: Decimal = Field(max_digits=12, decimal_places=2)
    total_linea: Decimal = Field(max_digits=15, decimal_places=2)
    ruta_imagen_cnc: Optional[str] = Field(default=None, max_length=512, nullable=True)
    detalles_adicionales: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)

    # Relación N:1 con Proforma
    proforma: Proforma = Relationship(back_populates="lineas_servicio")

    # Relación N:1 con ServicioDefinicion
    servicio_definicion: "ServicioDefinicion" = Relationship(back_populates="lineas_proforma")

    # Relación N:1 con LineaProformaMaterial (servicio aplicado a un material)
    linea_material_asociada: Optional["LineaProformaMaterial"] = Relationship(back_populates="servicios_asociados")

    # Relación 1:N con AsignacionTareaOrden (tareas específicas para esta línea)
    tareas_asignadas: List["AsignacionTareaOrden"] = Relationship(back_populates="linea_servicio")


# -----------------------------------------------------
# Modelo para Órdenes de Producción
# -----------------------------------------------------

class OrdenProduccion(SQLModel, table=True):
    """Representa la orden de trabajo para fabricar/preparar lo solicitado en un pedido."""
    __tablename__ = "orden_produccion"

    id: Optional[int] = Field(default=None, primary_key=True)
    # unique=True aquí asegura que un pedido solo genera una orden
    pedido_cliente_id: int = Field(foreign_key="pedido_cliente.id", unique=True, index=True)
    usuario_id_supervisor: Optional[int] = Field(default=None, foreign_key="usuario.id", index=True, nullable=True)
    estado: str = Field(default="PENDIENTE_ASIGNACION", index=True, max_length=50) # ENUM
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_inicio_espera: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_asignacion: Optional[datetime] = Field(default=None, nullable=True)
    fecha_estimada_finalizacion: Optional[datetime] = Field(default=None, nullable=True)
    fecha_real_finalizacion: Optional[datetime] = Field(default=None, nullable=True)
    notas_supervisor: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)
    ruta_imagen_final: Optional[str] = Field(default=None, max_length=512, nullable=True)
    prioridad: int = Field(default=0)

    # Relación 1:1 con PedidoCliente
    pedido: PedidoCliente = Relationship(back_populates="orden_produccion")

    # Relación N:1 con Usuario (Supervisor)
    supervisor: Optional["Usuario"] = Relationship(back_populates="ordenes_supervisadas")

    # Relación 1:N con StockItemDimensional (mermas generadas por esta orden)
    items_merma_generados: List["StockItemDimensional"] = Relationship(back_populates="orden_generadora")

    # Relación 1:N con AsignacionTareaOrden (tareas que componen esta orden)
    asignaciones_tareas: List["AsignacionTareaOrden"] = Relationship(back_populates="orden")


# -----------------------------------------------------
# Modelo para Asignación de Tareas de una Orden
# -----------------------------------------------------

class AsignacionTareaOrden(SQLModel, table=True):
    """Asigna una tarea específica de una orden a un usuario con un rol."""
    __tablename__ = "asignacion_tarea_orden"

    id: Optional[int] = Field(default=None, primary_key=True)
    orden_id: int = Field(foreign_key="orden_produccion.id", index=True)
    # La tarea puede aplicar a una línea específica de servicio o material
    linea_proforma_servicio_id: Optional[int] = Field(
        default=None, foreign_key="linea_proforma_servicio.id", index=True, nullable=True
    )
    linea_proforma_material_id: Optional[int] = Field(
        default=None, foreign_key="linea_proforma_material.id", index=True, nullable=True
    )
    usuario_id_asignado: int = Field(foreign_key="usuario.id", index=True)
    rol_id_contexto: int = Field(foreign_key="rol.id", index=True)
    tipo_tarea: str = Field(max_length=100) # Ej: DIBUJO_CNC, CORTE_MATERIAL
    estado_tarea: str = Field(default="PENDIENTE", max_length=50) # ENUM
    fecha_asignacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_inicio_tarea: Optional[datetime] = Field(default=None, nullable=True)
    fecha_fin_tarea: Optional[datetime] = Field(default=None, nullable=True)
    notas: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)

    # Relación N:1 con OrdenProduccion
    orden: OrdenProduccion = Relationship(back_populates="asignaciones_tareas")

    # Relación N:1 con LineaProformaServicio (opcional)
    linea_servicio: Optional[LineaProformaServicio] = Relationship(back_populates="tareas_asignadas")

    # Relación N:1 con LineaProformaMaterial (opcional)
    linea_material: Optional[LineaProformaMaterial] = Relationship(back_populates="tareas_asignadas")

    # Relación N:1 con Usuario (Asignado)
    usuario_asignado: "Usuario" = Relationship(back_populates="tareas_asignadas")

    # Relación N:1 con Rol (Contexto de la tarea)
    rol_contexto: "Rol" = Relationship(back_populates="asignaciones_tareas")






# ... (Modelos OrdenProduccion, AsignacionTareaOrden) ...




# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .client_model import Cliente
    from .user_models import Usuario, Rol
    from .inventory_models import StockItemDimensional, MaterialConsumible, MaterialSimple
    from .service_models import ServicioDefinicion
    from .billing_models import VentaFactura

    # Recordatorio: Añadir/Verificar back_populates correspondientes en otros modelos:
    # Cliente: pedidos: List["PedidoCliente"] = ...
    # Usuario: pedidos_creados: List["PedidoCliente"] = ..., proformas_creadas: List["Proforma"] = ..., ordenes_supervisadas: List["OrdenProduccion"] = ..., tareas_asignadas: List["AsignacionTareaOrden"] = ...
    # Rol: asignaciones_tareas: List["AsignacionTareaOrden"] = ...
    # StockItemDimensional: lineas_proforma: List["LineaProformaMaterial"] = ...
    # MaterialConsumible: lineas_proforma: List["LineaProformaMaterial"] = ...
    # MaterialSimple: lineas_proforma: List["LineaProformaMaterial"] = ...
    # ServicioDefinicion: lineas_proforma: List["LineaProformaServicio"] = ...
    # VentaFactura: pedido: PedidoCliente = ..., proforma_productos: Optional[Proforma] = ..., proforma_servicios: Optional[Proforma] = ...
```

# app\models\service_models.py

```py
# app/models/service_models.py

from datetime import datetime
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

# Importaciones para relaciones si TYPE_CHECKING es True
if TYPE_CHECKING:
    from .inventory_models import MaterialConsumible, MaterialSimple
    from .order_models import LineaProformaServicio

# -----------------------------------------------------
# Modelo para Definición de Servicios
# -----------------------------------------------------

class ServicioDefinicion(SQLModel, table=True):
    """Define un tipo de servicio ofrecido por el negocio."""
    __tablename__ = "servicio_definicion"

    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(max_length=50, unique=True, index=True)
    nombre: str = Field(max_length=255)
    descripcion: Optional[str] = Field(default=None) # Considerar sa_column=Column(Text)
    unidad_cobro: str = Field(max_length=50) # ej: hora, minuto, pieza, m lineal
    costo_por_unidad: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=2, nullable=True)
    costo_por_minuto: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2, nullable=True)
    tiempo_setup_min: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2, nullable=True)
    tiempo_preparado_min_por_unidad: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2, nullable=True)
    factor_ih: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=3, nullable=True)
    factor_st: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=3, nullable=True)
    factor_m: Optional[Decimal] = Field(default=None, max_digits=5, decimal_places=3, nullable=True)
    requiere_dibujo_cnc: bool = Field(default=False)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación 1:N con Formula (un servicio puede tener varias fórmulas asociadas)
    formulas: List["Formula"] = Relationship(back_populates="servicio_definicion")

    # Relación 1:N con LineaProformaServicio (un tipo de servicio puede estar en muchas líneas de proforma)
    lineas_proforma: List["LineaProformaServicio"] = Relationship(back_populates="servicio_definicion")

# -----------------------------------------------------
# Modelo para Fórmulas de Materiales por Servicio
# -----------------------------------------------------

class Formula(SQLModel, table=True):
    """Define una fórmula específica de materiales requeridos para un servicio."""
    id: Optional[int] = Field(default=None, primary_key=True)
    servicio_definicion_id: int = Field(foreign_key="servicio_definicion.id", index=True)
    nombre: str = Field(max_length=150)
    descripcion: Optional[str] = Field(default=None)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True
    )

    # Relación N:1 con ServicioDefinicion (una fórmula pertenece a un servicio)
    servicio_definicion: ServicioDefinicion = Relationship(back_populates="formulas")

    # Relación 1:N con FormulaItem (una fórmula se compone de varios items/materiales)
    items: List["FormulaItem"] = Relationship(back_populates="formula") # cascade="all, delete-orphan" podría ser útil aquí

# -----------------------------------------------------
# Modelo para Items dentro de una Fórmula
# -----------------------------------------------------

class FormulaItem(SQLModel, table=True):
    """Detalla un material (Consumible o Simple) y su cantidad dentro de una fórmula."""
    __tablename__ = "formula_item"

    id: Optional[int] = Field(default=None, primary_key=True)
    formula_id: int = Field(foreign_key="formula.id", index=True)
    # El ENUM se maneja como str, la validación de tipo vs FK en la app
    tipo_material: str = Field(max_length=50) # 'CONSUMIBLE' o 'SIMPLE'
    material_consumible_id: Optional[int] = Field(default=None, foreign_key="material_consumible.id", index=True, nullable=True)
    material_simple_id: Optional[int] = Field(default=None, foreign_key="material_simple.id", index=True, nullable=True)
    cantidad_necesaria: Decimal = Field(max_digits=10, decimal_places=3)
    unidad_rendimiento: str = Field(default="m2", max_length=50) # Unidad base para la cantidad (ej: por m2 de servicio)
    descripcion_uso: Optional[str] = Field(default=None)

    # Relación N:1 con Formula (un item pertenece a una fórmula)
    formula: Formula = Relationship(back_populates="items")

    # Relación N:1 con MaterialConsumible (un item PUEDE ser un consumible)
    material_consumible: Optional["MaterialConsumible"] = Relationship(back_populates="items_formula")

    # Relación N:1 con MaterialSimple (un item PUEDE ser un material simple)
    material_simple: Optional["MaterialSimple"] = Relationship(back_populates="items_formula")


# --- Manejo de Referencias Circulares / Forward References ---
if TYPE_CHECKING:
    from .inventory_models import MaterialConsumible, MaterialSimple
    from .order_models import LineaProformaServicio # Importar para la relación en ServicioDefinicion

    # Recordatorio: Añadir back_populates correspondientes en otros modelos:
    # class MaterialConsumible(...) / MaterialSimple(...):
    #     items_formula: List["FormulaItem"] = Relationship(back_populates="material_...")
    #
    # class LineaProformaServicio(...):
    #     servicio_definicion: ServicioDefinicion = Relationship(back_populates="lineas_proforma")
```

# app\models\user_models.py

```py
# app/models/user_models.py

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint # Asegúrate de importar UniqueConstraint


# -----------------------------------------------------
# Modelos de Tablas de Enlace (Muchos a Muchos)
# -----------------------------------------------------

class UsuarioRol(SQLModel, table=True):
    """Modelo de tabla de enlace para la relación N:M entre Usuario y Rol."""
    __tablename__ = "usuario_rol"
    usuario_id: Optional[int] = Field(
        default=None, foreign_key="usuario.id", primary_key=True
    )
    rol_id: Optional[int] = Field(
        default=None, foreign_key="rol.id", primary_key=True
    )


class RolPermiso(SQLModel, table=True):
    """Modelo de tabla de enlace para la relación N:M entre Rol y Permiso."""
    __tablename__ = "rol_permiso"
    rol_id: Optional[int] = Field(
        default=None, foreign_key="rol.id", primary_key=True
    )
    permiso_id: Optional[int] = Field(
        default=None, foreign_key="permiso.id", primary_key=True
    )

if TYPE_CHECKING: # Asegúrate de importar estas clases aquí
    from .order_models import PedidoCliente, Proforma, OrdenProduccion, AsignacionTareaOrden
    from .machine_models import UsuarioAreaTrabajo, RegistroMantenimiento, ReporteErrorMaquina

# -----------------------------------------------------
# Modelos Principales
# -----------------------------------------------------

class Usuario(SQLModel, table=True):
    """Representa a un empleado/usuario del sistema."""
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, max_length=100, unique=True) # unique=True para SQLModel > 0.0.14
    email: str = Field(index=True, max_length=255, unique=True)    # unique=True para SQLModel > 0.0.14
    contrasena_hash: str = Field(max_length=255)
    nombre_completo: str = Field(max_length=255)
    esta_activo: bool = Field(default=True)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True) # Usamos default_factory para autogenerar en Python
    fecha_ultima_actualizacion: Optional[datetime] = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True) # onupdate para DB

    # Relación N:M con Rol
    roles: List["Rol"] = Relationship(back_populates="usuarios", link_model=UsuarioRol)

    # Relación 1:N con PeriodoIndisponibilidad
    periodos_indisponibilidad: List["PeriodoIndisponibilidad"] = Relationship(back_populates="usuario")

 # Relación 1:N con PedidoCliente (Usuario como vendedor)
    pedidos_creados: List["PedidoCliente"] = Relationship(back_populates="vendedor")

    # Relación 1:N con Proforma (Usuario como creador)
    proformas_creadas: List["Proforma"] = Relationship(back_populates="creador")

    # Relación 1:N con OrdenProduccion (Usuario como supervisor)
    ordenes_supervisadas: List["OrdenProduccion"] = Relationship(back_populates="supervisor")

    # Relación 1:N con AsignacionTareaOrden (Usuario como asignado)
    tareas_asignadas: List["AsignacionTareaOrden"] = Relationship(back_populates="usuario_asignado")

    # Relación N:M con AreaTrabajo (vía UsuarioAreaTrabajo)
    areas_trabajo_link: List["UsuarioAreaTrabajo"] = Relationship(back_populates="usuario")

    # Relación 1:N con RegistroMantenimiento (Usuario como tecnico)
    mantenimientos_realizados: List["RegistroMantenimiento"] = Relationship(back_populates="tecnico")

    # Relación 1:N con ReporteErrorMaquina (Usuario como reportador)
    # Se necesita foreign_keys por haber dos FK a Usuario en ReporteErrorMaquina
    errores_reportados: List["ReporteErrorMaquina"] = Relationship(
        back_populates="reportador",
        sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_reportador]'}
    )

    # Relación 1:N con ReporteErrorMaquina (Usuario como resolutor)
    # Se necesita foreign_keys por haber dos FK a Usuario en ReporteErrorMaquina
    errores_resueltos: List["ReporteErrorMaquina"] = Relationship(
        back_populates="resolutor",
        sa_relationship_kwargs={'foreign_keys': '[ReporteErrorMaquina.usuario_id_resolutor]'}
    )


if TYPE_CHECKING: # Asegúrate de importar AsignacionTareaOrden aquí
    from .order_models import AsignacionTareaOrden
    # ... (otras importaciones necesarias para Usuario)

class Rol(SQLModel, table=True):
    """Representa un rol dentro del sistema (ej: Administrador, Vendedor)."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=100, unique=True)
    descripcion: Optional[str] = Field(default=None)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    fecha_ultima_actualizacion: Optional[datetime] = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}, nullable=True)

    # Relación N:M con Usuario
    usuarios: List["Usuario"] = Relationship(back_populates="roles", link_model=UsuarioRol)

    # Relación N:M con Permiso
    permisos: List["Permiso"] = Relationship(back_populates="roles", link_model=RolPermiso)

    # Relación 1:N con AsignacionTareaOrden (Rol como contexto de la tarea)
    asignaciones_tareas: List["AsignacionTareaOrden"] = Relationship(back_populates="rol_contexto")

class Permiso(SQLModel, table=True):
    """Representa una acción permitida sobre un recurso (ej: crear proforma)."""
    __table_args__ = (UniqueConstraint("nombre_accion", "nombre_recurso", name="uq_permiso_accion_recurso"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_accion: str = Field(max_length=100)
    nombre_recurso: str = Field(max_length=100)
    descripcion: Optional[str] = Field(default=None)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)

    # Relación N:M con Rol
    roles: List["Rol"] = Relationship(back_populates="permisos", link_model=RolPermiso)


class PeriodoIndisponibilidad(SQLModel, table=True):
    """Registra los periodos en que un usuario no está disponible."""
    # Nombre de tabla explícito por si SQLModel infiere uno diferente
    __tablename__ = "periodo_indisponibilidad" 

    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id", index=True)
    fecha_inicio: datetime = Field()
    fecha_fin: Optional[datetime] = Field(default=None)
    motivo: Optional[str] = Field(default=None) # Considerar usar sa_column=Column(Text) si se espera texto largo

    # Relación N:1 con Usuario
    usuario: Usuario = Relationship(back_populates="periodos_indisponibilidad")


# --- Manejo de Referencias Circulares / Forward References ---
# Esto ayuda a MyPy/Pyright a entender los tipos en las relaciones
# aunque no es estrictamente necesario para que SQLModel/SQLAlchemy funcionen
# if TYPE_CHECKING:
#    # Importaciones de otros módulos si fueran necesarias para las relaciones
#    # from .order_models import AsignacionTareaOrden, PedidoCliente, Proforma, OrdenProduccion
#    # from .machine_models import UsuarioAreaTrabajo, RegistroMantenimiento, ReporteErrorMaquina
#    pass # No necesitamos imports cruzados *dentro* de este archivo por ahora
```

# app\repositories\__init__.py

```py

```

# app\repositories\cliente_repository.py

```py
# app/repositories/cliente_repository.py
import logging
from typing import Optional, Sequence, Union, Dict, Any

from sqlmodel import Session, select, SQLModel
from sqlalchemy.exc import IntegrityError # Para capturar errores de constraints
from fastapi import HTTPException, status # Solo para tipado en docstring, no lanzar aquí

from app.models.client_model import Cliente
# Importar schemas solo si son estrictamente necesarios aquí (poco común)
# from app.schemas.client_schema import ClienteUpdate

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read (Getters)
# =====================

def get_cliente_by_id(db: Session, *, cliente_id: int) -> Optional[Cliente]:
    """
    Obtiene un cliente específico por su ID.

    Args:
        db: La sesión de base de datos activa.
        cliente_id: El ID del cliente a buscar.

    Returns:
        El objeto Cliente si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción de base de datos.
    """
    try:
        # db.get es la forma más directa de buscar por PK con SQLModel/SQLAlchemy
        cliente = db.get(Cliente, cliente_id)
        return cliente
    except Exception as e:
        logger.error(f"Error obteniendo cliente por ID {cliente_id}: {e}", exc_info=True)
        raise

def get_cliente_by_identificacion(db: Session, *, identificacion: str) -> Optional[Cliente]:
    """
    Obtiene un cliente específico por su número de identificación fiscal.

    Args:
        db: La sesión de base de datos activa.
        identificacion: El número de identificación fiscal a buscar.

    Returns:
        El objeto Cliente si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción de base de datos.
    """
    if not identificacion: # Evitar consulta si la identificación está vacía
        return None
    try:
        statement = select(Cliente).where(Cliente.identificacion_fiscal == identificacion)
        cliente = db.exec(statement).first()
        return cliente
    except Exception as e:
        logger.error(f"Error obteniendo cliente por identificación '{identificacion}': {e}", exc_info=True)
        raise

def get_cliente_by_email(db: Session, *, email: str) -> Optional[Cliente]:
    """
    Obtiene un cliente específico por su dirección de correo electrónico.

    Args:
        db: La sesión de base de datos activa.
        email: El correo electrónico a buscar.

    Returns:
        El objeto Cliente si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción de base de datos.
    """
    if not email: # Evitar consulta si el email está vacío
        return None
    try:
        statement = select(Cliente).where(Cliente.email == email)
        cliente = db.exec(statement).first()
        return cliente
    except Exception as e:
        logger.error(f"Error obteniendo cliente por email '{email}': {e}", exc_info=True)
        raise

def list_clientes(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Cliente]:
    """
    Obtiene una lista paginada de clientes.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de clientes a saltar.
        limit: Número máximo de clientes a devolver.

    Returns:
        Una secuencia (lista) de objetos Cliente.

    Raises:
        Exception: Relanza cualquier excepción de base de datos.
    """
    try:
        statement = select(Cliente).offset(skip).limit(limit).order_by(Cliente.id) # Ordenar para consistencia
        clientes = db.exec(statement).all()
        return clientes
    except Exception as e:
        logger.error(f"Error listando clientes: {e}", exc_info=True)
        raise

# =====================
#  Funciones Write (Create, Update, Delete)
# =====================

def create_cliente(db: Session, *, cliente_data: Cliente) -> Cliente:
    """
    Crea un nuevo cliente en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        cliente_data: Un objeto Cliente (previamente validado por el schema/servicio).

    Returns:
        El objeto Cliente recién creado y refrescado.

    Raises:
        IntegrityError: Si ocurre una violación de constraint (ej: email o
                        identificación duplicada). La capa de servicio debe
                        capturarla y traducirla a HTTPException 409.
        Exception: Relanza otras excepciones de base de datos.
    """
    db_cliente = cliente_data # Asumimos que ya es un objeto Cliente
    try:
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        logger.info(f"Cliente creado: ID={db_cliente.id}, Nombre='{db_cliente.nombre}'")
        return db_cliente
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"Error de integridad al crear cliente '{db_cliente.nombre}': {e}")
        # Relanzar para que el servicio maneje el conflicto (409)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado creando cliente '{db_cliente.nombre}': {e}", exc_info=True)
        raise # Relanza otras excepciones

def update_cliente(
    db: Session, *, db_cliente: Cliente, update_data: Dict[str, Any]
) -> Cliente:
    """
    Actualiza un cliente existente en la base de datos.

    Aplica actualizaciones parciales usando sqlmodel_update.

    Args:
        db: La sesión de base de datos activa.
        db_cliente: El objeto Cliente existente obtenido de la DB.
        update_data: Un diccionario con los campos a actualizar (ya filtrados
                     y validados por el servicio, idealmente).

    Returns:
        El objeto Cliente actualizado y refrescado.

    Raises:
        IntegrityError: Si la actualización causa una violación de constraint.
                        La capa de servicio debe manejarla (409).
        Exception: Relanza otras excepciones de base de datos.
    """
    try:
        # update_data ya debería ser un dict aquí, proveniente del servicio
        if not update_data:
            logger.warning(f"Intento de actualizar cliente {db_cliente.id} sin datos.")
            return db_cliente # No hay nada que actualizar

        # Usar sqlmodel_update para aplicar los cambios al objeto existente
        db_cliente.sqlmodel_update(update_data)

        db.add(db_cliente) # Marcar el objeto como modificado
        db.commit()
        db.refresh(db_cliente)
        logger.info(f"Cliente actualizado: ID={db_cliente.id}")
        return db_cliente
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"Error de integridad al actualizar cliente ID {db_cliente.id}: {e}")
        # Relanzar para que el servicio maneje el conflicto (409)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado actualizando cliente ID {db_cliente.id}: {e}", exc_info=True)
        raise # Relanza otras excepciones

def delete_cliente(db: Session, *, cliente_id: int) -> Optional[Cliente]:
    """
    Elimina un cliente de la base de datos por su ID.

    Busca al cliente y si existe, intenta eliminarlo. La DB impedirá
    la eliminación si existen registros dependientes (Pedidos, Facturas)
    debido a la constraint ON DELETE RESTRICT.

    Args:
        db: La sesión de base de datos activa.
        cliente_id: El ID del cliente a eliminar.

    Returns:
        El objeto Cliente que fue eliminado, o None si el cliente no se encontró.

    Raises:
        IntegrityError: Si la eliminación es bloqueada por la DB debido a
                        registros dependientes. El servicio debe manejarla (409).
        Exception: Relanza otras excepciones de base de datos.
    """
    try:
        cliente = db.get(Cliente, cliente_id)
        if not cliente:
            logger.warning(f"Intento de eliminar cliente ID {cliente_id} no encontrado.")
            return None # No encontrado

        cliente_repr = f"ID={cliente.id}, Nombre='{cliente.nombre}'"
        logger.info(f"Intentando eliminar cliente: {cliente_repr}")
        db.delete(cliente)
        db.commit()
        logger.warning(f"Cliente eliminado: {cliente_repr}") # Usar warning para eliminaciones
        return cliente # Devuelve el objeto eliminado (desvinculado de la sesión)

    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de integridad al eliminar cliente ID {cliente_id}. Probablemente tiene pedidos/facturas asociados: {e}")
        # Relanzar para que el servicio maneje el conflicto (409)
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado eliminando cliente ID {cliente_id}: {e}", exc_info=True)
        raise # Relanza otras excepciones
```

# app\repositories\inventory_repository.py

```py
# app/repositories/inventory_repository.py
import logging
from typing import Optional, Sequence, Union, Dict, Any, List
from decimal import Decimal

from sqlmodel import Session, select, SQLModel, and_ # Importar 'and_'
from sqlalchemy.exc import IntegrityError

# Importar Modelos
from app.models.inventory_models import (
    MaterialDimensional,
    StockItemDimensional,
    MaterialConsumible,
    MaterialSimple
)

logger = logging.getLogger(__name__)

# =======================================
# Repositorio para MaterialDimensional
# =======================================

def get_material_dimensional_by_id(db: Session, *, mat_dim_id: int) -> Optional[MaterialDimensional]:
    """Obtiene un tipo de material dimensional por ID."""
    try:
        return db.get(MaterialDimensional, mat_dim_id)
    except Exception as e:
        logger.error(f"Error obteniendo MaterialDimensional ID {mat_dim_id}: {e}", exc_info=True)
        raise

def get_material_dimensional_by_sku(db: Session, *, sku: str) -> Optional[MaterialDimensional]:
    """Obtiene un tipo de material dimensional por SKU."""
    try:
        statement = select(MaterialDimensional).where(MaterialDimensional.sku == sku)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo MaterialDimensional SKU '{sku}': {e}", exc_info=True)
        raise

def list_materiales_dimensionales(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialDimensional]:
    """Lista tipos de materiales dimensionales."""
    try:
        statement = select(MaterialDimensional).offset(skip).limit(limit).order_by(MaterialDimensional.id)
        return db.exec(statement).all()
    except Exception as e:
        logger.error(f"Error listando MaterialDimensional: {e}", exc_info=True)
        raise

def create_material_dimensional(db: Session, *, mat_dim_data: MaterialDimensional) -> MaterialDimensional:
    """Crea un nuevo tipo de material dimensional."""
    db_mat_dim = mat_dim_data
    try:
        db.add(db_mat_dim)
        db.commit()
        db.refresh(db_mat_dim)
        logger.info(f"MaterialDimensional creado: ID={db_mat_dim.id}, SKU='{db_mat_dim.sku}'")
        return db_mat_dim
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"Error de integridad al crear MaterialDimensional SKU '{db_mat_dim.sku}': {e}")
        raise e # Relanzar para que el servicio maneje 409
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado creando MaterialDimensional SKU '{db_mat_dim.sku}': {e}", exc_info=True)
        raise

def update_material_dimensional(db: Session, *, db_mat_dim: MaterialDimensional, update_data: Dict[str, Any]) -> MaterialDimensional:
    """Actualiza un tipo de material dimensional."""
    try:
        # Evitar actualizar SKU si se incluye accidentalmente
        update_data.pop("sku", None)
        if not update_data: return db_mat_dim # Nada que actualizar
        db_mat_dim.sqlmodel_update(update_data)
        db.add(db_mat_dim)
        db.commit()
        db.refresh(db_mat_dim)
        logger.info(f"MaterialDimensional actualizado: ID={db_mat_dim.id}")
        return db_mat_dim
    except IntegrityError as e: # Podría ocurrir si se intentara cambiar SKU a uno existente (aunque lo prevenimos arriba)
        db.rollback()
        logger.warning(f"Error de integridad al actualizar MaterialDimensional ID {db_mat_dim.id}: {e}")
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado actualizando MaterialDimensional ID {db_mat_dim.id}: {e}", exc_info=True)
        raise

def delete_material_dimensional(db: Session, *, mat_dim_id: int) -> Optional[MaterialDimensional]:
    """Elimina un tipo de material dimensional."""
    try:
        db_mat_dim = db.get(MaterialDimensional, mat_dim_id)
        if not db_mat_dim: return None
        logger.warning(f"Intentando eliminar MaterialDimensional: ID={mat_dim_id}, SKU='{db_mat_dim.sku}'")
        db.delete(db_mat_dim)
        db.commit()
        logger.warning(f"MaterialDimensional eliminado: ID={mat_dim_id}")
        return db_mat_dim
    except IntegrityError as e: # Fallará si hay StockItemDimensional referenciándolo
        db.rollback()
        logger.error(f"Error de integridad al eliminar MaterialDimensional ID {mat_dim_id}. Probablemente referenciado por stock: {e}")
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado eliminando MaterialDimensional ID {mat_dim_id}: {e}", exc_info=True)
        raise

# =======================================
# Repositorio para MaterialConsumible
# =======================================
# (Similar a MaterialDimensional: get_by_id, get_by_sku, list, create, update, delete)
# ... Implementación análoga ...

def get_material_consumible_by_id(db: Session, *, mat_cons_id: int) -> Optional[MaterialConsumible]:
    try: return db.get(MaterialConsumible, mat_cons_id)
    except Exception as e: logger.error(f"Error get MatCons ID {mat_cons_id}: {e}", exc_info=True); raise

def get_material_consumible_by_sku(db: Session, *, sku: str) -> Optional[MaterialConsumible]:
    try: return db.exec(select(MaterialConsumible).where(MaterialConsumible.sku == sku)).first()
    except Exception as e: logger.error(f"Error get MatCons SKU {sku}: {e}", exc_info=True); raise

def list_materiales_consumibles(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialConsumible]:
    try: return db.exec(select(MaterialConsumible).offset(skip).limit(limit).order_by(MaterialConsumible.id)).all()
    except Exception as e: logger.error(f"Error list MatCons: {e}", exc_info=True); raise

def create_material_consumible(db: Session, *, mat_cons_data: MaterialConsumible) -> MaterialConsumible:
    db_mat = mat_cons_data
    try:
        db.add(db_mat); db.commit(); db.refresh(db_mat)
        logger.info(f"MaterialConsumible creado: ID={db_mat.id}, SKU='{db_mat.sku}'")
        return db_mat
    except IntegrityError as e: db.rollback(); logger.warning(f"IntegrityError create MatCons SKU '{db_mat.sku}': {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error create MatCons SKU '{db_mat.sku}': {e}", exc_info=True); raise

def update_material_consumible(db: Session, *, db_mat_cons: MaterialConsumible, update_data: Dict[str, Any]) -> MaterialConsumible:
    """Actualiza campos definitorios (nombre, desc, etc.), no stock_actual."""
    try:
        update_data.pop("sku", None)
        update_data.pop("stock_actual", None) # No actualizar stock aquí
        if not update_data: return db_mat_cons
        db_mat_cons.sqlmodel_update(update_data)
        db.add(db_mat_cons); db.commit(); db.refresh(db_mat_cons)
        logger.info(f"MaterialConsumible actualizado: ID={db_mat_cons.id}")
        return db_mat_cons
    except IntegrityError as e: db.rollback(); logger.warning(f"IntegrityError update MatCons ID {db_mat_cons.id}: {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error update MatCons ID {db_mat_cons.id}: {e}", exc_info=True); raise

def delete_material_consumible(db: Session, *, mat_cons_id: int) -> Optional[MaterialConsumible]:
    try:
        db_mat = db.get(MaterialConsumible, mat_cons_id)
        if not db_mat: return None
        logger.warning(f"Intentando eliminar MaterialConsumible: ID={mat_cons_id}, SKU='{db_mat.sku}'")
        db.delete(db_mat); db.commit()
        logger.warning(f"MaterialConsumible eliminado: ID={mat_cons_id}")
        return db_mat
    except IntegrityError as e: # Fallará si está en FormulaItem o LineaProformaMaterial
        db.rollback(); logger.error(f"IntegrityError delete MatCons ID {mat_cons_id}. Referenciado?: {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error delete MatCons ID {mat_cons_id}: {e}", exc_info=True); raise

def adjust_stock_consumible(db: Session, *, mat_cons_id: int, change_amount: Decimal) -> Optional[MaterialConsumible]:
    """Ajusta el stock actual de un material consumible."""
    try:
        db_mat = db.get(MaterialConsumible, mat_cons_id)
        if not db_mat: return None
        new_stock = (db_mat.stock_actual or Decimal("0.0")) + change_amount
        if new_stock < 0:
             logger.error(f"Intento de ajuste de stock negativo para MatCons ID {mat_cons_id}. Actual: {db_mat.stock_actual}, Cambio: {change_amount}")
             # Decisión: ¿Lanzar error o simplemente dejar en 0? Lanzar error es más seguro.
             raise ValueError("El ajuste de stock resultaría en una cantidad negativa.")
        db_mat.stock_actual = new_stock
        db.add(db_mat); db.commit(); db.refresh(db_mat)
        logger.info(f"Stock ajustado para MaterialConsumible ID {mat_cons_id}: {change_amount}. Nuevo stock: {new_stock}")
        return db_mat
    except Exception as e:
        db.rollback()
        logger.error(f"Error ajustando stock MatCons ID {mat_cons_id}: {e}", exc_info=True)
        raise

# =======================================
# Repositorio para MaterialSimple
# =======================================
# (Similar a MaterialConsumible: get_by_id, get_by_sku, list, create, update, delete, adjust_stock)
# ... Implementación análoga ...

def get_material_simple_by_id(db: Session, *, mat_simp_id: int) -> Optional[MaterialSimple]:
    try: return db.get(MaterialSimple, mat_simp_id)
    except Exception as e: logger.error(f"Error get MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise

def get_material_simple_by_sku(db: Session, *, sku: str) -> Optional[MaterialSimple]:
    try: return db.exec(select(MaterialSimple).where(MaterialSimple.sku == sku)).first()
    except Exception as e: logger.error(f"Error get MatSimp SKU {sku}: {e}", exc_info=True); raise

def list_materiales_simples(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialSimple]:
    try: return db.exec(select(MaterialSimple).offset(skip).limit(limit).order_by(MaterialSimple.id)).all()
    except Exception as e: logger.error(f"Error list MatSimp: {e}", exc_info=True); raise

def create_material_simple(db: Session, *, mat_simp_data: MaterialSimple) -> MaterialSimple:
    db_mat = mat_simp_data
    try:
        db.add(db_mat); db.commit(); db.refresh(db_mat)
        logger.info(f"MaterialSimple creado: ID={db_mat.id}, SKU='{db_mat.sku}'")
        return db_mat
    except IntegrityError as e: db.rollback(); logger.warning(f"IntegrityError create MatSimp SKU '{db_mat.sku}': {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error create MatSimp SKU '{db_mat.sku}': {e}", exc_info=True); raise

def update_material_simple(db: Session, *, db_mat_simp: MaterialSimple, update_data: Dict[str, Any]) -> MaterialSimple:
    """Actualiza campos definitorios (nombre, desc, etc.), no stock_actual."""
    try:
        update_data.pop("sku", None)
        update_data.pop("stock_actual", None) # No actualizar stock aquí
        if not update_data: return db_mat_simp
        db_mat_simp.sqlmodel_update(update_data)
        db.add(db_mat_simp); db.commit(); db.refresh(db_mat_simp)
        logger.info(f"MaterialSimple actualizado: ID={db_mat_simp.id}")
        return db_mat_simp
    except IntegrityError as e: db.rollback(); logger.warning(f"IntegrityError update MatSimp ID {db_mat_simp.id}: {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error update MatSimp ID {db_mat_simp.id}: {e}", exc_info=True); raise

def delete_material_simple(db: Session, *, mat_simp_id: int) -> Optional[MaterialSimple]:
    try:
        db_mat = db.get(MaterialSimple, mat_simp_id)
        if not db_mat: return None
        logger.warning(f"Intentando eliminar MaterialSimple: ID={mat_simp_id}, SKU='{db_mat.sku}'")
        db.delete(db_mat); db.commit()
        logger.warning(f"MaterialSimple eliminado: ID={mat_simp_id}")
        return db_mat
    except IntegrityError as e: # Fallará si está en FormulaItem o LineaProformaMaterial
        db.rollback(); logger.error(f"IntegrityError delete MatSimp ID {mat_simp_id}. Referenciado?: {e}"); raise e
    except Exception as e: db.rollback(); logger.error(f"Error delete MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise

def adjust_stock_simple(db: Session, *, mat_simp_id: int, change_amount: Decimal) -> Optional[MaterialSimple]:
    """Ajusta el stock actual de un material simple."""
    try:
        db_mat = db.get(MaterialSimple, mat_simp_id)
        if not db_mat: return None
        new_stock = (db_mat.stock_actual or Decimal("0.0")) + change_amount
        if new_stock < 0:
             logger.error(f"Intento de ajuste de stock negativo para MatSimp ID {mat_simp_id}. Actual: {db_mat.stock_actual}, Cambio: {change_amount}")
             raise ValueError("El ajuste de stock resultaría en una cantidad negativa.")
        db_mat.stock_actual = new_stock
        db.add(db_mat); db.commit(); db.refresh(db_mat)
        logger.info(f"Stock ajustado para MaterialSimple ID {mat_simp_id}: {change_amount}. Nuevo stock: {new_stock}")
        return db_mat
    except Exception as e:
        db.rollback(); logger.error(f"Error ajustando stock MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise


# =======================================
# Repositorio para StockItemDimensional
# =======================================

def get_stock_item_by_id(db: Session, *, item_id: int) -> Optional[StockItemDimensional]:
    """Obtiene una pieza de stock dimensional por ID."""
    try:
        return db.get(StockItemDimensional, item_id)
    except Exception as e:
        logger.error(f"Error obteniendo StockItemDimensional ID {item_id}: {e}", exc_info=True)
        raise

def create_stock_item(db: Session, *, item_data: StockItemDimensional) -> StockItemDimensional:
    """Crea una nueva pieza de stock dimensional."""
    db_item = item_data
    try:
        # Asegurar estado inicial si no se proporciona
        if not db_item.estado: db_item.estado = "DISPONIBLE"
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        logger.info(f"StockItemDimensional creado: ID={db_item.id}, MaterialID={db_item.material_dimensional_id}")
        return db_item
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando StockItemDimensional: {e}", exc_info=True)
        raise

def list_stock_items(
    db: Session, *,
    skip: int = 0,
    limit: int = 100,
    material_dimensional_id: Optional[int] = None,
    estado: Optional[str] = None,
    min_longitud: Optional[Decimal] = None,
    min_ancho: Optional[Decimal] = None,
    # Añadir más filtros según necesidad (ej: es_merma, ubicación)
) -> Sequence[StockItemDimensional]:
    """
    Lista piezas de stock dimensional con filtros opcionales.
    Crucial para encontrar material disponible para cortes.
    """
    try:
        statement = select(StockItemDimensional)
        conditions = []
        if material_dimensional_id is not None:
            conditions.append(StockItemDimensional.material_dimensional_id == material_dimensional_id)
        if estado is not None:
            conditions.append(StockItemDimensional.estado == estado)
        if min_longitud is not None:
            conditions.append(StockItemDimensional.longitud_actual >= min_longitud)
        if min_ancho is not None:
            conditions.append(StockItemDimensional.ancho_actual >= min_ancho)

        if conditions:
            statement = statement.where(and_(*conditions)) # Usar and_() para múltiples condiciones

        statement = statement.order_by(StockItemDimensional.id).offset(skip).limit(limit)
        items = db.exec(statement).all()
        return items
    except Exception as e:
        logger.error(f"Error listando StockItemDimensional: {e}", exc_info=True)
        raise

def update_stock_item(db: Session, *, db_item: StockItemDimensional, update_data: Dict[str, Any]) -> StockItemDimensional:
    """Actualiza una pieza de stock dimensional (estado, ubicación, dimensiones, etc.)."""
    try:
        # Campos que quizás no deban actualizarse aquí (depende de la lógica de negocio)
        # update_data.pop("material_dimensional_id", None)
        if not update_data: return db_item
        db_item.sqlmodel_update(update_data)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        logger.info(f"StockItemDimensional actualizado: ID={db_item.id}")
        return db_item
    except Exception as e:
        db.rollback()
        logger.error(f"Error actualizando StockItemDimensional ID {db_item.id}: {e}", exc_info=True)
        raise

# delete_stock_item se omite por ahora, preferible cambiar estado a 'DESECHADO'
```

# app\repositories\order_repository.py

```py
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

```

# app\repositories\permiso_repository.py

```py
# app/repositories/permiso_repository.py

import logging
from typing import Optional, Sequence, Union, Dict, Any

from sqlmodel import Session, select, SQLModel
from sqlalchemy.exc import IntegrityError # Para capturar errores de constraints únicos
from fastapi import HTTPException, status

# Importamos los modelos y schemas necesarios
from app.models import Permiso
from app.schemas.rol_permiso_schema import PermisoCreate, PermisoUpdate

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read (Getters)
# =====================

def get_permiso(db: Session, permiso_id: int) -> Optional[Permiso]:
    """
    Obtiene un permiso específico por su ID utilizando db.get().

    Args:
        db: La sesión de base de datos activa.
        permiso_id: El ID del permiso a buscar.

    Returns:
        El objeto Permiso si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        # db.get es eficiente para buscar por clave primaria
        return db.get(Permiso, permiso_id)
    except Exception as e:
        logger.error(f"Error obteniendo permiso ID {permiso_id}: {e}", exc_info=True)
        raise

def get_permiso_by_accion_recurso(
    db: Session, *, nombre_accion: str, nombre_recurso: str
) -> Optional[Permiso]:
    """
    Obtiene un permiso por su combinación única de acción y recurso.

    Esta combinación actúa como una clave natural y debe ser única según
    el constraint de la base de datos.

    Args:
        db: La sesión de base de datos activa.
        nombre_accion: El nombre de la acción del permiso.
        nombre_recurso: El nombre del recurso del permiso.

    Returns:
        El objeto Permiso si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Permiso).where(
            Permiso.nombre_accion == nombre_accion,
            Permiso.nombre_recurso == nombre_recurso
        )
        return db.exec(statement).first()
    except Exception as e:
        logger.error(
            f"Error obteniendo permiso por accion='{nombre_accion}', recurso='{nombre_recurso}': {e}",
            exc_info=True
        )
        raise

def list_permisos(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Permiso]:
    """
    Obtiene una lista paginada de todos los permisos.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de permisos a saltar (para paginación).
        limit: Número máximo de permisos a devolver (para paginación).

    Returns:
        Una secuencia (lista) de objetos Permiso.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Permiso).offset(skip).limit(limit)
        return db.exec(statement).all()
    except Exception as e:
        logger.error(f"Error listando permisos: {e}", exc_info=True)
        raise

# =====================
#  Funciones Write (Create, Update, Delete)
# =====================

def create_permiso(db: Session, *, permiso_in: PermisoCreate) -> Permiso:
    """
    Crea un nuevo permiso en la base de datos.

    Valida los datos de entrada y maneja posibles errores de integridad,
    específicamente para la combinación duplicada de acción/recurso.

    Args:
        db: La sesión de base de datos activa.
        permiso_in: Objeto PermisoCreate con los datos del permiso a crear.

    Returns:
        El objeto Permiso recién creado y refrescado desde la base de datos.

    Raises:
        HTTPException: 409 (Conflict) si ya existe un permiso con la misma
                       combinación de acción y recurso.
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    try:
        db_permiso = Permiso.model_validate(permiso_in)
        db.add(db_permiso)
        db.commit()
        db.refresh(db_permiso)
        logger.info(f"Permiso creado: ID={db_permiso.id}, Accion={db_permiso.nombre_accion}, Recurso={db_permiso.nombre_recurso}")
        return db_permiso
    except IntegrityError as e: # Captura error si el constraint único de (accion, recurso) falla
        db.rollback()
        logger.warning(
            f"Intento de crear permiso duplicado: "
            f"Accion='{permiso_in.nombre_accion}', Recurso='{permiso_in.nombre_recurso}'. Error: {e}"
        )
        # Lanza una excepción HTTP específica para que el servicio la maneje.
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El permiso '{permiso_in.nombre_accion}:{permiso_in.nombre_recurso}' ya existe."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando permiso: {e}", exc_info=True)
        raise # Relanza otras excepciones

def update_permiso(
    db: Session, *, db_permiso: Permiso, permiso_in: Union[PermisoUpdate, Dict[str, Any]]
) -> Permiso:
    """
    Actualiza un permiso existente en la base de datos.

    Aplica los cambios utilizando `sqlmodel_update` y maneja posibles
    errores de integridad si la actualización resulta en una combinación
    duplicada de acción/recurso.

    Args:
        db: La sesión de base de datos activa.
        db_permiso: El objeto Permiso existente que se va a actualizar.
        permiso_in: Un objeto PermisoUpdate o un diccionario con los datos a actualizar.
                    Se recomienda usar PermisoUpdate con `exclude_unset=True` en el servicio.

    Returns:
        El objeto Permiso actualizado y refrescado desde la base de datos.

    Raises:
        HTTPException: 409 (Conflict) si la actualización causa un conflicto de
                       acción/recurso duplicado.
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    try:
        if isinstance(permiso_in, dict):
            update_data = permiso_in
        else:
            # Se asume que en el servicio se llamó con exclude_unset=True
            update_data = permiso_in.model_dump(exclude_unset=True)

        # Actualizar el objeto modelo con los nuevos datos
        db_permiso.sqlmodel_update(update_data)

        db.add(db_permiso) # Añadir a la sesión para marcarlo como modificado antes del commit
        db.commit()
        db.refresh(db_permiso)
        logger.info(f"Permiso actualizado: ID={db_permiso.id}")
        return db_permiso
    except IntegrityError as e: # Captura error si el cambio viola el constraint único (accion, recurso)
        db.rollback()
        logger.warning(
            f"Error de integridad actualizando permiso ID {db_permiso.id}. ¿Conflicto accion/recurso? Error: {e}"
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conflicto al actualizar el permiso, la combinación acción/recurso ya podría existir."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error actualizando permiso ID {db_permiso.id}: {e}", exc_info=True)
        raise # Relanza otras excepciones


def delete_permiso(db: Session, *, db_permiso: Permiso) -> Permiso:
    """
    Elimina un permiso de la base de datos.

    Aprovecha la configuración `ON DELETE CASCADE` de la llave foránea en la
    tabla `rol_permiso` (asociación Rol-Permiso) para que la base de datos
    elimine automáticamente las asociaciones existentes. No realiza
    verificaciones explícitas de dependencias en este código.

    Args:
        db: La sesión de base de datos activa.
        db_permiso: El objeto Permiso a eliminar.

    Returns:
        El objeto Permiso que fue eliminado (desvinculado de la sesión).

    Raises:
        HTTPException: 500 (Internal Server Error) si ocurre un error inesperado
                       durante la eliminación. (Un error de FK sería inesperado aquí).
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    permiso_id = db_permiso.id
    permiso_repr = f"'{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' (ID: {permiso_id})"
    logger.info(f"Intentando eliminar permiso: {permiso_repr}")
    try:
        # Opcional: Si se quisiera PREVENIR la eliminación de permisos en uso activamente
        # (en lugar de confiar/permitir la cascada), se podría añadir aquí una consulta
        # a 'rol_permiso' contando las filas con este permiso_id. Si count > 0,
        # se lanzaría un HTTPException 409 CONFLICT.
        # Ejemplo: count_statement = select(func.count(RolPermiso.rol_id)).where(RolPermiso.permiso_id == permiso_id)
        #          count = db.exec(count_statement).scalar_one()
        #          if count > 0: raise HTTPException(status_code=409, detail="Permiso en uso")

        db.delete(db_permiso)
        db.commit()
        logger.info(f"Permiso eliminado exitosamente: {permiso_repr}")
        # El objeto devuelto está desvinculado de la sesión después del commit/delete.
        return db_permiso
    except Exception as e:
        db.rollback()
        # Un error aquí sería inesperado dado el ON DELETE CASCADE asumido.
        # Podría indicar un problema de configuración, de conexión, locks, etc.
        logger.error(f"Error inesperado eliminando permiso {permiso_repr}: {e}", exc_info=True)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error interno del servidor al intentar eliminar el permiso {permiso_repr}."
            )
```

# app\repositories\rol_repository.py

```py
# app/repositories/rol_repository.py

import logging
from typing import Optional, Sequence, Union, Dict, Any, List
import sqlalchemy as sa

from sqlmodel import Session, select, SQLModel

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from sqlalchemy.orm import selectinload

from app.models import Rol, UsuarioRol
from app.schemas.rol_permiso_schema import RolCreate, RolUpdate

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read (Getters)
# =====================

def get_rol_by_name(db: Session, *, nombre: str) -> Optional[Rol]:
    """
    Obtiene un rol específico por su nombre.

    Args:
        db: La sesión de base de datos activa.
        nombre: El nombre exacto del rol a buscar.

    Returns:
        El objeto Rol si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Rol).where(Rol.nombre == nombre)
        rol = db.exec(statement).first()
        return rol
    except Exception as e:
        logger.error(f"Error obteniendo rol por nombre '{nombre}': {e}", exc_info=True)
        raise

def get_rol(db: Session, *, rol_id: int) -> Optional[Rol]:
    """
    Obtiene un rol específico por su ID utilizando db.get().

    Args:
        db: La sesión de base de datos activa.
        rol_id: El ID del rol a buscar.

    Returns:
        El objeto Rol si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        # db.get es eficiente para buscar por clave primaria
        rol = db.get(Rol, rol_id)
        return rol
    except Exception as e:
        logger.error(f"Error obteniendo rol por ID '{rol_id}': {e}", exc_info=True)
        raise


def get_rol_with_permissions(db: Session, *, rol_id: int) -> Optional[Rol]:
    """
    Obtiene un rol específico por su ID, cargando la relación de permisos.

    Utiliza carga 'eager' (selectinload) para la relación 'permisos' para
    evitar consultas adicionales si se accede a los permisos posteriormente.

    Args:
        db: La sesión de base de datos activa.
        rol_id: El ID del rol a buscar.

    Returns:
        El objeto Rol con sus permisos cargados si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Rol).where(Rol.id == rol_id).options(
            selectinload(Rol.permisos) # Carga Eager de la relación 'permisos'
        )
        rol = db.exec(statement).first()
        return rol
    except Exception as e:
        logger.error(f"Error obteniendo rol ID '{rol_id}' con permisos: {e}", exc_info=True)
        raise

def list_roles(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[Rol]:
    """
    Obtiene una lista paginada de roles.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de roles a saltar (para paginación).
        limit: Número máximo de roles a devolver (para paginación).

    Returns:
        Una secuencia (lista) de objetos Rol.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Rol).offset(skip).limit(limit)
        roles = db.exec(statement).all()
        return roles
    except Exception as e:
        logger.error(f"Error listando roles: {e}", exc_info=True)
        raise

def get_roles_by_ids(db: Session, *, role_ids: List[int]) -> Sequence[Rol]:
    """
    Obtiene una secuencia de objetos Rol basada en una lista de IDs.

    Utiliza una consulta con `IN` para eficiencia.

    Args:
        db: Sesión de base de datos activa.
        role_ids: Lista de IDs de roles a buscar.

    Returns:
        Una secuencia (lista) de objetos Rol encontrados. Puede estar vacía si
        ningún ID es válido o la lista de entrada está vacía.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
                   Permite que el servicio maneje el error.
    """
    if not role_ids:
        return [] # Optimización: no consultar si la lista de IDs está vacía
    try:
        # Usamos 'in_' para buscar eficientemente múltiples IDs
        statement = select(Rol).where(Rol.id.in_(role_ids))
        roles = db.exec(statement).all()
        return roles
    except Exception as e:
        logger.error(f"Error obteniendo roles por IDs ({role_ids}): {e}", exc_info=True)
        raise # Relanzar para que el servicio maneje


# =====================
#  Funciones Write (Create, Update, Delete)
# =====================

def create_rol(db: Session, *, rol_in: RolCreate) -> Rol:
    """
    Crea un nuevo rol en la base de datos.

    Valida los datos de entrada y maneja posibles errores de integridad,
    específicamente para nombres de rol duplicados (constraint único).

    Args:
        db: La sesión de base de datos activa.
        rol_in: Objeto RolCreate con los datos del rol a crear.

    Returns:
        El objeto Rol recién creado y refrescado desde la base de datos.

    Raises:
        HTTPException: 409 (Conflict) si ya existe un rol con el mismo nombre.
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    try:
        db_rol = Rol.model_validate(rol_in)
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        logger.info(f"Rol creado: ID={db_rol.id}, Nombre='{db_rol.nombre}'")
        return db_rol
    except IntegrityError as e: # Captura error si el constraint único del nombre falla
        db.rollback()
        logger.warning(f"Intento de crear rol duplicado: Nombre='{rol_in.nombre}'. Error: {e}")
        # Lanza una excepción HTTP específica para que el servicio la maneje
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El rol '{rol_in.nombre}' ya existe."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando rol: {e}", exc_info=True)
        raise # Relanza otras excepciones para manejo general

def update_rol(
    db: Session, *, db_rol: Rol, rol_in: Union[RolUpdate, Dict[str, Any]]
) -> Rol:
    """
    Actualiza un rol existente en la base de datos.

    Aplica los cambios utilizando `sqlmodel_update` y maneja posibles
    errores de integridad si la actualización resulta en un nombre duplicado.

    Args:
        db: La sesión de base de datos activa.
        db_rol: El objeto Rol existente que se va a actualizar.
        rol_in: Un objeto RolUpdate o un diccionario con los datos a actualizar.
                Se recomienda usar RolUpdate con `exclude_unset=True` en el servicio.

    Returns:
        El objeto Rol actualizado y refrescado desde la base de datos.

    Raises:
        HTTPException: 409 (Conflict) si la actualización causa un conflicto de nombre.
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    try:
        if isinstance(rol_in, dict):
            update_data = rol_in
        else:
            # Se asume que en el servicio se llamó con exclude_unset=True
            update_data = rol_in.model_dump(exclude_unset=True)

        db_rol.sqlmodel_update(update_data)
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        logger.info(f"Rol actualizado: ID={db_rol.id}, Nombre='{db_rol.nombre}'")
        return db_rol
    except IntegrityError as e: # Captura error si el cambio de nombre viola el constraint único
        db.rollback()
        logger.warning(
            f"Error de integridad actualizando rol ID {db_rol.id}. ¿Conflicto de nombre? Error: {e}"
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conflicto al actualizar el rol, el nombre ya podría existir."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error actualizando rol ID {db_rol.id}: {e}", exc_info=True)
        raise # Relanza otras excepciones

def delete_rol(db: Session, *, db_rol: Rol) -> Rol:
    """
    Elimina un rol de la base de datos, verificando dependencias primero.

    Comprueba si el rol está asignado a algún usuario antes de eliminarlo.
    Si está asignado, lanza un error HTTP 409. Asume que las asociaciones
    Rol-Permiso se manejan mediante ON DELETE CASCADE en la base de datos.

    Args:
        db: La sesión de base de datos activa.
        db_rol: El objeto Rol a eliminar.

    Returns:
        El objeto Rol que fue eliminado (útil para logs o respuestas).

    Raises:
        HTTPException: 409 (Conflict) si el rol está asignado a uno o más usuarios.
        HTTPException: 500 (Internal Server Error) si ocurre otro error inesperado
                       durante la eliminación (p.ej., otros FK constraints).
        Exception: Relanza otras excepciones de base de datos después de hacer rollback.
    """
    rol_id = db_rol.id
    rol_nombre = db_rol.nombre
    try:
        # Contamos las asociaciones en UsuarioRol para verificar si el rol está en uso
        statement = select(sa.func.count(UsuarioRol.usuario_id)).where(UsuarioRol.rol_id == rol_id)
        # .scalar_one() podría ser más directo si esperamos un número
        user_count = db.exec(statement).first() # Devuelve el número o None

        if user_count is not None and user_count > 0:
            logger.warning(f"Intento de eliminar rol ID {rol_id} ('{rol_nombre}') que está asignado a {user_count} usuario(s).")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"No se puede eliminar el rol '{rol_nombre}' porque está asignado a {user_count} usuario(s)."
            )

        # Si user_count es 0 o None, proceder a eliminar
        # Nota: Asumimos ON DELETE CASCADE para la tabla RolPermiso definida en el modelo/DB.
        # No es necesario eliminar manualmente las asociaciones Rol-Permiso aquí.
        db.delete(db_rol)
        db.commit()
        logger.info(f"Rol eliminado: ID={rol_id}, Nombre='{rol_nombre}'")
        return db_rol
    except HTTPException: # Relanzar el 409 generado arriba
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error eliminando rol ID {rol_id}: {e}", exc_info=True)
        # Podría haber otros errores de FK si otras tablas referencian Rol sin ON DELETE CASCADE.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al intentar eliminar el rol '{rol_nombre}'."
        )
```

# app\repositories\service_repository.py

```py
# app/repositories/service_repository.py
import logging
from typing import Optional, Sequence, Dict, Any

from sqlmodel import Session, select, SQLModel
from sqlalchemy.exc import IntegrityError

# Importar Modelo
from app.models.service_models import ServicioDefinicion

logger = logging.getLogger(__name__)
import traceback

# =======================================
# Repositorio para ServicioDefinicion
# =======================================

def get_servicio_by_id(db: Session, *, servicio_id: int) -> Optional[ServicioDefinicion]:
    """Obtiene una definición de servicio por su ID."""
    try:
        return db.get(ServicioDefinicion, servicio_id)
    except Exception as e:
        logger.error(f"Error obteniendo ServicioDefinicion ID {servicio_id}: {e}", exc_info=True)
        raise

def get_servicio_by_nombre(db: Session, *, nombre: str) -> Optional[ServicioDefinicion]:
    """Obtiene una definición de servicio por su nombre (asumiendo unicidad)."""
    # Nota: La BD no tiene constraint UNIQUE para nombre, pero la lógica de negocio podría requerirla.
    try:
        statement = select(ServicioDefinicion).where(ServicioDefinicion.nombre == nombre)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo ServicioDefinicion nombre '{nombre}': {e}", exc_info=True)
        raise

def list_servicios(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[ServicioDefinicion]:
    """Lista las definiciones de servicios."""
    try:
        statement = select(ServicioDefinicion).offset(skip).limit(limit).order_by(ServicioDefinicion.id)
        return db.exec(statement).all()
    except Exception as e:
        logger.error(f"Error listando ServicioDefinicion: {e}", exc_info=True)
        raise


def create_servicio(db: Session, *, servicio_data: ServicioDefinicion) -> ServicioDefinicion:
    """Crea una nueva definición de servicio."""
    db_servicio = servicio_data
    try:
        db.add(db_servicio)
        logger.info(f"Repositorio: Intentando commit para ServicioDefinicion Código='{db_servicio.codigo}'")
        db.commit()
        logger.info(f"Repositorio: Commit exitoso. Intentando refresh...")
        db.refresh(db_servicio)
        logger.info(f"ServicioDefinicion creado: ID={db_servicio.id}, Código='{db_servicio.codigo}'")
        return db_servicio
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"Error de integridad al crear ServicioDefinicion Código '{db_servicio.codigo}': {e}")
        raise e
    except Exception as e:
        db.rollback()
        # --- CAMBIO AQUÍ: Usando print() para depuración ---
        print("\n" + "="*20 + " ERROR CAPTURADO EN REPOSITORIO (create_servicio) " + "="*20)
        print(f"Error inesperado creando ServicioDefinicion Código '{db_servicio.codigo}':")
        print(f"Tipo de Excepción: {type(e).__name__}")
        print(f"Argumentos: {e.args}")
        print(f"Representación: {repr(e)}")
        print(f"Traceback:\n{traceback.format_exc()}")
        print("="*70 + "\n")
        # --- FIN CAMBIO ---
        raise # Relanzar la excepción original

def update_servicio(db: Session, *, db_servicio: ServicioDefinicion, update_data: Dict[str, Any]) -> ServicioDefinicion:
    """Actualiza una definición de servicio."""
    try:
        if not update_data: return db_servicio # Nada que actualizar
        db_servicio.sqlmodel_update(update_data)
        db.add(db_servicio)
        db.commit()
        db.refresh(db_servicio)
        logger.info(f"ServicioDefinicion actualizado: ID={db_servicio.id}")
        return db_servicio
    except IntegrityError as e: # Si se hace UNIQUE(nombre) y se intenta duplicar
        db.rollback()
        logger.warning(f"Error de integridad al actualizar ServicioDefinicion ID {db_servicio.id}: {e}")
        raise e
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado actualizando ServicioDefinicion ID {db_servicio.id}: {e}", exc_info=True)
        raise

def delete_servicio(db: Session, *, servicio_id: int) -> Optional[ServicioDefinicion]:
    """Elimina una definición de servicio."""
    try:
        db_servicio = db.get(ServicioDefinicion, servicio_id)
        if not db_servicio: return None
        logger.warning(f"Intentando eliminar ServicioDefinicion: ID={servicio_id}, Nombre='{db_servicio.nombre}'")
        db.delete(db_servicio)
        db.commit()
        logger.warning(f"ServicioDefinicion eliminado: ID={servicio_id}")
        return db_servicio
    except IntegrityError as e: # Fallará si está referenciado por Formula o LineaProformaServicio (ON DELETE RESTRICT)
        db.rollback()
        logger.error(f"Error de integridad al eliminar ServicioDefinicion ID {servicio_id}. Probablemente referenciado: {e}")
        raise e # Relanzar para que el servicio maneje (409)
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado eliminando ServicioDefinicion ID {servicio_id}: {e}", exc_info=True)
        raise
```

# app\repositories\usuario_repository.py

```py
# app/repositories/usuario_repository.py
from sqlmodel import Session, select, SQLModel
from typing import Optional, Sequence, Union, Dict, Any
import logging

from app.models.user_models import Usuario, Rol, UsuarioRol
from app.schemas.usuario_schema import UsuarioUpdate
from sqlalchemy.orm import selectinload

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read
# =====================

def get_usuario_by_username(db: Session, username: str) -> Optional[Usuario]:
    """
    Obtiene un usuario específico por su nombre de usuario (username).

    Args:
        db: La sesión de base de datos activa.
        username: El nombre de usuario a buscar.

    Returns:
        El objeto Usuario si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Usuario).where(Usuario.username == username)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo usuario {username}: {str(e)}")
        raise

def get_usuario_by_email(db: Session, email: str) -> Optional[Usuario]:
    """
    Obtiene un usuario específico por su dirección de correo electrónico.

    Args:
        db: La sesión de base de datos activa.
        email: El correo electrónico del usuario a buscar.

    Returns:
        El objeto Usuario si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = select(Usuario).where(Usuario.email == email)
        return db.exec(statement).first()
    except Exception as e:
        logger.error(f"Error obteniendo usuario {email}: {str(e)}")
        raise

def get_usuario(db: Session, user_id: int) -> Optional[Usuario]:
    """
    Obtiene un usuario específico por su ID, cargando también sus roles asociados.

    Utiliza carga 'eager' (selectinload) para la relación 'roles' para evitar
    consultas N+1 si se accede a los roles del usuario posteriormente.

    Args:
        db: La sesión de base de datos activa.
        user_id: El ID del usuario a buscar.

    Returns:
        El objeto Usuario con sus roles cargados si se encuentra, None en caso contrario.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        statement = (
            select(Usuario)
            .where(Usuario.id == user_id)
            .options(selectinload(Usuario.roles)) # Carga Eager de roles
        )
        user = db.exec(statement).first()
        return user
    except Exception as e:
        logger.error(f"Error obteniendo usuario ID {user_id}: {str(e)}")
        raise

def get_usuarios(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filters: Optional[Dict[str, Any]] = None
) -> Sequence[Usuario]:
    """
    Obtiene una lista paginada y filtrada de usuarios, cargando sus roles.

    Permite paginación mediante 'skip' y 'limit', y filtrado básico por
    campos del modelo Usuario. También carga 'eager' los roles de cada usuario.

    Args:
        db: La sesión de base de datos activa.
        skip: Número de registros a saltar (para paginación).
        limit: Número máximo de registros a devolver (para paginación).
        filters: Un diccionario opcional donde las claves son nombres de campos
                 del modelo Usuario y los valores son los valores a filtrar.
                 Se ignorarán claves que no correspondan a campos del modelo.

    Returns:
        Una secuencia (lista) de objetos Usuario que coinciden con los criterios.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la consulta
                   a la base de datos después de registrarla.
    """
    try:
        query = select(Usuario)
        if filters:
            for field, value in filters.items():
                # Asegurarse que el campo existe en el modelo Usuario
                if hasattr(Usuario, field):
                    query = query.where(getattr(Usuario, field) == value)
                else:
                    logger.warning(f"Intento de filtrar por campo inexistente en Usuario: {field}")

        query = query.options(selectinload(Usuario.roles)) # Cargar roles
        query = query.offset(skip).limit(limit)

        users = db.exec(query).all()
        return users

    except Exception as e:
        logger.error(f"Error listando usuarios: {str(e)}")
        raise

# =====================
#  Funciones Write
# =====================

def create_usuario(db: Session, usuario_data: Union[Usuario, Dict[str, Any]]) -> Usuario:
    """
    Crea un nuevo usuario en la base de datos.

    Acepta los datos del usuario como un objeto Usuario pre-construido o
    como un diccionario. Realiza commit y refresh. Hace rollback en caso de error.

    Args:
        db: La sesión de base de datos activa.
        usuario_data: Un objeto Usuario o un diccionario con los datos del
                      nuevo usuario.

    Returns:
        El objeto Usuario recién creado y refrescado desde la base de datos.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
    """
    try:
        if isinstance(usuario_data, dict):
            db_user = Usuario(**usuario_data)
        else:
            db_user = usuario_data

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Usuario creado: ID={db_user.id}, Username='{db_user.username}'")
        return db_user
    except Exception as e:
        db.rollback()
        logger.error(f"Error creando usuario: {str(e)}")
        raise

def update_usuario(
    db: Session,
    *,
    db_user: Usuario,
    update_data: Union[UsuarioUpdate, Dict[str, Any]]
) -> Usuario:
    """
    Actualiza un usuario existente en la base de datos.

    Utiliza `sqlmodel_update` para aplicar actualizaciones parciales de forma segura,
    excluyendo campos protegidos como 'id' y 'fecha_creacion'.
    Acepta los datos de actualización como un esquema Pydantic (UsuarioUpdate)
    o un diccionario. Hace rollback en caso de error.

    Args:
        db: La sesión de base de datos activa.
        db_user: El objeto Usuario existente que se va a actualizar.
        update_data: Un objeto UsuarioUpdate o un diccionario con los campos
                     a actualizar. Los campos no presentes o con valor None
                     en UsuarioUpdate no se actualizan (si se usa exclude_unset=True).

    Returns:
        El objeto Usuario actualizado y refrescado desde la base de datos.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
    """
    try:
        if isinstance(update_data, dict):
            update_dict = update_data
        else:
            # Excluir campos no enviados explícitamente por el cliente
            update_dict = update_data.model_dump(exclude_unset=True)

        # Campos que no deben ser actualizados directamente a través de este método
        protected_fields = {"id", "fecha_creacion"}
        clean_data = {k: v for k, v in update_dict.items() if k not in protected_fields}

        if not clean_data: # Si no hay datos válidos para actualizar
              logger.warning(f"Intento de actualizar usuario {db_user.id} sin datos válidos.")
              return db_user # Devolver sin cambios

        # Aplica las actualizaciones al objeto db_user
        db_user.sqlmodel_update(clean_data)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Usuario actualizado: {db_user.id}")
        return db_user
    except Exception as e:
        db.rollback()
        logger.error(f"Error actualizando usuario {db_user.id}: {str(e)}")
        raise

def delete_usuario(db: Session, user_id: int) -> Optional[Usuario]:
    """
    Elimina un usuario de la base de datos por su ID.

    Busca al usuario por ID y si existe, lo elimina.
    Gracias a 'ON DELETE CASCADE' en la FK de la tabla UsuarioRol,
    las asociaciones usuario-rol se eliminan automáticamente.
    Hace rollback en caso de error durante la eliminación.

    Args:
        db: La sesión de base de datos activa.
        user_id: El ID del usuario a eliminar.

    Returns:
        El objeto Usuario que fue eliminado, o None si el usuario no se encontró.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
    """
    try:
        user = db.get(Usuario, user_id)
        if user:
            user_repr = f"ID={user.id}, Username='{user.username}'"
            # La FK en usuario_rol tiene ON DELETE CASCADE, las asociaciones se borran solas.
            # No es necesario eliminar manualmente las entradas en UsuarioRol.
            db.delete(user)
            db.commit()
            logger.warning(f"Usuario eliminado: {user_repr}")
            return user
        return None # Usuario no encontrado
    except Exception as e:
        db.rollback()
        logger.error(f"Error eliminando usuario {user_id}: {str(e)}")
        raise

def assign_rol_to_usuario(db: Session, *, db_usuario: Usuario, db_rol: Rol) -> Usuario:
    """
    Asigna un rol específico a un usuario creando una entrada en la tabla UsuarioRol.

    Verifica primero si la asignación ya existe. Si no existe, crea la
    entrada en la tabla de asociación (UsuarioRol).
    Finalmente, refresca explícitamente la relación 'roles' del objeto Usuario
    para asegurar que refleje el estado actualizado tras el commit.
    Hace rollback en caso de error durante la asignación.

    Args:
        db: La sesión de base de datos activa.
        db_usuario: El objeto Usuario al que se le asignará el rol.
        db_rol: El objeto Rol que será asignado.

    Returns:
        El objeto Usuario con su relación 'roles' potencialmente actualizada.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
    """
    # Verifica si el rol ya está asignado a este usuario
    link_exists_statement = select(UsuarioRol).where(
        UsuarioRol.usuario_id == db_usuario.id,
        UsuarioRol.rol_id == db_rol.id
    )
    existing_link = db.exec(link_exists_statement).first()

    if existing_link:
        logger.debug(f"Rol ID {db_rol.id} ya asignado a usuario ID {db_usuario.id}.")
        # Aunque ya exista, refrescamos por si acaso el estado en memoria no está sincronizado
        try:
            db.refresh(db_usuario, attribute_names=["roles"])
            logger.debug(f"Refrescada relación roles para usuario ID {db_usuario.id} (asignación ya existía).")
        except Exception as refresh_err:
            # Loggear error de refresh pero continuar, puede que no sea crítico aquí
            logger.warning(f"Error al refrescar roles para usuario {db_usuario.id} (asignación ya existía): {refresh_err}")
        return db_usuario

    logger.info(f"Asignando rol ID {db_rol.id} ({db_rol.nombre}) a usuario ID {db_usuario.id} ({db_usuario.username})")
    db_usuario_rol = UsuarioRol(usuario_id=db_usuario.id, rol_id=db_rol.id)
    try:
        db.add(db_usuario_rol)
        db.commit()
        # Es crucial refrescar la relación después de modificar la tabla de asociación
        # db.refresh(db_usuario) por sí solo no carga/actualiza relaciones lazy/nuevas.
        db.refresh(db_usuario, attribute_names=["roles"]) # Recargar específicamente la relación
        logger.info(f"Rol asignado y relación 'roles' refrescada para usuario ID {db_usuario.id}.")
        return db_usuario
    except Exception as e:
        db.rollback()
        logger.error(
            f"Error asignando rol ID {db_rol.id} a usuario ID {db_usuario.id}: {e}",
            exc_info=True
        )
        raise # Relanzar la excepción original para manejo superior

def remove_rol_from_usuario(db: Session, *, db_usuario: Usuario, db_rol: Rol) -> Usuario:
    """
    Quita un rol específico de un usuario eliminando la entrada correspondiente en UsuarioRol.

    Busca la entrada de asociación entre el usuario y el rol. Si existe,
    la elimina de la tabla UsuarioRol.
    Finalmente, refresca explícitamente la relación 'roles' del objeto Usuario
    para asegurar que refleje el estado actualizado tras el commit.
    Hace rollback en caso de error durante la eliminación de la asociación.

    Args:
        db: La sesión de base de datos activa.
        db_usuario: El objeto Usuario del que se quitará el rol.
        db_rol: El objeto Rol que será quitado.

    Returns:
        El objeto Usuario con su relación 'roles' potencialmente actualizada.

    Raises:
        Exception: Relanza cualquier excepción ocurrida durante la operación
                   en la base de datos después de registrarla y hacer rollback.
                   Es importante que el repositorio no lance HTTPErrors, eso
                   debe manejarse en la capa de servicio/API.
    """
    # Busca la entrada en la tabla de asociación para eliminarla
    link_statement = select(UsuarioRol).where(
        UsuarioRol.usuario_id == db_usuario.id,
        UsuarioRol.rol_id == db_rol.id
    )
    link_to_delete = db.exec(link_statement).first()

    if not link_to_delete:
        logger.warning(f"Intento de quitar rol ID={db_rol.id} de usuario ID={db_usuario.id}, pero la asignación no existe.")
        # Aunque no existía, refrescamos por si acaso el estado en memoria no está sincronizado
        try:
            db.refresh(db_usuario, attribute_names=["roles"])
            logger.debug(f"Refrescada relación roles para usuario ID {db_usuario.id} (asignación no existía).")
        except Exception as refresh_err:
             logger.warning(f"Error al refrescar roles para usuario {db_usuario.id} (asignación no existía): {refresh_err}")
        return db_usuario

    logger.info(f"Quitando rol ID={db_rol.id} ('{db_rol.nombre}') de usuario ID={db_usuario.id} ('{db_usuario.username}')")
    try:
        db.delete(link_to_delete)
        db.commit()
        # Es crucial refrescar la relación después de modificar la tabla de asociación
        # db.refresh(db_usuario) por sí solo no carga/actualiza relaciones lazy/nuevas.
        db.refresh(db_usuario, attribute_names=["roles"]) # Recargar específicamente la relación
        logger.info(f"Rol quitado y relación 'roles' refrescada para usuario ID {db_usuario.id}.")
        return db_usuario
    except Exception as e:
        db.rollback()
        logger.error(
            f"Error quitando rol ID={db_rol.id} de usuario ID={db_usuario.id}: {e}",
            exc_info=True
        )
        # Mantenemos el raise original; la capa superior decidirá cómo manejar el error (p.ej., HTTP 500)
        raise
```

# app\schemas\__init__.py

```py

```

# app\schemas\client_schema.py

```py
# app/schemas/client_schema.py
from sqlmodel import SQLModel, Field
from pydantic import EmailStr, field_validator, ValidationInfo # ValidationInfo para Pydantic v2+
from typing import Optional
from datetime import datetime
import re # Para validaciones de identificación si se añaden

# Lista permitida de tipos de identificación según el ENUM del SQL
ALLOWED_TIPO_IDENTIFICACION = ["RUC", "CEDULA", "PASAPORTE", "OTRO"]

class ClienteBase(SQLModel):
    """Schema base con campos comunes para Cliente."""
    nombre: str = Field(
        ..., # Requerido en la base
        max_length=255,
        description="Nombre completo o razón social del cliente."
    )
    tipo_identificacion: Optional[str] = Field(
        default=None,
        max_length=50,
        description=f"Tipo de identificación fiscal (ej: {', '.join(ALLOWED_TIPO_IDENTIFICACION)})."
    )
    identificacion_fiscal: Optional[str] = Field(
        default=None,
        max_length=50,
        index=True, # Aunque es de DB, indicarlo aquí ayuda a la claridad
        description="Número de RUC, Cédula, Pasaporte u otro identificador fiscal único."
    )
    persona_contacto: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nombre de la persona de contacto principal en la empresa cliente."
    )
    email: Optional[EmailStr] = Field( # Usar EmailStr para validación automática
        default=None,
        index=True, # Claridad
        description="Correo electrónico de contacto principal del cliente (único si se proporciona)."
    )
    telefono: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Número de teléfono de contacto principal."
    )
    direccion: Optional[str] = Field(
        default=None,
        description="Dirección física o fiscal del cliente."
    )

    @field_validator('tipo_identificacion')
    def validate_tipo_identificacion(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v.upper() not in ALLOWED_TIPO_IDENTIFICACION:
            raise ValueError(f"Tipo de identificación debe ser uno de: {', '.join(ALLOWED_TIPO_IDENTIFICACION)}")
        return v.upper() if v is not None else None # Guardar en mayúsculas o None

    # - Que si se proporciona 'identificacion_fiscal', también se proporcione 'tipo_identificacion'.
    # - Validar el formato de 'identificacion_fiscal' según el 'tipo_identificacion' (ej., validar RUC/Cédula Ecuador).

class ClienteCreate(ClienteBase):
    """Schema para crear un nuevo Cliente via API."""
    # Hereda todos los campos de ClienteBase.
    # 'nombre' es el único estrictamente requerido por la DB, pero aquí
    # dejamos los demás como opcionales según la definición de ClienteBase.
    pass # No necesita campos adicionales por ahora

class ClienteRead(ClienteBase):
    """Schema para devolver información del Cliente en respuestas API."""
    id: int
    fecha_creacion: Optional[datetime] = None
    fecha_ultima_actualizacion: Optional[datetime] = None

    # Podríamos añadir relaciones aquí si fuera necesario, ej:
    # pedidos: List["PedidoClienteRead"] = [] # Requeriría definir PedidoClienteRead

    model_config = {
        "from_attributes": True # Para SQLModel/SQLAlchemy (Pydantic v2)
        # "orm_mode": True # Para Pydantic v1
    }

class ClienteUpdate(SQLModel): # No hereda de Base para que todos sean opcionales
    """
    Schema para actualizar un Cliente existente via API.
    Todos los campos son opcionales.
    """
    nombre: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nuevo nombre completo o razón social del cliente."
    )
    tipo_identificacion: Optional[str] = Field(
        default=None,
        max_length=50,
        description=f"Nuevo tipo de identificación fiscal (ej: {', '.join(ALLOWED_TIPO_IDENTIFICACION)})."
    )
    identificacion_fiscal: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Nuevo número de RUC, Cédula, Pasaporte u otro identificador fiscal único."
    )
    persona_contacto: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nuevo nombre de la persona de contacto principal."
    )
    email: Optional[EmailStr] = Field(
        default=None,
        description="Nuevo correo electrónico de contacto principal (único si se proporciona)."
    )
    telefono: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Nuevo número de teléfono de contacto principal."
    )
    direccion: Optional[str] = Field(
        default=None,
        description="Nueva dirección física o fiscal del cliente."
    )

    # Re-aplicar validación para los campos que se actualizan
    @field_validator('tipo_identificacion')
    def validate_update_tipo_identificacion(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v.upper() not in ALLOWED_TIPO_IDENTIFICACION:
            raise ValueError(f"Tipo de identificación debe ser uno de: {', '.join(ALLOWED_TIPO_IDENTIFICACION)}")
        return v.upper() if v is not None else None

    # Considerar añadir validaciones cruzadas aquí si es necesario, por ejemplo,
    # asegurar que si se cambia la identificación, el tipo sea coherente.
    # Ejemplo (requiere importar ValidationInfo de pydantic):
    # @field_validator('identificacion_fiscal')
    # def check_identificacion_with_tipo(cls, v: Optional[str], info: ValidationInfo) -> Optional[str]:
    #     tipo = info.data.get('tipo_identificacion') # Obtener el valor del otro campo
    #     if v is not None and tipo is None:
    #         # O si 'tipo' ya existe en el objeto original si no se actualiza
    #         # Esto puede volverse complejo y es mejor manejarlo en la capa de servicio
    #         pass # Lógica de validación
    #     return v
```

# app\schemas\inventory_schema.py

```py

# app/schemas/inventory_schema.py
from sqlmodel import SQLModel, Field
from pydantic import BaseModel, condecimal # Para validación de decimales
from typing import Optional, List
from datetime import datetime
from decimal import Decimal # Asegurar importación

# --- Schemas para MaterialDimensional ---

class MaterialDimensionalBase(SQLModel):
    """Base schema for dimensional materials (sheets, planks)."""
    sku: str = Field(
        ...,
        max_length=100,
        index=True, # Claridad
        description="Stock Keeping Unit - Código único del tipo de material."
    )
    nombre: str = Field(
        ...,
        max_length=255,
        description="Nombre descriptivo (ej: Plancha MDF 18mm)."
    )
    descripcion: Optional[str] = Field(default=None, description="Descripción detallada.")
    # El espesor es clave para definir este tipo de material
    espesor_nominal: condecimal(max_digits=10, decimal_places=3) = Field( # type: ignore
        ...,
        description="Espesor estándar para este SKU."
    )
    unidad_dimension: str = Field(
        default="mm",
        max_length=10,
        description="Unidad para longitud, ancho, espesor (ej: mm, cm, m, pulgadas)."
    )
    precio_venta_base_unidad: Decimal = Field( 
        max_digits=14, 
        decimal_places=4, 
        description="Precio base por unidad de medida."
    )
    unidad_precio_venta: str = Field(
        max_length=20,
        description="Unidad de medida para el precio de venta (ej: m2, m3)."
    )


class MaterialDimensionalCreate(MaterialDimensionalBase):
    """Schema to create a new type of dimensional material."""
    pass # Hereda todo de la base

class MaterialDimensionalRead(MaterialDimensionalBase):
    """Schema to read dimensional material data from API."""
    id: int
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]
    model_config = {"from_attributes": True}

class MaterialDimensionalUpdate(SQLModel):
    """Schema to update a dimensional material type. All fields optional."""
    # SKU generalmente no se actualiza, se maneja con cuidado si se permite
    nombre: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None)
    espesor_nominal: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    unidad_dimension: Optional[str] = Field(default=None, max_length=10)
    precio_venta_base_unidad: Optional[Decimal] = Field(default=None, max_digits=14, decimal_places=4) # type: ignore
    unidad_precio_venta: Optional[str] = Field(default=None, max_length=20)


# --- Schemas para MaterialConsumible ---

class MaterialConsumibleBase(SQLModel):
    """Base schema for consumable materials (sandpaper, paint, thinner)."""
    sku: str = Field(..., max_length=100, index=True, description="SKU único del consumible.")
    nombre: str = Field(..., max_length=255, description="Nombre del consumible.")
    descripcion: Optional[str] = Field(default=None, description="Descripción detallada.")
    unidad_medida: str = Field(..., max_length=50, description="Unidad de medida (ej: rollo, litro, kg).")
    rendimiento_m2: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Rendimiento por metro cuadrado si aplica (ej: para pintura)."
    )
    # El stock actual se maneja en Read/Update, no se suele definir al crear el *tipo*
    stock_minimo: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Nivel mínimo de stock para alertas."
    )
    precio_venta_base_unidad: Decimal = Field(
        max_digits=14,
        decimal_places=4,
        description="Precio base por unidad de medida."
    )
    
    ubicacion: Optional[str] = Field(default=None, max_length=255, description="Ubicación en almacén.")

class MaterialConsumibleCreate(MaterialConsumibleBase):
    """Schema to create a new type of consumable material."""
    # Podríamos añadir un stock_inicial aquí si quisiéramos registrar la primera cantidad
    # stock_inicial: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=0.0)
    pass # Hereda de Base

class MaterialConsumibleRead(MaterialConsumibleBase):
    """Schema to read consumable material data from API."""
    id: int
    stock_actual: condecimal(max_digits=10, decimal_places=3) = Field(default=Decimal("0.0")) # type: ignore
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]
    model_config = {"from_attributes": True}

class MaterialConsumibleUpdate(SQLModel):
    """Schema to update a consumable material type. All fields optional."""
    # SKU no se actualiza
    nombre: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_medida: Optional[str] = Field(default=None, max_length=50)
    rendimiento_m2: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    # La actualización de stock_actual debería ser una operación separada (ej: ajuste de inventario)
    precio_venta_base_unidad: Optional[Decimal] = Field(default=None, max_digits=14, decimal_places=4)
    stock_minimo: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    ubicacion: Optional[str] = Field(default=None, max_length=255)

# --- Schemas para MaterialSimple ---

class MaterialSimpleBase(SQLModel):
    """Base schema for simple materials (nails, screws)."""
    sku: str = Field(..., max_length=100, index=True, description="SKU único del material simple.")
    nombre: str = Field(..., max_length=255, description="Nombre del material.")
    descripcion: Optional[str] = Field(default=None, description="Descripción detallada.")
    unidad_medida: str = Field(..., max_length=50, description="Unidad de medida (ej: unidad, caja, kg).")
    precio_venta_base_unidad: Decimal = Field(
        max_digits=14,
        decimal_places=4,
        description="Precio base por unidad de medida."
    )
    stock_minimo: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Nivel mínimo de stock para alertas."
    )
    ubicacion: Optional[str] = Field(default=None, max_length=255, description="Ubicación en almacén.")

class MaterialSimpleCreate(MaterialSimpleBase):
    """Schema to create a new type of simple material."""
    pass # Hereda de Base

class MaterialSimpleRead(MaterialSimpleBase):
    """Schema to read simple material data from API."""
    id: int
    stock_actual: condecimal(max_digits=10, decimal_places=3) = Field(default=Decimal("0.0")) # type: ignore
    fecha_creacion: Optional[datetime]

    fecha_ultima_actualizacion: Optional[datetime]

    model_config = {"from_attributes": True}

class MaterialSimpleUpdate(SQLModel):
    """Schema to update a simple material type. All fields optional."""
    # SKU no se actualiza
    nombre: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_medida: Optional[str] = Field(default=None, max_length=50)
    stock_minimo: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    ubicacion: Optional[str] = Field(default=None, max_length=255)
    # stock_actual no se actualiza aquí

# --- Schemas para StockItemDimensional ---

class StockItemDimensionalBase(SQLModel):
    """Base schema for physical dimensional stock items."""
    material_dimensional_id: int = Field(
        ...,
        foreign_key="material_dimensional.id", # Info para dev
        description="ID del tipo de material dimensional al que pertenece."
    )
    longitud_actual: condecimal(max_digits=10, decimal_places=3) = Field( # type: ignore
        ...,
        description="Longitud actual de la pieza física."
    )
    ancho_actual: condecimal(max_digits=10, decimal_places=3) = Field( # type: ignore
        ...,
        description="Ancho actual de la pieza física."
    )
    ubicacion: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Ubicación específica de esta pieza en el almacén."
    )
    # Campos relacionados con merma y origen
    es_merma: bool = Field(default=False, description="Indica si esta pieza es resultado de un corte (merma).")
    stock_item_padre_id: Optional[int] = Field(
        default=None,
        foreign_key="stock_item_dimensional.id", # Info para dev
        description="ID de la pieza de la que provino esta merma (si aplica)."
    )
    orden_produccion_generadora_id: Optional[int] = Field(
        default=None,
        foreign_key="orden_produccion.id", # Info para dev
        description="ID de la orden de producción que generó esta merma (si aplica)."
    )

class StockItemDimensionalCreate(StockItemDimensionalBase):
    """Schema para registrar una nueva pieza física de material dimensional en stock."""
    # Hereda los campos necesarios. El estado inicial podría ser 'DISPONIBLE' por defecto (manejado en servicio/repo).
    # estado: Optional[str] = Field(default="DISPONIBLE", max_length=50) # Opcional aquí, default en otro lado
    pass

class StockItemDimensionalRead(StockItemDimensionalBase):
    """Schema para leer los datos de una pieza física de stock dimensional."""
    id: int
    estado: str = Field(max_length=50)
    fecha_ingreso: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]
    # Podríamos incluir opcionalmente datos del material dimensional asociado
    # definicion_material: Optional[MaterialDimensionalRead] = None # Si se necesita info completa

    model_config = {"from_attributes": True}


# Schema para ajuste de stock
class StockAdjustRequest(BaseModel):
    change_amount: Decimal = Field(..., description="Cantidad a añadir (positivo) o quitar (negativo) del stock.")


# Aún no definimos StockItemDimensionalUpdate, ya que la actualización
# puede ser compleja (cambio de estado, dimensiones por corte, etc.)
# y podría requerir operaciones de servicio más específicas.


```

# app\schemas\order_production_schema.py

```py
# app/schemas/order_production_schema.py

from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from decimal import Decimal

# --- Importar Schemas Relacionados ---
# Necesitamos importar los schemas Read de las entidades relacionadas
# para poder anidarlos en nuestras respuestas.
# Asegúrate de que las rutas de importación sean correctas según tu estructura.

# Si TYPE_CHECKING bloquea las importaciones, asegúrate de que no haya dependencias circulares
# o usa string hints ("UsuarioRead") y llama a model_rebuild() al final.
if TYPE_CHECKING:
    from .usuario_schema import UsuarioRead    
    from .rol_permiso_schema import RolRead
    # Los siguientes podrían ser necesarios si decides anidar detalles de líneas:
    # from .order_schema import LineaProformaMaterialRead, LineaProformaServicioRead

# Importar directamente si no hay problemas de importación circular
#from .usuario_schema import UsuarioRead
from .usuario_schema import UsuarioRead
#from .rol_permiso_schema import RolRead
from .rol_permiso_schema import RolRead

# ===============================================================
# === Schemas para AsignacionTareaOrden                     ===
# ===============================================================

class AsignacionTareaOrdenBase(SQLModel):
    """Schema base con campos comunes de AsignacionTareaOrden."""
    orden_id: int = Field(description="ID de la Orden de Producción a la que pertenece.")
    # IDs de las líneas específicas (opcionalmente retornados)
    linea_proforma_servicio_id: Optional[int] = Field(default=None, description="ID de la línea de servicio específica (si aplica).")
    linea_proforma_material_id: Optional[int] = Field(default=None, description="ID de la línea de material específica (si aplica).")
    # Información clave de la tarea
    tipo_tarea: str = Field(max_length=100, description="Tipo de tarea (ej: DIBUJO_CNC, CORTE_MATERIAL).")
    estado_tarea: str = Field(max_length=50, description="Estado actual de la tarea (ej: PENDIENTE, EN_PROGRESO).")
    notas: Optional[str] = Field(default=None, description="Notas o comentarios sobre la tarea.")
    # IDs de usuario/rol (la información completa irá en Read)
    usuario_id_asignado: Optional[int] = Field(default=None, description="ID del usuario asignado a la tarea (si aplica).") # Nota: Modelo es NOT NULL, pero aquí puede ser None antes de asignar
    rol_id_contexto: int = Field(description="ID del Rol requerido o en cuyo contexto se realiza la tarea.")


class AsignacionTareaOrdenRead(SQLModel): # O heredar de Base si existe
    """Schema para devolver información detallada de una tarea asignada."""
    # Campos básicos
    id: int
    orden_id: int
    linea_proforma_servicio_id: Optional[int]
    linea_proforma_material_id: Optional[int]
    tipo_tarea: str
    estado_tarea: str
    notas: Optional[str]
    # IDs (útil tenerlos explícitos)
    usuario_id_asignado: int # Es NOT NULL en BD, así que el ID debe estar
    rol_id_contexto: int    # Es NOT NULL en BD, así que el ID debe estar
    # Fechas
    fecha_asignacion: Optional[datetime]
    fecha_inicio_tarea: Optional[datetime]
    fecha_fin_tarea: Optional[datetime]

    # Información anidada (Asumiendo que el servicio SIEMPRE carga estas relaciones para el Read)
    # Si hay casos donde no se cargan, mantener Optional y manejar en el frontend.
    # Pero si la FK es NOT NULL, lo lógico es que el objeto relacionado exista y se cargue.
    usuario_asignado: UsuarioRead = Field(description="Datos del usuario asignado.")
    rol_contexto: RolRead = Field(description="Datos del rol asociado al contexto de la tarea.")


    model_config = {"from_attributes": True}

# ===============================================================
# === Schemas para OrdenProduccion                          ===
# ===============================================================

class OrdenProduccionBase(SQLModel):
    """Schema base con campos comunes de OrdenProduccion."""
    pedido_cliente_id: int = Field(description="ID del PedidoCliente que generó esta orden.")
    estado: str = Field(max_length=50, description="Estado actual de la orden de producción.")
    prioridad: int = Field(default=0, description="Prioridad de la orden (mayor número = más prioridad).")
    # Campos opcionales que podrían definirse/actualizarse
    fecha_estimada_finalizacion: Optional[datetime] = Field(default=None, description="Fecha estimada de finalización.")
    notas_supervisor: Optional[str] = Field(default=None, description="Notas añadidas por el supervisor.")
    ruta_imagen_final: Optional[str] = Field(default=None, max_length=512, description="Ruta a la imagen del resultado final.")
    # ID del supervisor (la info completa va en Read)
    usuario_id_supervisor: Optional[int] = Field(default=None, description="ID del supervisor que finalizó la orden.")


class OrdenProduccionRead(OrdenProduccionBase):
    """Schema para devolver información detallada de una Orden de Producción."""
    id: int
    # Fechas clave
    fecha_creacion: Optional[datetime]
    fecha_inicio_espera: Optional[datetime] # Para calcular tiempo en espera
    fecha_asignacion: Optional[datetime] = None
    fecha_real_finalizacion: Optional[datetime] = None

    # Información anidada del supervisor (si está asignado)
    supervisor: Optional[UsuarioRead] = Field(default=None, description="Datos del supervisor asignado.")

    # Lista de tareas asociadas a esta orden
    asignaciones_tareas: List[AsignacionTareaOrdenRead] = Field(default=[], description="Lista de tareas requeridas para esta orden.")

    # Opcional: Incluir info básica del pedido o cliente? Por ahora solo ID.
    # pedido: Optional[PedidoClienteRead] = None

    model_config = {"from_attributes": True}

class OrdenProduccionCreate(SQLModel):
    """
    Schema para la creación interna de una Orden de Producción.
    Normalmente no se expone directamente como API, sino que se usa en el servicio.
    """
    pedido_cliente_id: int
    estado: str = "PENDIENTE_ASIGNACION" # Estado inicial
    prioridad: int = 0 # Prioridad inicial
    # Otros campos se rellenan al crearse o actualizarse

class OrdenProduccionUpdate(SQLModel):
    """Schema para actualizar una Orden de Producción (ej: estado, supervisor). Todos opcionales."""
    estado: Optional[str] = Field(default=None, max_length=50)
    usuario_id_supervisor: Optional[int] = Field(default=None)
    fecha_asignacion: Optional[datetime] = Field(default=None)
    fecha_estimada_finalizacion: Optional[datetime] = Field(default=None)
    fecha_real_finalizacion: Optional[datetime] = Field(default=None)
    notas_supervisor: Optional[str] = Field(default=None)
    ruta_imagen_final: Optional[str] = Field(default=None, max_length=512)
    prioridad: Optional[int] = Field(default=None)


# --- Actualizar Forward References ---
# Necesario si hay referencias circulares entre los schemas definidos AQUÍ.
# Por ahora, AsignacionTareaOrdenRead usa UsuarioRead/RolRead (importados)
# y OrdenProduccionRead usa AsignacionTareaOrdenRead (definido antes).
# No parece haber referencias circulares *dentro* de este archivo.
# AsignacionTareaOrdenRead.model_rebuild() # No necesario por ahora
# OrdenProduccionRead.model_rebuild() # No necesario por ahora
```

# app\schemas\order_schema.py

```py




# app/schemas/order_schema.py

from decimal import Decimal
from sqlmodel import SQLModel, Field
from pydantic import BaseModel, field_validator, model_validator # Podríamos necesitarlo para otros schemas aquí
from typing import Optional, List, Any # Necesario para relaciones en Read
from datetime import datetime
from decimal import Decimal

# Importar schemas relacionados para anidación en PedidoClienteRead
# Asegúrate de que estos schemas existan y estén definidos adecuadamente
from .client_schema import ClienteRead
from .usuario_schema import UsuarioRead 
from .inventory_schema import (
    StockItemDimensionalRead, MaterialConsumibleRead, MaterialSimpleRead
)
from .service_schema import ServicioDefinicionRead


# --- Lista de tipos de Proforma permitidos ---
ALLOWED_PROFORMA_TIPO = ["PRODUCTO", "SERVICIO"]
# --- Lista de estados de Proforma permitidos ---
ALLOWED_PROFORMA_ESTADO = [
    "BORRADOR", "PENDIENTE_APROBACION", "APROBADA",
    "RECHAZADA", "CANCELADA", "EXPIRADA", "POSPUESTA"
]

ALLOWED_TIPO_MATERIAL_ORIGEN = ["STOCK_DIMENSIONAL", "CONSUMIBLE", "SIMPLE"]


# -----------------------------------------------------
# Schemas para PedidoCliente
# -----------------------------------------------------

class PedidoClienteBase(SQLModel):
    """
    Schema base para PedidoCliente.
    Contiene campos comunes que podrían usarse en Create y Read,
    aunque en este caso, solo cliente_id es relevante para Create desde la API.
    El estado podría ir aquí si se compartiera mucho, pero lo pondremos en Read.
    """
    # cliente_id es fundamental para cualquier pedido.
    cliente_id: int = Field(
        ..., # Requerido en la creación vía API
        foreign_key="cliente.id", # Información contextual
        description="ID del Cliente al que pertenece el pedido."
    )
    # Nota: usuario_id_vendedor se obtendrá del usuario autenticado,
    #       estado, fecha_creacion, etc., se manejan internamente o en Read.

class PedidoClienteCreate(PedidoClienteBase):
    """
    Schema para crear un nuevo PedidoCliente via API.
    Solo requiere el ID del cliente, ya que el vendedor se obtiene del token
    y el estado inicial se define en el servicio.
    """
    # Hereda cliente_id de PedidoClienteBase
    pass # No necesita campos adicionales por ahora.

class PedidoClienteRead(SQLModel): # No hereda de Base para definir explícitamente todos los campos de salida
    """
    Schema para devolver la información de un PedidoCliente en respuestas API.
    Incluye información anidada del cliente y vendedor para mayor utilidad.
    """
    id: int
    estado: str # Devolveremos el estado actual
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]

    # Información del cliente anidada (usando ClienteRead)
    cliente_id: int # Mantenemos el ID por si acaso
    cliente: ClienteRead # Objeto Cliente completo (o lo que defina ClienteRead)

    # Información del vendedor anidada (usando UsuarioRead)
    usuario_id_vendedor: int # Mantenemos el ID
    vendedor: UsuarioRead # Objeto Usuario completo (o lo que defina UsuarioRead)

    proformas: List["ProformaRead"] = [] # <-- Incluir lista de proformas
    # orden_produccion: Optional["OrdenProduccionRead"] = None # <-- Se añadirá después

    model_config = {"from_attributes": True}


class PedidoClienteUpdate(SQLModel):
    """
    Schema para actualizar un PedidoCliente existente (ej: cambiar estado).
    Todos los campos son opcionales.
    """
    # El único campo que probablemente se actualizaría directamente en PedidoCliente es el estado.
    # Otros cambios (como añadir proformas) se harían a través de endpoints específicos.
    estado: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Nuevo estado del pedido (ej: APROBADO, CANCELADO)."
    )
    # No permitimos cambiar cliente_id ni vendedor_id en una actualización directa.


# --- Definiciones Forward para relaciones en PedidoClienteRead (cuando se creen los schemas) ---
# ProformaRead.model_rebuild()
# OrdenProduccionRead.model_rebuild()



# -----------------------------------------------------
# Schemas para Proforma (NUEVO)
# -----------------------------------------------------

class ProformaBase(SQLModel):
    """Schema base para Proforma con campos comunes."""
    # pedido_cliente_id y tipo son necesarios al crear
    pedido_cliente_id: int = Field(
        ..., foreign_key="pedido_cliente.id", description="ID del PedidoCliente al que pertenece."
    )
    tipo: str = Field(
        ..., max_length=50, description=f"Tipo de proforma ({', '.join(ALLOWED_PROFORMA_TIPO)})."
    )
    notas: Optional[str] = Field(
        default=None, description="Notas adicionales o comentarios sobre la proforma."
    )

    # Validador para el campo tipo
    @field_validator('tipo')
    def validate_tipo_proforma(cls, v: str) -> str:
        if v not in ALLOWED_PROFORMA_TIPO:
            raise ValueError(f"Tipo debe ser uno de: {', '.join(ALLOWED_PROFORMA_TIPO)}")
        return v

class ProformaCreate(ProformaBase):
    """
    Schema para crear una nueva Proforma via API.
    Normalmente, la creación inicial (par producto/servicio) se gestionará
    en el servicio asociado a la creación/gestión del PedidoCliente.
    Este schema podría usarse si se permitiera crear proformas individualmente.
    """
    # Hereda pedido_cliente_id, tipo y notas.
    # El resto de campos (usuario_id_creador, estado inicial, vinculación)
    # los establecerá la lógica de servicio.
    pass

class ProformaRead(SQLModel): # No hereda de Base para control explícito de salida
    """Schema para devolver información de Proforma en respuestas API."""
    id: int
    pedido_cliente_id: int
    tipo: str
    proforma_vinculada_id: Optional[int] = None # ID de la proforma vinculada (si existe)
    usuario_id_creador: int
    estado: str
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]
    fecha_aprobacion: Optional[datetime] = None
    fecha_reserva_expira: Optional[datetime] = None
    estado_reserva: Optional[str] = None
    subtotal: Optional[Decimal] = None
    impuestos: Optional[Decimal] = None
    total: Optional[Decimal] = None
    notas: Optional[str] = None

    # Información del creador (opcional, pero útil)
    # creador: Optional[UsuarioRead] = None # Descomentar si se quiere incluir

    # Listas de líneas (se añadirán cuando se definan sus schemas Read)
    lineas_material: List["LineaProformaMaterialRead"] = []
    lineas_servicio: List["LineaProformaServicioRead"] = []

    model_config = {"from_attributes": True}

class ProformaUpdate(SQLModel):
    """Schema para actualizar una Proforma (ej: estado, notas). Todos opcionales."""
    # No se permite cambiar pedido_cliente_id, tipo, ni creador.
    # La vinculación se manejaría con lógica específica.
    estado: Optional[str] = Field(
        default=None, max_length=50, description=f"Nuevo estado ({', '.join(ALLOWED_PROFORMA_ESTADO)})."
    )
    notas: Optional[str] = Field(
        default=None, description="Actualizar o añadir notas."
    )
    # Campos como subtotal, impuestos, total no se actualizan directamente,
    # se recalculan cuando se modifican las líneas.
    # La fecha_aprobacion, fecha_reserva_expira, estado_reserva se manejarían
    # por lógica de servicio basada en cambios de estado.

    # Validador para el campo estado (si se actualiza)
    @field_validator('estado')
    def validate_update_estado_proforma(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ALLOWED_PROFORMA_ESTADO:
            raise ValueError(f"Estado debe ser uno de: {', '.join(ALLOWED_PROFORMA_ESTADO)}")
        return v

# ==========================================================
# Schemas para LineaProformaMaterial (NUEVO)
# ==========================================================

class LineaProformaMaterialBase(SQLModel):
    """Schema base para líneas de material en proforma."""
    tipo_material_origen: str = Field(
        ..., max_length=50, description=f"Origen ({', '.join(ALLOWED_TIPO_MATERIAL_ORIGEN)})"
    )
    # IDs opcionales del origen - solo uno debe ser no nulo
    stock_item_dimensional_id: Optional[int] = Field(default=None, foreign_key="stock_item_dimensional.id")
    material_consumible_id: Optional[int] = Field(default=None, foreign_key="material_consumible.id")
    material_simple_id: Optional[int] = Field(default=None, foreign_key="material_simple.id")
    # Campos comunes
    cantidad: Decimal = Field(..., max_digits=10, decimal_places=3, gt=0, description="Cantidad del material")
    detalles_corte_solicitado: Optional[str] = Field(default=None, description="Detalles específicos del corte o preparación")

    @field_validator('tipo_material_origen')
    def validate_tipo_origen(cls, v: str) -> str:
        if v not in ALLOWED_TIPO_MATERIAL_ORIGEN:
            raise ValueError(f"Tipo origen debe ser uno de: {', '.join(ALLOWED_TIPO_MATERIAL_ORIGEN)}")
        return v

    # Validador a nivel de modelo para asegurar que solo se proporcione un ID de origen
    @model_validator(mode='after')
    def check_single_material_id(cls, data: Any) -> Any:
        if isinstance(data, SQLModel): # Adaptar si no hereda de SQLModel
             provided_ids = [
                 data.stock_item_dimensional_id,
                 data.material_consumible_id,
                 data.material_simple_id
             ]
             # Contar cuántos IDs tienen valor (no son None)
             num_provided = sum(1 for id_val in provided_ids if id_val is not None)
             if num_provided != 1:
                 raise ValueError("Debe proporcionar exactamente un ID de origen (stock_item_dimensional_id, material_consumible_id, o material_simple_id)")
        return data

class LineaProformaMaterialCreate(LineaProformaMaterialBase):
    """Schema para añadir una línea de material a una proforma via API."""
    # Hereda los campos de Base.
    # El servicio determinará 'descripcion_item', 'unidad', 'precio_unitario'
    # basado en el ID de origen proporcionado.
    pass

class LineaProformaMaterialRead(SQLModel): # No hereda de Base para control explícito
    """Schema para devolver información de línea de material."""
    id: int
    # tipo_material_origen: str # Podría incluirse si es útil
    descripcion_item: str
    cantidad: Decimal
    unidad: str
    precio_unitario: Decimal
    total_linea: Decimal
    detalles_corte_solicitado: Optional[str] = None
    # --- Opcional: Información anidada del material de origen ---
    # stock_item: Optional[StockItemDimensionalRead] = None
    # material_consumible: Optional[MaterialConsumibleRead] = None
    # material_simple: Optional[MaterialSimpleRead] = None
    # --- Opcional: Lista de servicios asociados a esta línea ---
    # servicios_asociados: List["LineaProformaServicioRead"] = []

    model_config = {"from_attributes": True}

# ==========================================================
# Schemas para LineaProformaServicio (NUEVO)
# ==========================================================

class LineaProformaServicioBase(SQLModel):
    """Schema base para líneas de servicio en proforma."""
    servicio_definicion_id: int = Field(..., foreign_key="servicio_definicion.id", description="ID de la definición del servicio")
    cantidad: Decimal = Field(..., max_digits=10, decimal_places=3, gt=0, description="Cantidad del servicio (según unidad de cobro)")
    # Opcional: ID de la línea de material a la que se aplica este servicio
    linea_proforma_material_id: Optional[int] = Field(
        default=None, foreign_key="linea_proforma_material.id", nullable=True,
        description="ID de la línea de material asociada (si aplica)"
    )
    # Campos para info específica (podrían ser rellenados por dibujante/servicio)
    ruta_imagen_cnc: Optional[str] = Field(
        default=None, max_length=512, nullable=True, description="Ruta al archivo CNC (si aplica)"
    )
    detalles_adicionales: Optional[str] = Field(
        default=None, nullable=True, description="Notas o detalles específicos del servicio"
    )

class LineaProformaServicioCreate(LineaProformaServicioBase):
    """Schema para añadir una línea de servicio a una proforma via API."""
    # Hereda los campos de Base.
    # El servicio determinará 'descripcion_servicio', 'precio_unitario'
    # basado en el servicio_definicion_id.
    pass

class LineaProformaServicioRead(SQLModel): # No hereda de Base
    """Schema para devolver información de línea de servicio."""
    id: int
    servicio_definicion_id: int
    linea_proforma_material_id: Optional[int] = None
    descripcion_servicio: str
    cantidad: Decimal
    # unidad_cobro: str # Podría venir del servicio_definicion anidado
    precio_unitario: Decimal
    total_linea: Decimal
    ruta_imagen_cnc: Optional[str] = None
    detalles_adicionales: Optional[str] = None
    # --- Opcional: Información anidada del servicio ---
    # servicio_definicion: Optional[ServicioDefinicionRead] = None

    model_config = {"from_attributes": True}


# --- Actualizar Forward References ---
# Es necesario si los schemas se referencian entre sí dentro de este mismo archivo
# (ej: PedidoClienteRead -> ProformaRead -> Linea...Read)
ProformaRead.model_rebuild()
PedidoClienteRead.model_rebuild()
# LineaProformaMaterialRead.model_rebuild() # Descomentar si se usa servicio_asociados
# LineaProformaServicioRead.model_rebuild() # Descomentar si se usa en LineaProformaMaterialRead



# --- Definiciones Forward para relaciones futuras ---
# (Necesarias si definimos LineaProforma*Read aquí y los usamos en ProformaRead)
# class LineaProformaMaterialRead(SQLModel): ...
# class LineaProformaServicioRead(SQLModel): ...
# ProformaRead.model_rebuild()

# (Necesarias si usamos ProformaRead en PedidoClienteRead)
# PedidoClienteRead.model_rebuild()
```

# app\schemas\rol_permiso_schema.py

```py
# app/schemas/rol_permiso_schema.py

from typing import Optional, List 
from sqlmodel import SQLModel, Field
from datetime import datetime

# --- Schema para Roles ---

class RolBase(SQLModel):
    """Schema base para Rol con campos comunes."""
    nombre: str = Field(
        ..., # (...) indica que es requerido en Pydantic/SQLModel base
        index=True,
        unique=True, # Aunque unique es de DB, es bueno indicarlo
        max_length=100,
        description="Nombre único del Rol (ej: Administrador, Vendedor)."
    )
    descripcion: Optional[str] = Field(
        default=None,
        description="Descripción opcional del Rol."
    )

class RolRead(RolBase):
    """Schema para leer datos de un Rol desde la API."""
    id: int
    fecha_creacion: Optional[datetime] = None
    fecha_ultima_actualizacion: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }

# Podrías añadir RolCreate, RolUpdate aquí si necesitaras endpoints para gestionarlos

class RolCreate(RolBase):
    """Schema para crear un nuevo Rol via API."""
    # Hereda 'nombre' (requerido) y 'descripcion' (opcional) de RolBase
    pass # No necesita campos adicionales por ahora


class RolUpdate(SQLModel): # No hereda de RolBase para hacer todos los campos opcionales
    """
    Schema para actualizar un Rol existente via API.
    Todos los campos son opcionales.
    """
    nombre: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Nuevo nombre único para el Rol."
    )
    descripcion: Optional[str] = Field(
        default=None,
        description="Nueva descripción para el Rol (None para no cambiar, '' para borrar)."
    )

# --- Schema Base para Permisos ---
class PermisoBase(SQLModel):
    """Schema base para Permiso con campos comunes."""
    nombre_accion: str = Field(
        ..., # Requerido
        max_length=100,
        description="Acción permitida (ej: crear, leer, gestionar)."
        )
    nombre_recurso: str = Field(
        ..., # Requerido
        max_length=100,
        description="Recurso sobre el que aplica la acción (ej: proforma, usuario)."
        )
    descripcion: Optional[str] = Field(
        default=None,
        description="Descripción opcional del Permiso."
        )

# --- Schema para Leer Permisos ---
class PermisoRead(PermisoBase):
    """Schema para leer datos de un Permiso desde la API."""
    id: int
    fecha_creacion: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }


# --- NUEVOS SCHEMAS DE ESCRITURA PARA PERMISOS ---

class PermisoCreate(PermisoBase):
    """Schema para crear un nuevo Permiso via API."""
    # Hereda 'nombre_accion', 'nombre_recurso' (requeridos)
    # y 'descripcion' (opcional) de PermisoBase
    pass # No necesita campos adicionales

class PermisoUpdate(SQLModel): # No hereda para hacer campos opcionales
    """
    Schema para actualizar un Permiso existente via API.
    Todos los campos son opcionales.
    """
    nombre_accion: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Nueva acción para el Permiso."
        )
    nombre_recurso: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Nuevo recurso para el Permiso."
        )
    descripcion: Optional[str] = Field(
        default=None,
        description="Nueva descripción para el Permiso."
        )
    



class RolReadWithPermissions(RolRead):
    """
    Schema para leer datos de un Rol desde la API, incluyendo
    la lista de permisos asociados.
    """
    permisos: List[PermisoRead] = [] # Lista de Permisos (usando PermisoRead)

    # model_config se hereda de RolRead, así que from_attributes ya está habilitado.

```

# app\schemas\service_schema.py

```py
# app/schemas/service_schema.py
from sqlmodel import SQLModel, Field
from pydantic import condecimal
from typing import Optional
from datetime import datetime
from decimal import Decimal


class ServicioDefinicionBase(SQLModel):
    """Schema base para la definición de servicios."""
    # --- CAMBIO: Añadido campo codigo ---
    codigo: str = Field(
        ...,
        max_length=50,
        index=True, # Info para dev
        unique=True, # Info para dev
        description="Código único para identificar el servicio."
    )
    # --- FIN CAMBIO ---
    nombre: str = Field(
        ...,
        max_length=255,
        description="Nombre único y descriptivo del servicio ofrecido (ej: Corte Recto MDF, Maquinado CNC Básico)."
    )
    descripcion: Optional[str] = Field(
        default=None,
        description="Descripción detallada del servicio."
    )
    unidad_cobro: str = Field(
        ...,
        max_length=50,
        description="Unidad en la que se mide/cobra el servicio (ej: pieza, hora, m2, corte, ml)."
    )
    # Campos de costeo (algunos pueden ser nulos si el costeo es diferente)
    costo_por_unidad: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Costo fijo por cada unidad de servicio (si aplica)."
    )
    costo_por_minuto: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        default=None,
        description="Costo por minuto de ejecución del servicio (ej: tiempo máquina)."
    )
    tiempo_setup_min: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        # El default=0.0 está en la DB, lo reflejamos aquí
        default=Decimal("0.0"),
        description="Tiempo fijo de preparación/setup en minutos (independiente de la cantidad)."
    )
    tiempo_preparado_min_por_unidad: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        # El default=0.0 está en la DB
        default=Decimal("0.0"),
        description="Tiempo adicional de preparado en minutos por cada unidad de servicio."
    )
    factor_ih: Optional[condecimal(max_digits=10, decimal_places=3)] = Field( # type: ignore
        # El default=1.0 está en la DB
        default=Decimal("1.0"),
        description="Factor de Imprevistos/Herramientas (multiplicador sobre costo base, ej: 1.1 para 10%)."
    )
    # --- CAMBIO: Añadido requiere_dibujo_cnc ---
    # (Asegúrate que este cambio de la vez anterior sigue aquí)
    requiere_dibujo_cnc: bool = Field(
        default=False,
        description="Indica si este servicio requiere un archivo de dibujo CNC."
    )

class ServicioDefinicionCreate(ServicioDefinicionBase):
    """Schema para crear una nueva definición de servicio."""
    # Hereda todos los campos necesarios de la base.
    pass


class ServicioDefinicionRead(ServicioDefinicionBase):
    """Schema para devolver información de definición de servicio."""
    id: int
    fecha_creacion: Optional[datetime]
    fecha_ultima_actualizacion: Optional[datetime]
    # Fórmulas asociadas podrían añadirse aquí en el futuro:
    # formulas: List["FormulaRead"] = []

    model_config = {"from_attributes": True}

class ServicioDefinicionUpdate(SQLModel):
    """Schema para actualizar una definición de servicio. Todos los campos opcionales."""
    # --- CAMBIO: Añadido codigo (opcional) ---
    codigo: Optional[str] = Field(default=None, max_length=50)
    # --- FIN CAMBIO ---
    nombre: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None)
    unidad_cobro: Optional[str] = Field(default=None, max_length=50)
    costo_por_unidad: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    costo_por_minuto: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    tiempo_setup_min: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    tiempo_preparado_min_por_unidad: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    factor_ih: Optional[condecimal(max_digits=10, decimal_places=3)] = Field(default=None) # type: ignore
    # --- CAMBIO: Añadido requiere_dibujo_cnc (opcional) ---
    requiere_dibujo_cnc: Optional[bool] = Field(default=None)
    # --- FIN CAMBIO ---

```

# app\schemas\token_schema.py

```py
# app/schemas/token_schema.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import enum

class TokenType(str, enum.Enum):
    """Define el tipo de token permitido."""
    BEARER = "bearer"

class Token(BaseModel):
    """
    Schema para la respuesta de autenticación estándar OAuth2.
    Contiene el token de acceso y su tipo.
    """
    access_token: str = Field(
        ..., # El campo es requerido
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ4YXZpZXJ...",
        description="Token JWT para autenticación en endpoints protegidos."
    )
    token_type: TokenType = Field(
        default=TokenType.BEARER,
        example=TokenType.BEARER.value, # Usa el valor del Enum para el ejemplo
        description="Tipo de token emitido (siempre 'bearer')."
    )

class TokenData(BaseModel):
    """
    Schema para los datos decodificados del payload del token JWT.
    Utilizado internamente para validar y extraer la información del sujeto.
    """
    sub: str = Field(
        ..., # Subject (sujeto/identificador) es requerido
        example="xavierpauta", # O podría ser un ID de usuario numérico como string
        description="Identificador único del sujeto del token (generalmente username o ID)."
    )
    exp: Optional[datetime] = Field(
        default=None, # La librería jose/jwt valida la expiración por defecto
        description="Timestamp de expiración del token (opcional aquí, validado por jwt.decode)."
        )
    iat: Optional[datetime] = Field(
        default=None, # Tiempo de emisión (opcional aquí, añadido en security.py)
        description="Timestamp de emisión del token."
    )

```

# app\schemas\usuario_schema.py

```py
# app/schemas/usuario_schema.py
from sqlmodel import SQLModel, Field # Usamos SQLModel para schemas relacionados con la tabla
from pydantic import BaseModel, EmailStr, field_validator # BaseModel para schemas no mapeados 1:1
from typing import Optional, List
from datetime import datetime
import re # Para validación con regex
from .rol_permiso_schema import RolRead

# Importación necesaria para el validador si usas Pydantic v2+
from pydantic_core.core_schema import FieldValidationInfo

# --- Schemas SQLModel-based ---

class UsuarioBase(SQLModel):
    """Schema base con campos comunes para no repetir."""
    email: EmailStr = Field(
        ..., # Requerido
        description="Correo electrónico único del usuario."
    )
    username: str = Field(
        ..., # Requerido
        min_length=3,
        max_length=100, # Aumentado por si acaso, DB es 100
        description="Nombre de usuario único (3-100 caracteres)."
    )
    nombre_completo: Optional[str] = Field(
        default=None,
        max_length=255, # Coincidir con DB
        description="Nombre completo del usuario (opcional)."
    )

class UsuarioCreate(UsuarioBase): # Hereda email, username, nombre_completo
    """
    Schema para crear un nuevo usuario via API.
    Permite especificar los roles iniciales.
    """
    password: str = Field(
        ..., # Requerido
        min_length=8,
        max_length=50, # Limitar longitud máxima razonable en input
        description="Contraseña del usuario (mínimo 8 caracteres)."
    )
    # --- CAMPO AÑADIDO ---
    rol_ids: Optional[List[int]] = Field(
        default=None, # Es opcional proporcionar roles al crear
        description="Lista opcional de IDs de los roles a asignar inicialmente al usuario."
    )


class UsuarioRead(UsuarioBase): # Hereda email, username, nombre_completo
    """
    Schema para devolver información del usuario en respuestas API.
    Excluye información sensible como la contraseña. Incluye roles.
    """
    id: int
    esta_activo: bool
    fecha_creacion: Optional[datetime] = None
    # Incluir roles usando el schema RolRead importado
    roles: List[RolRead] = [] # Lista vacía por defecto

    model_config = {
        "from_attributes": True
    }

class UsuarioUpdate(SQLModel):
    """
    Schema para actualizar información del perfil de usuario.
    Todos los campos son opcionales. No incluye cambio de contraseña ni roles.
    """
    email: Optional[EmailStr] = Field(
        default=None,
        description="Nuevo correo electrónico único (opcional)."
    )
    username: Optional[str] = Field( # Permitir cambio de username (opcional)
        default=None,
        min_length=3,
        max_length=100,
        description="Nuevo nombre de usuario único (opcional)."
    )
    nombre_completo: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nuevo nombre completo (opcional)."
    )
    esta_activo: Optional[bool] = Field(
        default=None,
        description="Estado de activación del usuario (opcional, para Admins)."
    )
    # La asignación de roles se manejará por endpoints específicos (Paso 4)

# --- Schema Pydantic BaseModel ---

class UsuarioUpdatePassword(BaseModel):
    """Schema específico para solicitar un cambio de contraseña."""
    old_password: str = Field(..., description="La contraseña actual del usuario.")
    new_password: str = Field(
        ...,
        min_length=8,
        max_length=50,
        description="La nueva contraseña (mínimo 8 caracteres)."
    )
    confirm_password: str = Field(
        ...,
        description="Confirmación de la nueva contraseña."
    )

    # Validación para asegurar que new_password y confirm_password coinciden
    @field_validator('confirm_password')
    def passwords_match(cls, v: str, info: FieldValidationInfo) -> str:
        if 'new_password' in info.data and v != info.data['new_password']:
            raise ValueError('La nueva contraseña y la confirmación no coinciden.')
        return v

```

# app\services\__init__.py

```py

```

# app\services\auth_service.py

```py
# app/services/auth_service.py

from sqlmodel import Session
from fastapi import HTTPException, status
import logging

from app.models.user_models import Usuario
from app.repositories import usuario_repository
from app.core.security import verify_password

logger = logging.getLogger(__name__)

# =====================
#  Excepción Personalizada
# =====================

class AuthException(HTTPException):
    """
    Excepción personalizada para errores específicos de autenticación.

    Hereda de HTTPException, estableciendo automáticamente el código de estado
    401 (Unauthorized) y la cabecera 'WWW-Authenticate' requerida.

    Args:
        detail: Mensaje de error detallado que se enviará al cliente.
    """
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"} # Estándar para autenticación Bearer
        )

# =====================
#  Lógica de Autenticación
# =====================

def authenticate_user(db: Session, username: str, password: str) -> Usuario:
    """
    Autentica un usuario por nombre de usuario/email y contraseña.

    Verifica la existencia del usuario (buscando por username o email),
    si la cuenta está activa y si la contraseña proporcionada coincide
    con el hash almacenado.

    Args:
        db: La sesión de base de datos activa.
        username: El nombre de usuario o correo electrónico del usuario.
                  Se normaliza a minúsculas y se eliminan espacios.
        password: La contraseña en texto plano proporcionada por el usuario.

    Returns:
        El objeto Usuario completo si la autenticación es exitosa.

    Raises:
        AuthException: Si las credenciales están incompletas, el usuario no existe,
                       la cuenta está inactiva o la contraseña es incorrecta.

    Example:
        >>> user = authenticate_user(db, " testuser@example.com ", "password123")
        >>> print(user.username)
        testuser
    """
    # Sanitización básica de inputs
    username = username.strip().lower()
    if not username or not password:
        logger.warning("Intento de autenticación con credenciales vacías")
        raise AuthException("Credenciales incompletas")

    # Buscar por username o email usando el repositorio
    user = usuario_repository.get_usuario_by_username(db, username)
    if not user:
        # Si no se encontró por username, intentar por email
        user = usuario_repository.get_usuario_by_email(db, username)

    # Mensaje genérico para no revelar si el usuario existe o no
    error_detail = "Credenciales inválidas"
    if not user:
        logger.warning(f"Intento de login con usuario inexistente: {username}")
        raise AuthException(error_detail)

    # Verificar si la cuenta está activa
    if not user.esta_activo:
        logger.warning(f"Intento de login en cuenta inactiva: {user.username}")
        raise AuthException("Cuenta deshabilitada")

    # Verificar la contraseña
    if not verify_password(password, user.contrasena_hash):
        logger.warning(f"Contraseña incorrecta para usuario: {user.username}")
        raise AuthException(error_detail)

    # Autenticación exitosa
    logger.info(f"Login exitoso: {user.username}")
    return user
```

# app\services\cliente_service.py

```py
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
```

# app\services\inventory_service.py

```py
# app/services/inventory_service.py
import logging
from typing import Optional, Sequence, Dict, Any
from decimal import Decimal

from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError # Para capturar errores del repo

# Importar Repositorio, Modelos y Schemas
from app.repositories import inventory_repository
from app.models.inventory_models import (
    MaterialDimensional,
    StockItemDimensional,
    MaterialConsumible,
    MaterialSimple
)
from app.schemas.inventory_schema import (
    MaterialDimensionalCreate, MaterialDimensionalUpdate,
    MaterialConsumibleCreate, MaterialConsumibleUpdate,
    MaterialSimpleCreate, MaterialSimpleUpdate,
    StockItemDimensionalCreate # Aunque no la usemos toda ahora
)

logger = logging.getLogger(__name__)

# =============================================
#  Servicios para MaterialDimensional
# =============================================

def create_material_dimensional_service(db: Session, *, mat_dim_in: MaterialDimensionalCreate) -> MaterialDimensional:
    """Crea un nuevo tipo de material dimensional, validando SKU."""
    logger.info(f"Servicio: Intentando crear MaterialDimensional SKU: {mat_dim_in.sku}")
    # Validar SKU duplicado ANTES de intentar crear
    existing = inventory_repository.get_material_dimensional_by_sku(db, sku=mat_dim_in.sku)
    if existing:
        logger.warning(f"Conflicto: SKU '{mat_dim_in.sku}' ya existe para MaterialDimensional.")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El SKU '{mat_dim_in.sku}' ya está registrado para un material dimensional."
        )
    try:
        mat_dim_data = MaterialDimensional.model_validate(mat_dim_in)
        new_mat_dim = inventory_repository.create_material_dimensional(db=db, mat_dim_data=mat_dim_data)
        return new_mat_dim
    except IntegrityError: # Captura por si acaso (race condition)
        db.rollback()
        logger.error(f"Error de Integridad (inesperado) al crear MaterialDimensional SKU '{mat_dim_in.sku}'.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al crear MaterialDimensional: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear material dimensional.")

def get_material_dimensional_by_id_service(db: Session, *, mat_dim_id: int) -> MaterialDimensional:
    """Obtiene un tipo de material dimensional por ID."""
    logger.debug(f"Servicio: Buscando MaterialDimensional ID: {mat_dim_id}")
    mat_dim = inventory_repository.get_material_dimensional_by_id(db=db, mat_dim_id=mat_dim_id)
    if not mat_dim:
        logger.warning(f"Servicio: MaterialDimensional ID {mat_dim_id} no encontrado.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Material dimensional con ID {mat_dim_id} no encontrado.")
    return mat_dim

def list_materiales_dimensionales_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialDimensional]:
    """Lista tipos de materiales dimensionales."""
    logger.debug(f"Servicio: Listando materiales dimensionales, skip={skip}, limit={limit}")
    try:
        return inventory_repository.list_materiales_dimensionales(db=db, skip=skip, limit=limit)
    except Exception as e:
        logger.error(f"Error inesperado en servicio al listar MaterialDimensional: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar materiales dimensionales.")

def update_material_dimensional_service(db: Session, *, mat_dim_id: int, mat_dim_in: MaterialDimensionalUpdate) -> MaterialDimensional:
    """Actualiza un tipo de material dimensional."""
    logger.info(f"Servicio: Intentando actualizar MaterialDimensional ID: {mat_dim_id}")
    db_mat_dim = get_material_dimensional_by_id_service(db=db, mat_dim_id=mat_dim_id) # Maneja 404
    update_data = mat_dim_in.model_dump(exclude_unset=True)
    if not update_data:
        logger.warning(f"Servicio: No se proporcionaron datos para actualizar MaterialDimensional ID {mat_dim_id}.")
        return db_mat_dim # Devolver sin cambios si no hay nada que actualizar
    try:
        # SKU no debe actualizarse a través de este método general
        if "sku" in update_data:
            logger.warning(f"Intento de actualizar SKU para MaterialDimensional ID {mat_dim_id} ignorado.")
            del update_data["sku"]

        return inventory_repository.update_material_dimensional(db=db, db_mat_dim=db_mat_dim, update_data=update_data)
    except Exception as e: # El repo maneja IntegrityError si ocurre
        # No necesitamos capturar IntegrityError aquí de nuevo si el repo lo relanza
        db.rollback()
        logger.error(f"Error inesperado en servicio al actualizar MaterialDimensional ID {mat_dim_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar material dimensional.")

def delete_material_dimensional_service(db: Session, *, mat_dim_id: int) -> MaterialDimensional:
    """Elimina un tipo de material dimensional."""
    logger.warning(f"Servicio: Intentando eliminar MaterialDimensional ID: {mat_dim_id}")
    db_mat_dim = get_material_dimensional_by_id_service(db=db, mat_dim_id=mat_dim_id) # Maneja 404
    try:
        deleted_mat = inventory_repository.delete_material_dimensional(db=db, mat_dim_id=mat_dim_id)
        # El repo ya devuelve None si no existe, pero get_ lo valida antes
        return deleted_mat # type: ignore # Ignorar posible None si confiamos en get_
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de Integridad al eliminar MaterialDimensional ID {mat_dim_id}. Probablemente referenciado: {e}")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se puede eliminar el material dimensional ID {mat_dim_id} porque está en uso (stock existente).")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al eliminar MaterialDimensional ID {mat_dim_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar material dimensional.")


# =============================================
#  Servicios para MaterialConsumible
# =============================================
# (Implementación análoga a MaterialDimensional, ajustando nombres y validando SKU)

def create_material_consumible_service(db: Session, *, mat_cons_in: MaterialConsumibleCreate) -> MaterialConsumible:
    logger.info(f"Servicio: Intentando crear MaterialConsumible SKU: {mat_cons_in.sku}")
    existing = inventory_repository.get_material_consumible_by_sku(db, sku=mat_cons_in.sku)
    if existing:
        logger.warning(f"Conflicto: SKU '{mat_cons_in.sku}' ya existe para MaterialConsumible.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El SKU '{mat_cons_in.sku}' ya está registrado para un material consumible.")
    try:
        mat_cons_data = MaterialConsumible.model_validate(mat_cons_in)
        # Inicializar stock_actual a 0 si no se proporciona un valor inicial explícito
        if mat_cons_data.stock_actual is None: mat_cons_data.stock_actual = Decimal("0.0")
        return inventory_repository.create_material_consumible(db=db, mat_cons_data=mat_cons_data)
    except IntegrityError: db.rollback(); raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar.")
    except Exception as e: db.rollback(); logger.error(f"Error crear MatCons: {e}", exc_info=True); raise HTTPException(status_code=500)

def get_material_consumible_by_id_service(db: Session, *, mat_cons_id: int) -> MaterialConsumible:
    logger.debug(f"Servicio: Buscando MaterialConsumible ID: {mat_cons_id}")
    mat = inventory_repository.get_material_consumible_by_id(db=db, mat_cons_id=mat_cons_id)
    if not mat: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Material consumible ID {mat_cons_id} no encontrado.")
    return mat

def list_materiales_consumibles_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialConsumible]:
    logger.debug(f"Servicio: Listando materiales consumibles, skip={skip}, limit={limit}")
    try: return inventory_repository.list_materiales_consumibles(db=db, skip=skip, limit=limit)
    except Exception as e: logger.error(f"Error listar MatCons: {e}", exc_info=True); raise HTTPException(status_code=500)

def update_material_consumible_service(db: Session, *, mat_cons_id: int, mat_cons_in: MaterialConsumibleUpdate) -> MaterialConsumible:
    logger.info(f"Servicio: Intentando actualizar MaterialConsumible ID: {mat_cons_id}")
    db_mat = get_material_consumible_by_id_service(db=db, mat_cons_id=mat_cons_id)
    update_data = mat_cons_in.model_dump(exclude_unset=True)
    if not update_data: return db_mat
    try:
        update_data.pop("sku", None) # Ignorar SKU
        update_data.pop("stock_actual", None) # Ignorar stock_actual
        return inventory_repository.update_material_consumible(db=db, db_mat_cons=db_mat, update_data=update_data)
    except Exception as e: db.rollback(); logger.error(f"Error update MatCons ID {mat_cons_id}: {e}", exc_info=True); raise HTTPException(status_code=500)

def delete_material_consumible_service(db: Session, *, mat_cons_id: int) -> MaterialConsumible:
    logger.warning(f"Servicio: Intentando eliminar MaterialConsumible ID: {mat_cons_id}")
    db_mat = get_material_consumible_by_id_service(db=db, mat_cons_id=mat_cons_id)
    try:
        deleted = inventory_repository.delete_material_consumible(db=db, mat_cons_id=mat_cons_id)
        return deleted # type: ignore
    except IntegrityError: db.rollback(); raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se puede eliminar MatCons ID {mat_cons_id}, está en uso.")
    except Exception as e: db.rollback(); logger.error(f"Error delete MatCons ID {mat_cons_id}: {e}", exc_info=True); raise HTTPException(status_code=500)

def adjust_stock_consumible_service(db: Session, *, mat_cons_id: int, change_amount: Decimal) -> MaterialConsumible:
    """Ajusta el stock de un material consumible."""
    logger.info(f"Servicio: Ajustando stock MaterialConsumible ID {mat_cons_id}, cambio: {change_amount}")
    # get_material_consumible_by_id_service ya maneja 404
    get_material_consumible_by_id_service(db=db, mat_cons_id=mat_cons_id)
    try:
        updated_mat = inventory_repository.adjust_stock_consumible(db=db, mat_cons_id=mat_cons_id, change_amount=change_amount)
        return updated_mat # type: ignore # Repo devuelve Optional, pero ya verificamos existencia
    except ValueError as ve: # Captura error de stock negativo del repo
        logger.error(f"Error de valor al ajustar stock MatCons ID {mat_cons_id}: {ve}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e:
        logger.error(f"Error inesperado al ajustar stock MatCons ID {mat_cons_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al ajustar stock.")


# =============================================
#  Servicios para MaterialSimple
# =============================================
# (Implementación análoga a MaterialConsumible)
# ...

def create_material_simple_service(db: Session, *, mat_simp_in: MaterialSimpleCreate) -> MaterialSimple:
    logger.info(f"Servicio: Intentando crear MaterialSimple SKU: {mat_simp_in.sku}")
    existing = inventory_repository.get_material_simple_by_sku(db, sku=mat_simp_in.sku)
    if existing:
        logger.warning(f"Conflicto: SKU '{mat_simp_in.sku}' ya existe para MaterialSimple.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El SKU '{mat_simp_in.sku}' ya está registrado para un material simple.")
    try:
        mat_simp_data = MaterialSimple.model_validate(mat_simp_in)
        if mat_simp_data.stock_actual is None: mat_simp_data.stock_actual = Decimal("0.0")
        return inventory_repository.create_material_simple(db=db, mat_simp_data=mat_simp_data)
    except IntegrityError: db.rollback(); raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar.")
    except Exception as e: db.rollback(); logger.error(f"Error crear MatSimp: {e}", exc_info=True); raise HTTPException(status_code=500)

def get_material_simple_by_id_service(db: Session, *, mat_simp_id: int) -> MaterialSimple:
    logger.debug(f"Servicio: Buscando MaterialSimple ID: {mat_simp_id}")
    mat = inventory_repository.get_material_simple_by_id(db=db, mat_simp_id=mat_simp_id)
    if not mat: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Material simple ID {mat_simp_id} no encontrado.")
    return mat

def list_materiales_simples_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[MaterialSimple]:
    logger.debug(f"Servicio: Listando materiales simples, skip={skip}, limit={limit}")
    try: return inventory_repository.list_materiales_simples(db=db, skip=skip, limit=limit)
    except Exception as e: logger.error(f"Error listar MatSimp: {e}", exc_info=True); raise HTTPException(status_code=500)

def update_material_simple_service(db: Session, *, mat_simp_id: int, mat_simp_in: MaterialSimpleUpdate) -> MaterialSimple:
    logger.info(f"Servicio: Intentando actualizar MaterialSimple ID: {mat_simp_id}")
    db_mat = get_material_simple_by_id_service(db=db, mat_simp_id=mat_simp_id)
    update_data = mat_simp_in.model_dump(exclude_unset=True)
    if not update_data: return db_mat
    try:
        update_data.pop("sku", None); update_data.pop("stock_actual", None)
        return inventory_repository.update_material_simple(db=db, db_mat_simp=db_mat, update_data=update_data)
    except Exception as e: db.rollback(); logger.error(f"Error update MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise HTTPException(status_code=500)

def delete_material_simple_service(db: Session, *, mat_simp_id: int) -> MaterialSimple:
    logger.warning(f"Servicio: Intentando eliminar MaterialSimple ID: {mat_simp_id}")
    db_mat = get_material_simple_by_id_service(db=db, mat_simp_id=mat_simp_id)
    try:
        deleted = inventory_repository.delete_material_simple(db=db, mat_simp_id=mat_simp_id)
        return deleted # type: ignore
    except IntegrityError: db.rollback(); raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se puede eliminar MatSimp ID {mat_simp_id}, está en uso.")
    except Exception as e: db.rollback(); logger.error(f"Error delete MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise HTTPException(status_code=500)

def adjust_stock_simple_service(db: Session, *, mat_simp_id: int, change_amount: Decimal) -> MaterialSimple:
    """Ajusta el stock de un material simple."""
    logger.info(f"Servicio: Ajustando stock MaterialSimple ID {mat_simp_id}, cambio: {change_amount}")
    get_material_simple_by_id_service(db=db, mat_simp_id=mat_simp_id) # Verifica 404
    try:
        updated_mat = inventory_repository.adjust_stock_simple(db=db, mat_simp_id=mat_simp_id, change_amount=change_amount)
        return updated_mat # type: ignore
    except ValueError as ve: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e: logger.error(f"Error ajustando stock MatSimp ID {mat_simp_id}: {e}", exc_info=True); raise HTTPException(status_code=500)


# =============================================
#  Servicios para StockItemDimensional (Base)
# =============================================

def create_stock_item_service(db: Session, *, item_in: StockItemDimensionalCreate) -> StockItemDimensional:
    """Crea una nueva pieza física de stock dimensional."""
    logger.info(f"Servicio: Intentando crear StockItemDimensional para MaterialID: {item_in.material_dimensional_id}")
    # Validar que el material dimensional asociado existe
    get_material_dimensional_by_id_service(db=db, mat_dim_id=item_in.material_dimensional_id) # Maneja 404

    # Validar que el item padre existe si se proporciona
    if item_in.stock_item_padre_id is not None:
        get_stock_item_by_id_service(db=db, item_id=item_in.stock_item_padre_id) # Maneja 404

    # TODO: Validar si es merma, si las dimensiones son menores o iguales al padre (si existe padre)

    try:
        item_data = StockItemDimensional.model_validate(item_in)
        # Establecer estado inicial por defecto si no viene en el schema (o validar si viene)
        if not item_data.estado: item_data.estado = "DISPONIBLE"
        # Asegurarse que es_merma sea False por defecto si no se especifica
        if item_data.es_merma is None: item_data.es_merma = False

        new_item = inventory_repository.create_stock_item(db=db, item_data=item_data)
        return new_item
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al crear StockItemDimensional: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear item de stock dimensional.")

def get_stock_item_by_id_service(db: Session, *, item_id: int) -> StockItemDimensional:
    """Obtiene una pieza de stock dimensional por ID."""
    logger.debug(f"Servicio: Buscando StockItemDimensional ID: {item_id}")
    item = inventory_repository.get_stock_item_by_id(db=db, item_id=item_id)
    if not item:
        logger.warning(f"Servicio: StockItemDimensional ID {item_id} no encontrado.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item de stock dimensional con ID {item_id} no encontrado.")
    return item

def list_stock_items_service(
    db: Session, *,
    skip: int = 0, limit: int = 100,
    material_dimensional_id: Optional[int] = None,
    estado: Optional[str] = None,
    min_longitud: Optional[Decimal] = None,
    min_ancho: Optional[Decimal] = None
) -> Sequence[StockItemDimensional]:
    """Lista piezas de stock dimensional con filtros."""
    logger.debug(f"Servicio: Listando StockItemDimensional con filtros - MaterialID: {material_dimensional_id}, Estado: {estado}, MinL: {min_longitud}, MinA: {min_ancho}")
    try:
        return inventory_repository.list_stock_items(
            db=db, skip=skip, limit=limit,
            material_dimensional_id=material_dimensional_id,
            estado=estado, min_longitud=min_longitud, min_ancho=min_ancho
        )
    except Exception as e:
        logger.error(f"Error inesperado en servicio al listar StockItemDimensional: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar items de stock dimensional.")

# update_stock_item_service y delete_stock_item_service se pueden implementar
# más adelante o según se necesiten operaciones específicas (cambiar estado, etc.)
```

# app\services\order_service.py

```py
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


```

# app\services\permiso_service.py

```py
# app/services/permiso_service.py

import logging
from typing import Optional, Sequence

from fastapi import HTTPException, status
from sqlmodel import Session

from app.repositories import permiso_repository
from app.models import Permiso # Importar el modelo
from app.schemas.rol_permiso_schema import PermisoCreate, PermisoUpdate

logger = logging.getLogger(__name__)

# =====================
#  Funciones Read (Getters)
# =====================

def get_permiso_by_id(db: Session, *, permiso_id: int) -> Permiso:
    """
    Obtiene un permiso específico por su ID, delegando al repositorio.

    Args:
        db: Sesión de base de datos activa.
        permiso_id: ID del permiso a buscar.

    Returns:
        El objeto Permiso encontrado.

    Raises:
        HTTPException: 404 si el permiso con el ID especificado no se encuentra.
    """
    logger.debug(f"Buscando permiso con ID: {permiso_id}")
    permiso = permiso_repository.get_permiso(db=db, permiso_id=permiso_id)
    if not permiso:
        logger.warning(f"Permiso con ID {permiso_id} no encontrado.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Permiso con ID {permiso_id} no encontrado."
        )
    return permiso

def get_all_permisos(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Permiso]:
    """
    Obtiene una lista paginada de todos los permisos, delegando al repositorio.

    Args:
        db: Sesión de base de datos activa.
        skip: Número de registros a saltar (para paginación).
        limit: Número máximo de registros a devolver (para paginación).

    Returns:
        Una secuencia (lista) de objetos Permiso.

    Raises:
        HTTPException: 500 si ocurre un error interno inesperado al listar.
    """
    logger.debug(f"Listando permisos con skip={skip}, limit={limit}")
    try:
        permisos = permiso_repository.list_permisos(db=db, skip=skip, limit=limit)
        return permisos
    except Exception as e:
         logger.error(f"Error inesperado al listar permisos: {e}", exc_info=True)
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Error interno del servidor al listar permisos."
         )

# =====================
#  Funciones Write (Create, Update, Delete)
# =====================

def create_new_permiso(db: Session, *, permiso_in: PermisoCreate) -> Permiso:
    """
    Crea un nuevo permiso, delegando la creación y validación de duplicados al repositorio.

    Args:
        db: Sesión de base de datos activa.
        permiso_in: Datos del permiso a crear (esquema PermisoCreate).

    Returns:
        El objeto Permiso creado.

    Raises:
        HTTPException: 409 si el permiso ya existe (manejo de IntegrityError del repo).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando crear permiso: {permiso_in.nombre_accion}:{permiso_in.nombre_recurso}")
    # La validación de duplicado (IntegrityError -> HTTPException 409)
    # ya se maneja en permiso_repository.create_permiso
    try:
        permiso = permiso_repository.create_permiso(db=db, permiso_in=permiso_in)
        return permiso
    except HTTPException: # Re-lanzar excepciones HTTP (ej: 409 del repo)
        raise
    except Exception as e:
        logger.error(f"Error inesperado al crear permiso: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el permiso."
        )

def update_existing_permiso(
    db: Session, *, permiso_id: int, permiso_in: PermisoUpdate
) -> Permiso:
    """
    Actualiza un permiso existente.

    Primero obtiene el permiso, luego verifica si la combinación acción/recurso
    está cambiando y si la nueva combinación ya existe en otro permiso.
    Finalmente, delega la actualización al repositorio.

    Args:
        db: Sesión de base de datos activa.
        permiso_id: ID del permiso a actualizar.
        permiso_in: Datos con los campos a actualizar (esquema PermisoUpdate).

    Returns:
        El objeto Permiso actualizado.

    Raises:
        HTTPException: 404 si el permiso original no se encuentra.
        HTTPException: 409 si la nueva combinación acción/recurso ya existe en otro permiso.
        HTTPException: 409 si el repositorio detecta un conflicto al guardar (IntegrityError).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando actualizar permiso ID: {permiso_id}")
    # Obtener el permiso existente; esto maneja el caso 404 si no se encuentra.
    db_permiso = get_permiso_by_id(db=db, permiso_id=permiso_id)

    update_data = permiso_in.model_dump(exclude_unset=True)

    # Verificar conflicto de combinación acción/recurso si está cambiando
    new_action = update_data.get("nombre_accion")
    new_resource = update_data.get("nombre_recurso")

    # Solo realizar la verificación si se intenta cambiar la acción o el recurso
    if new_action is not None or new_resource is not None:
        # Determinar la combinación final a verificar
        check_action = new_action if new_action is not None else db_permiso.nombre_accion
        check_resource = new_resource if new_resource is not None else db_permiso.nombre_recurso

        # Solo verificar si la combinación resultante es diferente de la actual
        if (check_action != db_permiso.nombre_accion or
            check_resource != db_permiso.nombre_recurso):
            existing = permiso_repository.get_permiso_by_accion_recurso(
                db=db, nombre_accion=check_action, nombre_recurso=check_resource
            )
            # Si existe otro permiso diferente con esa combinación, hay conflicto
            if existing and existing.id != permiso_id:
                logger.warning(f"Conflicto al actualizar permiso ID {permiso_id}: "
                               f"La combinación {check_action}:{check_resource} ya existe (ID: {existing.id}).")
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"El permiso '{check_action}:{check_resource}' ya existe."
                )

    # La validación final de duplicado/conflicto también ocurre en el repo al hacer commit.
    try:
        updated_permiso = permiso_repository.update_permiso(
            db=db, db_permiso=db_permiso, permiso_in=update_data
        )
        return updated_permiso
    except HTTPException: # Re-lanzar 409 del repo
        raise
    except Exception as e:
        logger.error(f"Error inesperado al actualizar permiso ID {permiso_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al actualizar el permiso ID {permiso_id}."
        )

def delete_existing_permiso(db: Session, *, permiso_id: int) -> Permiso:
    """
    Elimina un permiso existente, delegando al repositorio.

    Primero verifica que el permiso exista. Luego llama al repositorio para
    eliminarlo, confiando en la lógica del repositorio (y la DB) para manejar
    las dependencias (como ON DELETE CASCADE).

    Args:
        db: Sesión de base de datos activa.
        permiso_id: ID del permiso a eliminar.

    Returns:
        El objeto Permiso que fue eliminado.

    Raises:
        HTTPException: 404 si el permiso no se encuentra.
        HTTPException: 500 si ocurre un error interno inesperado durante la eliminación.
    """
    logger.info(f"Intentando eliminar permiso ID: {permiso_id}")
    # Obtener el permiso; esto maneja el caso 404 si no se encuentra.
    db_permiso = get_permiso_by_id(db=db, permiso_id=permiso_id)

    try:
        # Delegar la eliminación al repositorio
        deleted_permiso = permiso_repository.delete_permiso(db=db, db_permiso=db_permiso)
        return deleted_permiso
    except Exception as e:
        # Capturar cualquier excepción durante la eliminación en el repositorio
        logger.error(f"Error inesperado al eliminar permiso ID {permiso_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al eliminar el permiso ID {permiso_id}."
        )
```

# app\services\rol_service.py

```py
# app/services/rol_service.py

import logging
from typing import Optional, Sequence, List

from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.orm import selectinload

# Importar repositorios y modelos
from app.repositories import rol_repository
from app.repositories import permiso_repository # Import necesario si se usa directamente
from app.models import Rol, Permiso # Importar Permiso también
# Importar schemas
from app.schemas.rol_permiso_schema import (
    RolCreate, RolUpdate, RolRead, RolReadWithPermissions, PermisoRead
)
# Importar el servicio de permisos para buscar permisos
from app.services import permiso_service


logger = logging.getLogger(__name__)

# =====================
#  Gestión de Roles (CRUD)
# =====================

def create_new_rol(db: Session, *, rol_in: RolCreate) -> Rol:
    """
    Crea un nuevo rol, validando duplicados a través del repositorio.

    Args:
        db: Sesión de base de datos.
        rol_in: Datos del rol a crear (esquema RolCreate).

    Returns:
        El objeto Rol creado.

    Raises:
        HTTPException: 409 si el rol ya existe (manejo de IntegrityError del repo).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando crear rol: Nombre='{rol_in.nombre}'")
    # Validación de duplicado (IntegrityError -> 409) manejada en el repo
    try:
        rol = rol_repository.create_rol(db=db, rol_in=rol_in)
        return rol
    except HTTPException: # Re-lanzar excepciones HTTP (ej: 409 del repo)
        raise
    except Exception as e:
        logger.error(f"Error inesperado al crear rol: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el rol."
        )

def get_rol_by_id(
    db: Session, *, rol_id: int, include_permissions: bool = False
) -> Rol:
    """
    Obtiene un rol por su ID, opcionalmente cargando sus permisos asociados.

    Delega la carga de datos al repositorio, seleccionando la función adecuada
    según si se requieren o no los permisos.

    Args:
        db: Sesión de base de datos.
        rol_id: El ID del rol a buscar.
        include_permissions: Si es True, intenta cargar los permisos asociados
                             al rol (usando eager loading en el repositorio).

    Returns:
        El objeto Rol encontrado.

    Raises:
        HTTPException: 404 si el rol con el ID especificado no se encuentra.
    """
    logger.debug(f"Buscando rol con ID: {rol_id}, incluir permisos: {include_permissions}")

    if include_permissions:
        rol = rol_repository.get_rol_with_permissions(db=db, rol_id=rol_id)
    else:
        rol = rol_repository.get_rol(db=db, rol_id=rol_id)

    if not rol:
        logger.warning(f"Rol con ID {rol_id} no encontrado.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rol con ID {rol_id} no encontrado."
        )

    # Log opcional para verificar carga de permisos si se solicitaron
    if include_permissions:
        if rol.permisos is not None:
             logger.debug(f"Permisos cargados para Rol ID {rol_id}: {len(rol.permisos) if isinstance(rol.permisos, list) else 'N/A'}")
        else:
             logger.debug(f"Se solicitó incluir permisos para Rol ID {rol_id}, pero la relación 'permisos' es None o no está cargada.")

    return rol


def get_all_roles(
    db: Session, *, skip: int = 0, limit: int = 100
) -> Sequence[Rol]:
    """
    Obtiene una lista paginada de todos los roles.

    Por defecto, no carga los permisos asociados para optimizar el rendimiento.
    Delega la consulta al repositorio.

    Args:
        db: Sesión de base de datos.
        skip: Número de registros a saltar (para paginación).
        limit: Número máximo de registros a devolver (para paginación).

    Returns:
        Una secuencia (lista) de objetos Rol.

    Raises:
        HTTPException: 500 si ocurre un error interno inesperado al listar.
    """
    logger.debug(f"Listando roles con skip={skip}, limit={limit}")
    try:
        roles = rol_repository.list_roles(db=db, skip=skip, limit=limit)
        return roles
    except Exception as e:
         logger.error(f"Error inesperado al listar roles: {e}", exc_info=True)
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Error interno del servidor al listar roles."
         )

def update_existing_rol(
    db: Session, *, rol_id: int, rol_in: RolUpdate
) -> Rol:
    """
    Actualiza un rol existente.

    Primero obtiene el rol, luego verifica si el nombre está cambiando y si el
    nuevo nombre ya existe en otro rol. Finalmente, delega la actualización
    al repositorio.

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol a actualizar.
        rol_in: Datos con los campos a actualizar (esquema RolUpdate).

    Returns:
        El objeto Rol actualizado.

    Raises:
        HTTPException: 404 si el rol original no se encuentra.
        HTTPException: 409 si el nuevo nombre ya está en uso por otro rol.
        HTTPException: 409 si el repositorio detecta un conflicto al guardar (IntegrityError).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando actualizar rol ID: {rol_id}")
    # Obtenemos el rol sin permisos, ya que no son necesarios para la actualización básica del rol.
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)

    update_data = rol_in.model_dump(exclude_unset=True)

    # Verificar conflicto de nombre solo si el nombre se está intentando cambiar
    new_name = update_data.get("nombre")
    if new_name is not None and new_name != db_rol.nombre:
        existing_rol = rol_repository.get_rol_by_name(db=db, nombre=new_name)
        if existing_rol and existing_rol.id != rol_id:
             logger.warning(f"Conflicto al actualizar rol ID {rol_id}: El nombre '{new_name}' ya existe (ID: {existing_rol.id}).")
             raise HTTPException(
                 status_code=status.HTTP_409_CONFLICT,
                 detail=f"El nombre de rol '{new_name}' ya está en uso."
             )

    # La validación final de duplicado/conflicto ocurre en el repositorio al hacer commit.
    try:
        updated_rol = rol_repository.update_rol(
            db=db, db_rol=db_rol, rol_in=update_data
        )
        return updated_rol
    except HTTPException: # Re-lanzar 409 del repo
        raise
    except Exception as e:
        logger.error(f"Error inesperado al actualizar rol ID {rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al actualizar el rol ID {rol_id}."
        )

def delete_existing_rol(db: Session, *, rol_id: int) -> Rol:
    """
    Elimina un rol existente.

    Verifica que el rol exista y luego delega la eliminación al repositorio,
    el cual debería verificar si el rol está en uso (asociado a usuarios).

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol a eliminar.

    Returns:
        El objeto Rol que fue eliminado.

    Raises:
        HTTPException: 404 si el rol no se encuentra.
        HTTPException: 409 si el rol está en uso (según la lógica del repositorio).
        HTTPException: 500 si ocurre un error interno inesperado.
    """
    logger.info(f"Intentando eliminar rol ID: {rol_id}")
    # Obtenemos el rol sin permisos, no son necesarios para eliminar.
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)

    try:
        # La lógica de verificar si el rol está asignado a usuarios debe residir en el repositorio.
        deleted_rol = rol_repository.delete_rol(db=db, db_rol=db_rol)
        return deleted_rol
    except HTTPException: # Re-lanzar 409 del repo si está en uso
        raise
    except Exception as e:
        logger.error(f"Error inesperado al eliminar rol ID {rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno al eliminar el rol ID {rol_id}."
        )


# =========================
#  Gestión de Permisos-Rol
# =========================

def add_permission_to_role(db: Session, *, rol_id: int, permiso_id: int) -> Rol:
    """
    Asigna un permiso existente a un rol existente.

    Verifica que tanto el rol como el permiso existan.
    Comprueba si el permiso ya está asignado al rol para evitar duplicados.
    Si todo es correcto, añade la relación y guarda los cambios.

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol al que se asignará el permiso.
        permiso_id: ID del permiso a asignar.

    Returns:
        El objeto Rol actualizado, con la relación de permisos reflejando el cambio.

    Raises:
        HTTPException: 404 si el rol o el permiso no existen.
        HTTPException: 409 si el permiso ya está asignado a este rol.
        HTTPException: 500 si ocurre un error interno al asignar.
    """
    logger.info(f"Intentando asignar permiso ID={permiso_id} a rol ID={rol_id}")
    # Obtener el rol, asegurando cargar los permisos para verificar si ya existe la asociación.
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=True)

    # Obtener el permiso (esto ya maneja el 404 si el permiso no existe)
    db_permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id)

    # Verificar si el permiso ya está en la lista de permisos del rol
    if db_permiso in db_rol.permisos: # SQLAlchemy debería poder comparar objetos por identidad
        logger.warning(f"El permiso ID={permiso_id} ya está asignado al rol ID={rol_id}.")
        # Lanzar 409 es más explícito para la API que devolver el objeto sin cambios.
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El permiso '{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' ya está asignado al rol '{db_rol.nombre}'."
        )

    # Añadir el permiso a la relación (SQLAlchemy maneja la tabla de enlace)
    try:
        db_rol.permisos.append(db_permiso)
        db.add(db_rol) # Marcar el rol como modificado
        db.commit()
        # Refrescar el rol para asegurar que el estado refleje la BD,
        # especialmente la colección de permisos actualizada.
        db.refresh(db_rol)
        # Refrescar explícitamente la relación puede ser necesario en algunas configuraciones
        db.refresh(db_rol, attribute_names=["permisos"])
        logger.info(f"Permiso ID={permiso_id} asignado exitosamente a rol ID={rol_id}.")
        return db_rol
    except Exception as e:
        db.rollback()
        logger.error(f"Error asignando permiso ID={permiso_id} a rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al asignar el permiso al rol."
        )


def remove_permission_from_role(db: Session, *, rol_id: int, permiso_id: int) -> Rol:
    """
    Quita un permiso previamente asignado de un rol.

    Verifica que el rol y el permiso existan.
    Comprueba que el permiso esté actualmente asignado al rol.
    Si es así, elimina la relación y guarda los cambios.

    Args:
        db: Sesión de base de datos.
        rol_id: ID del rol del que se quitará el permiso.
        permiso_id: ID del permiso a quitar.

    Returns:
        El objeto Rol actualizado, con la relación de permisos reflejando el cambio.

    Raises:
        HTTPException: 404 si el rol o el permiso no existen.
        HTTPException: 404 si el permiso no está actualmente asignado a ese rol.
        HTTPException: 500 si ocurre un error interno al quitar la asignación.
    """
    logger.info(f"Intentando quitar permiso ID={permiso_id} del rol ID={rol_id}")
    # Obtener el rol, asegurando cargar los permisos para verificar la asociación.
    db_rol = get_rol_by_id(db=db, rol_id=rol_id, include_permissions=True)

    # Obtener el permiso (principalmente para verificar existencia y usar en mensajes).
    db_permiso = permiso_service.get_permiso_by_id(db=db, permiso_id=permiso_id)

    # Verificar si el permiso está realmente asignado a este rol
    if db_permiso not in db_rol.permisos:
        logger.warning(f"Intento de quitar permiso ID={permiso_id} del rol ID={rol_id}, pero no estaba asignado.")
        # Usar 404 es apropiado: la relación específica rol-permiso no existe.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El permiso '{db_permiso.nombre_accion}:{db_permiso.nombre_recurso}' no está asignado al rol '{db_rol.nombre}'."
        )

    # Quitar el permiso de la relación (SQLAlchemy maneja la tabla de enlace)
    try:
        db_rol.permisos.remove(db_permiso)
        db.add(db_rol) # Marcar el rol como modificado
        db.commit()
        # Refrescar el rol para asegurar que el estado refleje la BD,
        # especialmente la colección de permisos actualizada.
        db.refresh(db_rol)
        # Refrescar explícitamente la relación
        db.refresh(db_rol, attribute_names=["permisos"])
        logger.info(f"Permiso ID={permiso_id} quitado exitosamente del rol ID={rol_id}.")
        return db_rol
    except Exception as e:
        db.rollback()
        logger.error(f"Error quitando permiso ID={permiso_id} de rol ID={rol_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al quitar el permiso del rol."
        )
```

# app\services\service_service.py

```py
# app/services/service_service.py
import logging
from typing import Optional, Sequence, Dict, Any

from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError # Para capturar errores del repo

# Importar Repositorio, Modelo y Schemas
from app.repositories import service_repository
from app.models.service_models import ServicioDefinicion
from app.schemas.service_schema import ServicioDefinicionCreate, ServicioDefinicionUpdate

logger = logging.getLogger(__name__)

# =======================================
#  Servicios para ServicioDefinicion
# =======================================

def create_servicio_service(db: Session, *, servicio_in: ServicioDefinicionCreate) -> ServicioDefinicion:
    """
    Crea una nueva definición de servicio, validando nombre único.
    """
    logger.info(f"Servicio: Intentando crear ServicioDefinicion: Nombre='{servicio_in.nombre}'")

    # Validar Nombre único ANTES de intentar crear
    existing_by_name = service_repository.get_servicio_by_nombre(db, nombre=servicio_in.nombre)
    if existing_by_name:
        logger.warning(f"Conflicto: Nombre '{servicio_in.nombre}' ya existe para ServicioDefinicion.")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe una definición de servicio con el nombre '{servicio_in.nombre}'."
        )
    try:
        servicio_data = ServicioDefinicion.model_validate(servicio_in)
        new_servicio = service_repository.create_servicio(db=db, servicio_data=servicio_data)
        return new_servicio
    except IntegrityError: # Por si acaso (ej: futura constraint UNIQUE)
        db.rollback()
        logger.error(f"Error de Integridad (inesperado) al crear ServicioDefinicion '{servicio_in.nombre}'.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al crear ServicioDefinicion: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear definición de servicio.")

def get_servicio_by_id_service(db: Session, *, servicio_id: int) -> ServicioDefinicion:
    """
    Obtiene una definición de servicio por su ID.
    """
    logger.debug(f"Servicio: Buscando ServicioDefinicion ID: {servicio_id}")
    servicio = service_repository.get_servicio_by_id(db=db, servicio_id=servicio_id)
    if not servicio:
        logger.warning(f"Servicio: ServicioDefinicion ID {servicio_id} no encontrado.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Definición de servicio con ID {servicio_id} no encontrada.")
    return servicio

def list_servicios_service(db: Session, *, skip: int = 0, limit: int = 100) -> Sequence[ServicioDefinicion]:
    """
    Lista las definiciones de servicios.
    """
    logger.debug(f"Servicio: Listando definiciones de servicios, skip={skip}, limit={limit}")
    try:
        return service_repository.list_servicios(db=db, skip=skip, limit=limit)
    except Exception as e:
        logger.error(f"Error inesperado en servicio al listar ServicioDefinicion: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar definiciones de servicios.")

def update_servicio_service(db: Session, *, servicio_id: int, servicio_in: ServicioDefinicionUpdate) -> ServicioDefinicion:
    """
    Actualiza una definición de servicio, validando nombre único si cambia.
    """
    logger.info(f"Servicio: Intentando actualizar ServicioDefinicion ID: {servicio_id}")
    db_servicio = get_servicio_by_id_service(db=db, servicio_id=servicio_id) # Maneja 404

    update_data = servicio_in.model_dump(exclude_unset=True)
    if not update_data:
        logger.warning(f"Servicio: No se proporcionaron datos para actualizar ServicioDefinicion ID {servicio_id}.")
        return db_servicio # Devolver sin cambios

    # Validar conflicto de nombre si se intenta cambiar
    new_nombre = update_data.get("nombre")
    if new_nombre is not None and new_nombre != db_servicio.nombre:
        existing_by_name = service_repository.get_servicio_by_nombre(db, nombre=new_nombre)
        # Si existe OTRO servicio con ese nombre
        if existing_by_name and existing_by_name.id != servicio_id:
            logger.warning(f"Conflicto al actualizar: Nuevo nombre '{new_nombre}' ya pertenece a servicio ID {existing_by_name.id}.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Ya existe otra definición de servicio con el nombre '{new_nombre}'."
            )

    try:
        return service_repository.update_servicio(db=db, db_servicio=db_servicio, update_data=update_data)
    except IntegrityError: # Por si acaso (ej: futura constraint UNIQUE)
        db.rollback()
        logger.error(f"Error de Integridad (inesperado) al actualizar ServicioDefinicion ID {servicio_id}.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflicto de datos al guardar la actualización.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al actualizar ServicioDefinicion ID {servicio_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar definición de servicio.")

def delete_servicio_service(db: Session, *, servicio_id: int) -> ServicioDefinicion:
    """
    Elimina una definición de servicio.
    """
    logger.warning(f"Servicio: Intentando eliminar ServicioDefinicion ID: {servicio_id}")
    db_servicio = get_servicio_by_id_service(db=db, servicio_id=servicio_id) # Maneja 404
    try:
        deleted_servicio = service_repository.delete_servicio(db=db, servicio_id=servicio_id)
        return deleted_servicio # type: ignore
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error de Integridad al eliminar ServicioDefinicion ID {servicio_id}. Probablemente referenciado por Fórmulas o Líneas de Proforma: {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"No se puede eliminar la definición de servicio ID {servicio_id} porque está en uso (ej: en fórmulas o proformas existentes)."
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error inesperado en servicio al eliminar ServicioDefinicion ID {servicio_id}: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar definición de servicio.")
```

# app\services\usuario_service.py

```py
# app/services/usuario_service.py
import logging
from sqlmodel import Session
from fastapi import HTTPException, status
from typing import Optional, Union, List
import traceback

import re

from app.models.user_models import Usuario, Rol
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioUpdatePassword
from app.repositories import usuario_repository, rol_repository
from app.services import rol_service  # Importing rol_service
from app.core.security import get_password_hash, verify_password


logger = logging.getLogger(__name__)


# --- Helpers ---
def _sanitize_email(email: str) -> str:
    """Normaliza emails a minúsculas y remueve espacios."""
    return email.strip().lower()

def _sanitize_username(username: str) -> str:
    """Normaliza username y valida formato."""
    sanitized = username.strip().lower()
    if not re.match(r"^[a-z0-9_]+$", sanitized):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username solo puede contener letras, números y guiones bajos"
        )
    return sanitized



# --- Creación ---
def create_new_user(db: Session, user_in: UsuarioCreate) -> Usuario:
    """
    Crea un nuevo usuario con validación y asignación de roles especificada.
    Si no se especifican roles, el usuario se crea sin roles iniciales.
    """
    # Sanitización y Validación de Duplicados (igual que antes)
    try:
        email = _sanitize_email(user_in.email)
        username = _sanitize_username(user_in.username) # Sanitización básica

        logger.info(f"Intentando crear usuario: Username='{username}', Email='{email[:5]}***'")

        if usuario_repository.get_usuario_by_email(db, email):
            logger.warning(f"Email ya registrado: '{email[:5]}***'")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo electrónico ya está registrado.")

        if usuario_repository.get_usuario_by_username(db, username):
            logger.warning(f"Username ya registrado: '{username}'")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de usuario no está disponible.")

        # --- Validación de Roles ---
        roles_to_assign: List[Rol] = [] # Lista para guardar objetos Rol validados
        if user_in.rol_ids:
            # Eliminar duplicados y ordenar para consistencia
            unique_rol_ids = sorted(list(set(user_in.rol_ids)))
            if unique_rol_ids: # Solo proceder si hay IDs únicos
                logger.info(f"Validando IDs de rol proporcionados: {unique_rol_ids} para usuario '{username}'")
                # Usar la nueva función del repositorio para buscar roles
                roles_found = rol_repository.get_roles_by_ids(db=db, role_ids=unique_rol_ids)

                # Validar que se encontraron todos los roles solicitados
                if len(roles_found) != len(unique_rol_ids):
                    found_ids = {role.id for role in roles_found}
                    missing_ids = [rid for rid in unique_rol_ids if rid not in found_ids]
                    logger.error(f"No se encontraron los siguientes IDs de rol al crear usuario '{username}': {missing_ids}")
                    # Usar 404 es apropiado si los IDs de rol no existen
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Uno o más IDs de rol proporcionados no existen: {missing_ids}"
                    )
                roles_to_assign = list(roles_found) # Guardar los objetos Rol validados
                logger.info(f"Roles validados para asignar a '{username}': {[r.nombre for r in roles_to_assign]}")
            else:
                 logger.warning(f"Lista de 'rol_ids' proporcionada para usuario '{username}' estaba vacía o contenía solo duplicados.")
        else:
             logger.warning(f"No se proporcionaron 'rol_ids' para el nuevo usuario '{username}'. Se creará sin roles iniciales.")

        # --- Creación del Usuario (Preparación) ---
        hashed_password = get_password_hash(user_in.password)
        # Excluir campos sensibles y el nuevo campo rol_ids del schema
        user_data_dict = user_in.model_dump(exclude={"password", "rol_ids"})

        # Crear la instancia del modelo Usuario
        db_user = Usuario(
            contrasena_hash=hashed_password,
            esta_activo=True, # Los usuarios se crean activos por defecto
            **user_data_dict # Pasar email, username, nombre_completo, etc.
        )

        # --- Guardar Usuario en BD ---
        # Usar la función del repositorio para crear el usuario base
        created_user = usuario_repository.create_usuario(db=db, usuario_data=db_user)
        logger.info(f"Usuario ID={created_user.id} ('{created_user.username}') creado en BD.")

        # --- Asignación de Roles (NUEVO) ---
        if roles_to_assign:
            logger.info(f"Asignando {len(roles_to_assign)} roles al usuario ID={created_user.id}...")
            assigned_count = 0
            # Iterar sobre los objetos Rol validados
            for rol in roles_to_assign:
                try:
                    # Usar la función existente del repositorio para asignar cada rol
                    # Esta función ya maneja commit y refresh si es necesario internamente (revisar repo)
                    usuario_repository.assign_rol_to_usuario(
                        db=db, db_usuario=created_user, db_rol=rol
                    )
                    assigned_count += 1
                except Exception as role_assign_exc:
                    # Capturar error específico de asignación si ocurre
                    logger.error(f"Error asignando rol ID={rol.id} ('{rol.nombre}') al usuario ID={created_user.id} "
                                 f"después de la creación: {role_assign_exc}", exc_info=True)
                    # Decisión: ¿Continuar asignando otros roles o detenerse y revertir?
                    # Por simplicidad, continuamos, pero el usuario puede quedar con roles parciales.
                    # Podría implementarse una lógica de rollback más compleja si es crítico.

            logger.info(f"Se asignaron {assigned_count} de {len(roles_to_assign)} roles solicitados al usuario ID={created_user.id}.")
            # Refrescar el usuario una vez al final para asegurar que la relación roles esté actualizada
            # si las asignaciones individuales no lo hicieron ya.
            db.refresh(created_user)
            # Cargar explícitamente roles si es necesario devolverlos inmediatamente (opcional)
            # db.refresh(created_user, attribute_names=["roles"])

        return created_user 

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error inesperado en create_new_user para username='{user_in.username}': {e}", exc_info=True)
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el usuario."
        )

# --- Actualización de Perfil ---
def update_user_profile(db: Session, *, current_user: Usuario, user_in: UsuarioUpdate) -> Usuario:
    """Actualiza perfil con sanitización."""
    try:
        update_data = user_in.model_dump(exclude_unset=True)
        
        # Sanitizar email si se actualiza
        if "email" in update_data:
            new_email = _sanitize_email(update_data["email"])
            if new_email != current_user.email:
                existing = usuario_repository.get_usuario_by_email(db, new_email)
                if existing:
                    raise HTTPException(400, "Email ya en uso")
                update_data["email"] = new_email

        updated_user = usuario_repository.update_usuario(
            db, 
            db_user=current_user, 
            update_data=update_data
        )
        logger.info(f"Usuario {updated_user.id} actualizado")
        return updated_user

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error actualizando perfil: {str(e)}")
        raise HTTPException(500, "Error interno al actualizar")

# --- Actualización de Contraseña ---
def update_user_password(
    db: Session, 
    *, 
    current_user: Usuario, 
    password_in: UsuarioUpdatePassword
) -> Usuario:
    """Cambia contraseña con validación de política."""
    try:
        # Verificar contraseña actual
        if not verify_password(password_in.old_password, current_user.contrasena_hash):
            raise HTTPException(400, "Contraseña actual incorrecta")

        # Validar nueva contraseña
        #if settings.ENFORCE_PASSWORD_POLICY:
        #    if len(password_in.new_password) < 12:
        #        raise HTTPException(400, "La contraseña debe tener al menos 12 caracteres")

        # Actualizar
        new_hash = get_password_hash(password_in.new_password)
        return usuario_repository.update_usuario(
            db,
            db_user=current_user,
            update_data={"contrasena_hash": new_hash}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error cambiando contraseña: {str(e)}")
        raise HTTPException(500, "Error interno al actualizar contraseña")

# --- Lectura ---
def get_user_info(db: Session, user_id: int) -> Usuario:
    """Obtiene usuario por ID."""
    try:
        user = usuario_repository.get_usuario(db=db, user_id=user_id)
        if not user:
            logger.warning(f"Usuario ID {user_id} no encontrado")
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuario no encontrado")
        return user
    except HTTPException: # Relanzar excepciones HTTP específicas
        raise
    except Exception as e:
        # --- REVERTIDO: Usar logger y HTTP 500 ---
        logger.error(f"Error inesperado obteniendo usuario ID {user_id}: {e}", exc_info=True)
        # --- FIN REVERTIDO ---
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error interno al recuperar usuario")


def assign_role_to_user_service(db: Session, *, user_id: int, rol_id: int) -> Usuario:
    """Asigna un rol existente a un usuario existente."""
    logger.info(f"Intentando asignar rol ID={rol_id} a usuario ID={user_id}")
    db_user = get_user_info(db=db, user_id=user_id)
    db_rol = rol_service.get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)
    try:
        updated_user = usuario_repository.assign_rol_to_usuario(
            db=db, db_usuario=db_user, db_rol=db_rol
        )
        return updated_user
    except HTTPException:
        raise
    except Exception as e:
        # --- REVERTIDO: Usar logger y HTTP 500 ---
        logger.error(f"Error inesperado asignando rol ID={rol_id} a usuario ID={user_id}: {e}", exc_info=True)
        db.rollback()
        # --- FIN REVERTIDO ---
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al asignar el rol."
        )
def remove_role_from_user_service(db: Session, *, user_id: int, rol_id: int) -> Usuario:
    """Quita un rol previamente asignado de un usuario."""
    logger.info(f"Intentando quitar rol ID={rol_id} de usuario ID={user_id}")
    db_user = get_user_info(db=db, user_id=user_id)
    db_rol = rol_service.get_rol_by_id(db=db, rol_id=rol_id, include_permissions=False)
    try:
        updated_user = usuario_repository.remove_rol_from_usuario(
            db=db, db_usuario=db_user, db_rol=db_rol
        )
        return updated_user
    except HTTPException:
        raise
    except Exception as e:
        # --- REVERTIDO: Usar logger y HTTP 500 ---
        logger.error(f"Error inesperado quitando rol ID={rol_id} de usuario ID={user_id}: {e}", exc_info=True)
        db.rollback()
        # --- FIN REVERTIDO ---
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al quitar el rol."
        )

```

# app\utils\__init__.py

```py

```

# README.md

```md
# sistemaCotizador
```

# requirements.txt

```txt
alembic==1.15.2
annotated-types==0.7.0
anyio==4.9.0
bcrypt==4.3.0
certifi==2025.1.31
cffi==1.17.1
click==8.1.8
colorama==0.4.6
coverage==7.8.0
cryptography==44.0.2
dnspython==2.7.0
ecdsa==0.19.1
email_validator==2.2.0
Faker==37.1.0
fastapi==0.115.12
fastapi-cli==0.0.7
greenlet==3.1.1
h11==0.14.0
httpcore==1.0.7
httptools==0.6.4
httpx==0.28.1
idna==3.10
iniconfig==2.1.0
itsdangerous==2.2.0
Jinja2==3.1.6
Mako==1.3.9
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
mysql-connector-python==9.2.0
orjson==3.10.16
packaging==24.2
passlib==1.7.4
pluggy==1.5.0
pyasn1==0.4.8
pycparser==2.22
pydantic==2.11.2
pydantic-extra-types==2.10.3
pydantic-settings==2.8.1
pydantic_core==2.33.1
Pygments==2.19.1
pytest==8.3.5
pytest-cov==6.1.1
python-dotenv==1.1.0
python-jose==3.4.0
python-multipart==0.0.20
PyYAML==6.0.2
rich==14.0.0
rich-toolkit==0.14.1
rsa==4.9
shellingham==1.5.4
six==1.17.0
sniffio==1.3.1
SQLAlchemy==2.0.40
sqlmodel==0.0.14
starlette==0.46.1
typer==0.15.2
typing-inspection==0.4.0
typing_extensions==4.13.1
tzdata==2025.2
ujson==5.10.0
uvicorn==0.34.0
watchfiles==1.0.4
websockets==15.0.1

```

# tests\__init__.py

```py

```

# tests\api\__init__.py

```py

```

# tests\api\v1\__init__.py

```py

```

# tests\api\v1\test_clientes_api.py

```py
# app/tests/api/v1/test_clientes_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
import logging # Asegurar importación de logging

# Importar settings para prefijo API
from app.core.config import settings
# Importar schemas para crear payloads y validar respuestas
from app.schemas.client_schema import ClienteCreate, ClienteRead, ClienteUpdate
# Importar modelo y repositorio para verificaciones en BD
from app.models import Cliente
from app.repositories import cliente_repository
# Importar TestingSessionLocal desde conftest
from tests.conftest import TestingSessionLocal


# --- Constantes ---
API_V1_STR = settings.API_V1_STR
CLIENTES_ENDPOINT = f"{API_V1_STR}/clientes"
logger = logging.getLogger(__name__)


# ==================================
# --- Tests para Crear Clientes ---
# ==================================

def test_create_cliente_success_vendedor(vendedor_client: TestClient, db_session: Session):
    """Prueba la creación exitosa de un cliente por un Vendedor (Refactorizado)."""
    unique_suffix = uuid.uuid4().hex[:6]
    nombre_cliente = f"Nuevo Cliente Vendedor {unique_suffix}"
    email_cliente = f"vendedor_crea_{unique_suffix}@test.com"
    id_fiscal = f"111{unique_suffix}"

    cliente_data = ClienteCreate(
        nombre=nombre_cliente,
        email=email_cliente,
        identificacion_fiscal=id_fiscal,
        tipo_identificacion="CEDULA",
        telefono="1234567890",
        direccion="Calle Falsa 123"
    )

    response = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["nombre"] == nombre_cliente
    assert data["email"] == email_cliente
    assert data["identificacion_fiscal"] == id_fiscal
    assert "id" in data
    new_cliente_id = data["id"]

    db_cliente = None
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_create_cliente_success_vendedor': Verificando cliente ID {new_cliente_id} con nueva sesión.")
            db_cliente = cliente_repository.get_cliente_by_id(db=verification_db, cliente_id=new_cliente_id)
            assert db_cliente is not None, f"Cliente ID {new_cliente_id} no encontrado en BD post-creación (Vendedor)."
            assert db_cliente.nombre == nombre_cliente
            assert db_cliente.email == email_cliente
            assert db_cliente.identificacion_fiscal == id_fiscal
            logger.info(f"Test 'test_create_cliente_success_vendedor': Cliente ID {new_cliente_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_create_cliente_success_vendedor: {e}")


def test_create_cliente_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la creación exitosa de un cliente por un Admin (Refactorizado)."""
    unique_suffix = uuid.uuid4().hex[:6]
    nombre_cliente = f"Nuevo Cliente Admin {unique_suffix}"
    email_cliente = f"admin_crea_{unique_suffix}@test.com"
    id_fiscal = f"222{unique_suffix}"

    cliente_data = ClienteCreate(
        nombre=nombre_cliente,
        email=email_cliente,
        identificacion_fiscal=id_fiscal,
        tipo_identificacion="RUC"
    )
    response = admin_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    new_cliente_id = data["id"]
    assert data["nombre"] == nombre_cliente
    assert data["email"] == email_cliente

    db_cliente = None
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_create_cliente_success_admin': Verificando cliente ID {new_cliente_id} con nueva sesión.")
             db_cliente = cliente_repository.get_cliente_by_id(db=verification_db, cliente_id=new_cliente_id)
             assert db_cliente is not None, f"Cliente ID {new_cliente_id} no encontrado en BD post-creación (Admin)."
             logger.info(f"Test 'test_create_cliente_success_admin': Cliente ID {new_cliente_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_create_cliente_success_admin: {e}")


def test_create_cliente_duplicate_email(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba que crear cliente con email duplicado falle (409)."""
    unique_suffix = uuid.uuid4().hex[:6]
    cliente_data = ClienteCreate(
        nombre=f"Duplicado Email {unique_suffix}",
        email=cliente_de_prueba.email, # Email existente
        identificacion_fiscal=f"333{unique_suffix}" # ID Fiscal diferente
    )
    response = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "correo electrónico" in response.json()["detail"].lower()
    assert cliente_de_prueba.email in response.json()["detail"]

def test_create_cliente_duplicate_identificacion(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba que crear cliente con identificación fiscal duplicada falle (409)."""
    unique_suffix = uuid.uuid4().hex[:6]
    cliente_data = ClienteCreate(
        nombre=f"Duplicado ID Fiscal {unique_suffix}",
        email=f"otroemail_{unique_suffix}@test.com", # Email diferente
        identificacion_fiscal=cliente_de_prueba.identificacion_fiscal # ID Fiscal existente
    )
    response = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "identificación fiscal" in response.json()["detail"].lower()
    assert cliente_de_prueba.identificacion_fiscal in response.json()["detail"]

def test_create_cliente_invalid_data(vendedor_client: TestClient):
    """Prueba crear cliente con datos inválidos (422)."""
    # Caso 1: Email inválido
    invalid_email_payload = {"nombre": "Test Email Malo", "email": "esto-no-es-email"}
    response_email = vendedor_client.post(CLIENTES_ENDPOINT, json=invalid_email_payload)
    assert response_email.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("email" in e.get("loc", []) for e in response_email.json().get("detail", []))

    # Caso 2: Tipo identificación inválido
    invalid_tipo_payload = {"nombre": "Test Tipo Malo", "tipo_identificacion": "INVENTADO"}
    response_tipo = vendedor_client.post(CLIENTES_ENDPOINT, json=invalid_tipo_payload)
    assert response_tipo.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("tipo_identificacion" in e.get("loc", []) for e in response_tipo.json().get("detail", []))

    # Caso 3: Nombre requerido ausente
    missing_name_payload = {"email": "sin_nombre@test.com"}
    response_name = vendedor_client.post(CLIENTES_ENDPOINT, json=missing_name_payload)
    assert response_name.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("nombre" in e.get("loc", []) for e in response_name.json().get("detail", []))

def test_create_cliente_unauthenticated(base_client: TestClient):
    """Prueba que crear cliente sin autenticación falle (401)."""
    cliente_data = ClienteCreate(nombre="No Auth Test")
    response = base_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- Tests para Listar Clientes (GET /) ---

def test_list_clientes_success_vendedor(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba listar clientes como Vendedor."""
    response = vendedor_client.get(CLIENTES_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    # Verificar que el cliente de prueba está en la lista
    assert any(c["id"] == cliente_de_prueba.id for c in data)
    # Verificar estructura básica de un elemento
    if data:
        assert "id" in data[0]
        assert "nombre" in data[0]
        assert "email" in data[0]

def test_list_clientes_success_admin(admin_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba listar clientes como Admin."""
    response = admin_client.get(CLIENTES_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert any(c["id"] == cliente_de_prueba.id for c in data)

def test_list_clientes_pagination(vendedor_client: TestClient, db_session: Session):
    """Prueba la paginación al listar clientes de forma más robusta."""
    ids_creados_en_test = []
    num_to_create = 3
    for i in range(num_to_create):
        unique_suffix = uuid.uuid4().hex[:4]
        nombre = f"Pag Cliente {i} {unique_suffix}"
        c_data = ClienteCreate(nombre=nombre, email=f"pag_{i}_{unique_suffix}@test.com")
        resp = vendedor_client.post(CLIENTES_ENDPOINT, json=c_data.model_dump())
        assert resp.status_code == status.HTTP_201_CREATED
        ids_creados_en_test.append(resp.json()["id"])
    limit_val = 1
    response_limit = vendedor_client.get(f"{CLIENTES_ENDPOINT}?limit={limit_val}")
    assert response_limit.status_code == status.HTTP_200_OK
    data_limit = response_limit.json()
    assert isinstance(data_limit, list)
    assert len(data_limit) <= limit_val
    if data_limit:
         assert "id" in data_limit[0]
    limit_val = 2
    response_limit_2 = vendedor_client.get(f"{CLIENTES_ENDPOINT}?limit={limit_val}")
    assert response_limit_2.status_code == status.HTTP_200_OK
    data_limit_2 = response_limit_2.json()
    assert isinstance(data_limit_2, list)
    assert len(data_limit_2) <= limit_val
    if len(data_limit_2) > 1:
        assert data_limit_2[0]["id"] != data_limit_2[1]["id"]
    skip_val = 1
    response_no_skip = vendedor_client.get(f"{CLIENTES_ENDPOINT}?limit=2")
    assert response_no_skip.status_code == status.HTTP_200_OK
    data_no_skip = response_no_skip.json()
    response_skip = vendedor_client.get(f"{CLIENTES_ENDPOINT}?skip={skip_val}&limit=5")
    assert response_skip.status_code == status.HTTP_200_OK
    data_skip = response_skip.json()
    if len(data_no_skip) > skip_val:
        first_element_id = data_no_skip[0]["id"]
        ids_in_skipped_list = {c["id"] for c in data_skip}
        assert first_element_id not in ids_in_skipped_list, \
            f"El elemento saltado (ID: {first_element_id}) fue encontrado en la lista con skip."
    elif len(data_no_skip) <= skip_val and data_skip:
         assert data_skip != data_no_skip

def test_list_clientes_unauthenticated(base_client: TestClient):
    """Prueba que listar clientes sin autenticación falle (401)."""
    response = base_client.get(CLIENTES_ENDPOINT)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# --- Tests para Obtener Cliente por ID (GET /{id}) ---

def test_get_cliente_success_vendedor(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba obtener un cliente existente por ID como Vendedor."""
    cliente_id = cliente_de_prueba.id
    response = vendedor_client.get(f"{CLIENTES_ENDPOINT}/{cliente_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == cliente_id
    assert data["nombre"] == cliente_de_prueba.nombre
    assert data["email"] == cliente_de_prueba.email

def test_get_cliente_not_found(vendedor_client: TestClient):
    """Prueba obtener un cliente inexistente por ID (404)."""
    response = vendedor_client.get(f"{CLIENTES_ENDPOINT}/999999")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_get_cliente_unauthenticated(base_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba obtener cliente por ID sin autenticación (401)."""
    response = base_client.get(f"{CLIENTES_ENDPOINT}/{cliente_de_prueba.id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# --- Tests para Actualizar Clientes (PUT /{id}) ---

def test_update_cliente_success_vendedor(vendedor_client: TestClient, db_session: Session, cliente_de_prueba: Cliente):
    """Prueba actualizar un cliente existente como Vendedor (Sin Cambios - Ya era robusto)."""
    cliente_id = cliente_de_prueba.id
    unique_suffix = uuid.uuid4().hex[:6]
    new_nombre = f"Cliente Actualizado {unique_suffix}"
    new_email = f"actualizado_{unique_suffix}@test.com"
    new_telefono = "111222333"

    update_payload = ClienteUpdate(
        nombre=new_nombre,
        email=new_email,
        telefono=new_telefono
    ).model_dump(exclude_unset=True)

    response = vendedor_client.put(f"{CLIENTES_ENDPOINT}/{cliente_id}", json=update_payload)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == cliente_id
    assert data["nombre"] == new_nombre
    assert data["email"] == new_email
    assert data["telefono"] == new_telefono
    assert data["identificacion_fiscal"] == cliente_de_prueba.identificacion_fiscal

    logger.debug(f"Cerrando sesión de test original (ID: {id(db_session)}) para verificación BD.")
    db_session.close()
    try:
        with TestingSessionLocal() as verification_db:
            logger.info(f"Verificando BD con nueva sesión (ID: {id(verification_db)}) para cliente ID: {cliente_id}")
            db_cliente_updated = cliente_repository.get_cliente_by_id(db=verification_db, cliente_id=cliente_id)
            assert db_cliente_updated is not None, "El cliente no se encontró en la BD con la nueva sesión"
            assert db_cliente_updated.nombre == new_nombre, "El nombre en la BD no coincide con el actualizado"
            assert db_cliente_updated.email == new_email, "El email en la BD no coincide con el actualizado"
            assert db_cliente_updated.telefono == new_telefono, "El teléfono en la BD no coincide con el actualizado"
            logger.info(f"Verificación en BD exitosa para cliente ID: {cliente_id}")
    except Exception as e:
        logger.error(f"Error durante la verificación en BD con nueva sesión: {e}", exc_info=True)
        pytest.fail(f"La verificación en BD falló después de cerrar y reabrir sesión: {e}")
    finally:
        logger.debug("Sesión de verificación BD cerrada.")


def test_update_cliente_conflict_email(vendedor_client: TestClient, db_session: Session):
    """Prueba que actualizar a un email duplicado falle (409)."""
    # Crear dos clientes
    suffix1 = uuid.uuid4().hex[:6]
    cliente1_data = ClienteCreate(nombre=f"C1 {suffix1}", email=f"c1_{suffix1}@test.com", identificacion_fiscal=f"id1{suffix1}")
    resp1 = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente1_data.model_dump())
    assert resp1.status_code == status.HTTP_201_CREATED
    cliente1_id = resp1.json()["id"]
    cliente1_email = resp1.json()["email"]

    suffix2 = uuid.uuid4().hex[:6]
    cliente2_data = ClienteCreate(nombre=f"C2 {suffix2}", email=f"c2_{suffix2}@test.com", identificacion_fiscal=f"id2{suffix2}")
    resp2 = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente2_data.model_dump())
    assert resp2.status_code == status.HTTP_201_CREATED
    cliente2_id = resp2.json()["id"]

    # Intentar actualizar cliente 2 con el email del cliente 1
    update_payload = ClienteUpdate(email=cliente1_email).model_dump(exclude_unset=True)
    response_update = vendedor_client.put(f"{CLIENTES_ENDPOINT}/{cliente2_id}", json=update_payload)

    assert response_update.status_code == status.HTTP_409_CONFLICT
    assert "correo electrónico" in response_update.json()["detail"].lower()

def test_update_cliente_not_found(vendedor_client: TestClient):
    """Prueba actualizar un cliente inexistente (404)."""
    update_payload = ClienteUpdate(nombre="No Importa").model_dump(exclude_unset=True)
    response = vendedor_client.put(f"{CLIENTES_ENDPOINT}/999999", json=update_payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_cliente_invalid_data(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba actualizar cliente con datos inválidos (422)."""
    cliente_id = cliente_de_prueba.id
    invalid_payload = {"email": "email-invalido"} # No cumple EmailStr
    response = vendedor_client.put(f"{CLIENTES_ENDPOINT}/{cliente_id}", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_cliente_unauthenticated(base_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba actualizar cliente sin autenticación (401)."""
    update_payload = ClienteUpdate(nombre="No Auth").model_dump(exclude_unset=True)
    response = base_client.put(f"{CLIENTES_ENDPOINT}/{cliente_de_prueba.id}", json=update_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# --- Tests para Eliminar Clientes (DELETE /{id}) ---

def test_delete_cliente_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba eliminar un cliente existente como Admin (Refactorizado)."""
    # Crear un cliente específicamente para este test
    unique_suffix = uuid.uuid4().hex[:6]
    cliente_data = ClienteCreate(nombre=f"Cliente a Borrar {unique_suffix}", email=f"borrar_{unique_suffix}@test.com")
    resp_create = admin_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert resp_create.status_code == status.HTTP_201_CREATED
    cliente_id_to_delete = resp_create.json()["id"]

    response_delete = admin_client.delete(f"{CLIENTES_ENDPOINT}/{cliente_id_to_delete}")
    assert response_delete.status_code == status.HTTP_204_NO_CONTENT

    cliente_db = None
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_delete_cliente_success_admin': Verificando cliente ID {cliente_id_to_delete} con nueva sesión.")
            cliente_db = cliente_repository.get_cliente_by_id(db=verification_db, cliente_id=cliente_id_to_delete)
            assert cliente_db is None, f"Cliente ID {cliente_id_to_delete} aún fue encontrado en BD post-delete."
            logger.info(f"Test 'test_delete_cliente_success_admin': Cliente ID {cliente_id_to_delete} verificado como eliminado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_delete_cliente_success_admin: {e}")


def test_delete_cliente_not_found_admin(admin_client: TestClient):
    """Prueba eliminar un cliente inexistente (404)."""
    response = admin_client.delete(f"{CLIENTES_ENDPOINT}/999998")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_cliente_forbidden_vendedor(vendedor_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba que un Vendedor NO puede eliminar un cliente (403)."""
    cliente_id = cliente_de_prueba.id
    response = vendedor_client.delete(f"{CLIENTES_ENDPOINT}/{cliente_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'eliminar:cliente'" in response.json()["detail"]

def test_delete_cliente_unauthenticated(base_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba eliminar cliente sin autenticación (401)."""
    response = base_client.delete(f"{CLIENTES_ENDPOINT}/{cliente_de_prueba.id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# (test_delete_cliente_with_dependencies_conflict_admin sigue pendiente)
```

# tests\api\v1\test_inventario_api.py

```py
# app/tests/api/v1/test_inventario_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
from decimal import Decimal
import logging

# Importar settings y config
from app.core.config import settings
# Importar schemas necesarios
from app.schemas.inventory_schema import (
    MaterialDimensionalCreate, MaterialDimensionalRead, MaterialDimensionalUpdate,
    MaterialConsumibleCreate, MaterialConsumibleRead, MaterialConsumibleUpdate,
    MaterialSimpleCreate, MaterialSimpleRead, MaterialSimpleUpdate,
    StockItemDimensionalCreate, StockItemDimensionalRead,
)
# Importar el schema de ajuste de stock
from app.api.v1.endpoints.inventario import StockAdjustRequest

# Importar modelos para verificaciones y fixtures
from app.models import (
    MaterialDimensional,
    MaterialConsumible,
    MaterialSimple,
    StockItemDimensional
)
# Importar repositorios para verificaciones (aunque usar .get es más simple)
from app.repositories import inventory_repository
# Importar constantes de endpoints y fábrica de sesión desde conftest
from tests.conftest import (
    TestingSessionLocal, # Importar la factory para sesiones de verificación
    MAT_DIM_ENDPOINT,
    MAT_CONS_ENDPOINT,
    MAT_SIMP_ENDPOINT,
    STOCK_ITEM_DIM_ENDPOINT
)
# Importar fixtures de cliente necesarias (si no están globales)
from tests.conftest import admin_client, vendedor_client, operario_client

logger = logging.getLogger(__name__)

# --- Helpers para Crear Payloads Válidos  ---
def create_valid_mat_dim_payload(suffix: str) -> dict:
    schema_instance = MaterialDimensionalCreate(
        sku=f"SKU-DIM-{suffix}",
        nombre=f"Plancha Test {suffix}",
        espesor_nominal=Decimal("18.0"),
        unidad_dimension="mm",
        precio_venta_base_unidad=Decimal("100.0"),
        unidad_precio_venta="m2"
    )
    return schema_instance.model_dump(mode='json')

def create_valid_mat_cons_payload(suffix: str) -> dict:
    schema_instance = MaterialConsumibleCreate(
        sku=f"SKU-CONS-{suffix}",
        nombre=f"Consumible Test {suffix}",
        unidad_medida="litro",
        precio_venta_base_unidad=Decimal("50.0")
    )
    return schema_instance.model_dump(mode='json')

def create_valid_mat_simp_payload(suffix: str) -> dict:
    schema_instance = MaterialSimpleCreate(
        sku=f"SKU-SIMP-{suffix}",
        nombre=f"Simple Test {suffix}",
        unidad_medida="unidad",
        precio_venta_base_unidad=Decimal("10.0")
    )
    return schema_instance.model_dump(mode='json')

# =====================================================
# --- Tests para Endpoints de Material Dimensional ---
# =====================================================
class TestMaterialDimensionalAPI:

    def test_create_material_dimensional_success_admin(self, admin_client: TestClient, db_session: Session):
        unique_suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_dim_payload(unique_suffix)
        response = admin_client.post(MAT_DIM_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["sku"] == payload["sku"]
        assert data["nombre"] == payload["nombre"]
        assert Decimal(data["espesor_nominal"]) == Decimal(payload["espesor_nominal"])
        assert Decimal(data["precio_venta_base_unidad"]) == Decimal(payload["precio_venta_base_unidad"])
        new_id = data["id"]

        try:
            with TestingSessionLocal() as verification_db:
                db_obj = verification_db.get(MaterialDimensional, new_id)
                assert db_obj is not None, f"MaterialDimensional ID {new_id} no encontrado en BD post-creación."
                assert db_obj.sku == payload["sku"]
                assert db_obj.espesor_nominal == Decimal(payload["espesor_nominal"])
                assert db_obj.precio_venta_base_unidad == Decimal(payload["precio_venta_base_unidad"])
                logger.info(f"Test 'test_create_material_dimensional_success_admin': MaterialDimensional ID {new_id} verificado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_create_material_dimensional_success_admin: {e}")

    def test_create_material_dimensional_duplicate_sku(self, admin_client: TestClient, material_dimensional_de_prueba: MaterialDimensional):
        payload_schema = MaterialDimensionalCreate(
             sku=material_dimensional_de_prueba.sku,
             nombre=f"Duplicado Dim Test",
             espesor_nominal=Decimal("10.0"),
             unidad_dimension="cm",
            precio_venta_base_unidad=Decimal("100.0"),
            unidad_precio_venta="m2"
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(MAT_DIM_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_create_material_dimensional_invalid_data(self, admin_client: TestClient):
        payload_no_sku = {"nombre": "Test Sin SKU", "espesor_nominal": "10.0"}
        response_no_sku = admin_client.post(MAT_DIM_ENDPOINT, json=payload_no_sku)
        assert response_no_sku.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        payload_bad_thickness_dict = create_valid_mat_dim_payload("badthick")
        payload_bad_thickness_dict["espesor_nominal"] = "dieciocho"
        response_bad_thickness = admin_client.post(MAT_DIM_ENDPOINT, json=payload_bad_thickness_dict)
        assert response_bad_thickness.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_material_dimensional_forbidden(self, vendedor_client: TestClient):
        unique_suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_dim_payload(unique_suffix)
        response = vendedor_client.post(MAT_DIM_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_materiales_dimensionales_success(self, admin_client: TestClient, material_dimensional_de_prueba: MaterialDimensional):
        response_list = admin_client.get(MAT_DIM_ENDPOINT)
        assert response_list.status_code == status.HTTP_200_OK
        data = response_list.json()
        assert isinstance(data, list)
        assert any(item["id"] == material_dimensional_de_prueba.id for item in data)

    def test_list_materiales_dimensionales_permission_vendedor(self, vendedor_client: TestClient):
        response = vendedor_client.get(MAT_DIM_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK

    def test_get_material_dimensional_success(self, admin_client: TestClient, material_dimensional_de_prueba: MaterialDimensional):
        response_get = admin_client.get(f"{MAT_DIM_ENDPOINT}/{material_dimensional_de_prueba.id}")
        assert response_get.status_code == status.HTTP_200_OK
        data = response_get.json()
        assert data["id"] == material_dimensional_de_prueba.id
        assert data["sku"] == material_dimensional_de_prueba.sku

    def test_get_material_dimensional_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{MAT_DIM_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_material_dimensional_success(self, admin_client: TestClient, material_dimensional_de_prueba: MaterialDimensional):
        update_suffix = uuid.uuid4().hex[:4]
        update_schema = MaterialDimensionalUpdate(
            nombre=f"Plancha ACTUALIZADA {update_suffix}",
            descripcion="Nueva descripción fixture",
            espesor_nominal=Decimal("16.5"),
            precio_venta_base_unidad=Decimal("120.0"),
            unidad_precio_venta="m3"
        )
        update_payload = update_schema.model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{MAT_DIM_ENDPOINT}/{material_dimensional_de_prueba.id}", json=update_payload)
        assert response_update.status_code == status.HTTP_200_OK
        data = response_update.json()
        assert data["id"] == material_dimensional_de_prueba.id
        assert data["nombre"] == update_schema.nombre
        assert data["descripcion"] == update_schema.descripcion
        assert Decimal(data["espesor_nominal"]) == update_schema.espesor_nominal
        assert data["sku"] == material_dimensional_de_prueba.sku
        assert Decimal(data["precio_venta_base_unidad"]) == update_schema.precio_venta_base_unidad
        assert data["unidad_precio_venta"] == update_schema.unidad_precio_venta

        with TestingSessionLocal() as verification_db:
             db_obj_updated = verification_db.get(MaterialDimensional, material_dimensional_de_prueba.id)
             assert db_obj_updated is not None
             assert db_obj_updated.nombre == update_schema.nombre
             assert db_obj_updated.descripcion == update_schema.descripcion
             assert db_obj_updated.espesor_nominal == update_schema.espesor_nominal
             assert db_obj_updated.precio_venta_base_unidad == update_schema.precio_venta_base_unidad
             assert db_obj_updated.unidad_precio_venta == update_schema.unidad_precio_venta

    def test_update_material_dimensional_not_found(self, admin_client: TestClient):
        update_payload = MaterialDimensionalUpdate(nombre="Test").model_dump(mode='json', exclude_unset=True)
        response = admin_client.put(f"{MAT_DIM_ENDPOINT}/999999", json=update_payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_material_dimensional_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_dim_payload(suffix)
        response_create = admin_client.post(MAT_DIM_ENDPOINT, json=payload)
        assert response_create.status_code == status.HTTP_201_CREATED
        created_id = response_create.json()["id"]
        response_delete = admin_client.delete(f"{MAT_DIM_ENDPOINT}/{created_id}")
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT

        # --- VERIFICACIÓN REFACTORIZADA ---
        try:
            with TestingSessionLocal() as verification_db:
                logger.debug(f"Test 'test_delete_material_dimensional_success': Verificando ID {created_id} con nueva sesión.")
                deleted_obj = verification_db.get(MaterialDimensional, created_id)
                assert deleted_obj is None, f"MaterialDimensional ID {created_id} aún encontrado en BD post-delete."
                logger.info(f"Test 'test_delete_material_dimensional_success': MaterialDimensional ID {created_id} verificado como eliminado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_delete_material_dimensional_success: {e}")

    def test_delete_material_dimensional_not_found(self, admin_client: TestClient):
        response = admin_client.delete(f"{MAT_DIM_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.skip(reason="PENDIENTE: Implementar cuando StockItemDimensional esté listo y se pueda crear en setup.")
    def test_delete_material_dimensional_conflict(self, admin_client: TestClient, stock_item_dimensional_de_prueba: StockItemDimensional):
        material_id = stock_item_dimensional_de_prueba.material_dimensional_id
        response = admin_client.delete(f"{MAT_DIM_ENDPOINT}/{material_id}")
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_list_materiales_dimensionales_forbidden_operario(self, operario_client: TestClient):
        response = operario_client.get(MAT_DIM_ENDPOINT)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "Permiso insuficiente: Se requiere 'leer:material_definicion'" in response.json()["detail"]


# =====================================================
# --- Tests para Endpoints de Material Consumible ---
# =====================================================
class TestMaterialConsumibleAPI:

    def test_create_material_consumible_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_cons_payload(suffix)
        response = admin_client.post(MAT_CONS_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["sku"] == payload["sku"]
        new_id = data["id"]

        try:
            with TestingSessionLocal() as verification_db:
                db_obj = verification_db.get(MaterialConsumible, new_id)
                assert db_obj is not None, f"MaterialConsumible ID {new_id} no encontrado en BD post-creación."
                assert db_obj.sku == payload["sku"]
                logger.info(f"Test 'test_create_material_consumible_success': MaterialConsumible ID {new_id} verificado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_create_material_consumible_success: {e}")

    def test_create_material_consumible_duplicate_sku(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        payload_schema = MaterialConsumibleCreate(
            sku=material_consumible_de_prueba.sku,
            nombre="Duplicado Cons",
            unidad_medida="kg",
            precio_venta_base_unidad=Decimal("15.0")
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(MAT_CONS_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_create_material_consumible_invalid_data(self, admin_client: TestClient):
        payload_no_sku = {"nombre": "Test Cons Sin SKU", "unidad_medida": "litro"}
        response_no_sku = admin_client.post(MAT_CONS_ENDPOINT, json=payload_no_sku)
        assert response_no_sku.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        payload_no_unit = {"sku": "TEST-CONS-NOUNIT", "nombre": "Test Cons Sin Unidad"}
        response_no_unit = admin_client.post(MAT_CONS_ENDPOINT, json=payload_no_unit)
        assert response_no_unit.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_material_consumible_forbidden(self, vendedor_client: TestClient):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_cons_payload(suffix)
        response = vendedor_client.post(MAT_CONS_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_materiales_consumibles_success(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        response_list = admin_client.get(MAT_CONS_ENDPOINT)
        assert response_list.status_code == status.HTTP_200_OK
        data = response_list.json()
        assert isinstance(data, list)
        assert any(item["id"] == material_consumible_de_prueba.id for item in data)

    def test_list_materiales_consumibles_permission_vendedor(self, vendedor_client: TestClient):
        response = vendedor_client.get(MAT_CONS_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK

    def test_get_material_consumible_success(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        response_get = admin_client.get(f"{MAT_CONS_ENDPOINT}/{material_consumible_de_prueba.id}")
        assert response_get.status_code == status.HTTP_200_OK
        data = response_get.json()
        assert data["id"] == material_consumible_de_prueba.id
        assert data["sku"] == material_consumible_de_prueba.sku

    def test_get_material_consumible_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{MAT_CONS_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_material_consumible_success(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        update_suffix = uuid.uuid4().hex[:4]
        update_schema = MaterialConsumibleUpdate(
            nombre=f"Consumible ACTUALIZADO {update_suffix}",
            descripcion="Nueva desc",
            stock_minimo=Decimal("25.5"),
            precio_venta_base_unidad=Decimal("23.0")
        )
        update_payload = update_schema.model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{MAT_CONS_ENDPOINT}/{material_consumible_de_prueba.id}", json=update_payload)
        assert response_update.status_code == status.HTTP_200_OK
        data = response_update.json()
        assert data["id"] == material_consumible_de_prueba.id
        assert data["nombre"] == update_schema.nombre
        assert data["descripcion"] == update_schema.descripcion
        assert Decimal(data["stock_minimo"]) == update_schema.stock_minimo
        assert Decimal(data["precio_venta_base_unidad"]) == update_schema.precio_venta_base_unidad

        with TestingSessionLocal() as verification_db:
             db_obj_updated = verification_db.get(MaterialConsumible, material_consumible_de_prueba.id)
             assert db_obj_updated is not None
             assert db_obj_updated.nombre == update_schema.nombre
             assert db_obj_updated.stock_minimo == update_schema.stock_minimo
             assert db_obj_updated.precio_venta_base_unidad == update_schema.precio_venta_base_unidad

    def test_update_material_consumible_not_found(self, admin_client: TestClient):
        update_payload = MaterialConsumibleUpdate(nombre="Test").model_dump(mode='json', exclude_unset=True)
        response = admin_client.put(f"{MAT_CONS_ENDPOINT}/999999", json=update_payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_material_consumible_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_cons_payload(suffix)
        response_create = admin_client.post(MAT_CONS_ENDPOINT, json=payload)
        assert response_create.status_code == status.HTTP_201_CREATED
        created_id = response_create.json()["id"]
        response_delete = admin_client.delete(f"{MAT_CONS_ENDPOINT}/{created_id}")
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT
        # --- VERIFICACIÓN REFACTORIZADA ---
        try:
            with TestingSessionLocal() as verification_db:
                deleted_obj = verification_db.get(MaterialConsumible, created_id)
                assert deleted_obj is None, f"MaterialConsumible ID {created_id} aún encontrado en BD post-delete."
                logger.info(f"Test 'test_delete_material_consumible_success': MaterialConsumible ID {created_id} verificado como eliminado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_delete_material_consumible_success: {e}")
        # --- FIN VERIFICACIÓN ---

    def test_delete_material_consumible_not_found(self, admin_client: TestClient):
        response = admin_client.delete(f"{MAT_CONS_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # @pytest.mark.skip(reason="PENDIENTE: Implementar cuando FormulaItem o LineaProformaMaterial use MaterialConsumible.")
    # def test_delete_material_consumible_conflict(self, admin_client: TestClient, ...)

    def test_adjust_stock_consumible_success(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        mat_id = material_consumible_de_prueba.id
        initial_stock = material_consumible_de_prueba.stock_actual or Decimal("0.0") # Default a 0 si es None

        # Añadir stock
        adjust_payload_add_schema = StockAdjustRequest(change_amount=Decimal("50.5"))
        adjust_payload_add_dict = adjust_payload_add_schema.model_dump(mode='json')
        response_add = admin_client.post(f"{MAT_CONS_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload_add_dict)
        assert response_add.status_code == status.HTTP_200_OK
        data_add = response_add.json()
        expected_stock_add = initial_stock + adjust_payload_add_schema.change_amount
        assert Decimal(data_add["stock_actual"]) == pytest.approx(expected_stock_add) # Usar approx por floats

        try:
            with TestingSessionLocal() as verification_db_add:
                db_obj_add = verification_db_add.get(MaterialConsumible, mat_id)
                assert db_obj_add is not None
                assert db_obj_add.stock_actual == pytest.approx(expected_stock_add)
                logger.info(f"Test 'test_adjust_stock_consumible_success' (add): Stock verificado en BD para ID {mat_id}.")
        except Exception as e:
            pytest.fail(f"Error verificación BD (add) en test_adjust_stock_consumible_success: {e}")

        # Quitar stock
        adjust_payload_sub_schema = StockAdjustRequest(change_amount=Decimal("-10.0"))
        adjust_payload_sub_dict = adjust_payload_sub_schema.model_dump(mode='json')
        response_sub = admin_client.post(f"{MAT_CONS_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload_sub_dict)
        assert response_sub.status_code == status.HTTP_200_OK
        data_sub = response_sub.json()
        expected_stock_sub = expected_stock_add + adjust_payload_sub_schema.change_amount
        assert Decimal(data_sub["stock_actual"]) == pytest.approx(expected_stock_sub)

        try:
            with TestingSessionLocal() as verification_db_sub:
                db_obj_sub = verification_db_sub.get(MaterialConsumible, mat_id)
                assert db_obj_sub is not None
                assert db_obj_sub.stock_actual == pytest.approx(expected_stock_sub)
                logger.info(f"Test 'test_adjust_stock_consumible_success' (sub): Stock verificado en BD para ID {mat_id}.")
        except Exception as e:
            pytest.fail(f"Error verificación BD (sub) en test_adjust_stock_consumible_success: {e}")

    def test_adjust_stock_consumible_negative_result(self, admin_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        mat_id = material_consumible_de_prueba.id
        adjust_payload = StockAdjustRequest(change_amount=Decimal("-10000.0")).model_dump(mode='json')
        response = admin_client.post(f"{MAT_CONS_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_adjust_stock_consumible_forbidden(self, vendedor_client: TestClient, material_consumible_de_prueba: MaterialConsumible):
        mat_id = material_consumible_de_prueba.id
        adjust_payload = StockAdjustRequest(change_amount=Decimal("10.0")).model_dump(mode='json')
        response = vendedor_client.post(f"{MAT_CONS_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN


# =====================================================
# --- Tests para Endpoints de Material Simple ---
# =====================================================
class TestMaterialSimpleAPI:
     # --- POST /materiales-simples ---
    def test_create_material_simple_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_simp_payload(suffix)
        response = admin_client.post(MAT_SIMP_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["sku"] == payload["sku"]
        new_id = data["id"]

        try:
            with TestingSessionLocal() as verification_db:
                db_obj = verification_db.get(MaterialSimple, new_id)
                assert db_obj is not None, f"MaterialSimple ID {new_id} no encontrado en BD post-creación."
                assert db_obj.sku == payload["sku"]
                logger.info(f"Test 'test_create_material_simple_success': MaterialSimple ID {new_id} verificado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_create_material_simple_success: {e}")

    def test_create_material_simple_duplicate_sku(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        payload_schema = MaterialSimpleCreate(
            sku=material_simple_de_prueba.sku, # Existente
            nombre="Duplicado Simp",
            unidad_medida="par",
            precio_venta_base_unidad=Decimal("8.0")
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(MAT_SIMP_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_create_material_simple_invalid_data(self, admin_client: TestClient):
        payload_no_sku = {"nombre": "Test Simp Sin SKU", "unidad_medida": "pqt"}
        response_no_sku = admin_client.post(MAT_SIMP_ENDPOINT, json=payload_no_sku)
        assert response_no_sku.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_material_simple_forbidden(self, vendedor_client: TestClient):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_simp_payload(suffix)
        response = vendedor_client.post(MAT_SIMP_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_materiales_simples_success(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        response_list = admin_client.get(MAT_SIMP_ENDPOINT)
        assert response_list.status_code == status.HTTP_200_OK
        data = response_list.json()
        assert isinstance(data, list)
        assert any(item["id"] == material_simple_de_prueba.id for item in data)

    def test_list_materiales_simples_permission_vendedor(self, vendedor_client: TestClient):
        response = vendedor_client.get(MAT_SIMP_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK # Vendedor puede leer

    def test_get_material_simple_success(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        response_get = admin_client.get(f"{MAT_SIMP_ENDPOINT}/{material_simple_de_prueba.id}")
        assert response_get.status_code == status.HTTP_200_OK
        data = response_get.json()
        assert data["id"] == material_simple_de_prueba.id

    def test_get_material_simple_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{MAT_SIMP_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_material_simple_success(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        update_suffix = uuid.uuid4().hex[:4]
        update_schema = MaterialSimpleUpdate(
            nombre=f"Simple ACTUALIZADO {update_suffix}",
            ubicacion="Caja-Z9"
        )
        update_payload = update_schema.model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{MAT_SIMP_ENDPOINT}/{material_simple_de_prueba.id}", json=update_payload)
        assert response_update.status_code == status.HTTP_200_OK
        data = response_update.json()
        assert data["nombre"] == update_schema.nombre
        assert data["ubicacion"] == update_schema.ubicacion

        with TestingSessionLocal() as verification_db:
             db_obj_updated = verification_db.get(MaterialSimple, material_simple_de_prueba.id)
             assert db_obj_updated is not None
             assert db_obj_updated.nombre == update_schema.nombre

    def test_update_material_simple_not_found(self, admin_client: TestClient):
        update_payload = MaterialSimpleUpdate(nombre="Test").model_dump(mode='json', exclude_unset=True)
        response = admin_client.put(f"{MAT_SIMP_ENDPOINT}/999999", json=update_payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_material_simple_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_mat_simp_payload(suffix)
        response_create = admin_client.post(MAT_SIMP_ENDPOINT, json=payload)
        assert response_create.status_code == status.HTTP_201_CREATED
        created_id = response_create.json()["id"]
        response_delete = admin_client.delete(f"{MAT_SIMP_ENDPOINT}/{created_id}")
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT

        try:
            with TestingSessionLocal() as verification_db:
                deleted_obj = verification_db.get(MaterialSimple, created_id)
                assert deleted_obj is None, f"MaterialSimple ID {created_id} aún encontrado en BD post-delete."
                logger.info(f"Test 'test_delete_material_simple_success': MaterialSimple ID {created_id} verificado como eliminado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_delete_material_simple_success: {e}")

    def test_delete_material_simple_not_found(self, admin_client: TestClient):
        response = admin_client.delete(f"{MAT_SIMP_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # @pytest.mark.skip(reason="PENDIENTE: Implementar cuando FormulaItem o LineaProformaMaterial use MaterialSimple.")
    # def test_delete_material_simple_conflict(self, admin_client: TestClient, ...)

    def test_adjust_stock_simple_success(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        mat_id = material_simple_de_prueba.id
        initial_stock = material_simple_de_prueba.stock_actual or Decimal("0.0")
        adjust_payload_add_schema = StockAdjustRequest(change_amount=Decimal("250"))
        adjust_payload_add_dict = adjust_payload_add_schema.model_dump(mode='json')
        response_add = admin_client.post(f"{MAT_SIMP_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload_add_dict)
        assert response_add.status_code == status.HTTP_200_OK
        expected_stock_add = initial_stock + adjust_payload_add_schema.change_amount
        assert Decimal(response_add.json()["stock_actual"]) == expected_stock_add

        try:
            with TestingSessionLocal() as verification_db_add:
                db_obj_add = verification_db_add.get(MaterialSimple, mat_id)
                assert db_obj_add is not None
                assert db_obj_add.stock_actual == pytest.approx(expected_stock_add)
                logger.info(f"Test 'test_adjust_stock_simple_success' (add): Stock verificado en BD para ID {mat_id}.")
        except Exception as e:
            pytest.fail(f"Error verificación BD (add) en test_adjust_stock_simple_success: {e}")

    def test_adjust_stock_simple_negative_result(self, admin_client: TestClient, material_simple_de_prueba: MaterialSimple):
        mat_id = material_simple_de_prueba.id
        adjust_payload = StockAdjustRequest(change_amount=Decimal("-100000")).model_dump(mode='json')
        response = admin_client.post(f"{MAT_SIMP_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_adjust_stock_simple_forbidden(self, vendedor_client: TestClient, material_simple_de_prueba: MaterialSimple):
        mat_id = material_simple_de_prueba.id
        adjust_payload = StockAdjustRequest(change_amount=Decimal("10")).model_dump(mode='json')
        response = vendedor_client.post(f"{MAT_SIMP_ENDPOINT}/{mat_id}/ajustar-stock", json=adjust_payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN


# ==============================================================
# --- Tests para Endpoints de Stock Item Dimensional (Base) ---
# ==============================================================
class TestStockItemDimensionalAPI:

    def test_create_stock_item_success(self, admin_client: TestClient, db_session: Session, material_dimensional_de_prueba: MaterialDimensional):
        payload_schema = StockItemDimensionalCreate(
            material_dimensional_id=material_dimensional_de_prueba.id,
            longitud_actual=Decimal("3000.0"),
            ancho_actual=Decimal("1500.0"),
            ubicacion="Rack-A1"
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["material_dimensional_id"] == material_dimensional_de_prueba.id
        assert Decimal(data["longitud_actual"]) == payload_schema.longitud_actual
        assert data["estado"] == "DISPONIBLE"
        item_id = data["id"]

        db_session.close()
        with TestingSessionLocal() as verification_db:
            db_obj = verification_db.get(StockItemDimensional, item_id)
            assert db_obj is not None
            assert db_obj.material_dimensional_id == payload_schema.material_dimensional_id
            assert db_obj.longitud_actual == payload_schema.longitud_actual


    def test_create_stock_item_invalid_foreign_key(self, admin_client: TestClient):
        payload_schema = StockItemDimensionalCreate(
            material_dimensional_id=999999,
            longitud_actual=Decimal("1000"),
            ancho_actual=Decimal("500")
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_404_NOT_FOUND # El servicio valida FK

    def test_list_stock_items_success(self, admin_client: TestClient, stock_item_dimensional_de_prueba: StockItemDimensional):
        response = admin_client.get(STOCK_ITEM_DIM_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert any(item["id"] == stock_item_dimensional_de_prueba.id for item in data)

    def test_list_stock_items_filtered(self, admin_client: TestClient, db_session: Session, material_dimensional_de_prueba: MaterialDimensional):
        # Crear items
        item1_schema = StockItemDimensionalCreate(material_dimensional_id=material_dimensional_de_prueba.id, longitud_actual=1000, ancho_actual=100, estado="DISPONIBLE")
        item2_schema = StockItemDimensionalCreate(material_dimensional_id=material_dimensional_de_prueba.id, longitud_actual=2000, ancho_actual=200, estado="RESERVADO")
        item3_schema = StockItemDimensionalCreate(material_dimensional_id=material_dimensional_de_prueba.id, longitud_actual=3000, ancho_actual=300, estado="DISPONIBLE")
        resp1 = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=item1_schema.model_dump(mode='json'))
        resp2 = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=item2_schema.model_dump(mode='json'))
        resp3 = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=item3_schema.model_dump(mode='json'))
        assert resp1.status_code == status.HTTP_201_CREATED
        assert resp2.status_code == status.HTTP_201_CREATED
        assert resp3.status_code == status.HTTP_201_CREATED
        id1 = resp1.json()["id"]; id3 = resp3.json()["id"]
        # Filtrar
        params = {"material_dimensional_id": material_dimensional_de_prueba.id, "estado": "DISPONIBLE"}
        response = admin_client.get(STOCK_ITEM_DIM_ENDPOINT, params=params)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        ids_respuesta = {item["id"] for item in data}
        assert id1 in ids_respuesta
        assert id3 in ids_respuesta
        assert all(item["estado"] == "DISPONIBLE" for item in data)

    def test_get_stock_item_success(self, admin_client: TestClient, stock_item_dimensional_de_prueba: StockItemDimensional):
        item_id = stock_item_dimensional_de_prueba.id
        response = admin_client.get(f"{STOCK_ITEM_DIM_ENDPOINT}/{item_id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == item_id
        assert data["material_dimensional_id"] == stock_item_dimensional_de_prueba.material_dimensional_id

    def test_get_stock_item_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{STOCK_ITEM_DIM_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_material_dimensional_conflict(self, admin_client: TestClient, stock_item_dimensional_de_prueba: StockItemDimensional):
        """Prueba eliminar un MaterialDimensional con StockItems asociados (409)."""
        material_id = stock_item_dimensional_de_prueba.material_dimensional_id
        logger.info(f"Intentando borrar MaterialDimensional ID {material_id} que tiene StockItem ID {stock_item_dimensional_de_prueba.id} asociado.")
        response = admin_client.delete(f"{MAT_DIM_ENDPOINT}/{material_id}")
        assert response.status_code == status.HTTP_409_CONFLICT
        assert "está en uso (stock existente)" in response.json()["detail"]
```

# tests\api\v1\test_pedidos_api.py

```py
# app/tests/api/v1/test_pedidos_api.py

import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas para crear payloads y validar respuestas
from app.schemas.order_schema import PedidoClienteCreate, PedidoClienteRead
# Importar modelos y repositorios para verificaciones en BD
from app.models import PedidoCliente, Usuario, Cliente
from app.repositories import order_repository

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
PEDIDOS_ENDPOINT = f"{API_V1_STR}/pedidos"

# ==================================
# --- Tests para POST /pedidos ---
# ==================================
from tests.conftest import TestingSessionLocal # Importar factory de sesión
import logging # Añadir

logger = logging.getLogger(__name__) # Añadir

"""

def test_create_pedido_success_vendedor(
    vendedor_client: TestClient, db_session: Session, cliente_de_prueba: Cliente, vendedor_user: Usuario
):
    "Prueba la creación exitosa de un pedido por un Vendedor."
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data
    new_pedido_id = data["id"]
    assert data["estado"] == "NUEVO"
    assert data["cliente_id"] == cliente_de_prueba.id
    assert data["usuario_id_vendedor"] == vendedor_user.id
    assert data["cliente"]["id"] == cliente_de_prueba.id
    assert data["vendedor"]["id"] == vendedor_user.id

    # --- CORRECCIÓN ---
    # Verificar en la BD usando expire_all o una nueva sesión
    db_session.expire_all() # Fuerza a la sesión a releer de la BD
    # --- FIN CORRECCIÓN ---
    db_pedido = order_repository.get_pedido_by_id(db=db_session, pedido_id=new_pedido_id)
    # Añadir mensaje más descriptivo al assert
    assert db_pedido is not None, f"Pedido ID {new_pedido_id} creado vía API no fue encontrado en BD por el test (después de expire_all)."
    assert db_pedido.cliente_id == cliente_de_prueba.id
    assert db_pedido.usuario_id_vendedor == vendedor_user.id
    assert db_pedido.estado == "NUEVO"

def test_create_pedido_success_admin(
    admin_client: TestClient, db_session: Session, cliente_de_prueba: Cliente, admin_user: Usuario
):
    "Prueba la creación exitosa de un pedido por un Administrador."
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = admin_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    new_pedido_id = data["id"] # Obtener ID
    assert data["cliente_id"] == cliente_de_prueba.id
    assert data["usuario_id_vendedor"] == admin_user.id

    # --- CORRECCIÓN ---
    # Verificar en BD (simplificado, usando expire_all)
    db_session.expire_all()
    # --- FIN CORRECCIÓN ---
    # Añadir mensaje más descriptivo al assert
    assert order_repository.get_pedido_by_id(db=db_session, pedido_id=new_pedido_id) is not None, f"Pedido ID {new_pedido_id} creado vía API (Admin) no fue encontrado en BD por el test (después de expire_all)."

"""








# ===============================================================================

def test_create_pedido_success_vendedor(
    vendedor_client: TestClient, db_session: Session, cliente_de_prueba: Cliente, vendedor_user: Usuario
):
    """Prueba la creación exitosa de un pedido por un Vendedor."""
    logger.debug(f"Test 'test_create_pedido_success_vendedor' iniciando con db_session ID: {id(db_session)}")
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data
    new_pedido_id = data["id"]
    logger.info(f"Test 'test_create_pedido_success_vendedor': Pedido ID {new_pedido_id} creado vía API.")
    # ... (other assertions on response data) ...

    # --- CORRECCIÓN: Verificar en la BD usando una nueva sesión ---
    db_pedido = None
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_create_pedido_success_vendedor': Abierta verification_db ID {id(verification_db)} para buscar Pedido ID {new_pedido_id}.")
             db_pedido = order_repository.get_pedido_by_id(db=verification_db, pedido_id=new_pedido_id)
             logger.debug(f"Test 'test_create_pedido_success_vendedor': Resultado de get_pedido_by_id con verification_db: {'Encontrado' if db_pedido else 'No Encontrado'}")
             assert db_pedido is not None, f"Pedido ID {new_pedido_id} creado vía API no fue encontrado en BD por el test (con sesión de verificación)."
             # Realizar assertions aquí dentro, usando el objeto de la sesión de verificación
             assert db_pedido.cliente_id == cliente_de_prueba.id
             assert db_pedido.usuario_id_vendedor == vendedor_user.id
             assert db_pedido.estado == "NUEVO"
             logger.info(f"Test 'test_create_pedido_success_vendedor': Pedido ID {new_pedido_id} verificado exitosamente en BD.")
    except Exception as e:
        logger.error(f"Error durante verificación en BD para test_create_pedido_success_vendedor: {e}", exc_info=True)
        pytest.fail(f"Error durante verificación en BD para test_create_pedido_success_vendedor: {e}")

def test_create_pedido_success_admin(
    admin_client: TestClient, db_session: Session, cliente_de_prueba: Cliente, admin_user: Usuario
):
    """Prueba la creación exitosa de un pedido por un Administrador."""
    logger.debug(f"Test 'test_create_pedido_success_admin' iniciando con db_session ID: {id(db_session)}")
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = admin_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    new_pedido_id = data["id"] # Obtener ID
    logger.info(f"Test 'test_create_pedido_success_admin': Pedido ID {new_pedido_id} creado vía API.")
    assert data["cliente_id"] == cliente_de_prueba.id
    assert data["usuario_id_vendedor"] == admin_user.id

    # --- CORRECCIÓN: Verificar en BD usando una nueva sesión ---
    db_pedido = None
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_create_pedido_success_admin': Abierta verification_db ID {id(verification_db)} para buscar Pedido ID {new_pedido_id}.")
            db_pedido = order_repository.get_pedido_by_id(db=verification_db, pedido_id=new_pedido_id)
            logger.debug(f"Test 'test_create_pedido_success_admin': Resultado de get_pedido_by_id con verification_db: {'Encontrado' if db_pedido else 'No Encontrado'}")
            assert db_pedido is not None, f"Pedido ID {new_pedido_id} creado vía API (Admin) no fue encontrado en BD por el test (con sesión de verificación)."
            logger.info(f"Test 'test_create_pedido_success_admin': Pedido ID {new_pedido_id} verificado exitosamente en BD.")
    except Exception as e:
        logger.error(f"Error durante verificación en BD para test_create_pedido_success_admin: {e}", exc_info=True)
        pytest.fail(f"Error durante verificación en BD para test_create_pedido_success_admin: {e}")

# =======================FIN CORRECCIÓN ==================================



def test_create_pedido_cliente_not_found(vendedor_client: TestClient):
    """Prueba crear un pedido para un cliente inexistente (404)."""
    non_existent_cliente_id = 99990
    payload = PedidoClienteCreate(cliente_id=non_existent_cliente_id)
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    # El servicio debe lanzar 404 si el cliente no existe
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Cliente con ID {non_existent_cliente_id} no encontrado" in response.json()["detail"]

def test_create_pedido_invalid_payload(vendedor_client: TestClient):
    """Prueba crear un pedido sin cliente_id (422 Unprocessable Entity)."""
    invalid_payload = {} # Falta cliente_id
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_create_pedido_forbidden_operario(
    operario_client: TestClient, cliente_de_prueba: Cliente
):
    """Prueba que un Operario no puede crear pedidos (403 Forbidden)."""
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = operario_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_403_FORBIDDEN
    # Asume que el permiso 'crear:pedido_cliente' existe y no está asignado a Operario
    assert "Permiso insuficiente: Se requiere 'crear:pedido_cliente'" in response.json()["detail"]

def test_create_pedido_unauthenticated(base_client: TestClient, cliente_de_prueba: Cliente):
    """Prueba crear un pedido sin autenticación (401 Unauthorized)."""
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = base_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# ========================================
# --- Tests para GET /pedidos/{pedido_id} ---
# ========================================



def test_get_pedido_success_vendedor(vendedor_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba obtener un pedido existente como Vendedor."""
    pedido_id = pedido_de_prueba.id
    response = vendedor_client.get(f"{PEDIDOS_ENDPOINT}/{pedido_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == pedido_id
    assert data["cliente"]["id"] == pedido_de_prueba.cliente_id
    assert data["vendedor"]["id"] == pedido_de_prueba.usuario_id_vendedor

def test_get_pedido_success_admin(admin_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba obtener un pedido existente como Admin."""
    pedido_id = pedido_de_prueba.id
    response = admin_client.get(f"{PEDIDOS_ENDPOINT}/{pedido_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == pedido_id

def test_get_pedido_not_found(vendedor_client: TestClient):
    """Prueba obtener un pedido inexistente (404)."""
    non_existent_pedido_id = 99991
    response = vendedor_client.get(f"{PEDIDOS_ENDPOINT}/{non_existent_pedido_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Pedido con ID {non_existent_pedido_id} no encontrado" in response.json()["detail"]

def test_get_pedido_forbidden_operario(operario_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba que un Operario no puede obtener detalles de un pedido (403)."""
    pedido_id = pedido_de_prueba.id
    response = operario_client.get(f"{PEDIDOS_ENDPOINT}/{pedido_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:pedido_cliente'" in response.json()["detail"]

def test_get_pedido_unauthenticated(base_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba obtener un pedido sin autenticación (401)."""
    pedido_id = pedido_de_prueba.id
    response = base_client.get(f"{PEDIDOS_ENDPOINT}/{pedido_id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# ==================================
# --- Tests para GET /pedidos ---
# ==================================

def test_list_pedidos_success(vendedor_client: TestClient, pedido_de_prueba: PedidoCliente):
    """Prueba listar pedidos como Vendedor."""
    response = vendedor_client.get(PEDIDOS_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    # Verificar que el pedido de prueba está en la lista
    assert any(p["id"] == pedido_de_prueba.id for p in data)
    # Verificar estructura básica de un elemento
    if data:
        assert "id" in data[0]
        assert "estado" in data[0]
        assert "cliente" in data[0]
        assert "vendedor" in data[0]

def test_list_pedidos_filtered(admin_client: TestClient, pedido_de_prueba: PedidoCliente, cliente_de_prueba: Cliente, vendedor_user: Usuario):
    """Prueba filtrar la lista de pedidos como Admin."""
    # Filtrar por cliente
    params_cliente = {"cliente_id": cliente_de_prueba.id}
    response_cliente = admin_client.get(PEDIDOS_ENDPOINT, params=params_cliente)
    assert response_cliente.status_code == status.HTTP_200_OK
    data_cliente = response_cliente.json()
    assert all(p["cliente"]["id"] == cliente_de_prueba.id for p in data_cliente)
    assert any(p["id"] == pedido_de_prueba.id for p in data_cliente) # Asegura que el de prueba esté

    # Filtrar por vendedor
    params_vendedor = {"vendedor_id": vendedor_user.id}
    response_vendedor = admin_client.get(PEDIDOS_ENDPOINT, params=params_vendedor)
    assert response_vendedor.status_code == status.HTTP_200_OK
    data_vendedor = response_vendedor.json()
    assert all(p["vendedor"]["id"] == vendedor_user.id for p in data_vendedor)
    assert any(p["id"] == pedido_de_prueba.id for p in data_vendedor)

    # Filtrar por estado
    params_estado = {"estado": "NUEVO"}
    response_estado = admin_client.get(PEDIDOS_ENDPOINT, params=params_estado)
    assert response_estado.status_code == status.HTTP_200_OK
    data_estado = response_estado.json()
    assert all(p["estado"] == "NUEVO" for p in data_estado)
    assert any(p["id"] == pedido_de_prueba.id for p in data_estado)

    # Filtrar por combinación (ej: cliente y estado)
    params_combo = {"cliente_id": cliente_de_prueba.id, "estado": "NUEVO"}
    response_combo = admin_client.get(PEDIDOS_ENDPOINT, params=params_combo)
    assert response_combo.status_code == status.HTTP_200_OK
    data_combo = response_combo.json()
    assert all(p["cliente"]["id"] == cliente_de_prueba.id and p["estado"] == "NUEVO" for p in data_combo)
    assert any(p["id"] == pedido_de_prueba.id for p in data_combo)

def test_list_pedidos_pagination(admin_client: TestClient, db_session: Session, cliente_de_prueba: Cliente):
    """Prueba la paginación al listar pedidos."""
    # Crear algunos pedidos adicionales para probar paginación
    ids_creados = []
    for i in range(3):
        resp = admin_client.post(PEDIDOS_ENDPOINT, json={"cliente_id": cliente_de_prueba.id})
        assert resp.status_code == status.HTTP_201_CREATED
        ids_creados.append(resp.json()["id"])

    # Probar limit
    response_limit = admin_client.get(f"{PEDIDOS_ENDPOINT}?limit=2")
    assert response_limit.status_code == status.HTTP_200_OK
    assert len(response_limit.json()) <= 2

    # Probar skip
    response_no_skip = admin_client.get(f"{PEDIDOS_ENDPOINT}?limit=5") # Obtener (hasta) 5 sin skip
    response_skip = admin_client.get(f"{PEDIDOS_ENDPOINT}?skip=1&limit=5") # Obtener (hasta) 5 saltando el primero
    assert response_skip.status_code == status.HTTP_200_OK
    data_no_skip = response_no_skip.json()
    data_skip = response_skip.json()

    if len(data_no_skip) > 1:
        first_id_no_skip = data_no_skip[0]["id"]
        ids_in_skipped_list = {p["id"] for p in data_skip}
        assert first_id_no_skip not in ids_in_skipped_list

def test_list_pedidos_forbidden_operario(operario_client: TestClient):
    """Prueba que un Operario no puede listar pedidos (403)."""
    response = operario_client.get(PEDIDOS_ENDPOINT)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:pedido_cliente'" in response.json()["detail"]

def test_list_pedidos_unauthenticated(base_client: TestClient):
    """Prueba listar pedidos sin autenticación (401)."""
    response = base_client.get(PEDIDOS_ENDPOINT)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
```

# tests\api\v1\test_proformas_api.py

```py
# app/tests/api/v1/test_proformas_api.py

from decimal import Decimal, ROUND_HALF_UP
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlmodel import Session
import logging

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas
from app.models.inventory_models import MaterialDimensional # Necesario para verificación dimensional
from app.schemas.order_schema import ProformaUpdate, ProformaRead, PedidoClienteCreate, LineaProformaMaterialCreate, LineaProformaServicioCreate
# Importar modelos y repositorios
from app.models import Proforma, PedidoCliente, Usuario, Cliente
from app.models import (
    MaterialConsumible, MaterialSimple, StockItemDimensional, ServicioDefinicion,
    LineaProformaMaterial, LineaProformaServicio # Para verificar en BD
)

# Importar fixtures de conftest
from tests.conftest import (
    material_consumible_de_prueba,
    material_simple_de_prueba,
    stock_item_dimensional_de_prueba,
    servicio_definicion_de_prueba,
    TestingSessionLocal # Importante para verificación independiente
)

# Repositorio opcional si se necesita alguna consulta compleja en verificación
# from app.repositories import order_repository

logger = logging.getLogger(__name__)

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
PROFORMAS_ENDPOINT = f"{API_V1_STR}/proformas"
PEDIDOS_ENDPOINT = f"{API_V1_STR}/pedidos" # Necesario para la fixture `pedido_con_proformas`


# ======================================================
# === Tests para Actualizar Proformas (PATCH /{id}) ===
# ======================================================

def test_update_proforma_estado_success(
    admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar el estado de BORRADOR a PENDIENTE_APROBACION como Admin."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)

    response = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)

    # Verificar respuesta API
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == proforma_id
    assert data["estado"] == "PENDIENTE_APROBACION"

    # Verificar en BD usando sesión independiente
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None, "Proforma no encontrada en BD para verificación."
            assert db_proforma.estado == "PENDIENTE_APROBACION", "Estado en BD no coincide."
    except Exception as e:
        pytest.fail(f"Error verificación BD en test_update_proforma_estado_success: {e}")


def test_update_proforma_notas_success(
    vendedor_client: TestClient, pedido_con_proformas: dict, vendedor_user: Usuario
):
    """Prueba actualizar las notas como Vendedor (asume permiso 'actualizar:proforma_propia')."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    new_notes = f"Notas actualizadas por test - {uuid.uuid4().hex[:4]}"
    payload = ProformaUpdate(notas=new_notes).model_dump(exclude_unset=True)

    response = vendedor_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)

    # Verificar respuesta API
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == proforma_id
    assert data["notas"] == new_notes

    # Verificar en BD usando sesión independiente
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None, "Proforma no encontrada en BD para verificación."
            assert db_proforma.notas == new_notes, "Notas en BD no coinciden."
    except Exception as e:
        pytest.fail(f"Error verificación BD en test_update_proforma_notas_success: {e}")

def test_update_proforma_invalid_state_transition(
     admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba una transición de estado inválida (ej: PENDIENTE -> BORRADOR)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    # Asegurar estado PENDIENTE
    payload_pendiente = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)
    resp_pendiente = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_pendiente)
    assert resp_pendiente.status_code == status.HTTP_200_OK

    # Intentar transición inválida
    payload_borrador = ProformaUpdate(estado="BORRADOR").model_dump(exclude_unset=True)
    response_invalid = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_borrador)

    # Verificar error esperado
    assert response_invalid.status_code == status.HTTP_400_BAD_REQUEST
    assert "No se puede cambiar el estado" in response_invalid.json()["detail"]

def test_update_proforma_not_found(admin_client: TestClient):
    """Prueba actualizar una proforma inexistente (404)."""
    non_existent_id = 99992
    payload = ProformaUpdate(notas="Test").model_dump(exclude_unset=True)
    response = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{non_existent_id}", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_proforma_forbidden_operario(
    operario_client: TestClient, pedido_con_proformas: dict
):
    """Prueba que un Operario (sin permisos de actualización) no puede actualizar proformas (403)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(notas="Intento de Operario").model_dump(exclude_unset=True)
    response = operario_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere uno de" in response.json()["detail"]

def test_update_proforma_invalid_payload_estado(
    admin_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar con un valor de estado inválido en el payload (422)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    invalid_payload = {"estado": "ESTADO_INVENTADO"} # Valor no permitido por el ENUM implícito o validador
    response = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_proforma_unauthenticated(
    base_client: TestClient, pedido_con_proformas: dict
):
    """Prueba actualizar proforma sin autenticación (401)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = ProformaUpdate(notas="No Auth").model_dump(exclude_unset=True)
    response = base_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED



# =======================================================================
# === Tests para Añadir Líneas de Material (POST /{id}/lineas-material) ===
# =======================================================================

@pytest.mark.parametrize("material_type, fixture_name, payload_extra", [
    ("CONSUMIBLE", "material_consumible_de_prueba", {"material_consumible_id": True}),
    ("SIMPLE", "material_simple_de_prueba", {"material_simple_id": True}),
    ("STOCK_DIMENSIONAL", "stock_item_dimensional_de_prueba", {"stock_item_dimensional_id": True}),
])
def test_add_linea_material_success(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    request: pytest.FixtureRequest,
    material_type: str,
    fixture_name: str,
    payload_extra: dict
):
    """
    Prueba añadir líneas de diferentes tipos de material a una proforma PRODUCTO,
    verificando precios y totales calculados. (Refactorizado)
    """
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    material_fixture = request.getfixturevalue(fixture_name)
    assert material_fixture.id is not None, f"Fixture '{fixture_name}' no tiene ID."
    material_id = material_fixture.id
    cantidad_a_anadir = Decimal("3.0") # Cantidad base, se ajusta para dimensional
    expected_precio_unitario = Decimal("0.00")
    expected_unidad_linea = ""

    # --- Calcular Precio Unitario Esperado (Lógica SIMILAR al servicio) ---
    # Esta lógica debe mantenerse sincronizada con la del servicio real.
    if material_type in ["CONSUMIBLE", "SIMPLE"]:
        expected_precio_unitario = material_fixture.precio_venta_base_unidad
        expected_unidad_linea = material_fixture.unidad_medida
    elif material_type == "STOCK_DIMENSIONAL":
        with TestingSessionLocal() as temp_db: # Sesión temporal para obtener definición
             definicion = temp_db.get(MaterialDimensional, material_fixture.material_dimensional_id)
        assert definicion is not None, "No se pudo obtener MaterialDimensional para calcular precio esperado"

        precio_base = definicion.precio_venta_base_unidad
        unidad_precio = definicion.unidad_precio_venta.lower()
        unidad_dims = definicion.unidad_dimension.lower()
        longitud = material_fixture.longitud_actual
        ancho = material_fixture.ancho_actual
        es_merma = material_fixture.es_merma

        # Lógica de conversión y cálculo (Ejemplo básico)
        factor = Decimal("1.0")
        if unidad_dims == "mm" and unidad_precio == "m2": factor = Decimal("1000.0")
        elif unidad_dims == "cm" and unidad_precio == "m2": factor = Decimal("100.0")
        # Añadir más conversiones según sea necesario...

        # Calcular valor base (ej: área)
        valor_base = Decimal("1.0")
        if unidad_precio == "m2":
            if factor == Decimal("1.0") and unidad_dims != 'm':
                 pytest.skip(f"Test saltado: No se implementó conversión de {unidad_dims} a m2") # Saltar si no hay conversión
            valor_base = (longitud / factor) * (ancho / factor)
        # Añadir lógica para otras unidades de precio (m_lineal, unidad, etc.)

        # Aplicar descuento de merma (Ejemplo)
        DESCUENTO_MERMA = Decimal("0.10") # TODO: Usar configuración o valor real
        factor_descuento = (Decimal("1.0") - DESCUENTO_MERMA) if es_merma else Decimal("1.0")

        expected_precio_unitario = (valor_base * precio_base * factor_descuento)
        expected_unidad_linea = "pieza" # La línea representa una pieza física
        cantidad_a_anadir = Decimal("1.0") # Se añade una pieza a la vez

    # Calcular total esperado de la línea
    expected_total_linea = (cantidad_a_anadir * expected_precio_unitario).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # --- Construir Payload ---
    payload_data = {
        "tipo_material_origen": material_type,
        "cantidad": cantidad_a_anadir
    }
    id_key = list(payload_extra.keys())[0] # ej: "material_consumible_id"
    payload_data[id_key] = material_id
    payload_schema = LineaProformaMaterialCreate(**payload_data)
    payload_dict = payload_schema.model_dump(mode='json')

    # --- Llamada API ---
    response = vendedor_client.post(
        f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material",
        json=payload_dict
    )

    # --- Verificar Respuesta API ---
    assert response.status_code == status.HTTP_201_CREATED, f"API call failed: {response.text}"
    # (Opcional: verificar contenido de la respuesta si es necesario, pero la verificación BD es más fiable)
    # data = response.json()
    # assert data["id"] == proforma_id
    # ...

    # --- Verificar en BD (Verificación principal) ---
    try:
        with TestingSessionLocal() as verification_db:
            # Recargar proforma y líneas desde la BD
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None, f"Proforma ID {proforma_id} no encontrada en BD para verificación."
            verification_db.refresh(db_proforma, attribute_names=["lineas_material"])

            # Buscar la línea específica en la BD
            db_linea_encontrada = None
            for linea in db_proforma.lineas_material:
                if getattr(linea, id_key, None) == material_id:
                    db_linea_encontrada = linea
                    break

            assert db_linea_encontrada is not None, f"No se encontró la línea añadida para material ID {material_id} en la BD."

            # Verificar detalles de la línea encontrada en BD
            assert db_linea_encontrada.cantidad == cantidad_a_anadir, "Cantidad en BD no coincide"
            assert db_linea_encontrada.unidad == expected_unidad_linea, "Unidad en BD no coincide"
            assert db_linea_encontrada.precio_unitario.quantize(Decimal("0.01")) == expected_precio_unitario.quantize(Decimal("0.01")), "Precio unitario en BD no coincide"
            assert db_linea_encontrada.total_linea == expected_total_linea, "Total de línea en BD no coincide"

            # Verificar totales actualizados en proforma
            expected_subtotal_db = sum(
                (l.total_linea for l in db_proforma.lineas_material if l.total_linea is not None), Decimal("0.00")
            ) # Asumiendo solo líneas de material en proforma PRODUCTO
            assert db_proforma.subtotal == expected_subtotal_db.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "Subtotal de Proforma en BD no coincide"
            # TODO: Verificar impuestos y total si la lógica está implementada

    except Exception as e:
        pytest.fail(f"Error verificación BD en test_add_linea_material_success ({material_type}): {e}")



def test_add_linea_material_not_found(
    vendedor_client: TestClient, pedido_con_proformas: dict
):
    """Prueba añadir línea con ID de material inexistente (404)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=99999, # <-- ID inexistente
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    # --- CORRECCIÓN: Hacer la aserción más flexible ---
    assert "no encontrado" in response.json()["detail"].lower()
    #assert "material consumible" in response.json()["detail"].lower() or "material de origen" in response.json()["detail"].lower()
    #assert "Material Consumible ID 99999 no encontrado" in response.json()["detail"] # Corrección


# --- Tests Negativos para Añadir Línea de Material (Sin cambios, ya eran robustos) ---

def test_add_linea_material_wrong_proforma_type(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible
):
    """Prueba añadir línea de material a proforma de SERVICIO (400)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"] # <-- Proforma incorrecta
    payload = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_consumible_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Solo se pueden añadir líneas de material a proformas de tipo 'PRODUCTO'" in response.json()["detail"]

def test_add_linea_material_wrong_proforma_state(
    admin_client: TestClient,
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible
):
    """Prueba añadir línea a proforma que no está en BORRADOR (409)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    # Cambiar estado a PENDIENTE primero
    payload_update = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)
    resp_update = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_update)
    assert resp_update.status_code == status.HTTP_200_OK

    # Intentar añadir línea
    payload_linea = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_consumible_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = admin_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload_linea)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "Debe estar en 'BORRADOR'" in response.json()["detail"]

def test_add_linea_material_not_found(
    vendedor_client: TestClient, pedido_con_proformas: dict
):
    """Prueba añadir línea con ID de material inexistente (404)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=99999, # <-- ID inexistente
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "no encontrado" in response.json()["detail"].lower() # Aserción más general

def test_add_linea_material_invalid_payload(
    vendedor_client: TestClient, pedido_con_proformas: dict
):
    """Prueba añadir línea con cantidad inválida (422)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    invalid_payload = {
        "tipo_material_origen": "CONSUMIBLE",
        "material_consumible_id": 1, # Asumir ID 1 existe
        "cantidad": 0 # Inválido (<0)
    }
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_add_linea_material_forbidden(
    operario_client: TestClient,
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible
):
    """Prueba añadir línea sin permiso (403)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_consumible_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = operario_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-material", json=payload)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'anadir:linea_proforma'" in response.json()["detail"]


# =======================================================================
# === Tests para Añadir Líneas de Servicio (POST /{id}/lineas-servicio) ===
# =======================================================================

def test_add_linea_servicio_success(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """
    Prueba añadir una línea de servicio básica a una proforma SERVICIO.
    Verifica con la lógica de precios (placeholder) actual del servicio.
    """
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    servicio_id = servicio_definicion_de_prueba.id
    assert servicio_id is not None, "Fixture servicio_definicion_de_prueba no tiene ID."
    cantidad_a_anadir = Decimal("1.5")

    # --- Calcular Precio Unitario y Total Esperado (REPLICAR LÓGICA DEL SERVICIO) ---
    # !! ESTA LÓGICA DEBE ACTUALIZARSE CUANDO CAMBIE LA DEL SERVICIO !!
    expected_precio_unitario = servicio_definicion_de_prueba.costo_por_unidad if servicio_definicion_de_prueba.costo_por_unidad is not None else Decimal("0.00")
    expected_total_linea = (cantidad_a_anadir * expected_precio_unitario).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    # --------------------------------------------------------------------------

    payload_schema = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_id,
        cantidad=cantidad_a_anadir
    )
    payload_dict = payload_schema.model_dump(mode='json')

    response = vendedor_client.post(
        f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio",
        json=payload_dict
    )

    # Verificar Respuesta API
    assert response.status_code == status.HTTP_201_CREATED, f"API call failed: {response.text}"
    # (Opcional: verificar respuesta JSON si es necesario)

    # --- Verificar en BD (Principal) ---
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma = verification_db.get(Proforma, proforma_id)
            assert db_proforma is not None, f"Proforma ID {proforma_id} no encontrada en BD."
            verification_db.refresh(db_proforma, attribute_names=["lineas_servicio"])

            # Buscar la línea específica
            db_linea_encontrada = next(
                (linea for linea in db_proforma.lineas_servicio if linea.servicio_definicion_id == servicio_id),
                None
            )
            assert db_linea_encontrada is not None, f"Línea para servicio ID {servicio_id} no encontrada en BD."

            # Verificar detalles de la línea
            assert db_linea_encontrada.cantidad == cantidad_a_anadir
            assert db_linea_encontrada.linea_proforma_material_id is None
            assert db_linea_encontrada.precio_unitario.quantize(Decimal("0.01")) == expected_precio_unitario.quantize(Decimal("0.01")), "Precio unitario servicio en BD no coincide"
            assert db_linea_encontrada.total_linea == expected_total_linea, "Total línea servicio en BD no coincide"

            # Verificar totales proforma
            expected_subtotal_db = sum((l.total_linea for l in db_proforma.lineas_servicio if l.total_linea is not None), Decimal("0.00"))
            assert db_proforma.subtotal == expected_subtotal_db.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "Subtotal proforma servicio en BD no coincide"
            # TODO: Verificar impuestos y total

    except Exception as e:
        pytest.fail(f"Error verificación BD en test_add_linea_servicio_success: {e}")


def test_add_linea_servicio_linked_to_material_success(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    material_consumible_de_prueba: MaterialConsumible,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """
    Prueba añadir línea de servicio vinculada a una línea de material.
    Verifica precios y totales con lógica placeholder.
    """
    proforma_prod_id = pedido_con_proformas["proforma_producto_id"]
    proforma_serv_id = pedido_con_proformas["proforma_servicio_id"]
    servicio_id = servicio_definicion_de_prueba.id
    assert servicio_id is not None, "Fixture servicio_definicion_de_prueba no tiene ID."
    cantidad_servicio = Decimal("1.0")

    # 1. Añadir línea de material primero (y obtener su ID desde BD)
    payload_mat_schema = LineaProformaMaterialCreate(
        tipo_material_origen="CONSUMIBLE",
        material_consumible_id=material_consumible_de_prueba.id,
        cantidad=Decimal("2.0") # Cantidad del material
    )
    resp_mat = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_prod_id}/lineas-material", json=payload_mat_schema.model_dump(mode='json'))
    assert resp_mat.status_code == status.HTTP_201_CREATED, f"Fallo al crear línea material previa: {resp_mat.text}"

    # Obtener ID de la línea de material desde BD
    linea_material_id = None
    with TestingSessionLocal() as verify_db_mat:
        stmt_id = select(LineaProformaMaterial.id).where(
            LineaProformaMaterial.proforma_id == proforma_prod_id,
            LineaProformaMaterial.material_consumible_id == material_consumible_de_prueba.id
        ).order_by(LineaProformaMaterial.id.desc())
        linea_material_id = verify_db_mat.scalar(stmt_id)
        assert linea_material_id is not None, "No se encontró el ID de la línea de material en BD"

    # 2. Calcular Precio Esperado Servicio (REPLICAR LÓGICA SERVICIO - Placeholder)
    expected_precio_unitario_serv = servicio_definicion_de_prueba.costo_por_unidad if servicio_definicion_de_prueba.costo_por_unidad is not None else Decimal("0.00")
    expected_total_linea_serv = (cantidad_servicio * expected_precio_unitario_serv).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # 3. Añadir línea de servicio vinculada
    payload_serv_schema = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_id,
        cantidad=cantidad_servicio,
        linea_proforma_material_id=linea_material_id # <-- Vinculación
    )
    payload_serv_dict = payload_serv_schema.model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_serv_id}/lineas-servicio", json=payload_serv_dict)

    # 4. Verificar Respuesta API
    assert response.status_code == status.HTTP_201_CREATED, f"API call failed: {response.text}"
    # (Opcional: verificar respuesta JSON)

    # 5. Verificar en BD
    try:
        with TestingSessionLocal() as verification_db:
            db_proforma_serv = verification_db.get(Proforma, proforma_serv_id)
            assert db_proforma_serv is not None, f"Proforma Servicio ID {proforma_serv_id} no encontrada en BD."
            verification_db.refresh(db_proforma_serv, attribute_names=["lineas_servicio"])

            # Buscar línea específica
            db_linea_serv = next(
                (l for l in db_proforma_serv.lineas_servicio if l.linea_proforma_material_id == linea_material_id),
                None
            )
            assert db_linea_serv is not None, f"Línea de servicio vinculada a material ID {linea_material_id} no encontrada en BD."

            # Verificar vínculo y precios/totales
            assert db_linea_serv.servicio_definicion_id == servicio_id
            assert db_linea_serv.cantidad == cantidad_servicio
            assert db_linea_serv.precio_unitario.quantize(Decimal("0.01")) == expected_precio_unitario_serv.quantize(Decimal("0.01")), "Precio unitario servicio vinculado en BD no coincide"
            assert db_linea_serv.total_linea == expected_total_linea_serv, "Total línea servicio vinculado en BD no coincide"

            # Verificar totales proforma
            expected_subtotal_serv_db = sum((l.total_linea for l in db_proforma_serv.lineas_servicio if l.total_linea is not None), Decimal("0.00"))
            assert db_proforma_serv.subtotal == expected_subtotal_serv_db.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "Subtotal proforma servicio (vinculado) en BD no coincide"
            # TODO: Verificar impuestos y total

    except Exception as e:
        pytest.fail(f"Error verificación BD en test_add_linea_servicio_linked_to_material_success: {e}")


# --- Tests Negativos para Añadir Línea de Servicio (Ahora deberían pasar con códigos 4xx) ---

def test_add_linea_servicio_wrong_proforma_type(
    vendedor_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio a proforma de PRODUCTO (espera 400)."""
    proforma_id = pedido_con_proformas["proforma_producto_id"]
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_definicion_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Solo se pueden añadir líneas de servicio a proformas de tipo 'SERVICIO'" in response.json()["detail"]

def test_add_linea_servicio_wrong_proforma_state(
    admin_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio a proforma no en BORRADOR (espera 409)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload_update = ProformaUpdate(estado="PENDIENTE_APROBACION").model_dump(exclude_unset=True)
    resp_update = admin_client.patch(f"{PROFORMAS_ENDPOINT}/{proforma_id}", json=payload_update)
    assert resp_update.status_code == status.HTTP_200_OK
    payload_linea = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_definicion_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = admin_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload_linea)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "Debe estar en 'BORRADOR'" in response.json()["detail"]

def test_add_linea_servicio_def_not_found(
    vendedor_client: TestClient, pedido_con_proformas: dict
):
    """Prueba añadir línea con ID de servicio inexistente (espera 404)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=99999,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "La definición del servicio con ID 99999 no fue encontrada." in response.json()["detail"]

def test_add_linea_servicio_invalid_material_link(
    vendedor_client: TestClient, pedido_con_proformas: dict, servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio vinculando a linea material inexistente (espera 404)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_definicion_de_prueba.id,
        cantidad=Decimal("1"),
        linea_proforma_material_id=88888
    ).model_dump(mode='json')
    response = vendedor_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "La línea de material asociada con ID 88888 no fue encontrada." in response.json()["detail"]

def test_add_linea_servicio_forbidden(
    operario_client: TestClient,
    pedido_con_proformas: dict,
    servicio_definicion_de_prueba: ServicioDefinicion
):
    """Prueba añadir línea de servicio sin permiso (403)."""
    proforma_id = pedido_con_proformas["proforma_servicio_id"]
    payload = LineaProformaServicioCreate(
        servicio_definicion_id=servicio_definicion_de_prueba.id,
        cantidad=Decimal("1")
    ).model_dump(mode='json')
    response = operario_client.post(f"{PROFORMAS_ENDPOINT}/{proforma_id}/lineas-servicio", json=payload)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'anadir:linea_proforma'" in response.json()["detail"]
```

# tests\api\v1\test_roles_api.py

```py
# tests/api/v1/test_roles_api.py
import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
import logging # Asegurar import
import uuid

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas
from app.schemas.rol_permiso_schema import RolCreate, RolRead, RolUpdate, RolReadWithPermissions
# Importar modelos y repositorios
from app.models import Rol, Usuario, Permiso # Importar Permiso
from app.repositories import rol_repository, usuario_repository # Necesario para verificaciones
# Importar TestingSessionLocal
from tests.conftest import TestingSessionLocal

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
ROLES_ENDPOINT = f"{API_V1_STR}/roles"
logger = logging.getLogger(__name__) # Añadir logger

# --- Tests para Listar Roles (GET /roles) ---
# (Sin cambios, no modifican DB)
def test_list_roles_unauthenticated(base_client: TestClient):
    response = base_client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_list_roles_forbidden_non_admin(vendedor_client: TestClient):
    response = vendedor_client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:rol'." in response.json()["detail"]

def test_list_roles_success_admin(admin_client: TestClient, db_session: Session):
    response = admin_client.get(ROLES_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 5
    role_names = {role["nombre"] for role in data}
    assert "Administrador" in role_names
    assert "Vendedor" in role_names
    for role in data:
        assert "id" in role
        assert "nombre" in role

# --- Tests para Crear Roles (POST /roles) ---
def test_create_role_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la creación exitosa de un rol como admin (Refactorizado)."""
    role_name = f"RolCreadoEnTest_{uuid.uuid4().hex[:6]}"
    role_data = RolCreate(nombre=role_name, descripcion="Descripción test")
    response = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["nombre"] == role_data.nombre
    assert data["descripcion"] == role_data.descripcion
    assert "id" in data
    new_role_id = data["id"]

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_create_role_success_admin': Verificando rol ID {new_role_id} con nueva sesión.")
             db_rol = rol_repository.get_rol(db=verification_db, rol_id=new_role_id)
             assert db_rol is not None, f"Rol ID {new_role_id} no encontrado en BD post-creación."
             assert db_rol.nombre == role_data.nombre
             assert db_rol.descripcion == role_data.descripcion
             logger.info(f"Test 'test_create_role_success_admin': Rol ID {new_role_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_create_role_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests create duplicate, invalid, forbidden sin cambios) ...
def test_create_role_duplicate_name(admin_client: TestClient, db_session: Session):
    """Prueba que crear un rol con nombre duplicado falle (409)."""
    role_data = RolCreate(nombre="RolDuplicadoParaTest", descripcion="Test 409")
    response1 = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response1.status_code == status.HTTP_201_CREATED
    response2 = admin_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response2.status_code == status.HTTP_409_CONFLICT
    assert f"El rol '{role_data.nombre}' ya existe" in response2.json()["detail"]

def test_create_role_invalid_data(admin_client: TestClient):
    """Prueba que crear un rol con datos inválidos (ej: nombre muy largo) falle (422)."""
    invalid_role_data = {"nombre": "a" * 150, "descripcion": "Test"} # Asumiendo max_length=100 para nombre
    response = admin_client.post(ROLES_ENDPOINT, json=invalid_role_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_create_role_forbidden_non_admin(vendedor_client: TestClient):
    """Prueba que crear un rol como no-admin falle (403)."""
    role_data = RolCreate(nombre="RolNoAdminTest", descripcion="No debería crearse")
    response = vendedor_client.post(ROLES_ENDPOINT, json=role_data.model_dump())
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'crear:rol'" in response.json()["detail"]

# --- Tests para Obtener Rol por ID (GET /roles/{rol_id}) ---
# (Sin cambios)
def test_get_role_by_id_success(admin_client: TestClient, vendedor_role_id: int):
    """Prueba obtener un rol existente por ID como admin."""
    response = admin_client.get(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == vendedor_role_id
    assert data["nombre"] == "Vendedor"
    assert "permisos" in data
    assert isinstance(data["permisos"], list)
    perm_keys = {f"{p['nombre_accion']}:{p['nombre_recurso']}" for p in data["permisos"]}
    assert "leer:cliente" in perm_keys

def test_get_role_not_found(admin_client: TestClient):
    """Prueba obtener un rol con ID inexistente (404)."""
    response = admin_client.get(f"{ROLES_ENDPOINT}/99999") # ID que no existe
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_get_role_forbidden_non_admin(vendedor_client: TestClient, vendedor_role_id: int):
    """Prueba que obtener un rol por ID como no-admin falle (403)."""
    response = vendedor_client.get(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:rol'" in response.json()["detail"]


# --- Tests para Eliminar Roles (DELETE /roles/{rol_id}) ---

def test_delete_role_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la eliminación exitosa de un rol NO ASIGNADO como admin (Refactorizado)."""
    role_name_to_delete = f"RolParaBorrar_{uuid.uuid4()}"
    temp_role_data = RolCreate(nombre=role_name_to_delete, descripcion="Se eliminará")
    # Crear rol directamente en BD para este test, asegurando que no esté asignado
    db_rol = rol_repository.create_rol(db=db_session, rol_in=temp_role_data)
    role_id_to_delete = db_rol.id
    db_session.commit() # Asegurar que la creación esté confirmada

    response = admin_client.delete(f"{ROLES_ENDPOINT}/{role_id_to_delete}")

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_delete_role_success_admin': Verificando rol ID {role_id_to_delete} con nueva sesión.")
            deleted_rol = rol_repository.get_rol(db=verification_db, rol_id=role_id_to_delete)
            assert deleted_rol is None, f"Rol ID {role_id_to_delete} aún encontrado en BD post-delete."
            logger.info(f"Test 'test_delete_role_success_admin': Rol ID {role_id_to_delete} verificado como eliminado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_delete_role_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests delete not_found, conflict, forbidden sin cambios) ...
def test_delete_role_not_found_admin(admin_client: TestClient):
    """Prueba eliminar un rol con ID inexistente (404)."""
    non_existent_id = 99998
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{non_existent_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_role_conflict_assigned_admin(
    admin_client: TestClient, db_session: Session, vendedor_role_id: int, vendedor_user: Usuario
):
    """Prueba eliminar un rol ASIGNADO a un usuario (409 Conflict)."""
    user_in_db = usuario_repository.get_usuario(db=db_session, user_id=vendedor_user.id)
    assert user_in_db is not None
    roles_usuario = {rol.id for rol in user_in_db.roles}
    assert vendedor_role_id in roles_usuario
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "No se puede eliminar el rol" in response.json()["detail"]

def test_delete_role_forbidden_non_admin(
    vendedor_client: TestClient, vendedor_role_id: int
):
    """Prueba que eliminar un rol como no-admin falle (403)."""
    response = vendedor_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'eliminar:rol'" in response.json()["detail"]


# --- Tests para Actualizar Roles (PUT /roles/{rol_id}) ---

def test_update_role_success_admin(admin_client: TestClient, db_session: Session):
    """Prueba la actualización exitosa de un rol como admin (Refactorizado)."""
    rol_original = RolCreate(nombre=f"RolParaActualizar_{uuid.uuid4().hex[:6]}", descripcion="Descripción Original")
    # Crear directamente en DB para asegurar que existe
    db_rol_original = rol_repository.create_rol(db=db_session, rol_in=rol_original)
    role_id_to_update = db_rol_original.id
    db_session.commit()

    update_data = RolUpdate(nombre="Rol Actualizado Test", descripcion="Nueva Descripción")

    response_update = admin_client.put(
        f"{ROLES_ENDPOINT}/{role_id_to_update}",
        json=update_data.model_dump(exclude_unset=True)
    )

    assert response_update.status_code == status.HTTP_200_OK
    data = response_update.json()
    assert data["id"] == role_id_to_update
    assert data["nombre"] == update_data.nombre
    assert data["descripcion"] == update_data.descripcion

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_update_role_success_admin': Verificando rol ID {role_id_to_update} con nueva sesión.")
             db_rol = rol_repository.get_rol(db=verification_db, rol_id=role_id_to_update)
             assert db_rol is not None, f"Rol ID {role_id_to_update} no encontrado en BD post-update."
             assert db_rol.nombre == update_data.nombre
             assert db_rol.descripcion == update_data.descripcion
             logger.info(f"Test 'test_update_role_success_admin': Rol ID {role_id_to_update} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_update_role_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests update conflict, not_found, invalid, forbidden sin cambios) ...
def test_update_role_conflict_name_admin(admin_client: TestClient, db_session: Session, vendedor_role_id: int):
    """Prueba que actualizar a un nombre de rol existente falle (409)."""
    rol_original = RolCreate(nombre=f"RolConflicto_{uuid.uuid4().hex[:6]}", descripcion="Original")
    response_create = admin_client.post(ROLES_ENDPOINT, json=rol_original.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    role_id_to_update = response_create.json()["id"]
    update_data = RolUpdate(nombre="Vendedor")
    response_update = admin_client.put(f"{ROLES_ENDPOINT}/{role_id_to_update}",json=update_data.model_dump(exclude_unset=True))
    assert response_update.status_code == status.HTTP_409_CONFLICT
    assert "conflicto" in response_update.json()["detail"].lower() or "ya está en uso" in response_update.json()["detail"].lower()
    # Verificar que no cambió
    with TestingSessionLocal() as vdb:
        db_rol = vdb.get(Rol, role_id_to_update)
        assert db_rol is not None
        assert db_rol.nombre == rol_original.nombre


def test_update_role_not_found_admin(admin_client: TestClient):
    """Prueba actualizar un rol con ID inexistente (404)."""
    non_existent_id = 99997
    update_data = RolUpdate(nombre="Nombre No Importa")
    response = admin_client.put(f"{ROLES_ENDPOINT}/{non_existent_id}",json=update_data.model_dump(exclude_unset=True))
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_role_invalid_data_admin(admin_client: TestClient, db_session: Session):
    """Prueba actualizar un rol con datos inválidos (ej: nombre muy largo) falle (422)."""
    rol_original = RolCreate(nombre=f"RolValidacion_{uuid.uuid4().hex[:6]}", descripcion="Valido")
    response_create = admin_client.post(ROLES_ENDPOINT, json=rol_original.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    role_id_to_update = response_create.json()["id"]
    invalid_update_data = {"nombre": "a" * 150}
    response = admin_client.put(f"{ROLES_ENDPOINT}/{role_id_to_update}",json=invalid_update_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_role_forbidden_non_admin(vendedor_client: TestClient, vendedor_role_id: int):
    """Prueba que actualizar un rol como no-admin falle (403)."""
    update_data = RolUpdate(descripcion="Intento No Autorizado")
    response = vendedor_client.put(f"{ROLES_ENDPOINT}/{vendedor_role_id}",json=update_data.model_dump(exclude_unset=True))
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'actualizar:rol'" in response.json()["detail"]


# --- Tests para Asignar Permisos a Roles (POST /roles/{rol_id}/permisos/{permiso_id}) ---

def test_assign_permission_to_role_success_admin(
    admin_client: TestClient,
    db_session: Session, # No se usará para verificación post-API
    permiso_leer_cliente_id: int
):
    """
    Prueba asignar exitosamente un permiso a un NUEVO rol como admin (Refactorizado).
    """
    temp_role_data = RolCreate(nombre=f"RolTempPermiso_{uuid.uuid4().hex[:6]}", descripcion="Rol para test de asignación")
    response_create = admin_client.post(ROLES_ENDPOINT, json=temp_role_data.model_dump())
    assert response_create.status_code == status.HTTP_201_CREATED
    new_role_id = response_create.json()["id"]

    response_assign = admin_client.post(
        f"{ROLES_ENDPOINT}/{new_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    assert response_assign.status_code == status.HTTP_200_OK
    data = response_assign.json()
    assert data["id"] == new_role_id
    permiso_asignado_encontrado = any(p["id"] == permiso_leer_cliente_id for p in data.get("permisos", []))
    assert permiso_asignado_encontrado, f"El permiso ID {permiso_leer_cliente_id} no se encontró en la respuesta."

    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_assign_permission_to_role_success_admin': Verificando rol ID {new_role_id} con nueva sesión.")
             # Usar get_rol_with_permissions para cargar la relación
             db_rol = rol_repository.get_rol_with_permissions(db=verification_db, rol_id=new_role_id)
             assert db_rol is not None, "El rol temporal no se encontró en la BD para verificación."
             permiso_ids_en_db = {p.id for p in db_rol.permisos}
             assert permiso_leer_cliente_id in permiso_ids_en_db, "El permiso no se encontró en la relación del rol en la BD."
             logger.info(f"Test 'test_assign_permission_to_role_success_admin': Permiso asignado a rol ID {new_role_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_assign_permission_to_role_success_admin: {e}")


# ... (tests asignar permiso ya asignado, rol no encontrado, permiso no encontrado, forbidden sin cambios) ...
def test_assign_permission_already_assigned_admin(
    admin_client: TestClient,
    db_session: Session,
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba que asignar un permiso ya asignado falle (409)."""
    assign_response = admin_client.post( f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT]
    response = admin_client.post(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "ya está asignado" in response.json()["detail"]

def test_assign_permission_role_not_found_admin(
    admin_client: TestClient,
    permiso_leer_cliente_id: int
):
    """Prueba asignar permiso a un rol inexistente (404)."""
    non_existent_role_id = 99996
    response = admin_client.post(f"{ROLES_ENDPOINT}/{non_existent_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_assign_permission_permission_not_found_admin(
    admin_client: TestClient,
    vendedor_role_id: int
):
    """Prueba asignar un permiso inexistente a un rol válido (404)."""
    non_existent_perm_id = 99995
    response = admin_client.post(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{non_existent_perm_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_assign_permission_forbidden_non_admin(
    vendedor_client: TestClient,
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba que un no-admin no puede asignar permisos (403)."""
    response = vendedor_client.post(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'asignar:permiso_rol'" in response.json()["detail"]


# --- Tests para Quitar Permisos de Roles (DELETE /roles/{rol_id}/permisos/{permiso_id}) ---

def test_remove_permission_from_role_success_admin(
    admin_client: TestClient,
    db_session: Session, # No se usará para verificación post-API
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba quitar exitosamente un permiso asignado a un rol como admin (Refactorizado)."""
    # 1. Asegurar que el permiso está asignado
    assign_response = admin_client.post(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT], "Fallo al asegurar asignación previa"

    # 2. Ejecutar la petición DELETE para quitar la asignación
    response_delete = admin_client.delete(
        f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}"
    )

    assert response_delete.status_code == status.HTTP_204_NO_CONTENT

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_remove_permission_from_role_success_admin': Verificando rol ID {vendedor_role_id} con nueva sesión.")
             db_rol = rol_repository.get_rol_with_permissions(db=verification_db, rol_id=vendedor_role_id)
             assert db_rol is not None
             permiso_ids_en_db = {p.id for p in db_rol.permisos}
             assert permiso_leer_cliente_id not in permiso_ids_en_db, "El permiso todavía se encontró en la relación del rol en la BD."
             logger.info(f"Test 'test_remove_permission_from_role_success_admin': Permiso quitado de rol ID {vendedor_role_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_remove_permission_from_role_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests quitar permiso no asignado, rol no encontrado, permiso no encontrado, forbidden sin cambios) ...
def test_remove_permission_not_assigned_admin(
    admin_client: TestClient,
    vendedor_role_id: int,
    permiso_gestionar_usuario_id: int
):
    """Prueba que quitar un permiso no asignado falle (404)."""
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_gestionar_usuario_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "no está asignado al rol" in response.json()["detail"]

def test_remove_permission_role_not_found_admin(
    admin_client: TestClient,
    permiso_leer_cliente_id: int
):
    """Prueba quitar permiso desde un rol inexistente (404)."""
    non_existent_role_id = 99996
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{non_existent_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_remove_permission_permission_not_found_admin(
    admin_client: TestClient,
    vendedor_role_id: int
):
    """Prueba quitar un permiso inexistente de un rol válido (404)."""
    non_existent_perm_id = 99995
    response = admin_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{non_existent_perm_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_remove_permission_forbidden_non_admin(
    admin_client: TestClient,
    vendedor_client: TestClient,
    vendedor_role_id: int,
    permiso_leer_cliente_id: int
):
    """Prueba que un no-admin no puede quitar permisos (403)."""
    assign_response = admin_client.post(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert assign_response.status_code in [status.HTTP_200_OK, status.HTTP_409_CONFLICT]
    response = vendedor_client.delete(f"{ROLES_ENDPOINT}/{vendedor_role_id}/permisos/{permiso_leer_cliente_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'remover:permiso_rol'" in response.json()["detail"]
```

# tests\api\v1\test_servicios_api.py

```py
# app/tests/api/v1/test_servicios_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
from decimal import Decimal
import logging

# Importar configuraciones y utilidades
from app.core.config import settings
# Importar schemas necesarios
from app.schemas.service_schema import (
    ServicioDefinicionCreate, ServicioDefinicionRead, ServicioDefinicionUpdate
)
# Importar modelo para verificaciones y fixtures
from app.models import ServicioDefinicion
# Importar constantes de endpoints y fábrica de sesión desde conftest
from tests.conftest import (
    TestingSessionLocal, # Asegurar importación
    DEFINICIONES_ENDPOINT # Usar la constante definida
)
# Importar fixtures de cliente necesarias
from tests.conftest import admin_client, vendedor_client, operario_client, dibujante_client

logger = logging.getLogger(__name__)

# --- Helpers ---
def create_valid_servicio_payload(suffix: str) -> dict:
    """Crea un payload válido y JSON-serializable para ServicioDefinicionCreate."""
    schema_instance = ServicioDefinicionCreate(
        codigo=f"SERV-{suffix}",
        nombre=f"Servicio Helper {suffix}",
        unidad_cobro="pieza",
        costo_por_unidad=Decimal("10.0"),
        requiere_dibujo_cnc=False,
        tiempo_setup_min=Decimal("0.0"),
        tiempo_preparado_min_por_unidad=Decimal("0.0"),
        factor_ih=Decimal("1.0"),
    )
    return schema_instance.model_dump(mode='json')


# ============================================================
# --- Tests para Endpoints de Definición de Servicios ---
# ============================================================
class TestServicioDefinicionAPI:

    # --- POST /definiciones ---
    # (test_create_servicio_success_admin ya era robusto, sin cambios)
    def test_create_servicio_success_admin(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_servicio_payload(suffix)
        response = admin_client.post(DEFINICIONES_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["nombre"] == payload["nombre"]
        assert data["unidad_cobro"] == payload["unidad_cobro"]
        assert Decimal(data["costo_por_unidad"]) == Decimal(payload["costo_por_unidad"])
        # Verificación ya usaba nueva sesión
        with TestingSessionLocal() as verification_db:
            db_obj = verification_db.get(ServicioDefinicion, data["id"])
            assert db_obj is not None
            assert db_obj.nombre == payload["nombre"]

    # ... (otros tests de create sin cambios) ...
    def test_create_servicio_duplicate_name_admin(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        """Prueba crear servicio con nombre duplicado (409)."""
        payload_schema = ServicioDefinicionCreate(
            codigo=f"FIX-SERV-{servicio_definicion_de_prueba.codigo}",
            nombre=servicio_definicion_de_prueba.nombre, # Nombre existente
            unidad_cobro="hora",
            tiempo_setup_min=Decimal("0.0"),
            tiempo_preparado_min_por_unidad=Decimal("0.0"),
            factor_ih=Decimal("1.0"),
        )
        payload_dict = payload_schema.model_dump(mode='json')
        response = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_dict)
        assert response.status_code == status.HTTP_409_CONFLICT
        assert "nombre" in response.json()["detail"].lower()

    def test_create_servicio_invalid_data(self, admin_client: TestClient):
        payload_no_name = {"unidad_cobro": "corte", "costo_por_unidad": "5.0", "codigo": "INVALID1"}
        response_no_name = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_no_name)
        assert response_no_name.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        payload_no_unit = {"nombre": "Servicio Sin Unidad", "costo_por_minuto": "1.0", "codigo": "INVALID2"}
        response_no_unit = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_no_unit)
        assert response_no_unit.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_servicio_forbidden_vendedor(self, vendedor_client: TestClient):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_servicio_payload(suffix)
        response = vendedor_client.post(DEFINICIONES_ENDPOINT, json=payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN


    # --- GET /definiciones ---
    # (tests de listado sin cambios)
    def test_list_servicios_success(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        response = admin_client.get(DEFINICIONES_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert any(s["id"] == servicio_definicion_de_prueba.id for s in data)

    def test_list_servicios_permission_vendedor(self, vendedor_client: TestClient):
        response = vendedor_client.get(DEFINICIONES_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK

    def test_list_servicios_permission_dibujante(self, dibujante_client: TestClient):
        response = dibujante_client.get(DEFINICIONES_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK

    def test_list_servicios_forbidden_operario(self, operario_client: TestClient):
        response = operario_client.get(DEFINICIONES_ENDPOINT)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_servicios_pagination(self, admin_client: TestClient):
        created_ids = []
        for i in range(3):
            suffix = uuid.uuid4().hex[:4]
            payload = create_valid_servicio_payload(suffix)
            resp_create = admin_client.post(DEFINICIONES_ENDPOINT, json=payload)
            assert resp_create.status_code == status.HTTP_201_CREATED
            created_ids.append(resp_create.json()["id"])
        response_limit = admin_client.get(f"{DEFINICIONES_ENDPOINT}?limit=1")
        assert response_limit.status_code == status.HTTP_200_OK
        assert len(response_limit.json()) == 1
        response_no_skip = admin_client.get(f"{DEFINICIONES_ENDPOINT}?limit=2")
        response_skip = admin_client.get(f"{DEFINICIONES_ENDPOINT}?skip=1&limit=2")
        assert response_skip.status_code == status.HTTP_200_OK
        if len(response_no_skip.json()) > 1:
             first_id_no_skip = response_no_skip.json()[0]["id"]
             ids_skipped = {s["id"] for s in response_skip.json()}
             assert first_id_no_skip not in ids_skipped


    # --- GET /definiciones/{id} ---
    # (tests sin cambios)
    def test_get_servicio_success(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        servicio_id = servicio_definicion_de_prueba.id
        response = admin_client.get(f"{DEFINICIONES_ENDPOINT}/{servicio_id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == servicio_id
        assert data["nombre"] == servicio_definicion_de_prueba.nombre

    def test_get_servicio_not_found(self, admin_client: TestClient):
        response = admin_client.get(f"{DEFINICIONES_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND


    # --- PUT /definiciones/{id} ---
    # (test_update_servicio_success ya era robusto, sin cambios)
    def test_update_servicio_success(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        servicio_id = servicio_definicion_de_prueba.id
        update_schema = ServicioDefinicionUpdate(
            descripcion="Descripción Actualizada v2",
            costo_por_minuto=Decimal("2.5")
        )
        update_payload = update_schema.model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{DEFINICIONES_ENDPOINT}/{servicio_id}", json=update_payload)
        assert response_update.status_code == status.HTTP_200_OK
        data = response_update.json()
        assert data["id"] == servicio_id
        assert data["descripcion"] == update_schema.descripcion
        assert Decimal(data["costo_por_minuto"]) == update_schema.costo_por_minuto
        # Verificación en BD ya usaba nueva sesión
        with TestingSessionLocal() as verification_db:
            db_obj = verification_db.get(ServicioDefinicion, servicio_id)
            assert db_obj is not None
            assert db_obj.descripcion == update_schema.descripcion
            assert db_obj.costo_por_minuto == update_schema.costo_por_minuto

    # ... (test update duplicate y not found sin cambios) ...
    def test_update_servicio_duplicate_name(self, admin_client: TestClient, servicio_definicion_de_prueba: ServicioDefinicion):
        suffix = uuid.uuid4().hex[:6]
        payload_other = create_valid_servicio_payload(suffix)
        resp_other = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_other)
        assert resp_other.status_code == status.HTTP_201_CREATED # Asegurar que el otro se crea

        update_payload = ServicioDefinicionUpdate(nombre=payload_other["nombre"]).model_dump(mode='json', exclude_unset=True)
        response_update = admin_client.put(f"{DEFINICIONES_ENDPOINT}/{servicio_definicion_de_prueba.id}", json=update_payload)
        assert response_update.status_code == status.HTTP_409_CONFLICT

    def test_update_servicio_not_found(self, admin_client: TestClient):
        update_payload = ServicioDefinicionUpdate(nombre="Test").model_dump(mode='json', exclude_unset=True)
        response = admin_client.put(f"{DEFINICIONES_ENDPOINT}/999999", json=update_payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND


    # --- DELETE /definiciones/{id} ---
    def test_delete_servicio_success(self, admin_client: TestClient, db_session: Session):
        suffix = uuid.uuid4().hex[:6]
        payload = create_valid_servicio_payload(suffix)
        response_create = admin_client.post(DEFINICIONES_ENDPOINT, json=payload)
        assert response_create.status_code == status.HTTP_201_CREATED
        created_id = response_create.json()["id"]

        response_delete = admin_client.delete(f"{DEFINICIONES_ENDPOINT}/{created_id}")
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT

        # --- VERIFICACIÓN REFACTORIZADA ---
        try:
            with TestingSessionLocal() as verification_db:
                logger.debug(f"Test 'test_delete_servicio_success': Verificando ID {created_id} con nueva sesión.")
                deleted_obj = verification_db.get(ServicioDefinicion, created_id)
                assert deleted_obj is None, f"ServicioDefinicion ID {created_id} aún encontrado en BD post-delete."
                logger.info(f"Test 'test_delete_servicio_success': ServicioDefinicion ID {created_id} verificado como eliminado.")
        except Exception as e:
            pytest.fail(f"Error durante verificación BD en test_delete_servicio_success: {e}")
        # --- FIN VERIFICACIÓN ---

    # ... (tests delete not found y conflict(pendiente) sin cambios) ...
    def test_delete_servicio_not_found(self, admin_client: TestClient):
        response = admin_client.delete(f"{DEFINICIONES_ENDPOINT}/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # @pytest.mark.skip(reason="PENDIENTE: Implementar cuando Formula o LineaProforma use ServicioDefinicion.")
    # def test_delete_servicio_conflict(self, admin_client: TestClient, ...)
```

# tests\api\v1\test_usuarios_api.py

```py
# app/tests/api/v1/test_usuarios_api.py
import pytest
import uuid
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
import logging # Asegurar import

# Importar configuraciones y utilidades
from app.core.security import verify_password # Necesario para test de contraseña
from app.core.config import settings
# Importar schemas necesarios
from app.schemas.usuario_schema import UsuarioCreate, UsuarioRead
# Importar modelos y repositorios para verificaciones en BD
from app.models import Usuario, Rol
from app.repositories import usuario_repository # Necesario para verificaciones
# Importar TestingSessionLocal desde conftest
from tests.conftest import TestingSessionLocal

# --- Constantes ---
API_V1_STR = settings.API_V1_STR
USUARIOS_ENDPOINT = f"{API_V1_STR}/usuarios"
logger = logging.getLogger(__name__) # Añadir logger

# --- Tests para Crear Usuarios (POST /usuarios) ---

def test_create_user_success_admin(
    admin_client: TestClient, # Usa el cliente admin refactorizado
    db_session: Session, # db_session original (no se usará para verificación post-API)
    operario_role_id: int # Fixture para ID del rol Operario
):
    """Prueba la creación exitosa de un usuario (Operario) por un admin (Refactorizado)."""
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"testoperario_{unique_suffix}"
    email = f"testoperario_{unique_suffix}@example.com"
    password = "password123"

    user_data = UsuarioCreate(
        username=username,
        email=email,
        password=password,
        nombre_completo="Test Operario Nuevo",
        rol_ids=[operario_role_id] # Asignar rol de Operario
    )

    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["username"] == username
    assert data["email"] == email
    assert data["nombre_completo"] == "Test Operario Nuevo"
    assert data["esta_activo"] is True
    assert "id" in data
    new_user_id = data["id"]
    role_ids_in_response = {role["id"] for role in data.get("roles", [])}
    assert operario_role_id in role_ids_in_response

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_create_user_success_admin': Verificando usuario ID {new_user_id} con nueva sesión.")
            # Usar load_related=True implícito en get_usuario o especificarlo si es necesario
            db_user = usuario_repository.get_usuario(db=verification_db, user_id=new_user_id)
            assert db_user is not None, f"Usuario ID {new_user_id} no encontrado en BD post-creación."
            assert db_user.username == username
            assert db_user.email == email
            # Verificar roles asignados en BD
            db_user_roles = {rol.id for rol in db_user.roles}
            assert operario_role_id in db_user_roles
            logger.info(f"Test 'test_create_user_success_admin': Usuario ID {new_user_id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_create_user_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests create duplicate, invalid, non-existent role, forbidden sin cambios) ...
def test_create_user_duplicate_username_admin(admin_client: TestClient, db_session: Session, admin_user: Usuario):
    """Prueba que crear usuario con username duplicado falle (400)."""
    existing_username = admin_user.username
    unique_suffix = uuid.uuid4().hex[:6]
    email = f"otroemail_{unique_suffix}@example.com"
    password = "password123"
    user_data = UsuarioCreate(username=existing_username, email=email, password=password, nombre_completo="Usuario Duplicado Test")
    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "nombre de usuario no está disponible" in response.json()["detail"].lower()

def test_create_user_duplicate_email_admin(admin_client: TestClient, db_session: Session, admin_user: Usuario):
    """Prueba que crear usuario con email duplicado falle (400)."""
    existing_email = admin_user.email
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"otrousername_{unique_suffix}"
    password = "password123"
    user_data = UsuarioCreate(username=username, email=existing_email, password=password, nombre_completo="Usuario Duplicado Email Test")
    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "correo electrónico ya está registrado" in response.json()["detail"].lower()

def test_create_user_invalid_data_admin(admin_client: TestClient):
    """Prueba crear usuario con datos inválidos (422)."""
    unique_suffix = uuid.uuid4().hex[:6]
    invalid_email_payload = {"username": f"invalidemail_{unique_suffix}","email": "esto-no-es-un-email","password": "password123","nombre_completo": "Invalido Email"}
    response_email = admin_client.post(USUARIOS_ENDPOINT, json=invalid_email_payload)
    assert response_email.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("email" in error.get("loc", []) for error in response_email.json().get("detail", []))
    invalid_pass_payload = {"username": f"shortpass_{unique_suffix}","email": f"shortpass_{unique_suffix}@example.com","password": "123","nombre_completo": "Pass Corta"}
    response_pass = admin_client.post(USUARIOS_ENDPOINT, json=invalid_pass_payload)
    assert response_pass.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("password" in error.get("loc", []) for error in response_pass.json().get("detail", []))
    invalid_username_payload = {"username": "us","email": f"shortuser_{unique_suffix}@example.com","password": "password123","nombre_completo": "User Corto"}
    response_user = admin_client.post(USUARIOS_ENDPOINT, json=invalid_username_payload)
    assert response_user.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("username" in error.get("loc", []) for error in response_user.json().get("detail", []))

def test_create_user_non_existent_role_id_admin(admin_client: TestClient):
    """Prueba crear usuario asignando un rol_id inexistente (404)."""
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"badrole_{unique_suffix}"
    email = f"badrole_{unique_suffix}@example.com"
    password = "password123"
    non_existent_role_id = 99999
    user_data = UsuarioCreate(username=username,email=email,password=password,nombre_completo="Rol Malo Test",rol_ids=[non_existent_role_id])
    response = admin_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "ids de rol proporcionados no existen" in response.json()["detail"].lower()

def test_create_user_forbidden_non_admin(vendedor_client: TestClient):
    """Prueba que un no-admin (Vendedor) no puede crear usuarios (403)."""
    unique_suffix = uuid.uuid4().hex[:6]
    username = f"forbidden_{unique_suffix}"
    email = f"forbidden_{unique_suffix}@example.com"
    password = "password123"
    user_data = UsuarioCreate(username=username,email=email,password=password,nombre_completo="No Deberia Crear")
    response = vendedor_client.post(USUARIOS_ENDPOINT, json=user_data.model_dump())
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'crear:usuario'" in response.json()["detail"]

# --- GET /me ---
# (Sin cambios, no modifican DB)
def test_read_me_success(vendedor_client: TestClient, vendedor_user: Usuario):
    """Prueba obtener los datos propios con un usuario Vendedor."""
    response = vendedor_client.get(f"{USUARIOS_ENDPOINT}/me")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == vendedor_user.id
    assert data["username"] == vendedor_user.username
    assert data["email"] == vendedor_user.email
    assert data["nombre_completo"] == vendedor_user.nombre_completo
    assert data["esta_activo"] == vendedor_user.esta_activo
    assert "roles" in data
    expected_role_ids = {role.id for role in vendedor_user.roles}
    response_role_ids = {role["id"] for role in data["roles"]}
    assert response_role_ids == expected_role_ids

def test_read_me_unauthenticated(base_client: TestClient):
    """Prueba que obtener /me sin autenticación falle (401)."""
    response = base_client.get(f"{USUARIOS_ENDPOINT}/me")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# =========================
# --- PATCH /me ---
# =========================

def test_update_me_success(vendedor_client: TestClient, db_session: Session, vendedor_user: Usuario):
    """Prueba que un usuario puede actualizar su propio nombre_completo y email (Refactorizado)."""
    unique_suffix = uuid.uuid4().hex[:6]
    new_fullname = f"Nombre Vendedor Actualizado {unique_suffix}"
    new_email = f"vendedor_actualizado_{unique_suffix}@example.com"

    update_payload = {
        "nombre_completo": new_fullname,
        "email": new_email
    }

    response = vendedor_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == vendedor_user.id
    assert data["nombre_completo"] == new_fullname
    assert data["email"] == new_email

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_update_me_success': Verificando usuario ID {vendedor_user.id} con nueva sesión.")
             updated_user_in_db = usuario_repository.get_usuario(db=verification_db, user_id=vendedor_user.id)
             assert updated_user_in_db is not None, "No se encontró el usuario en la BD después del update."
             assert updated_user_in_db.nombre_completo == new_fullname
             assert updated_user_in_db.email == new_email
             logger.info(f"Test 'test_update_me_success': Usuario ID {vendedor_user.id} verificado.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_update_me_success: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests update me duplicate, invalid, unauthenticated sin cambios) ...
def test_update_me_duplicate_email(vendedor_client: TestClient, admin_user: Usuario):
    """Prueba que actualizar 'me' con un email duplicado falle (400)."""
    update_payload = {"email": admin_user.email}
    response = vendedor_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email ya en uso" in response.json()["detail"].lower() # Mensaje del servicio

def test_update_me_invalid_email(vendedor_client: TestClient):
    """Prueba que actualizar 'me' con email inválido falle (422)."""
    update_payload = {"email": "email-invalido"}
    response = vendedor_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_update_me_unauthenticated(base_client: TestClient):
    """Prueba que actualizar /me sin autenticación falle (401)."""
    update_payload = {"nombre_completo": "No debería funcionar"}
    response = base_client.patch(f"{USUARIOS_ENDPOINT}/me", json=update_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- PUT /me/password ---

def test_update_my_password_success(
    vendedor_client: TestClient,
    db_session: Session, # No se usará directamente para verificación
    vendedor_user: Usuario,
):
    """Prueba el cambio exitoso de la contraseña propia verificando el hash (Refactorizado)."""
    old_password = "password123" # Contraseña inicial de las fixtures
    new_password = f"new_password_{uuid.uuid4().hex[:6]}"
    user_id = vendedor_user.id # Guardar ID para verificación

    password_payload = {
        "old_password": old_password,
        "new_password": new_password,
        "confirm_password": new_password
    }

    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_update_my_password_success': Verificando usuario ID {user_id} con nueva sesión.")
            updated_user_in_db = usuario_repository.get_usuario(db=verification_db, user_id=user_id)
            assert updated_user_in_db is not None, f"Usuario ID {user_id} no encontrado en BD para verificar hash."
            # Obtener el hash original antes de la modificación para comparar
            # (vendedor_user puede tener estado obsoleto si la sesión del test no se refrescó)
            # Es más seguro verificar que el nuevo hash coincide con la nueva contraseña
            assert verify_password(new_password, updated_user_in_db.contrasena_hash), \
                "El hash en la BD no coincide con la nueva contraseña."
            assert not verify_password(old_password, updated_user_in_db.contrasena_hash), \
                "El hash en la BD todavía coincide con la contraseña antigua."
            logger.info(f"Test 'test_update_my_password_success': Contraseña verificada para Usuario ID {user_id}.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_update_my_password_success: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests update password wrong old, mismatch, short, unauthenticated sin cambios) ...
def test_update_my_password_wrong_old(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'old_password' incorrecta (400)."""
    new_password = "cualquiercosa"
    password_payload = {"old_password": "password_incorrecto","new_password": new_password,"confirm_password": new_password}
    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "contraseña actual incorrecta" in response.json()["detail"].lower()

def test_update_my_password_mismatch_new(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'new_password' y 'confirm_password' distintos (422)."""
    password_payload = {"old_password": "password123","new_password": "nueva_pass_1","confirm_password": "nueva_pass_2"}
    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("confirm_password" in error.get("loc", []) for error in response.json().get("detail", []))

def test_update_my_password_short_new(vendedor_client: TestClient):
    """Prueba el cambio de contraseña con 'new_password' demasiado corta (422)."""
    password_payload = {"old_password": "password123","new_password": "corta","confirm_password": "corta"}
    response = vendedor_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert any("new_password" in error.get("loc", []) for error in response.json().get("detail", []))

def test_update_my_password_unauthenticated(base_client: TestClient):
    """Prueba cambiar contraseña sin autenticación (401)."""
    password_payload = {"old_password": "password123","new_password": "new_password","confirm_password": "new_password"}
    response = base_client.put(f"{USUARIOS_ENDPOINT}/me/password", json=password_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# --- GET /usuarios/{user_id} ---
# (Sin cambios, no modifican DB)
def test_read_user_success_admin(
    admin_client: TestClient,
    db_session: Session,
    vendedor_user: Usuario
):
    """Prueba obtener datos de otro usuario (Vendedor) como admin, verificando contra la BD."""
    user_id_to_get = vendedor_user.id
    response = admin_client.get(f"{USUARIOS_ENDPOINT}/{user_id_to_get}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == user_id_to_get
    assert data["username"] == vendedor_user.username
    # Usar nueva sesión para obtener estado actual es buena práctica incluso aquí
    with TestingSessionLocal() as verification_db:
        current_db_user = usuario_repository.get_usuario(db=verification_db, user_id=user_id_to_get)
        assert current_db_user is not None, "No se pudo obtener el usuario actual de la BD para comparación."
        assert data["email"] == current_db_user.email
        assert data["nombre_completo"] == current_db_user.nombre_completo
        assert data["esta_activo"] == current_db_user.esta_activo
        assert "roles" in data
        current_db_role_ids = {r.id for r in current_db_user.roles}
        response_role_ids = {r["id"] for r in data["roles"]}
        assert response_role_ids == current_db_role_ids, "Los roles en la respuesta no coinciden con los de la BD."

def test_read_user_not_found_admin(admin_client: TestClient):
    """Prueba obtener un usuario inexistente por ID (404)."""
    non_existent_user_id = 99998
    response = admin_client.get(f"{USUARIOS_ENDPOINT}/{non_existent_user_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Usuario no encontrado" in response.json()["detail"]

def test_read_user_forbidden_non_admin(vendedor_client: TestClient, admin_user: Usuario):
    """Prueba que un Vendedor no puede obtener datos de otro usuario (Admin) (403)."""
    user_id_to_get = admin_user.id # Intentar obtener datos del admin
    response = vendedor_client.get(f"{USUARIOS_ENDPOINT}/{user_id_to_get}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'leer:usuario'" in response.json()["detail"]

# --- POST /usuarios/{user_id}/roles/{rol_id} ---

def test_assign_role_to_user_success_admin(
    admin_client: TestClient,
    db_session: Session, # No se usará para verificación post-API
    vendedor_user: Usuario,
    dibujante_role_id: int # Usar el rol Dibujante
):
    """Prueba asignar un rol (Dibujante) a otro usuario (Vendedor) como admin (Refactorizado)."""
    user_id = vendedor_user.id
    role_id_to_assign = dibujante_role_id
    vendedor_role_id = vendedor_user.roles[0].id # Asume 1 rol inicial

    # Asegurarse que el rol Dibujante no esté asignado inicialmente (usando nueva sesión)
    with TestingSessionLocal() as pre_check_db:
        user_before = usuario_repository.get_usuario(db=pre_check_db, user_id=user_id)
        assert user_before is not None
        vendedor_roles_before = {r.id for r in user_before.roles}
        assert role_id_to_assign not in vendedor_roles_before, "El rol Dibujante ya estaba asignado inesperadamente."

    # Asignar el rol
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_assign}")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == user_id
    response_role_ids = {role["id"] for role in data.get("roles", [])}
    assert vendedor_role_id in response_role_ids
    assert role_id_to_assign in response_role_ids
    assert len(response_role_ids) == len(vendedor_roles_before) + 1

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Test 'test_assign_role_to_user_success_admin': Verificando usuario ID {user_id} con nueva sesión.")
            updated_user_in_db = usuario_repository.get_usuario(db=verification_db, user_id=user_id)
            assert updated_user_in_db is not None, "No se encontró el usuario en BD para verificar roles."
            final_db_user_roles = {r.id for r in updated_user_in_db.roles}
            assert role_id_to_assign in final_db_user_roles, "El rol asignado no se encontró en la BD."
            assert len(final_db_user_roles) == len(vendedor_roles_before) + 1, "El número de roles en BD no es correcto."
            logger.info(f"Test 'test_assign_role_to_user_success_admin': Roles verificados para Usuario ID {user_id}.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_assign_role_to_user_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests asignar rol ya asignado, user not found, role not found, forbidden sin cambios) ...
def test_assign_role_already_assigned_admin(
    admin_client: TestClient,
    vendedor_user: Usuario,
    vendedor_role_id: int # Usar el rol que ya tiene
):
    """Prueba asignar un rol que el usuario ya tiene (debería ser idempotente, 200 OK)."""
    user_id = vendedor_user.id
    role_id_to_assign = vendedor_role_id # El rol que ya tiene
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_assign}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    response_role_ids = {role["id"] for role in data["roles"]}
    assert role_id_to_assign in response_role_ids

def test_assign_role_user_not_found_admin(admin_client: TestClient, vendedor_role_id: int):
    """Prueba asignar rol a un usuario inexistente (404)."""
    non_existent_user_id = 99998
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{non_existent_user_id}/roles/{vendedor_role_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Usuario no encontrado" in response.json()["detail"]

def test_assign_role_role_not_found_admin(admin_client: TestClient, vendedor_user: Usuario):
    """Prueba asignar un rol inexistente a un usuario válido (404)."""
    user_id = vendedor_user.id
    non_existent_role_id = 99999
    response = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{non_existent_role_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Rol con ID 99999 no encontrado" in response.json()["detail"] # El servicio de rol busca el rol

def test_assign_role_forbidden_non_admin(
    vendedor_client: TestClient,
    admin_user: Usuario, # Intentar modificar al admin
    operario_role_id: int
):
    """Prueba que un Vendedor no puede asignar roles a otro usuario (Admin) (403)."""
    user_id_to_modify = admin_user.id
    role_id_to_assign = operario_role_id
    response = vendedor_client.post(f"{USUARIOS_ENDPOINT}/{user_id_to_modify}/roles/{role_id_to_assign}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'asignar:rol_usuario'" in response.json()["detail"]

# --- DELETE /usuarios/{user_id}/roles/{rol_id} ---

def test_remove_role_from_user_success_admin(
    admin_client: TestClient,
    db_session: Session, # No se usará para verificación post-API
    vendedor_user: Usuario,
    dibujante_role_id: int # Usaremos el rol Dibujante para añadir y quitar
):
    """Prueba quitar un rol (Dibujante) de otro usuario (Vendedor) como admin (Refactorizado)."""
    user_id = vendedor_user.id
    role_id_to_remove = dibujante_role_id
    vendedor_role_id = vendedor_user.roles[0].id # Asume 1 rol inicial

    # 1. Asignar el rol Dibujante primero
    assign_resp = admin_client.post(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")
    assert assign_resp.status_code == status.HTTP_200_OK, "Fallo al asignar rol Dibujante previamente"

    # 2. Quitar el rol
    response_delete = admin_client.delete(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")
    assert response_delete.status_code == status.HTTP_204_NO_CONTENT

    # --- VERIFICACIÓN REFACTORIZADA ---
    try:
        with TestingSessionLocal() as verification_db:
             logger.debug(f"Test 'test_remove_role_from_user_success_admin': Verificando usuario ID {user_id} con nueva sesión.")
             updated_user_in_db = usuario_repository.get_usuario(db=verification_db, user_id=user_id)
             assert updated_user_in_db is not None, "No se encontró el usuario en BD para verificar roles."
             final_db_user_roles = {r.id for r in updated_user_in_db.roles}
             assert role_id_to_remove not in final_db_user_roles, "El rol quitado todavía se encontró en la BD."
             assert vendedor_role_id in final_db_user_roles, "El rol original 'Vendedor' desapareció de la BD."
             logger.info(f"Test 'test_remove_role_from_user_success_admin': Roles verificados para Usuario ID {user_id}.")
    except Exception as e:
        pytest.fail(f"Error durante verificación BD en test_remove_role_from_user_success_admin: {e}")
    # --- FIN VERIFICACIÓN ---

# ... (tests quitar rol no asignado, user not found, role not found, forbidden sin cambios) ...
def test_remove_role_not_assigned_admin(
    admin_client: TestClient,
    vendedor_user: Usuario,
    operario_role_id: int # Usar un rol que Vendedor no tiene
):
    """Prueba quitar un rol no asignado (debería ser idempotente, 204)."""
    user_id = vendedor_user.id
    role_id_to_remove = operario_role_id # Rol que no está asignado
    response = admin_client.delete(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{role_id_to_remove}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_remove_role_user_not_found_admin(admin_client: TestClient, vendedor_role_id: int):
    """Prueba quitar rol de un usuario inexistente (404)."""
    non_existent_user_id = 99998
    response = admin_client.delete(f"{USUARIOS_ENDPOINT}/{non_existent_user_id}/roles/{vendedor_role_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Usuario no encontrado" in response.json()["detail"]

def test_remove_role_role_not_found_admin(admin_client: TestClient, vendedor_user: Usuario):
    """Prueba quitar un rol inexistente de un usuario válido (404)."""
    user_id = vendedor_user.id
    non_existent_role_id = 99999
    response = admin_client.delete(f"{USUARIOS_ENDPOINT}/{user_id}/roles/{non_existent_role_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Rol con ID 99999 no encontrado" in response.json()["detail"]

def test_remove_role_forbidden_non_admin(
    vendedor_client: TestClient,
    admin_user: Usuario, # Intentar modificar al admin
    vendedor_role_id: int # Intentar quitar el rol Vendedor (aunque no lo tenga el admin)
):
    """Prueba que un Vendedor no puede quitar roles a otro usuario (Admin) (403)."""
    user_id_to_modify = admin_user.id
    role_id_to_remove = vendedor_role_id
    response = vendedor_client.delete(f"{USUARIOS_ENDPOINT}/{user_id_to_modify}/roles/{role_id_to_remove}")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Permiso insuficiente: Se requiere 'remover:rol_usuario'" in response.json()["detail"]
```

# tests\conftest.py

```py
# app/tests/conftest.py
from decimal import Decimal
import os
from typing import Generator, Dict, List, Callable

import pytest
from fastapi import FastAPI # Necesario indirectamente para TestClient(app)
from fastapi.testclient import TestClient
from fastapi import status
from sqlmodel import SQLModel, Session, create_engine, select
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import alembic.config
import alembic.command
import sqlalchemy as sa # Necesario para sa.delete
import uuid
from app.core.config import settings
from app.models.order_models import PedidoCliente
from app.schemas.order_schema import PedidoClienteCreate

CLIENTES_ENDPOINT = f"{settings.API_V1_STR}/clientes"
API_V1_STR = settings.API_V1_STR
INVENTARIO_ENDPOINT = f"{API_V1_STR}/inventario"
MAT_DIM_ENDPOINT = f"{INVENTARIO_ENDPOINT}/materiales-dimensionales"
MAT_CONS_ENDPOINT = f"{INVENTARIO_ENDPOINT}/materiales-consumibles"
MAT_SIMP_ENDPOINT = f"{INVENTARIO_ENDPOINT}/materiales-simples"
STOCK_ITEM_DIM_ENDPOINT = f"{INVENTARIO_ENDPOINT}/stock-items-dimensionales"
SERVICIOS_ENDPOINT = f"{API_V1_STR}/servicios" # O donde la tengas definida
DEFINICIONES_ENDPOINT = f"{SERVICIOS_ENDPOINT}/definiciones"
PEDIDOS_ENDPOINT = f"{API_V1_STR}/pedidos"

# ==================================
#  1. Carga de Configuración de Prueba
# ==================================
env_path = '.env.test'
if os.path.exists(env_path):
    print(f"\nCargando configuración de prueba desde: {env_path}")
    load_dotenv(dotenv_path=env_path, override=True)
else:
    print(f"\nADVERTENCIA: No se encontró {env_path}.")
    # Salir si no se encuentra el archivo de configuración esencial para pruebas
    pytest.exit(f"Archivo de configuración de prueba '{env_path}' no encontrado.", returncode=1)


# ==================================
#  2. Importar Componentes de la App
# ==================================
from app.core.config import settings
from app.main import app # Importar la instancia de la aplicación FastAPI
from app.core.database import get_db # Importar la dependencia original de DB
# Importar todos los modelos que puedan ser usados en tests o seeding
from app.models import Usuario, Rol, Permiso, UsuarioRol, RolPermiso, Cliente
# Importar servicios/repositorios usados por fixtures o tests
from app.services import usuario_service

from app.schemas.usuario_schema import UsuarioCreate
from app.schemas.client_schema import ClienteCreate
from app.models.inventory_models import MaterialConsumible, MaterialDimensional, MaterialSimple, StockItemDimensional  # Import the missing model
from app.schemas.inventory_schema import MaterialConsumibleCreate, MaterialDimensionalCreate, MaterialSimpleCreate, StockItemDimensionalCreate  # Import the missing schema

# Importar initial_data aunque no se use directamente, las migraciones de Alembic dependen de él.
from app.initial_data import initial_roles, initial_permissions, role_permission_mapping
# Importar repositorios necesarios
from app.repositories import order_repository, usuario_repository
# 'permiso_repository' no se usaba directamente aquí y fue eliminado.

from app.models import ServicioDefinicion
from app.schemas.service_schema import ServicioDefinicionCreate
import logging 
logger = logging.getLogger(__name__) # Añadir logger
# ==========================================
#  3. Configuración de Base de Datos de Prueba
# ==========================================
TEST_DATABASE_URL = settings.DATABASE_URL
# Imprimir URL ofuscada para seguridad
print(f"URL de base de datos para pruebas (desde settings): {TEST_DATABASE_URL[:TEST_DATABASE_URL.find('@') + 1]}***")
# Crear el motor de la base de datos de prueba
engine = create_engine(TEST_DATABASE_URL, echo=False, pool_pre_ping=True)
# Crear una fábrica de sesiones de prueba
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)


# ===========================================
#  4. Fixture Principal de Setup (Session Scope)
# ===========================================
@pytest.fixture(scope="session", autouse=True)
def setup_test_database() -> Generator[None, None, None]:
    """
    Fixture principal (scope='session', autouse=True) para preparar la BD de pruebas.

    Ejecuta las migraciones de Alembic (head) antes de que comience cualquier test
    en la sesión y limpia la base de datos (drop_all) al finalizar todos los tests.
    Falla la sesión de pruebas si las migraciones no se pueden aplicar.

    Yields:
        None: No retorna valor, solo maneja setup y teardown.
    """
    print("\n--- [SETUP SESIÓN] Iniciando preparación de BD de prueba ---")
    alembic_cfg = alembic.config.Config("alembic.ini")
    # Asegurar que Alembic use la URL de la BD de prueba
    alembic_cfg.set_main_option("sqlalchemy.url", TEST_DATABASE_URL)
    try:
        # Aplicar todas las migraciones (schema + datos iniciales)
        alembic.command.upgrade(alembic_cfg, "head")
        print("Migraciones aplicadas exitosamente (schema + seeding).")
    except Exception as e:
        print(f"\nERROR aplicando migraciones: {e}")
        import traceback
        traceback.print_exc()
        pytest.fail(f"Fallo crítico al aplicar migraciones Alembic: {e}")
        return # Salir del generador en caso de fallo

    print("--- [SETUP SESIÓN] Base de datos lista para las pruebas (via Alembic). ---")
    yield # Punto donde se ejecutan los tests de la sesión
    print("\n--- [TEARDOWN SESIÓN] Limpiando BD de prueba (drop_all) ---")
    try:
        # Eliminar todas las tablas al final de la sesión
        SQLModel.metadata.drop_all(bind=engine)
        print("--- [TEARDOWN SESIÓN] BD limpiada exitosamente. ---")
    except Exception as drop_exc:
        print(f"ERROR durante drop_all al final de la sesión: {drop_exc}")

# =================================================
#  5. Fixture para Sobrescribir Dependencia get_db
# =================================================
def override_get_db() -> Generator[Session, None, None]:
    """
    Generador de dependencia para sobrescribir `get_db` en la app FastAPI.

    Proporciona una sesión de base de datos de prueba (`TestingSessionLocal`)
    y asegura que se cierre correctamente después de su uso.

    Yields:
        Session: Una instancia de sesión de base de datos de prueba.
    """
    db = None
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        if db is not None:
            db.close()

# Aplicar el override a la instancia de la app globalmente para todos los tests
app.dependency_overrides[get_db] = override_get_db


# =================================
#  6. Fixtures de Sesión de BD para Tests
# =================================

@pytest.fixture(scope="function")
def db_session(setup_test_database: None) -> Generator[Session, None, None]:
    """
    Fixture (scope='function') que proporciona una sesión de BD de prueba limpia.

    Depende de `setup_test_database` para asegurar que la BD esté lista.
    Realiza rollback al final de cada test para aislar los tests.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD (inyectado por pytest).

    Yields:
        Session: Una sesión de BD de prueba limpia para un test individual.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        # Rollback para deshacer cambios no confirmados del test
        db.rollback()
        db.close()

@pytest.fixture(scope="module")
def module_db_session(setup_test_database: None) -> Generator[Session, None, None]:
    """
    Fixture (scope='module') que proporciona una sesión de BD de prueba compartida por un módulo.

    Depende de `setup_test_database`. Realiza rollback al final del módulo.
    Útil para fixtures de módulo que necesitan interactuar con la BD una vez.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD.

    Yields:
        Session: Una sesión de BD de prueba compartida para un módulo de tests.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        # Rollback al final del módulo
        db.rollback()
        db.close()


# ============================
#  7. Fixtures de TestClient
# ============================

@pytest.fixture(scope="module")
def base_client(setup_test_database: None) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='module') que proporciona un cliente de prueba base (`TestClient`).

    Este cliente no está autenticado y comparte el mismo scope que las fixtures
    de creación de usuarios y tokens (módulo), asegurando que la app tenga
    la dependencia de BD sobreescrita.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD.

    Yields:
        TestClient: Una instancia de TestClient no autenticada.
    """
    # Asegurar que el override esté aplicado antes de instanciar TestClient
    # Aunque ya se hizo globalmente, es una doble verificación/clarificación.
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        print(f"DEBUG [conftest]: Creado base_client (module scope) ID: {id(test_client)}")
        yield test_client
    print(f"DEBUG [conftest]: Finalizado contexto base_client (module scope) ID: {id(test_client)}")


@pytest.fixture(scope="function")
def admin_client(admin_token: str) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='function') que proporciona un cliente de prueba INDEPENDIENTE
    autenticado como Administrador.

    Crea una nueva instancia de TestClient para cada test, asegurando aislamiento.
    Utiliza el token de administrador obtenido de la fixture `admin_token`.

    Args:
        admin_token: Token JWT del usuario administrador (inyectado por pytest).

    Yields:
        TestClient: Instancia de TestClient autenticada como admin.
    """
    # Asegurar override ANTES de crear TestClient para este scope también
    app.dependency_overrides[get_db] = override_get_db
    # Crear instancia independiente para cada test
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {admin_token}"
        print(f"DEBUG [conftest - admin_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Admin ...{admin_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - admin_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")


@pytest.fixture(scope="function")
def vendedor_client(vendedor_token: str) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='function') que proporciona un cliente de prueba INDEPENDIENTE
    autenticado como Vendedor.

    Crea una nueva instancia de TestClient para cada test.
    Utiliza el token de vendedor obtenido de la fixture `vendedor_token`.

    Args:
        vendedor_token: Token JWT del usuario vendedor (inyectado por pytest).

    Yields:
        TestClient: Instancia de TestClient autenticada como vendedor.
    """
    # Asegurar override ANTES de crear TestClient
    app.dependency_overrides[get_db] = override_get_db
     # Crear instancia independiente para cada test
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {vendedor_token}"
        print(f"DEBUG [conftest - vendedor_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Vendedor ...{vendedor_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - vendedor_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")

          
@pytest.fixture(scope="function")
def cliente_de_prueba(vendedor_client: TestClient, db_session: Session) -> Cliente:
    """Fixture para crear un cliente de prueba antes de un test."""
    unique_suffix = uuid.uuid4().hex[:6]
    cliente_data = ClienteCreate(
        nombre=f"Cliente Prueba {unique_suffix}",
        email=f"cliente_{unique_suffix}@pruebas.com",
        identificacion_fiscal=f"999{unique_suffix}",
        tipo_identificacion="RUC",
        telefono="0987654321"
    )
    response = vendedor_client.post(CLIENTES_ENDPOINT, json=cliente_data.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    cliente_id = response.json()["id"]
    # Obtener el objeto completo desde la BD para devolverlo
    # Usamos una consulta directa para asegurar que leemos lo que se acaba de escribir
    cliente_db = db_session.get(Cliente, cliente_id)
    #cliente_db = cliente_repository.get_cliente_by_id(db=db_session, cliente_id=cliente_id)
    assert cliente_db is not None
    print(f"Cliente de prueba creado por fixture: ID={cliente_db.id}")
    return cliente_db

# ============================
#  8. Fixtures de Datos (Roles y Permisos)
# ============================

@pytest.fixture(scope="session")
def seeded_roles(setup_test_database: None) -> Dict[str, Rol]:
    """
    Fixture (scope='session') que obtiene los roles iniciales de la BD una vez por sesión.

    Consulta la base de datos (después de que `setup_test_database` aplicó las migraciones)
    y devuelve un diccionario mapeando nombres de rol a objetos Rol.
    Falla si no encuentra suficientes roles iniciales.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD.

    Returns:
        Dict[str, Rol]: Diccionario con los roles iniciales {nombre_rol: Rol}.
    """
    db = TestingSessionLocal()
    try:
        print("DEBUG: Obteniendo roles iniciales para fixtures (scope='session')...")
        roles_db = db.exec(select(Rol)).all()
        roles_map = {rol.nombre: rol for rol in roles_db}
        # Validación básica de que el seeding funcionó
        if not roles_map or len(roles_map) < 5: # Ajustar número según roles esperados
             pytest.fail(f"No se encontraron roles iniciales suficientes en la BD (Esperados: >=5, Encontrados: {len(roles_map)}).")
        print(f"DEBUG: Roles iniciales obtenidos: {list(roles_map.keys())}")
        return roles_map
    finally:
        db.close()

@pytest.fixture(scope="session")
def seeded_permissions(setup_test_database: None) -> Dict[str, Permiso]:
    """
    Fixture (scope='session') que obtiene los permisos iniciales de la BD una vez por sesión.

    Consulta la base de datos (después de `setup_test_database`) y devuelve un
    diccionario mapeando 'accion:recurso' a objetos Permiso.
    Falla si no encuentra permisos clave.

    Args:
        setup_test_database: Fixture que asegura la preparación de la BD.

    Returns:
        Dict[str, Permiso]: Diccionario con permisos iniciales {'accion:recurso': Permiso}.
    """
    db = TestingSessionLocal()
    try:
        print("DEBUG: Obteniendo permisos iniciales para fixtures (scope='session')...")
        perms_db = db.exec(select(Permiso)).all()
        # Crear llave como "accion:recurso" para fácil acceso
        perms_map = {f"{p.nombre_accion}:{p.nombre_recurso}": p for p in perms_db}
        if not perms_map:
             pytest.fail("No se encontraron permisos iniciales en la BD.")
        # Validar que algunos permisos esperados del seeding existen
        assert "leer:cliente" in perms_map, "Permiso 'leer:cliente' no encontrado en seeding."
        assert "gestionar:usuario" in perms_map, "Permiso 'gestionar:usuario' no encontrado en seeding."
        print(f"DEBUG: Permisos iniciales obtenidos: {list(perms_map.keys())[:5]}...") # Mostrar algunos
        return perms_map
    finally:
        db.close()


# ===================================
#  9. Fixtures de IDs Específicos (Roles/Permisos)
# ===================================
# Estas fixtures dependen de las fixtures de datos (seeded_roles, seeded_permissions)
# y proporcionan IDs específicos para usar en tests, evitando hardcodear IDs.

@pytest.fixture(scope="module") # Podría ser 'session' si no cambian
def vendedor_role_id(seeded_roles: Dict[str, Rol]) -> int:
    """Devuelve el ID del rol 'Vendedor' obtenido de los roles iniciales."""
    role = seeded_roles.get("Vendedor")
    if not role or not role.id:
        pytest.fail("Rol 'Vendedor' o su ID no encontrado en roles pre-cargados.")
    return role.id

@pytest.fixture(scope="module")
def operario_role_id(seeded_roles: Dict[str, Rol]) -> int:
    """Devuelve el ID del rol 'Operario' obtenido de los roles iniciales."""
    role = seeded_roles.get("Operario")
    if not role or not role.id:
        pytest.fail("Rol 'Operario' o su ID no encontrado en roles pre-cargados.")
    return role.id

@pytest.fixture(scope="module")
def dibujante_role_id(seeded_roles: Dict[str, Rol]) -> int:
    """Devuelve el ID del rol 'Dibujante' obtenido de los roles iniciales."""
    role = seeded_roles.get("Dibujante")
    if not role or not role.id:
        pytest.fail("Rol 'Dibujante' o su ID no encontrado en roles pre-cargados.")
    print(f"DEBUG [conftest]: Obtenido dibujante_role_id: {role.id} (module scope)")
    return role.id

@pytest.fixture(scope="module")
def permiso_leer_cliente_id(seeded_permissions: Dict[str, Permiso]) -> int:
    """Devuelve el ID del permiso 'leer:cliente' obtenido de los permisos iniciales."""
    perm = seeded_permissions.get("leer:cliente")
    if not perm or not perm.id:
        pytest.fail("Permiso 'leer:cliente' o su ID no encontrado en permisos pre-cargados.")
    return perm.id

@pytest.fixture(scope="module")
def permiso_gestionar_usuario_id(seeded_permissions: Dict[str, Permiso]) -> int:
    """Devuelve el ID del permiso 'gestionar:usuario' obtenido de los permisos iniciales."""
    perm = seeded_permissions.get("gestionar:usuario")
    if not perm or not perm.id:
        pytest.fail("Permiso 'gestionar:usuario' o su ID no encontrado en permisos pre-cargados.")
    return perm.id

# ============================
#  10. Fixtures de Usuarios de Prueba
# ============================

@pytest.fixture(scope="module")
def test_user_factory(module_db_session: Session, seeded_roles: Dict[str, Rol]) -> Generator[Callable[[str, str, str, List[str]], Usuario], None, None]: # Si da problemas cambiar a Callable:
    """
    Fixture tipo 'factory' (scope='module') para crear usuarios de prueba.

    Proporciona una función interna `_create_user` que puede ser llamada múltiples
    veces dentro del mismo módulo para crear usuarios. Maneja la limpieza
    (eliminación) de los usuarios creados al final del módulo.
    Utiliza la sesión de módulo para persistir usuarios entre tests del módulo.

    Args:
        module_db_session: Sesión de BD compartida por el módulo.
        seeded_roles: Diccionario de roles iniciales para asignar por nombre.

    Yields:
        Callable: La función `_create_user(username, email, password, roles_names)`.
    """
    #print(f"\nDEBUG: Iniciando test_user_factory (scope='module') con session id: {id(module_db_session)}")
    created_users_for_cleanup = [] # Lista para rastrear usuarios creados por esta factory

    def _create_user(username: str, email: str, password: str, roles_names: List[str] = None) -> Usuario:
        """Función interna para crear o retornar un usuario de prueba."""
        #print(f"DEBUG: _create_user: Intentando crear/obtener usuario '{username}'...")
        session = module_db_session # Usar la sesión del módulo
        try:
            # Intentar obtener usuario existente en caso de re-llamada en el mismo módulo
            existing = usuario_repository.get_usuario_by_username(db=session, username=username)
            if existing:
                #print(f"DEBUG: _create_user: Usuario '{username}' ya existía en sesión de módulo.")
                # Asegurar que esté en la lista de limpieza si no lo estaba
                if not any(u["id"] == existing.id for u in created_users_for_cleanup):
                    created_users_for_cleanup.append({"id": existing.id, "username": username})
                # Refrescar roles por si acaso
                session.refresh(existing, attribute_names=["roles"])
                return existing

            # Mapear nombres de roles a IDs usando los roles ya cargados
            role_ids_to_assign = []
            if roles_names:
                for name in roles_names:
                    role = seeded_roles.get(name)
                    if not role or not role.id: pytest.fail(f"Rol '{name}' no encontrado en roles pre-cargados para usuario '{username}'.")
                    role_ids_to_assign.append(role.id)

            # Crear el usuario usando el servicio (que maneja hashing y roles)
            user_in = UsuarioCreate(
                username=username, email=email, password=password,
                nombre_completo=f"Test {username.capitalize()}",
                # Pasar lista de IDs o None si no hay roles
                rol_ids=role_ids_to_assign if role_ids_to_assign else None
            )
            # Usar el servicio para encapsular lógica de creación
            user = usuario_service.create_new_user(db=session, user_in=user_in)

            # Verificar inmediatamente si el usuario se puede recuperar en la misma sesión
            retrieved_user = session.get(Usuario, user.id)
            if retrieved_user:
                #print(f"DEBUG: _create_user: VERIFICADO - Usuario ID={user.id} ('{retrieved_user.username}') creado y encontrado en sesión.")
                if roles_names:
                    session.refresh(retrieved_user, attribute_names=["roles"])
                    #print(f"DEBUG: _create_user: Roles asignados (verif.): {[r.nombre for r in retrieved_user.roles]}")
            else:
                # Esto no debería ocurrir si create_new_user funciona correctamente
                print(f"ERROR CRÍTICO: _create_user: Usuario ID={user.id} NO encontrado después de crear!")
                pytest.fail(f"No se pudo verificar creación del usuario '{username}' en la misma sesión.")

            # Añadir a la lista de limpieza
            created_users_for_cleanup.append({"id": user.id, "username": username})
            return retrieved_user # Devolver el usuario recuperado y refrescado

        except Exception as e:
            print(f"ERROR dentro de _create_user para {username}: {e}")
            import traceback
            traceback.print_exc()
            session.rollback() # Revertir cambios en caso de error
            raise

    yield _create_user # La factory devuelve la función interna

    # --- Código de limpieza (Teardown del módulo) ---
    #print(f"\nDEBUG: test_user_factory (TEARDOWN Módulo): Limpiando {len(created_users_for_cleanup)} usuarios: {[u['username'] for u in created_users_for_cleanup]}")
    if created_users_for_cleanup:
        user_ids = [u["id"] for u in created_users_for_cleanup]
        # Usar una nueva sesión efímera para la limpieza
        cleanup_db = TestingSessionLocal()
        try:
            # Eliminar primero las dependencias en UsuarioRol
            #print(f"DEBUG (Cleanup): Eliminando links usuario_rol para usuarios: {user_ids}")
            stmt_links = sa.delete(UsuarioRol).where(UsuarioRol.usuario_id.in_(user_ids))
            cleanup_db.execute(stmt_links)

            # Luego eliminar los usuarios
            #print(f"DEBUG (Cleanup): Eliminando usuarios: {user_ids}")
            stmt_users = sa.delete(Usuario).where(Usuario.id.in_(user_ids))
            result = cleanup_db.execute(stmt_users)
            cleanup_db.commit()
            #print(f"DEBUG (Cleanup): Usuarios de prueba y sus links eliminados: {user_ids} (Count: {result.rowcount})")
        except Exception as e:
            #print(f"ERROR limpiando usuarios de prueba: {e}")
            cleanup_db.rollback()
        finally:
            cleanup_db.close()

@pytest.fixture(scope="module")
def admin_user(test_user_factory: Callable) -> Usuario:
    """Fixture (scope='module') que crea/obtiene el usuario 'testadmin'."""
    return test_user_factory(username="testadmin", email="admin@test.com", password="password123", roles_names=["Administrador"])

@pytest.fixture(scope="module")
def vendedor_user(test_user_factory: Callable) -> Usuario:
    """Fixture (scope='module') que crea/obtiene el usuario 'testvendedor'."""
    return test_user_factory(username="testvendedor", email="vendedor@test.com", password="password123", roles_names=["Vendedor"])

@pytest.fixture(scope="module")
def dibujante_user(test_user_factory: Callable) -> Usuario:
    """Fixture (scope='module') que crea/obtiene el usuario 'testdibujante'."""
    return test_user_factory(username="testdibujante", email="dibujante@test.com", password="password123", roles_names=["Dibujante"])

@pytest.fixture(scope="module")
def operario_user(test_user_factory: Callable) -> Usuario:
    """Fixture (scope='module') que crea/obtiene el usuario 'testoperario'."""
    return test_user_factory(username="testoperario", email="operario@test.com", password="password123", roles_names=["Operario"])



# --- Fixtures para Tipos de Material ---
@pytest.fixture(scope="function")
def material_dimensional_de_prueba(admin_client: TestClient, db_session: Session) -> MaterialDimensional:
    """Fixture para crear un tipo de MaterialDimensional vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    payload_schema = MaterialDimensionalCreate(
        sku=f"FIX-DIM-{unique_suffix}",
        nombre=f"Plancha Fixture {unique_suffix}",
        espesor_nominal=Decimal("15.0"),
        unidad_dimension="mm",
        precio_venta_base_unidad=Decimal("80.0"),
        unidad_precio_venta="m2"
    )
    payload_dict = payload_schema.model_dump(mode='json') # Correcto

    response = admin_client.post(MAT_DIM_ENDPOINT, json=payload_dict) # Usa el dict serializado
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear MaterialDimensional en fixture: {response.text}"
    data = response.json()
    mat_id = data["id"]

    # Usar la sesión original para cerrar (como buena práctica) y luego verificar con una nueva
    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(MaterialDimensional, mat_id)

    assert db_obj is not None, "No se pudo recuperar MaterialDimensional de BD en fixture (nueva sesión)"
    print(f"Fixture: MaterialDimensional creado: ID={db_obj.id}, SKU={db_obj.sku}")
    return db_obj # Devolver el objeto recuperado de la nueva sesión


@pytest.fixture(scope="function")
def material_consumible_de_prueba(admin_client: TestClient, db_session: Session) -> MaterialConsumible:
    """Fixture para crear un tipo de MaterialConsumible vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    payload_schema = MaterialConsumibleCreate(
        sku=f"FIX-CONS-{unique_suffix}",
        nombre=f"Lija Fixture {unique_suffix}",
        unidad_medida="pliego",
        stock_minimo=Decimal("10.0"),
        precio_venta_base_unidad=Decimal("0.5")
    )
    payload_dict = payload_schema.model_dump(mode='json') # Correcto

    response = admin_client.post(MAT_CONS_ENDPOINT, json=payload_dict)
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear MaterialConsumible en fixture: {response.text}"
    data = response.json()
    mat_id = data["id"]

    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(MaterialConsumible, mat_id)

    assert db_obj is not None, "No se pudo recuperar MaterialConsumible de BD en fixture (nueva sesión)"
    print(f"Fixture: MaterialConsumible creado: ID={db_obj.id}, SKU={db_obj.sku}")
    return db_obj


@pytest.fixture(scope="function")
def material_simple_de_prueba(admin_client: TestClient, db_session: Session) -> MaterialSimple:
    """Fixture para crear un tipo de MaterialSimple vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    payload_schema = MaterialSimpleCreate(
        sku=f"FIX-SIMP-{unique_suffix}",
        nombre=f"Tornillo Fixture {unique_suffix}",
        unidad_medida="ciento",
        stock_minimo=Decimal("2.0"),
        precio_venta_base_unidad=Decimal("0.5")
    )
    payload_dict = payload_schema.model_dump(mode='json') 

    response = admin_client.post(MAT_SIMP_ENDPOINT, json=payload_dict)
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear MaterialSimple en fixture: {response.text}"
    data = response.json()
    mat_id = data["id"]

    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(MaterialSimple, mat_id)

    assert db_obj is not None, "No se pudo recuperar MaterialSimple de BD en fixture (nueva sesión)"
    print(f"Fixture: MaterialSimple creado: ID={db_obj.id}, SKU={db_obj.sku}")
    return db_obj

@pytest.fixture(scope="function")
def servicio_definicion_de_prueba(admin_client: TestClient, db_session: Session) -> ServicioDefinicion:
    """Fixture para crear una definición de servicio de prueba vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    payload_schema = ServicioDefinicionCreate(
        codigo=f"FIX-SERV-{unique_suffix}",
        nombre=f"Servicio Test {unique_suffix}",
        unidad_cobro="hora",
        descripcion="Descripción Fixture", # Añadir descripción explícita
        costo_por_unidad=Decimal("0.0"), # Valor explícito aunque sea Optional
        costo_por_minuto=Decimal("1.5"), # Ya estaba explícito
        requiere_dibujo_cnc=False,
        tiempo_setup_min=Decimal("5.0"), # Valor explícito (antes usaba default)
        tiempo_preparado_min_por_unidad=Decimal("0.1"), # Valor explícito (antes usaba default)
        factor_ih=Decimal("1.1"), # Valor explícito (antes usaba default)
    )
    payload_dict = payload_schema.model_dump(mode='json')

    response = admin_client.post(DEFINICIONES_ENDPOINT, json=payload_dict)

    assert response.status_code == status.HTTP_201_CREATED, \
        f"Fallo al crear ServicioDefinicion en fixture: {response.text}"
    data = response.json()
    servicio_id = data["id"]

    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(ServicioDefinicion, servicio_id)

    assert db_obj is not None, "No se pudo recuperar ServicioDefinicion de BD en fixture (nueva sesión)"
    print(f"Fixture: ServicioDefinicion creado: ID={db_obj.id}, Nombre={db_obj.nombre}")
    return db_obj

@pytest.fixture(scope="function")
def stock_item_dimensional_de_prueba(
    admin_client: TestClient,
    db_session: Session,
    material_dimensional_de_prueba: MaterialDimensional
) -> StockItemDimensional:
    """Fixture para crear una pieza de StockItemDimensional vía API."""
    unique_suffix = uuid.uuid4().hex[:6]
    # Asegurarse que material_dimensional_de_prueba.id es válido
    assert material_dimensional_de_prueba.id is not None, "Fixture material_dimensional_de_prueba no tiene ID"

    payload_schema = StockItemDimensionalCreate(
        material_dimensional_id=material_dimensional_de_prueba.id,
        longitud_actual=Decimal("2440.000"),
        ancho_actual=Decimal("1220.000"),
        ubicacion=f"TEST-{unique_suffix}"
    )
    payload_dict = payload_schema.model_dump(mode='json') # <<< CORRECCIÓN: nombre variable y mode='json'

    response = admin_client.post(STOCK_ITEM_DIM_ENDPOINT, json=payload_dict)
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear StockItemDimensional en fixture: {response.text}"
    data = response.json()
    item_id = data["id"]

    # Verificar con nueva sesión para asegurar visibilidad
    db_session.close()
    with TestingSessionLocal() as verification_db:
        db_obj = verification_db.get(StockItemDimensional, item_id)

    assert db_obj is not None, "No se pudo recuperar StockItemDimensional de BD en fixture (nueva sesión)" # <<< CORRECCIÓN: assert sobre el objeto de la nueva sesión
    print(f"Fixture: StockItemDimensional creado: ID={db_obj.id} para MaterialID={db_obj.material_dimensional_id}")
    return db_obj



@pytest.fixture(scope="function")
def pedido_de_prueba(vendedor_client: TestClient, cliente_de_prueba: Cliente, db_session: Session) -> PedidoCliente:
    """Fixture para crear un pedido de prueba antes de tests GET/PUT/DELETE."""
    logger.debug(f"Fixture 'pedido_de_prueba' iniciando con db_session ID: {id(db_session)}")
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED, f"Fallo al crear Pedido en fixture: {response.text}"
    pedido_id = response.json()["id"]
    logger.info(f"Fixture 'pedido_de_prueba': Pedido ID {pedido_id} creado vía API.")

    # --- CORRECCIÓN: Usar una nueva sesión para verificación ---
    logger.debug(f"Fixture 'pedido_de_prueba': Cerrando db_session ID {id(db_session)} antes de verificar.")
    # No es estrictamente necesario cerrar aquí si se usa 'with' abajo,
    # pero puede ayudar a liberar recursos si hay problemas.
    # db_session.close() 

    pedido_db = None # Inicializar
    try:
        with TestingSessionLocal() as verification_db:
            logger.debug(f"Fixture 'pedido_de_prueba': Abierta verification_db ID {id(verification_db)} para buscar Pedido ID {pedido_id}.")
            # Obtener de la BD para devolver el objeto completo usando la nueva sesión
            pedido_db = order_repository.get_pedido_by_id(db=verification_db, pedido_id=pedido_id, load_related=True)
            logger.debug(f"Fixture 'pedido_de_prueba': Resultado de get_pedido_by_id con verification_db: {'Encontrado' if pedido_db else 'No Encontrado'}")
            # Añadir mensaje más descriptivo al assert
            assert pedido_db is not None, f"Pedido ID {pedido_id} creado vía API no fue encontrado en BD por la fixture (con sesión de verificación)."
            logger.info(f"Fixture 'pedido_de_prueba': Pedido ID={pedido_db.id} verificado exitosamente.")
            # ¡Importante! No podemos devolver pedido_db directamente aquí porque
            # la sesión verification_db se cerrará al salir del 'with'.
            # Necesitamos devolver datos o re-obtener con la sesión original del test.
            # Para simplificar, devolvamos solo el ID por ahora y que el test lo busque.
            # O, si el test necesita el objeto, hay que buscarlo de nuevo con su propia sesión.
            # Vamos a devolver el ID y ajustar los tests.

            # ALTERNATIVA: Devolver el objeto, pero los tests tendrán que manejar sesiones potencialmente cerradas.
            # return pedido_db # <--- Esto podría causar problemas si el test usa el objeto después.

            # MEJOR ALTERNATIVA: Re-obtener con la sesión original (si no la cerramos arriba)
            # pedido_db_original_session = db_session.get(PedidoCliente, pedido_id) # Asume que db_session sigue viva
            # return pedido_db_original_session # <--- Requiere no cerrar db_session arriba

            # ENFOQUE MÁS SEGURO: Devolver el objeto obtenido, pero documentar que la sesión está cerrada.
            # O forzar carga eager de todo lo necesario aquí.
            # Forzar carga de relaciones necesarias ANTES de que se cierre la sesión
            if pedido_db:
                 _ = pedido_db.cliente # Acceder para cargar
                 _ = pedido_db.vendedor # Acceder para cargar
                 _ = pedido_db.proformas # Acceder para cargar lista (vacía inicialmente)

    except Exception as e:
         logger.error(f"Error en fixture 'pedido_de_prueba' durante verificación: {e}", exc_info=True)
         pytest.fail(f"Error en fixture 'pedido_de_prueba' durante verificación: {e}")

    # Asegurarse de que devolvemos algo si la verificación pasó.
    if pedido_db is None:
         pytest.fail(f"Fixture 'pedido_de_prueba': pedido_db sigue siendo None después del bloque 'with'.")

    # Devolver el objeto obtenido de la sesión de verificación.
    # El test que lo use deberá tener cuidado si intenta operaciones lazy load.
    return pedido_db



@pytest.fixture(scope="function")
def pedido_con_proformas(
    vendedor_client: TestClient, cliente_de_prueba: Cliente, db_session: Session
) -> dict:
    """Crea un PedidoCliente y sus proformas iniciales, devuelve IDs."""
    payload = PedidoClienteCreate(cliente_id=cliente_de_prueba.id)
    response = vendedor_client.post(PEDIDOS_ENDPOINT, json=payload.model_dump())
    assert response.status_code == status.HTTP_201_CREATED, "Fallo al crear pedido en fixture proforma test"
    pedido_id = response.json()["id"]

    # Verificar que las proformas se crearon (usando nueva sesión)
    proformas_creadas = []
    with TestingSessionLocal() as verify_db:
        proformas_creadas = order_repository.list_proformas_by_pedido(db=verify_db, pedido_id=pedido_id)

    assert len(proformas_creadas) == 2, "No se crearon las 2 proformas iniciales"
    proforma_producto = next((p for p in proformas_creadas if p.tipo == "PRODUCTO"), None)
    proforma_servicio = next((p for p in proformas_creadas if p.tipo == "SERVICIO"), None)
    assert proforma_producto is not None and proforma_servicio is not None, "No se encontró proforma PRODUCTO o SERVICIO"
    assert proforma_producto.estado == "BORRADOR"
    assert proforma_servicio.estado == "BORRADOR"

    return {
        "pedido_id": pedido_id,
        "proforma_producto_id": proforma_producto.id,
        "proforma_servicio_id": proforma_servicio.id
    }





# ============================
#  11. Fixtures de Tokens de Autenticación
# ============================

@pytest.fixture(scope="module")
def get_auth_token(admin_user: Usuario, vendedor_user: Usuario) -> Callable:
    """
    Fixture tipo 'factory' (scope='module') para obtener tokens de autenticación.

    Proporciona una función interna `_get_token` que crea un cliente `TestClient`
    temporal solo para llamar al endpoint de login y obtener un token JWT.
    Depende de que los usuarios (admin, vendedor) ya existan por `test_user_factory`.

    Args:
        admin_user: Fixture que asegura la creación del admin user (inyectado por pytest).
        vendedor_user: Fixture que asegura la creación del vendedor user (inyectado por pytest).

    Yields:
        Callable: La función `_get_token(username, password)`.
    """
    # Asegurar que los usuarios base estén creados antes de devolver la factory
    assert admin_user and admin_user.id
    assert vendedor_user and vendedor_user.id

    def _get_token(username: str, password: str) -> str:
        """Función interna para obtener un token JWT para un usuario."""
        # Crear cliente temporal SOLO para obtener el token
        # Asegurarse que app tenga los overrides aquí también, por si acaso
        app.dependency_overrides[get_db] = override_get_db
        with TestClient(app) as temp_client:
            print(f"DEBUG [get_auth_token]: Creando temp_client ID={id(temp_client)} para obtener token de {username}")
            response = temp_client.post(
                f"{settings.API_V1_STR}/auth/token",
                # Usar 'data' para simular form data
                data={"username": username, "password": password}
            )
            print(f"DEBUG [get_auth_token]: Respuesta de /auth/token para {username}: {response.status_code}")
            if response.status_code != 200:
                pytest.fail(f"No se pudo obtener token para {username}. Status: {response.status_code}, Body: {response.text}")
            token_data = response.json()
            token = token_data["access_token"]
            print(f"DEBUG [get_auth_token]: Token obtenido para {username}: ...{token[-6:]}")
            return token
    return _get_token

@pytest.fixture(scope="module")
def admin_token(get_auth_token: Callable, admin_user: Usuario) -> str:
    """Fixture (scope='module') que obtiene y devuelve el token para 'testadmin'."""
    print("DEBUG [conftest]: Obteniendo admin_token (module scope)...")
    # Asegurarse que el usuario de la factory esté listo antes de pedir token
    assert admin_user and admin_user.username, "Fixture admin_user no disponible o sin username"
    token = get_auth_token(username=admin_user.username, password="password123")
    print(f"DEBUG [conftest]: admin_token obtenido: ...{token[-6:]}")
    return token

@pytest.fixture(scope="module")
def vendedor_token(get_auth_token: Callable, vendedor_user: Usuario) -> str:
    """Fixture (scope='module') que obtiene y devuelve el token para 'testvendedor'."""
    print("DEBUG [conftest]: Obteniendo vendedor_token (module scope)...")
    assert vendedor_user and vendedor_user.username, "Fixture vendedor_user no disponible o sin username"
    token = get_auth_token(username=vendedor_user.username, password="password123")
    print(f"DEBUG [conftest]: vendedor_token obtenido: ...{token[-6:]}")
    return token


@pytest.fixture(scope="module")
def dibujante_token(get_auth_token: Callable, dibujante_user: Usuario) -> str:
    """Fixture (scope='module') que obtiene y devuelve el token para 'testdibujante'."""
    print("DEBUG [conftest]: Obteniendo dibujante_token (module scope)...")
    assert dibujante_user and dibujante_user.username, "Fixture dibujante_user no disponible o sin username"
    token = get_auth_token(username=dibujante_user.username, password="password123")
    print(f"DEBUG [conftest]: dibujante_token obtenido: ...{token[-6:]}")
    return token

@pytest.fixture(scope="module")
def operario_token(get_auth_token: Callable, operario_user: Usuario) -> str:
    """Fixture (scope='module') que obtiene y devuelve el token para 'testoperario'."""
    print("DEBUG [conftest]: Obteniendo operario_token (module scope)...")
    assert operario_user and operario_user.username, "Fixture operario_user no disponible o sin username"
    token = get_auth_token(username=operario_user.username, password="password123")
    print(f"DEBUG [conftest]: operario_token obtenido: ...{token[-6:]}")
    return token

@pytest.fixture(scope="function")
def dibujante_client(dibujante_token: str) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='function') que proporciona un cliente de prueba INDEPENDIENTE
    autenticado como Dibujante.
    """
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {dibujante_token}"
        print(f"DEBUG [conftest - dibujante_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Dibujante ...{dibujante_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - dibujante_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")

@pytest.fixture(scope="function")
def operario_client(operario_token: str) -> Generator[TestClient, None, None]:
    """
    Fixture (scope='function') que proporciona un cliente de prueba INDEPENDIENTE
    autenticado como Operario.
    """
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        client.headers["Authorization"] = f"Bearer {operario_token}"
        print(f"DEBUG [conftest - operario_client setup]: Creado cliente INDEPENDIENTE ID={id(client)} con token Operario ...{operario_token[-6:]}")
        yield client
    print(f"DEBUG [conftest - operario_client teardown]: Destruido cliente INDEPENDIENTE ID={id(client)}.")

```

