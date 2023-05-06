# URL
from django.shortcuts import render, redirect, reverse

# Modulo
from .models import Carga,CargaAcademicaDetalle

# CRUD
from django.db.models import Q
from django.db import transaction

# Formulario
from .forms import CargaForm

# Views
from django.views.generic import View,ListView,CreateView,UpdateView,DeleteView

# UTILS
from .utils import breadcrumb

# SETTINGS OF PROJECT
from proyecto.settings import MEDIA_URL, STATIC_URL
from django.shortcuts import  get_object_or_404

class CargaListView(ListView):
    template_name = "cargas/carga_list.html"    
    queryset = Carga.objects.all().order_by('-id')
    paginate_by = 5
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        context['message'] = 'Administración de Cargas'
        context['title'] = 'Cargas'
        context['breadcrumb'] = breadcrumb()

        return context
    

class CargaCreateView(CreateView):
    template_name = "cargas/carga_create.html"
    form_class = CargaForm

    def get_success_url(self):
        return reverse("cargas:carga")
    
    def get_queryset(self):
        return Carga.objects.all()
    
class CargaDeleteView(DeleteView):
    template_name = "cargas/carga_delete.html"

    def get_success_url(self):
        return reverse("cargas:carga")
    
    def get_queryset(self):
        return Carga.objects.all()
    

class CargaUpdateView(UpdateView):
    template_name = "cargas/carga_update.html"
    form_class = CargaForm

    def get_success_url(self):
        return reverse("cargas:carga")
    
    def get_queryset(self):
        return Carga.objects.all()
    

def detailCarga(request,pk):
    template_name='cargas/detalle_carga.html'
    carga= get_object_or_404(Carga,pk=pk)
    filtro = CargaAcademicaDetalle.objects.filter(Q(cargaId=pk))
    context = {
        'title': f'Carga Academica {carga.carreraId} ',
        'cargaAcademicaDetalle_list':filtro
    }
    return render(request,template_name,context)