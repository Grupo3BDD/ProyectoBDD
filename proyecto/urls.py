# URL PARA ACCEDER AL ADMIN DE DJANGO
from django.contrib import admin

# AGREGAR URLS
from django.urls import path, include

# VISTAS
from . import views

# CONFIGURANCION PARA MANEJAR LOS STATICS Y MEDIA
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.index, name='index'),
    path('', include('apps.users.urls')),
    path('edificio/',include('apps.edificios.urls')),
    path('admin/', admin.site.urls),
    path('carga/', include('apps.cargas.urls')),
    path('pensum/',include('apps.pensum.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
