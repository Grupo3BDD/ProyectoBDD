# ORM DE DJANGO
from django.db import models
import uuid
import random
import datetime


# MODELO

from django.db.models.signals import pre_save, post_save
from django.db import transaction
from django.contrib.auth.models import AbstractUser

# SETTINGS OF PROJECT
from proyecto.settings import MEDIA_URL, STATIC_URL
from django.shortcuts import  get_object_or_404

# Create your models here.

# Por hacer el apartado de permisos

class Rol(models.Model):
    rol = models.CharField(max_length=75, null=False, blank=False, unique=True)
    Descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rol


class Puesto(models.Model):
    tipoPuesto = models.CharField(
        max_length=100, null=False, blank=False, unique=True)
    escala = models.CharField(
        max_length=8, blank=False, null=False, unique=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tipoPuesto


class PaisOrigen(models.Model):
    pais = models.CharField(max_length=95, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pais


class TipoDocumento(models.Model):
    tipoDocumento = models.CharField(max_length=80, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tipoDocumento


class User(AbstractUser):
    tipo_usuario = [
        ('Usuario', 'Usuario'),
        ('Docente', 'Docente'),
        ('Estudiante', 'Estudiante')
    ]
    certificado_nacimiento = [
        ('Libro', 'Libro'),
        ('Acta', 'Acta'),
        ('Folio', 'Folio')
    ]
    
    tipo_usuario = models.CharField(
        choices=tipo_usuario, default='Usuario', null=True, blank=True, max_length=100)
    profesion = models.CharField(max_length=75, null=True, blank=True)
    acronimo = models.CharField(max_length=75, null=True, blank=True)
    tipoDocumento = models.ForeignKey(
        TipoDocumento, blank=True, null=True, on_delete=models.CASCADE)
    noDocumentoIdentificacion = models.CharField(
        max_length=20, null=True, blank=True)
    noPersonal = models.CharField(
        max_length=9, null=False, blank=False, unique=True)
    certificado_nacimiento = models.CharField(
        choices=certificado_nacimiento, null=True, blank=True, max_length=100)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    pais_origen = models.ForeignKey(
        PaisOrigen, blank=True, null=True, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='users/', null=True, blank=True)
    rol = models.ManyToManyField(Rol, blank=True)
    puesto = models.ManyToManyField(Puesto, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if(self.first_name==''):
            return '{}'.format(self.username)
        return '{} {}'.format(self.first_name, self.last_name)

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/usuario.png')
    
    def get_username(self):
        return '{}'.format(self.username)

class EncargadoArea(models.Model):
    user = models.ForeignKey(User, blank=False,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class CoordinadorAcademico(models.Model):
    user = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class Estudiante(models.Model):
    user = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Docente(models.Model):
    user = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username




def set_escala(sender, instance, *args, **kwargs):
    # Asigna una Escala automaitca para la entidad Puesto
    esc = esc = str(uuid.uuid4())[:8]
    if not instance.escala:
        for es in Puesto.objects.all():
            if (es.escala != esc):
                esc = str(uuid.uuid4())[:8]

        instance.escala = esc

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")

def set_noPersonal(sender, instance, *args, **kwargs):
    # Asigna un NoPersonal automatico para la entidad Perfil    
    codigo = '{}{}'.format(year, str(uuid.uuid4())[:5])

    if not instance.noPersonal:

        for per in User.objects.all():
            if (per.noPersonal != codigo):
                print('Generando codigo nuevo')
                codigo = '{}{}'.format(year, str(uuid.uuid4())[:5])

        instance.noPersonal = codigo

def set_tipoUser(sender,instance,*args,**kwargs):
    try:
        with transaction.atomic():
            
            userId = instance.id
            idUser = get_object_or_404(User, id=userId)

            if(instance.tipo_usuario == 'Docente'):
                docente=Docente(user=idUser)
                docente.save()
                
            elif(instance.tipo_usuario=='Estudiante'):
                estudiante = Estudiante(user=idUser)
                estudiante.save()
            else:
                # Definido como usurio
                print("Es definido como usuario...")

    except Exception as e:
        print(str(e))



pre_save.connect(set_noPersonal, sender=User)

pre_save.connect(set_escala, sender=Puesto)

post_save.connect(set_tipoUser,sender=User)
