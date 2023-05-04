from django.db import models

# Tiempo
from datetime import datetime

from apps.users.models import User


class Ciclo(models.Model):
    nombreCiclo = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.nombreCiclo


class Carrera(models.Model):


    idCarrera = models.CharField(max_length=10, null=False, blank=False, unique=True)
    nombreCarrera = models.CharField(max_length=60, null=False, blank=False, unique=True)
    duracionPeriodos = models.IntegerField(null=True,blank=True)
    clasificacion = models.CharField(max_length=20, null=True, blank=False)
    partida = models.CharField(max_length=20, null=True, blank=False)
    tipo_ciclo = models.ForeignKey(Ciclo, null=True, blank=True, on_delete=models.CASCADE)
    #encargado_area = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    #coordinador_acad = models.ForeignKey(Profesor, null=False, blank=False, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreCarrera

    def get_created_at(self):
        return self.fecha_creacion.strftime('%d-%m-%Y')



class Curso(models.Model):
    idCurso = models.CharField(max_length=10, null=False, blank=False, unique=True)
    nombreCurso = models.CharField(max_length=60, null=False, blank=False, unique=True)
    horasSemana = models.IntegerField(null=True,blank=True)
    carrera = models.ManyToManyField(Carrera, null=True, blank=True)
    laboratorio = models.BooleanField(default=False)
    codigo_lab = models.CharField(max_length=10, null=True, blank=True)
    horas_lab_sem = models.IntegerField(null=True,blank=True)
    valido_semestres = models.IntegerField(null=True,blank=True)
    habilitado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreCurso

