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
from. forms import edificioForm, clasificacionForm, salonForm, editForm, editSalon, editClasificacion

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
        context['message'] = 'Administración de Edificios'
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
        context['message'] = 'Crear'

        return context

    success_url = reverse_lazy('edificios:Edificio')


###-- MODULO QUE MODIFICA ALGUN EDIFICIO--###
class EdificioUpdate(UpdateView):
    model = Edificio
    form_class = editForm
    template_name = 'edificios/edificioForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Guardar'

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



###-- MODULO QUE ENLISTA A LOS SALONES--###
class SalonList(ListView):
    template_name = 'edificios/salones/salon.html'
    queryset = Salon.objects.all().order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['message'] = 'Administración de Salones'
        context['title'] = 'Salones'
        context['breadcrumb'] = breadcrumb()

        return context


###-- MODULO QUE CREA A LOS SALONES--###
class SalonCreate(CreateView):
    model = Salon
    form_class = salonForm
    template_name = 'edificios/salones/salonForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Crear'

        return context

    success_url = reverse_lazy('edificios:Salon')


###-- MODULO QUE MODIFICA ALGUN SALON--###
class SalonUpdate(UpdateView):
    model = Salon
    form_class = editSalon
    template_name = 'edificios/salones/salonForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Guardar'

        return context

    success_url = reverse_lazy('edificios:Salon')



###-- MODULO QUE ELIMINA ALGUN SALON--###
class SalonDelete(DeleteView):
    model = Salon
    template_name = 'edificios/salones/salonDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context

    success_url = reverse_lazy('edificios:Salon')

###-- MODULO QUE DETALLA ALGUN SALON--###
class SalonDetalle(DetailView):
    model = Salon
    template_name = 'edificios/salones/salonDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE BUSCA SALON--###
class SalonSearch(ListView):
    template_name = 'edificios/salones/salonBuscar.html'

    def get_queryset(self):
        filters = Q(nombreSalon__icontains=self.query())
        return Salon.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['salon_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE ENLISTA A LAS CLASIFICACIONES--###
class ClasificacionList(ListView):
    template_name = 'edificios/clasificaciones/clasificacion.html'
    queryset = Clasificacion.objects.all().order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de clasificación de Salones'
        context['title'] = 'Clasificaciones'
        context['breadcrumb'] = breadcrumb()

        return context


###-- MODULO QUE CREA A LAS CLASIFICACIONES--###
class ClasificacionCreate(CreateView):
    model = Clasificacion
    form_class = clasificacionForm
    template_name = 'edificios/clasificaciones/clasificacionForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Crear'

        return context

    success_url = reverse_lazy('edificios:Clasificacion')


###-- MODULO QUE MODIFICA ALGUNA CLASIFICACION--###
class ClasificacionUpdate(UpdateView):
    model = Clasificacion
    form_class = editClasificacion
    template_name = 'edificios/clasificaciones/clasificacionForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Guardar'

        return context

    success_url = reverse_lazy('edificios:Clasificacion')



###-- MODULO QUE ELIMINA ALGUNA CLASIFICACION--###
class ClasificacionDelete(DeleteView):
    model = Clasificacion
    template_name = 'edificios/clasificaciones/clasificacionDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context

    success_url = reverse_lazy('edificios:Clasificacion')

###-- MODULO QUE DETALLA ALGUNA CLASIFICACION--###
class ClasificacionDetalle(DetailView):
    model = Clasificacion
    template_name = 'edificios/clasificaciones/clasificacionDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE BUSCA CLAASIFICACIONES--###
class ClasificacionSearch(ListView):
    template_name = 'edificios/clasificaciones/clasificacionBuscar.html'

    def get_queryset(self):
        filters = Q(tipo_salon_uso__icontains=self.query())
        return Clasificacion.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['clasificacion_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context