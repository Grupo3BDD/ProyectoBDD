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
from .models import *

#FORMULARIOS
from. forms import *

# Decoradores
#from .decoradores import *

# EXTRAS
from .utils import breadcrumb

# Decorador
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

###-- MODULO QUE ENLISTA A LOS CURSOS--###
class CursoList(ListView):
    template_name = 'pensums/cursos/curso.html'
    queryset = Curso.objects.all().order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['message'] = 'Administración de Cursos'
        context['title'] = 'Cursos'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE CREA A LOS CURSOS--###
class CursoCreate(CreateView):
    model = Curso
    form_class = cursoForm
    template_name = 'pensums/cursos/cursoForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Crear'

        return context

    success_url = reverse_lazy('pensums:Curso')


###-- MODULO QUE MODIFICA ALGUN CURSO--###
class CursoUpdate(UpdateView):
    model = Curso
    form_class = editCurso
    template_name = 'pensums/cursos/cursoForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Guardar'

        return context

    success_url = reverse_lazy('pensums:Curso')


###-- MODULO QUE ELIMINA ALGUN CURSO--###
class CursoDelete(DeleteView):
    model = Curso
    template_name = 'pensums/cursos/cursoDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context

    success_url = reverse_lazy('pensums:Curso')

###-- MODULO QUE DETALLA ALGUN CURSO--###
class CursoDetalle(DetailView):
    model = Curso
    template_name = 'pensums/cursos/cursoDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE BUSCA CURSOS--###
class CursoSearch(ListView):
    template_name = 'pensums/cursos/cursoBuscar.html'

    def get_queryset(self):
        filters = Q(nombreCurso__icontains=self.query())
        return Curso.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['curso_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE ENLISTA A LAS CARRERAS--###
class CarreraList(ListView):
    template_name = 'pensums/carreras/carrera.html'
    queryset = Carrera.objects.all().order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['message'] = 'Administración de Carreras'
        context['title'] = 'Carrera'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE CREA A LAS CARRERAS--###
class CarreraCreate(CreateView):
    model = Carrera
    form_class = carreraForm
    template_name = 'pensums/carreras/carreraForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Crear'

        return context

    success_url = reverse_lazy('pensums:Carrera')


###-- MODULO QUE MODIFICA ALGUNA CARRERA--###
class CarreraUpdate(UpdateView):
    model = Carrera
    form_class = editCarrera
    template_name = 'pensums/carreras/carreraForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Guardar'

        return context

    success_url = reverse_lazy('pensums:Carrera')


###-- MODULO QUE ELIMINA ALGUNA CARRERA--###
class CarreraDelete(DeleteView):
    model = Carrera
    template_name = 'pensums/carreras/carreraDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context

    success_url = reverse_lazy('pensums:Carrera')

###-- MODULO QUE DETALLA ALGUNA CARRERA--###
class CarreraDetalle(DetailView):
    model = Curso
    template_name = 'pensums/carreras/carreraDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE BUSCA CARRERAS-###
class CarreraSearch(ListView):
    template_name = 'pensums/carreras/carreraBuscar.html'

    def get_queryset(self):
        filters = Q(nombreCarrera__icontains=self.query())
        return Carrera.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['carrera_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context



###-- MODULO QUE ENLISTA PENSUM--###
class PensumList(ListView):
    template_name = 'pensums/pensum/pensum.html'
    queryset = Pensum.objects.all().order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['message'] = 'Administrador de Pensum'
        context['title'] = 'Pensum'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE CREA PENSUM--###
class PensumCreate(CreateView):
    model = Pensum
    form_class = pensumForm
    template_name = 'pensums/pensum/pensumForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Crear'

        return context

    success_url = reverse_lazy('pensums:Pensum')

###-- MODULO QUE MODIFICA ALGUN PENSUM--###
class PensumUpdate(UpdateView):
    model = Pensum
    form_class = editPensum
    template_name = 'pensums/pensum/pensumForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Guardar'

        return context

    success_url = reverse_lazy('pensums:Pensum')


###-- MODULO QUE ELIMINA ALGUN PENSUM--###
class PensumDelete(DeleteView):
    model = Pensum
    template_name = 'pensums/pensum/pensumDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context

    success_url = reverse_lazy('pensums:Pensum')

def pensumDelete(request, pk):
    pensum = get_object_or_404(Pensum,pk=pk)
    print(pk)
    print(pensum)
    #if pensum:
        #pensum.delete()
    return redirect('pensums:Pensum')

###-- MODULO QUE DETALLA ALGUN PENSUM--###
class PensumDetalle(DetailView):
    model = Pensum
    template_name = 'pensums/pensum/pensumDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context

###-- MODULO QUE BUSCA PENSUMS-###
class PensumSearch(ListView):
    template_name = 'pensums/pensum/pensumBuscar.html'

    def get_queryset(self):
        filters = Q(codigo_pensum__icontains=self.query())
        return Pensum.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['pensum_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context
