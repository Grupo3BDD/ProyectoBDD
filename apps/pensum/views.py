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
from .forms import *

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
    template_name = 'pensums/cursos/cursosForm.html'

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
        filters = Q(idCurso__icontains=self.query())
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

