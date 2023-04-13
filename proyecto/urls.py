# URL PARA ACCEDER AL ADMIN DE DJANGO
from django.contrib import admin

# AGREGAR URLS
from django.urls import path, include

# VISTAS
from . import views

# CONFIGURANCION PARA MANEJAR LOS STATICS Y MEDIA
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('',include('apps.users.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
