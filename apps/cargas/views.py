from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Carga, ModCarga
from .forms import CargaForm, ModCargaForm
from django.views.generic import View
from .utils import breadcrumb


class CargaListView(generic.ListView):
    template_name = "cargas/carga_list.html"    
    queryset = Carga.objects.all().order_by('-id')
    paginate_by = 5
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        context['message'] = 'Administración de Cargas'
        context['title'] = 'Cargas'
        context['breadcrumb'] = breadcrumb()

        return context
    

class CargaCreateView(generic.CreateView):
    template_name = "cargas/carga_create.html"
    form_class = ModCargaForm

    def get_success_url(self):
        return reverse("cargas:carga-list")
    
    def get_queryset(self):
        return Carga.objects.all()
    
class CargaDeleteView(generic.DeleteView):
    template_name = "cargas/carga_delete.html"

    def get_success_url(self):
        return reverse("cargas:carga-list")
    
    def get_queryset(self):
        return Carga.objects.all()
    

class CargaUpdateView (generic.UpdateView):
    template_name = "cargas/carga_update.html"
    form_class = CargaForm

    def get_success_url(self):
        return reverse("cargas:carga-list")
    
    def get_queryset(self):
        return Carga.objects.all()
    

#--------------------------VISTAS PARA EL MÉTODO DE MODIFICAR


class ModCargaListView(generic.ListView):
    template_name = "cargas/sub/modcargalist.html"    
    queryset = ModCarga.objects.all().order_by('-id')
    paginate_by = 5
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        context['message'] = 'Administración de Cargas'
        context['title'] = 'Cargas'
        context['breadcrumb'] = breadcrumb()

        return context
    

class ModCargaCreateView(generic.CreateView):
    template_name = "cargas/sub/modcarga_create.html"
    form_class = ModCarga

    def get_success_url(self):
        return reverse("cargas:modificar-carga")
    
    def get_queryset(self):
        return Carga.objects.all()
    
class ModCargaDeleteView(generic.DeleteView):
    template_name = "cargas/sub/modcarga_delete.html"

    def get_success_url(self):
        return reverse("cargas:modificar-carga")
    
    def get_queryset(self):
        return Carga.objects.all()
    

class ModCargaUpdateView (generic.UpdateView):
    template_name = "cargas/carga_update.html"
    form_class = CargaForm

    def get_success_url(self):
        return reverse("cargas:modificar-carga")
    
    def get_queryset(self):
        return Carga.objects.all()
    
