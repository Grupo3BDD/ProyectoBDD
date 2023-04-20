
from django.db import models


# Create your models here.
class Edificio(models.Model):
    nombreEdificio = models.CharField(max_length=60, null=False, blank=False)
    cantidadSalones = models.IntegerField(null=True,blank=True)
    niveles = models.IntegerField(null=True,blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreEdificio


class Clasificacion(models.Model):
    tipo_salon_uso = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_salon_uso

class Salon(models.Model):
    edificio = models.ForeignKey(Edificio, null=False, blank=False, on_delete=models.CASCADE)
    clasificacion = models.ForeignKey(Clasificacion, null=False,blank=False, on_delete=models.CASCADE)
    nombreSalon = models.CharField(max_length=60, null=False, blank=False)
    capacidadEstudiantes = models.IntegerField(null=True,blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '{}{}'.format(self.edificio.nombreEdificio,self.nombreSalon)

