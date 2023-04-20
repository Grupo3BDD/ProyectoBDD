from django.contrib import admin
from .models import Edificio, Clasificacion, Salon


# Register your models here.
class SalonAdmin(admin.ModelAdmin):
    fields = ('edificio','clasificacion','nombreSalon','capacidadEstudiantes','estado')
    list_display = ('__str__',  'fecha_creacion')

admin.site.register(Salon,SalonAdmin)
admin.site.register(Edificio)
admin.site.register(Clasificacion)