from django.db import models

# Create your models here.

class Reciclador(models.Model):
    nombre_reciclador = models.CharField(max_length = 50, null = False, blank = False)
    apellido_reciclador = models.CharField(max_length = 50, null = False, blank = False)
    telefono_reciclador = models.CharField(max_length = 12, null = False, blank = False)
    correo_reciclador = models.EmailField(max_length = 12, null = False, blank = False)
    notificaciones_rechazadas = models.CharField(max_length = 12, null = False, blank = False)
    calificacion_recolector = models.FloatField()
    estado = models.IntegerField()
    cantidad_calificaciones = models.FloatField()
    suma_calificaciones = models.FloatField()

    class Meta:
        verbose_name = "Reciclador"
        verbose_name_plural = "Recicladores"
        ordering = ['nombre_reciclador']

    def __str__(self):
        return self.nombre_reciclador

class Historial_Reciclador(models.Model):
    id_reciclador = models.ForeignKey(Reciclador, null = True, blank = True, on_delete=models.CASCADE)
    fecha_finalizado = models.CharField(max_length = 50, null = False, blank = False)

    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"

    def __str__(self):
        return self.fecha_finalizado


class Comuna(models.Model):

    nombre_comuna = models.CharField(max_length=50, null = False, blank = False)

    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"
        ordering = ['nombre_comuna']

    def __str__(self):
        return self.nombre_comuna


class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, null = True, blank = True, on_delete=models.CASCADE)
    calle_direccion = models.CharField(max_length=50, null = False, blank = False)
  
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
        ordering = ['calle_direccion']

    def __str__(self):
        return self.calle_direccion


class Reciclador_Direccion(models.Model):

    id_reciclador = models.ForeignKey(Reciclador, null = True, blank = True, on_delete=models.CASCADE)
    id_direccion =models.ForeignKey(Direccion, null = True, blank = True, on_delete=models.CASCADE)

    



    