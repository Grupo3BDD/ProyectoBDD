#from django.shortcuts import render

# URL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse


# LIBRERIAS PARA REDERICCIONAR
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

# LIBRERIAS PARA CRUD
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q

#MODELOS
from .models import Edificio, Salon, Clasificacion

#FORMULARIOS
from. forms import edificioForm, clasificacionForm, salonForm

# Decoradores
#from .decoradores import *

# EXTRAS
from .utils import breadcrumb

# Decorador
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

###-- MODULO QUE ENLISTA A LOS EDIFICIOS--###
class EdificioList(ListView):
    template_name = 'edificios/edificio.html'
    queryset = Edificio.objects.all().order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Edificios'
        context['title'] = 'Edificios'
        context['breadcrumb'] = breadcrumb()

        return context


###-- MODULO QUE CREA A LOS EDIFICIOS--###
class EdificioCreate(CreateView):
    model = Edificio
    form_class = edificioForm
    template_name = 'edificios/edificioForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'

        return context

    success_url = reverse_lazy('edificios:Edificio')


###-- MODULO QUE MODIFICA ALGUN EDIFICIO--###
class EdificioUpdate(UpdateView):
    model = Edificio
    form_class = edificioForm
    template_name = 'edificios/edificioForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Editar'

        return context

    success_url = reverse_lazy('edificios:Edificio')

###-- MODULO QUE ELIMINA ALGUN EDIFICIO--###
class EdificioDelete(DeleteView):
    model = Edificio
    template_name = 'edificios/edificioDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context

    success_url = reverse_lazy('edificios:Edificio')

###-- MODULO QUE DETALLA ALGUN EDIFICIO--###
class EdificioDetalle(DetailView):
    model = Edificio
    template_name = 'edificios/edificioDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE BUSCA EDIFICIOS--###
class EdificioSearch(ListView):
    template_name = 'edificios/edificioBuscar.html'

    def get_queryset(self):
        filters = Q(nombreEdificio__icontains=self.query())
        return Edificio.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['edificio_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context