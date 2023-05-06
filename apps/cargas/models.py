import datetime
from django.db import models


# Modelos
from apps.pensum.models import Pensum,Carrera,Curso
from apps.users.models import Docente

# Obtener el año actual


currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
years = date.strftime("%Y")

class Carga(models.Model):
    year = models.IntegerField(default=years)
    # Choice
    tipo_ciclo = [
        ('Primer Ciclo', 'Primer Ciclo'),
        ('Segundo Ciclo', 'Segundo Ciclo'),
        ('Tercer Ciclo', 'Tercer Ciclo'),
        ('Cuarto Ciclo', 'Cuarto Ciclo'),
        ('Quinto Ciclo','Quinto Ciclo'),
        ('Sexto Ciclo','Sexto Ciclo'),
        ('Septimo Ciclo','Septimo Ciclo'),
        ('Octavo Ciclo','Octavo Ciclo'),
        ('Noveno Ciclo','Noveno Ciclo'),
        ('Decimo Ciclo','Decimo Ciclo'),
    ]
    ciclo_acad = models.CharField(choices=tipo_ciclo,max_length=100)
    carreraId = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    
    estados = (
        ('Solicitado', 'Solicitado'),
        ('En proceso', 'En proceso'),
        ('Aprobado', 'Aprobado'),
        ('No aprobado', 'No aprobado')
    )
    estado = models.CharField(max_length=255, choices=estados, default='En proceso')
    fecha_envio = models.DateField(auto_now_add=True) 
    fecha_aprob = models.DateField(null=True,blank=True)


    def __str__(self):
        return '{} {}'.format(self.year,self.carreraId)
    
class CargaAcademicaDetalle(models.Model):
    cargaId = models.ForeignKey(Carga, blank=False, null=False, on_delete=models.CASCADE)
    docenteId = models.ForeignKey(Docente,blank=False, null=False, on_delete=models.CASCADE)
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)
    cursoid = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    

    def __str__(self):
        return '{} {} {} {}'.format(self.cargaId, self.pensum,self.cursoid.nombreCurso,self.docenteId)


    

