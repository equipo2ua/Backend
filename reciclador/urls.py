from django.urls import path
from . import views 


reciclador_patterns = [

    path('crear_reciclador/<id>', views.crear_reciclador,name="crear_reciclador"),
    path('ver_reciclador/<id>', views.ver_reciclador,name="ver_reciclador"),
    path('editar_reciclador/<id>', views.editar_reciclador,name="editar_reciclador"),
    path('update_reciclador/<id>', views.update_reciclador,name="update_reciclador"),
    path('lista_reciclador/<id>', views.lista_reciclador,name="lista_reciclador"),
    path('add_reciclador/<id>', views.add_reciclador,name="add_reciclador"),
    path('activar/<id>', views.activar,name="activar"),
    path('bloquear/<id>', views.bloquear,name="bloquear"),
    path('borrar/<id>', views.borrar,name="borrar"),
    path('guardar_direccion/<id>', views.guardar_direccion,name="guardar_direccion"),
    path('borrar_direccion/<id>', views.borrar_direccion,name="borrar_direccion"),
    ]  