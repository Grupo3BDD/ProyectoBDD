# URL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import Http404

# Modelos
from .models import User, Rol, Permiso, Puesto, TipoDocumento, PaisOrigen, EncargadoArea, CoordinadorAcademico
from django.db.models import Q
from django.db import transaction

# LIBRERIAS PARA EL CRUD
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Login
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Decoradores
from .decoradores import *

# FORMS

from .forms import rolForm, permisoForm, editRol

from .forms import RegistroForm,  ChangePasswordForm, CreateUserForm,UpdateUserForm


# UTILS
from .utils import breadcrumb_usuarios, breadcrumb_estudiante, breadcrumb_docente, breadcrumb_puesto

# Paginacion
from django.core.paginator import Paginator

# SETTINGS OF PROJECT
from proyecto.settings import MEDIA_URL, STATIC_URL
# Create your views here.


### -- APARTADO DE REGISTRAR USUARIOS --##
class SignUp(user_authenticate, CreateView):
    '''
    MODULO PARA REGISTRO DE USUARIOS
    '''
    model = User
    form_class = RegistroForm
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Crear Cuenta Nueva'
        context['messages.success'] = 'BIENVENIDO'
        context['info'] = 'Crear Cuenta'

        context['users_list'] = User.objects.exists()

        return context

    def form_valid(self, form):
        form.save()
        # user = User.objects.last()
        # profile = Perfil.objects.create(usuario=user)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, 'USUARIO CREADO EXITOSAMENTE')
        return redirect('index')
        # return redirect('perfilUsuario')

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))


### -- APARTADO DE SALIR --##
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('users:login')


### -- APARTADO DE INICIO DE SESION --##
def login_view(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')  # diccionario
        password = request.POST.get('password')  # None

        user = authenticate(username=username, password=password)  # None
        if user:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            if user.is_superuser:
                messages.success(
                    request, 'Bienvenido ADMINISTRADOR: {}'.format(user.username))

            else:
                messages.success(
                    request, 'Bienvenido USUARIO: {}'.format(user.username))

            return redirect('index')

        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, "users/login.html", {
        'title': 'Iniciar Sesion',

    })

### -- APARTADO PARA CAMBIAR LA CONTRASEÑA DE UN USUARIO --##


class ChangePassword(View):
    template_name = 'users/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {
            'form': self.form_class,
            'title': 'Cambiar Contraseña',
            'info': 'Cambiar Contraseña',

        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.filter(pk=request.user.pk)
            if user.exists():
                user = user.first()
                user.set_password(form.cleaned_data.get('password1'))
                contra = form.cleaned_data.get('password1')
                user.save()
                user = authenticate(
                    username=request.user.username, password=contra)
                login(self.request, user)

                return redirect(self.success_url)
            return redirect(self.success_url)
        else:
            form = self.form_class(request.POST)

            return render(request, self.template_name, {
                'form': form,
                'title': 'Cambiar Contraseña',
                'info': 'Cambiar Contraseña',

            })


### -- Acceder al perfil del usuario que esta registrado --###
def detailUserRegister(request, pk):
    template_name = 'users/perfil.html'
    user = get_object_or_404(User, pk=request.user.pk)
    perfil = get_object_or_404(User, pk=pk)

    if (user == perfil):
        # Solo el mismo usuario puede ver su perfil
        context = {
            'perfil': perfil,
            'title': f'Perfil de Usuario {user}'
        }
        return render(request, template_name, context)
    return redirect('index')


def listDocente(request):
    template_name = 'users/Docente/docente.html'
    listado_docente = User.objects.all().filter(tipo_usuario='Docente')

    paginator = Paginator(listado_docente, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Listado De Docentes',
        'docente_list': listado_docente,
        'breadcrumb': breadcrumb_docente(),
        'page_obj': page_obj
    }
    return render(request, template_name, context)


def listEstudiante(request):
    template_name = 'users/Estudiante/estudiante.html'
    listado_estudiante = User.objects.all().filter(tipo_usuario='Estudiante')

    paginator = Paginator(listado_estudiante, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Listado De Estudiantes',
        'estudiante_list': listado_estudiante,
        'message': 'Estudiantes',
        'breadcrumb': breadcrumb_estudiante(),
        'page_obj': page_obj
    }
    return render(request, template_name, context)


