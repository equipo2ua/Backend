from django.contrib import admin
from .models import Reciclador, Reciclador_Direccion, Direccion, Comuna, Historial_Reciclador
# Register your models here.

admin.site.register(Reciclador)
admin.site.register(Reciclador_Direccion)
admin.site.register(Direccion)
admin.site.register(Comuna)
admin.site.register(Historial_Reciclador)