import datetime
from django.db import models

from apps.pensum.models import Pensum, Curso
from apps.users.models import User

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
years = date.strftime("%Y")

class Carga(models.Model):
    year = models.IntegerField(default=years)
    ciclo_acad = models.CharField(max_length=255)
    
    estados = (
        ('Solicitado', 'Solicitado'),
        ('En proceso', 'En proceso'),
        ('Aprobado', 'Aprobado'),
        ('No aprobado', 'No aprobado')
    )
    estado = models.CharField(max_length=255, choices=estados, default='En proceso')
    fecha_envio = models.DateField() 
    fecha_aprob = models.DateField()

    def get_created_at(self):
        return self.fecha_envio.strftime('%d-%m-%Y')
    

class ModCarga(models.Model):
    pensum = models.ForeignKey(Pensum, null=False, blank=False, on_delete=models.CASCADE)
    codigo = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE, related_name='mod_cargas')
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    num_personal = models.IntegerField(null=True)
    docente = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    