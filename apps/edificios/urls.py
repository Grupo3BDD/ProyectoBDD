from django.urls import path

# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required

app_name = 'edificios'

urlpatterns = [
    #Edificios
    path('', login_required(views.EdificioList.as_view()), name='Edificio'),
    path('crear/', login_required(views.EdificioCreate.as_view()), name='Crear'),
    path('actualizar/<int:pk>/', login_required(views.EdificioUpdate.as_view()), name='Actualizar'),
    path('eliminar/<int:pk>/', login_required(views.EdificioDelete.as_view()), name='Eliminar'),
    path('detalle/<int:pk>/', login_required(views.EdificioDetalle.as_view()), name='Detalle'),
    path('buscar/', login_required(views.EdificioSearch.as_view()), name='Buscar'),

    #Salones
    path('salon/', login_required(views.SalonList.as_view()), name='Salon'),
    path('salon/crear/', login_required(views.SalonCreate.as_view()), name='CrearSalon'),
    path('salon/actualizar/<int:pk>/', login_required(views.SalonUpdate.as_view()), name='ActualizarSalon'),
    path('salon/eliminar/<int:pk>/', login_required(views.SalonDelete.as_view()), name='EliminarSalon'),
    path('salon/detalle/<int:pk>/', login_required(views.SalonDetalle.as_view()), name='DetalleSalon'),
    path('salon/buscar/', login_required(views.SalonSearch.as_view()), name='BuscarSalon'),

    #Clasificaciones
    path('clasificacion/', login_required(views.ClasificacionList.as_view()), name='Clasificacion'),
    path('clasificacion/crear/', login_required(views.ClasificacionCreate.as_view()), name='CrearClasificacion'),
    path('clasificacion/actualizar/<int:pk>/', login_required(views.ClasificacionUpdate.as_view()), name='ActualizarClasificacion'),
    path('clasificacion/eliminar/<int:pk>/', login_required(views.ClasificacionDelete.as_view()), name='EliminarClasificacion'),
    path('clasificacion/detalle/<int:pk>/', login_required(views.ClasificacionDetalle.as_view()), name='DetalleClasificacion'),
    path('clasificacion/buscar/', login_required(views.ClasificacionSearch.as_view()), name='BuscarClasificacion'),

]