from django.urls import path
from . import views 

solicitud_patterns = [

    path('crear_solicitud/<id>', views.crear_solicitud,name="crear_solicitud"),
    
    ]  