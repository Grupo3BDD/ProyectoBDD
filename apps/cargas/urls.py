from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cargas'

urlpatterns = [
    path('', views.CargaListView.as_view(), name='carga'),
    path('add', views.CargaCreateView.as_view(), name='carga_add'),
    path('editar/<int:pk>/', views.CargaUpdateView.as_view(), name='carga_update'),
    path('delete/<int:pk>/', views.CargaDeleteView.as_view(), name='carga_delete'),
   
]