from django.urls import path
from . import views 


recolector_patterns = [

    path('crear_recolector/<id>', views.crear_recolector,name="crear_recolector"),
    path('editar_recolector/<id>', views.editar_recolector,name="editar_recolector"),
    path('update_recolector/<id>', views.update_recolector,name="update_recolector"),
    path('lista_recolector/<id>', views.lista_recolector,name="lista_recolector"),
    path('add_recolector/<id>', views.add_recolector,name="add_recolector"),
    path('activar_r/<id>', views.activar_r,name="activar_r"),
    path('bloquear_r/<id>', views.bloquear_r,name="bloquear_r"),
    path('borrar_r/<id>', views.borrar_r,name="borrar_r"),
    
    ]  