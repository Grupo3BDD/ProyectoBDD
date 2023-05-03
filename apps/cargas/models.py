from django.db import models

class Carga(models.Model):
    year = models.DecimalField(max_length=5)
    ciclo_acad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    fecha_envio = models.DateField()
    fecha_aprob = models.DateField()