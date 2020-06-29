from django.urls import path
from . import views 


recolector_patterns = [

    path('crear_recolector/<id>', views.crear_recolector,name="crear_recolector"),
    path('editar_recolector/<id>', views.editar_recolector,name="editar_recolector"),
    path('update_recolector/<id>', views.update_recolector,name="update_recolector"),
    path('lista_recolector/<id>', views.lista_recolector,name="lista_recolector"),
    path('add_recolector/<id>', views.add_recolector,name="add_recolector"),
    path('activar/<id>', views.activar,name="activar"),
    path('bloquear/<id>', views.bloquear,name="bloquear"),
    path('borrar/<id>', views.borrar,name="borrar"),
    ]  