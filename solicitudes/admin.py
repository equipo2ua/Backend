from django.contrib import admin
from .models import Solicitud, Reporte, Material, Tipo_Material
# Register your models here.

admin.site.register(Solicitud)
admin.site.register(Reporte)
admin.site.register(Material)
admin.site.register(Tipo_Material)
