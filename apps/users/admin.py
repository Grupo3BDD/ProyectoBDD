from django.contrib import admin
# Modelos
from .models import Perfil, Rol, Puesto, PaisOrigen, TipoDocumento
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Rol)
admin.site.register(Puesto)
admin.site.register(PaisOrigen)
admin.site.register(TipoDocumento)
admin.site.register(Permission)