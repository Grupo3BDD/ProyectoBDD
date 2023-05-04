from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Carga
from .forms import CargaForm
from django.views.generic import View

class CargaListView(generic.ListView):
    template_name = "cargas/carga_list.html"
    context_object_name = "carga"
    def get_queryset(self):
        return Carga.objects.all()
    

class CargaCreateView(generic.CreateView):
    template_name = "cargas/carga_create.html"
    form_class = CargaForm

    def get_success_url(self):
        return reverse("carga:carga-list")
    
    def get_queryset(self):
        return Carga.objects.all()
    
class CargaDeleteView(generic.DeleteView):
    template_name = "cargas/carga_delete.html"

    def get_success_url(self):
        return reverse("carga:carga-list")
    
    def get_queryset(self):
        return Carga.objects.all()
    

class CargaUpdateView (generic.UpdateView):
    template_name = "cargas/carga_update.html"
    form_class = CargaForm

    def get_success_url(self):
        return reverse("carga:carga-list")
    
    def get_queryset(self):
        return Carga.objects.all()