def listUsuario(request):
    template_name = 'users/Usuarios/usuario.html'
    listado_usuario = User.objects.all().filter(tipo_usuario='Usuario')
    paginator = Paginator(listado_usuario, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    

    context = {
        'title': 'Listado De Usuarios',
        'usuario_list': listado_usuario,
        'message': 'Usuarios',
        'breadcrumb': breadcrumb_usuarios(),
        'page_obj': page_obj
    }
    return render(request, template_name, context)


def listPermiso(request):
    template_name = 'users/RolPermiso/listPermisoRol.html'
    permiso = Permiso.objects.all().order_by('id')

    paginator = Paginator(permiso, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Listado De Roles y Permiso',
        'permisos': request.path,
        'permiso_list': permiso,
        'page_obj': page_obj

    }
    return render(request, template_name, context)


def listRol(request):

    template_name = 'users/RolPermiso/listPermisoRol.html'
    rol = Rol.objects.all().order_by('id')

    paginator = Paginator(rol, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        'title': 'Listado De Roles y Permiso',
        'roles': request.path,
        'rol_list': rol,
        'page_obj': page_obj
    }
    return render(request, template_name, context)






###-- MODULO QUE CREA A LOS ROLES--###
class RolCreate(CreateView):
    model = Rol
    form_class = rolForm
    template_name = 'users/RolPermiso/Rol/rolForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Crear'

        return context

    success_url = reverse_lazy('users:list_rolPermiso')


###-- MODULO QUE MODIFICA ALGUN ROL--###
class RolUpdate(UpdateView):
    model = Rol
    form_class = editRol
    template_name = 'users/RolPermiso/Rol/rolForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Guardar'

        return context

    success_url = reverse_lazy('users:list_rolPermiso')


###-- MODULO QUE ELIMINA ALGUN ROL--###
class RolDelete(DeleteView):
    model = Rol
    template_name = 'users/RolPermiso/Rol/rolDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context

    success_url = reverse_lazy('users:list_rolPermiso')




###-- MODULO QUE CREA A LOS PERMISOS--###
class PermisoCreate(CreateView):
    model = Permiso
    form_class = permisoForm
    template_name = 'users/RolPermiso/Permiso/permisoForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Crear'

        return context

    success_url = reverse_lazy('users:permiso')


###-- MODULO QUE MODIFICA ALGUN PERMISO--###
class PermisoUpdate(UpdateView):
    model = Permiso
    form_class = permisoForm
    template_name = 'users/RolPermiso/Permiso/permisoForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Guardar'

        return context

    success_url = reverse_lazy('users:permiso')


###-- MODULO QUE ELIMINA ALGUN PERMISO--###
class PermisoDelete(DeleteView):
    model = Permiso
    template_name = 'users/RolPermiso/Permiso/permisoDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context

    success_url = reverse_lazy('users:permiso')

def listPuesto(request):
    template_name = 'puesto/puesto.html'
    puesto = Puesto.objects.all().order_by('id')

    paginator = Paginator(puesto, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Puestos',
        'puesto_list': puesto,
        'page_obj': page_obj,
        'message': 'Puestos',
        'breadcrumb': breadcrumb_puesto(),
    }


    return render(request, template_name, context)


class crearUsuario(CreateView):
    model= User
    template_name = 'users/create.html'
    form_class = CreateUserForm   
    creandoUsuario = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'        
        context['info'] = 'Agregar'
        return context
        
class UpdateUser(UpdateView):
    model= User
    template_name = 'users/update.html'
    form_class = UpdateUserForm   
    creandoUsuario = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'        
        context['info'] = 'Agregar'
        return context

def deleteUser(request,pk):
    user = get_object_or_404(User,pk=pk)
    if user:
        user.delete()
    return redirect('users:usuario')

def detailUser(request,pk):
    user = get_object_or_404(User,pk=pk)
    template_name = 'users/detail.html'
    context ={
        'title':f'Detalle {user}',

    }

    return render(request,template_name,context)
 

    

