from django.urls import path
from views import *
from django.contrib.auth.decorators import login_required

app_name = 'carga'

urlpatterns = [
    path('listacarga/', CargaListView.as_view(), name='carga-list'),
    path('crearcarga/', CargaCreateView.as_view(), name='carga-create'),
    path('<int:pk>/editarcarga/', CargaUpdateView.as_view(), name='carga-update'),
    path('<int:pk>/borrarcarga/', CargaDeleteView.as_view(), name='carga-delete')
]