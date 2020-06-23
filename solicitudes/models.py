from django.db import models
from reciclador.models import Reciclador
from recolector.models import Recolector
# Create your models here.

class Reporte(models.Model):
   
    nombre_reporte = models.CharField(max_length = 50, null = False, blank = False)
    tipo_reporte = models.CharField(max_length = 50, null = False, blank = False)
    descripcion = models.TextField(max_length = 300, null = False, blank = False)
    codigo = models.IntegerField()
    fecha_reporte = models.DateField(auto_now=False, auto_now_add=False)
    motivo_reporte = models.CharField(max_length = 50, null = False, blank = False)

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

    def __str__(self):
        return self.nombre_reporte

class Solicitud(models.Model):
    id_recolector = models.ForeignKey(Recolector, null = True, blank = True, on_delete=models.CASCADE)
    id_reciclador = models.ForeignKey(Reciclador, null = True, blank = True, on_delete=models.CASCADE)
    id_reporte = models.OneToOneField(Reporte, null = True, blank = True, on_delete=models.CASCADE)
    hora_reciclaje = models.TimeField(auto_now=False, auto_now_add=False)
    fecha_reciclaje = models.DateField(auto_now=False, auto_now_add=False)
    peso_total_materiales = models.IntegerField(null = True, blank = True)
    volumen_total_materiales = models.IntegerField(null = True, blank = True)
    notificaciones_rechazadas = models.CharField(max_length = 12, null = False, blank = False)
    estado = models.IntegerField(null = True, blank = True)

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solitudes"
        

    def __str__(self):
        return self.id


class Material(models.Model):

    nombre_material = models.CharField(max_length = 50, null = False, blank = False)
    cantidad_material = models.IntegerField(null = False, blank = False)
    

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

    def __str__(self):
        return self.nombre_material


class Tipo_Material(models.Model):
    id_material = models.ForeignKey(Material, null = True, blank = True, on_delete=models.CASCADE)
    id_solicitud = models.ForeignKey(Solicitud, null = True, blank = True, on_delete=models.CASCADE)
    nombre_tipo = models.CharField(max_length = 12, null = False, blank = False)
    

    class Meta:
        verbose_name = "Tipo_material"
        verbose_name_plural = "Tipo_materiales"

    def __str__(self):
        return self.nombre_tipo

