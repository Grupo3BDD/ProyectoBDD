from django.db import models

# Tiempo
from datetime import datetime



class CicloAcademico(models.Model):
    nombreCiclo = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.nombreCiclo

class GradoAcademico(models.Model):
    nombreGrado = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.nombreGrado

class Plan(models.Model):
    nombrePlan = models.CharField(max_length=60, null=False, blank=False)
    matutina = models.BooleanField(default=False)
    verpertina = models.BooleanField(default=False)
    nocturna = models.BooleanField(default=False)
    sabados = models.BooleanField(default=False)
    domingos = models.BooleanField(default=False)

    def __str__(self):
        return self.nombrePlan

class Profesor(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)
    apellido = models.CharField(max_length=60, null=False, blank=False)
    registro_personal = models.IntegerField(null=True,blank=True)
    dpi = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    idCarrera = models.CharField(max_length=10, null=False, blank=False)
    nombreCarrera = models.CharField(max_length=60, null=False, blank=False)
    duracionPeriodos = models.IntegerField(null=True,blank=True)
    clasificacion = models.CharField(max_length=20, null=True, blank=False)
    partida = models.CharField(max_length=20, null=True, blank=False)
    tipo_ciclo = models.ForeignKey(CicloAcademico, null=False, blank=False, on_delete=models.CASCADE)
    encargado_area = models.ForeignKey(Profesor, null=False, blank=False, on_delete=models.CASCADE)
    #coordinador_acad = models.ForeignKey(Profesor, null=False, blank=False, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreCarrera

    def get_created_at(self):
        return self.fecha_creacion.strftime('%d-%m-%Y')

class Curso(models.Model):
    idCurso = models.CharField(max_length=10, null=False, blank=False)
    nombreCurso = models.CharField(max_length=60, null=False, blank=False)
    horasSemana = models.IntegerField(null=True,blank=True)
    #carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    laboratorio = models.BooleanField(default=False)
    codigo_lab = models.CharField(max_length=10, null=True, blank=True)
    horas_lab_sem = models.IntegerField(null=True,blank=True)
    valido_semestres = models.IntegerField(null=True,blank=True)
    habilitado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreCurso

class Pensum(models.Model):
    idPensum = models.CharField(max_length=10, null=False, blank=False)
    inicio_vigencia = models.IntegerField(null=True, blank=True)
    desc_proceso = models.TextField(null=True)
    cant_ciclos = models.IntegerField(null=True, blank=True)
    valor_ef = models.IntegerField(null=True, blank=True)
    habilitado = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.idPensum

    def get_created_at(self):
        return self.fecha_creacion.strftime('%d-%m-%Y')

