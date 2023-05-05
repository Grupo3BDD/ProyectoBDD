from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cargas'

urlpatterns = [
    path('listacarga/', views.CargaListView.as_view(), name='carga-list'),
    path('crearcarga/', views.CargaCreateView.as_view(), name='carga-create'),
    path('editarcarga/<int:pk>/', views.CargaUpdateView.as_view(), name='carga-update'),
    path('borrarcarga/<int:pk>/', views.CargaDeleteView.as_view(), name='carga-delete'),

#-----------------------Para modificar carga

    path('modificar/<int:pk>/', views.ModCargaListView.as_view(), name='modificar-carga'),
    path('modificar/crear', views.ModCargaCreateView.as_view(), name='modcarga-create'),
    path('borrarmod/<int:pk>/', views.ModCargaDeleteView.as_view(), name='carga-delete'),
]