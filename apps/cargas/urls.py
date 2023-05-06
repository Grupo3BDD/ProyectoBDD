from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cargas'

urlpatterns = [
    path('', login_required(views.CargaListView.as_view()), name='carga'),
    path('add', login_required(views.CargaCreateView.as_view()), name='carga_add'),
    path('editar/<int:pk>/', login_required(views.CargaUpdateView.as_view()), name='carga_update'),
    path('delete/<int:pk>/', login_required(views.CargaDeleteView.as_view()), name='carga_delete'),
    path('detail/<int:pk>/', login_required(views.detailCarga), name='carga_detail'),
   
]