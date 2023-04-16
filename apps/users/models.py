# ORM DE DJANGO
from django.db import models
import uuid
import random
from django.utils.text import slugify

from django.utils.text import slugify


# MODELO
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

# SETTINGS OF PROJECT
from proyecto.settings import MEDIA_URL, STATIC_URL



# Create your models here.

class Rol(models.Model):
    rol = models.CharField(max_length=75, null=False, blank=False, unique=True)
    Descripcion = models.TextField()

    def __str__(self):
        return self.rol

class Puesto(models.Model):
    tipoPuesto = models.CharField(max_length=100,null=False,blank=False, unique=True)
    escala = models.SlugField(blank=False, null=False,unique=True)
    estado = models.BooleanField(default=True)


    def __str__(self):
        return self.tipoPuesto

class PaisOrigen(models.Model):
    pais = models.CharField(max_length=95, null=False, blank=False)

    def __str__(self):
        return self.pais

class TipoDocumento(models.Model):
    tipoDocumento = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return self.tipoDocumento

class Perfil(models.Model):
    tipo_usuario = [
        ('Usuario','Usuario'),
        ('Docente','Docente'),
        ('Estudiante', 'Estudiante')
    ]
    certificado_nacimiento = [
        ('Libro','Libro'),
        ('Acta','Acta'),
        ('Folio','Folio')
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(choices=tipo_usuario,default='Usuario',null=True,blank=True,max_length=100)
    profesion = models.CharField(max_length=75, null=True, blank=True)
    acronimo = models.CharField(max_length=75, null=True, blank=True)
    tipoDocumento = models.ForeignKey(TipoDocumento, blank=True, null=True, on_delete=models.CASCADE)
    noDocumentoIdentificacion = models.CharField(max_length=20, null=True, blank=True)
    noPersonal = models.SlugField(null=False, blank=False, unique=True)
    certificado_nacimiento = models.CharField(choices=certificado_nacimiento, null=True, blank=True, max_length=100)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    pais_origen = models.ForeignKey(PaisOrigen, blank=False, null=False, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)    
    imagen = models.ImageField(upload_to='users/', null=True, blank=True)
    rol = models.ManyToManyField(Rol, blank=True)
    puesto = models.ManyToManyField(Puesto, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.usuario.first_name, self.usuario.last_name)   
   
    def get_image(self):
        if  self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/usuario.png')

"""
def set_escala(sender, instance, *args, **kwargs):
    if not instance.escala:
        esc = str(uuid.uuid4())[:6]

        while Puesto.objects.filter(escala=esc).exists():
            esc = esc

    instance.escala = esc

def set_noPersonal(sender, instance, *args, **kwargs):

    if not instance.noPersonal:
        personal = slugify(random.randint(1,19999999))

        while Perfil.objects.filter(noPersonal=personal).exists():
            personal = slugify('{}'.format(str(uuid.uuid4())[:8]))

    instance.noPersonal = personal

pre_save.connect(set_noPersonal,sender=Perfil)
""" 
#pre_save.connect(set_escala,sender=Puesto)