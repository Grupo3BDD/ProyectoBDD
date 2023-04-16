# ORM DE DJANGO
from django.db import models

# MODELO
from django.contrib.auth.models import AbstractUser

# SETTINGS OF PROJECT
from proyecto.settings import MEDIA_URL, STATIC_URL

# Create your models here.
class User(AbstractUser):
    imagen = models.ImageField(upload_to='users/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} / {}'.format(self.first_name, self.last_name, self.username)
    
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/usuario.png')