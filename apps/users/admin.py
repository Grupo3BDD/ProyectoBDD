from django.contrib import admin
# Modelos
from .models import User, Rol, Puesto, PaisOrigen, TipoDocumento, EncargadoArea,CoordinadorAcademico,Estudiante,Docente,Permiso
from django.contrib.auth.models import Permission

# Register your models here.
class UserAdmin(admin.ModelAdmin):    
    fields=('first_name','last_name','email','is_superuser',
            'password','username',
            'tipo_usuario','profesion','acronimo',
            'tipoDocumento','noDocumentoIdentificacion',
            'certificado_nacimiento','telefono','pais_origen',
            'estado','imagen','rol','puesto'
            )
    list_display=('__str__','fecha_creacion', 'noPersonal')

class PuestoAdmin(admin.ModelAdmin):
    fields=('tipoPuesto','estado')
    list_display=('__str__','fecha_creacion')

admin.site.register(User,UserAdmin)
admin.site.register(Rol)
admin.site.register(Puesto,PuestoAdmin)
admin.site.register(PaisOrigen)
admin.site.register(TipoDocumento)
admin.site.register(Permission)
admin.site.register(EncargadoArea)
admin.site.register(Estudiante)
admin.site.register(CoordinadorAcademico)
admin.site.register(Docente)
admin.site.register(Permiso)