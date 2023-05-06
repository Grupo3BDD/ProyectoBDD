from django.db import models
import datetime

# Tiempo


from apps.users.models import User,EncargadoArea,CoordinadorAcademico



class GradoAcademico(models.Model):
    grado_academico = models.CharField(max_length=75,null=False,blank=False)

    def __str__(self):
        return self.grado_academico
    
class Jornada(models.Model):
    plan = models.CharField(max_length=75,null=False,blank=False)

    def __str__(self):
        return self.plan

class TipoJornada(models.Model):
    plan_t= models.ForeignKey(Jornada, null=False,blank=False, on_delete=models.CASCADE)
    clasificacion_jorn=models.CharField(max_length=75,null=False,blank=False)

    def __str__(self):
        return self.clasificacion_jorn



class Carrera(models.Model):
    tipo_ciclo = [
        ('Trimestral', 'Trimestral'),
        ('Anual', 'Anual'),
        ('Bimestral', 'Bimestral'),
        ('Cuatrimestre','Cuatrimestre'),
        ('Semestral','Semestral')
    ]
    nombreCarrera = models.CharField(max_length=60, null=False, blank=False, unique=True)
    duracionPeriodos = models.IntegerField(null=True,blank=True)
    clasificacion = models.CharField(max_length=20, null=True, blank=False)
    partida = models.CharField(max_length=20, null=True, blank=False)
    tipo_ciclo = models.CharField(choices=tipo_ciclo,default='Semestral',max_length=100)
    encargado_area = models.ForeignKey(EncargadoArea, on_delete=models.CASCADE)
    coordinador_acad = models.ForeignKey(CoordinadorAcademico, on_delete=models.CASCADE)
    

    habilitado = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreCarrera

    def get_created_at(self):
        return self.fecha_creacion.strftime('%d-%m-%Y')

   
class DetalleCarrera(models.Model):
    carreraId= models.ForeignKey(Carrera, null=False,blank=False,on_delete=models.CASCADE)
    grado_acad = models.ForeignKey(GradoAcademico,null=True,blank=True, on_delete=models.CASCADE)
    type_jornada = models.ForeignKey(TipoJornada,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.carreraId



class Curso(models.Model):
    codigoCurso = models.CharField(max_length=60, null=False, blank=False,unique=True)    
    nombreCurso = models.CharField(max_length=80, null=False, blank=False, unique=True)
    horasSemana = models.IntegerField(null=True,blank=True)
    creditos = models.IntegerField(null=True,blank=True)
    creditosObligatorios = models.IntegerField(null=True,blank=True)
    with_laboratorio = models.BooleanField(default=False)    
    obligatorio = models.BooleanField(default=True)
    areaTecnica = models.BooleanField(default=True)
    habilitado = models.BooleanField(default=True)
    

    def __str__(self):
        return self.nombreCurso



class DetalleCurso(models.Model):
    cursoId = models.ForeignKey(Curso, null=False,blank=False,on_delete=models.CASCADE)
    facultad_carrera = models.ForeignKey(Carrera, null=False,blank=False,on_delete=models.CASCADE)
    

    def __str__(self):
        return '{}'.format(self.cursoId)
    
class Prerequisito(models.Model):
    detalleId = models.ForeignKey(DetalleCurso,null=False,blank=False,on_delete=models.CASCADE)
    prerrequisito= models.ForeignKey(Curso, null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.prerrequisito)

    
class Laboratorio(models.Model):
    codigoLaboratorio = models.CharField(max_length=60, null=False, blank=False,unique=True)
    codeCurso = models.ForeignKey(Curso, null=False,blank=False,on_delete=models.CASCADE)
    horas_lab_sem = models.IntegerField(null=True,blank=True)
    valido_semestres = models.IntegerField(null=True,blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.codeCurso,self.codigoLaboratorio)


currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
years = date.strftime("%Y")

class Pensum(models.Model):
    codigo_pensum = models.CharField(max_length=60, null=False, blank=False,unique=True)
    # Agregar a que carrera va este pensum
    carreraId = models.ForeignKey(Carrera, null=False,blank=False,on_delete=models.CASCADE)
    year_inicio_vigencia = models.IntegerField(default=years)
    descripcion = models.CharField(max_length=200)
    cantidad_ciclo = models.IntegerField()
    examen_final = models.DecimalField(max_digits=8,decimal_places=2,default=0.0)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} '.format(self.codigo_pensum)

    def get_created_at(self):
        return self.fecha_creacion.strftime('%d-%m-%Y')

class DetallePensumCurso(models.Model):
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
    tipociclo = models.CharField(max_length=100,null=False,blank=False,choices=tipo_ciclo)

    codigo_pensum = models.ForeignKey(Pensum,on_delete=models.CASCADE)
    cursoid = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{} {} {}'.format(self.cursoid.codigoCurso, self.cursoid.nombreCurso,self.codigo_pensum)



