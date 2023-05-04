from django.urls import path

# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required

app_name = 'pensums'

urlpatterns = [
    #Cursos
    path('curso/', login_required(views.CursoList.as_view()), name='Curso'),
    path('curso/crear/', login_required(views.CursoCreate.as_view()), name='CrearCurso'),
    path('curso/actualizar/<int:pk>/', login_required(views.CursoUpdate.as_view()), name='ActualizarCurso'),
    path('curso/eliminar/<int:pk>/', login_required(views.CursoDelete.as_view()), name='EliminarCurso'),
    path('curso/detalle/<int:pk>/', login_required(views.CursoDetalle.as_view()), name='DetalleCurso'),
    path('curso/buscar/', login_required(views.CursoSearch.as_view()), name='BuscarCurso'),

]