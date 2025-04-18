# app/initial_data.py

"""
Define los datos iniciales para roles, permisos y sus mapeos.
Se usa tanto para la migración de seeding como para las fixtures de prueba.
"""

# 1. Roles Iniciales
initial_roles = [
    {'nombre': 'Administrador', 'descripcion': 'Acceso total al sistema.'},
    {'nombre': 'Vendedor', 'descripcion': 'Gestión de ventas y clientes.'},
    {'nombre': 'Supervisor', 'descripcion': 'Supervisión de producción y operarios.'},
    {'nombre': 'Dibujante', 'descripcion': 'Cotización y preparación de trabajos CNC.'},
    {'nombre': 'Operario', 'descripcion': 'Ejecución de tareas de producción.'},
]

# 2. Permisos Iniciales (Lista refinada completa)
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
role_permission_mapping = {
    'Administrador': [
        'gestionar:usuario', 'gestionar:rol', 'gestionar:permiso', 'leer:usuario', 'crear:usuario',
        'actualizar:usuario', 'eliminar:usuario', 'leer:rol', 'crear:rol', 'actualizar:rol',
        'eliminar:rol', 'leer:permiso', 'asignar:rol_usuario', 'remover:rol_usuario',
        'asignar:permiso_rol', 'remover:permiso_rol', 'anular:venta_factura', 'ver:panel_admin',
        'leer:cliente', 'crear:cliente', 'actualizar:cliente', 'eliminar:cliente',
        'leer:proforma', 'crear:proforma', 'actualizar:proforma_global', 'cancelar:proforma',
        'enviar:proforma', 'posponer:proforma', 'adjuntar:archivo_proforma',
        'leer:pedido_cliente', 'leer:orden_produccion', 'gestionar:orden_produccion',
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
        'registrar:mi_indisponibilidad'
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