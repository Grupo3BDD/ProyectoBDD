from django.contrib import admin
from .models import GradoAcademico,Jornada,TipoJornada,Carrera,Curso,Laboratorio,DetalleCurso,DetalleCarrera,DetallePensumCurso,Pensum,Prerequisito
# Register your models here.

admin.site.register(GradoAcademico)
admin.site.register(Jornada)
admin.site.register(TipoJornada)
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Laboratorio)
admin.site.register(DetalleCurso)
admin.site.register(DetalleCarrera)
admin.site.register(DetallePensumCurso)
admin.site.register(Pensum)
admin.site.register(Prerequisito)