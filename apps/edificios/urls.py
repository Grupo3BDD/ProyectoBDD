from django.urls import path

# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required

app_name = 'edificios'

urlpatterns = [

    path('', login_required(views.EdificioList.as_view()), name='Edificio'),
    path('crear/', login_required(views.EdificioCreate.as_view()), name='Crear'),
    #path('category/add/', login_required(views.CategoryCreate.as_view()), name='category_add'),
    path('actualizar/<int:pk>/', login_required(views.EdificioUpdate.as_view()), name='Actualizar'),
    path('eliminar/<int:pk>/', login_required(views.EdificioDelete.as_view()), name='Eliminar'),
    path('detalle/<int:pk>/', login_required(views.EdificioDetalle.as_view()), name='Detalle'),
    path('buscar/', login_required(views.EdificioSearch.as_view()), name='Buscar'),

]