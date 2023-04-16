# URL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

# Modelos
from django.contrib.auth.models import User
from .models import Perfil
from django.db.models import Q 

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
from .forms import RegistroForm,  ChangePasswordForm

# Create your views here.


###-- APARTADO DE REGISTRAR USUARIOS --##
class SignUp(user_authenticate,CreateView):
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
        user = User.objects.last()
        profile = Perfil.objects.create(usuario=user)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, 'USUARIO CREADO EXITOSAMENTE')
        return redirect('index')
        #return redirect('perfilUsuario')

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))


###-- APARTADO DE SALIR --##
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('users:login')


###-- APARTADO DE INICIO DE SESION --##
def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password)#None
        if user:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])
            
            
            if user.is_superuser:
                messages.success(request, 'Bienvenido ADMINISTRADOR: {}'.format(user.username))
               
            else:
                messages.success(request, 'Bienvenido USUARIO: {}'.format(user.username))
               
           
            
            return redirect('index')

        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, "users/login.html", {
        'title':'Iniciar Sesion',
       
    })

###-- APARTADO PARA CAMBIAR LA CONTRASEÑA DE UN USUARIO --##
class ChangePassword(View):
    template_name ='users/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, {
            'form':self.form_class, 
            'title': 'Cambiar Contraseña',
            'info': 'Cambiar Contraseña',
            'perfil':Perfil.objects.get(pk=request.user.pk)
            })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.filter(pk = request.user.pk)
            if user.exists():
                user = user.first()
                user.set_password(form.cleaned_data.get('password1'))
                contra = form.cleaned_data.get('password1')
                user.save()
                user = authenticate(username=request.user.username, password=contra)
                login(self.request, user)

                return redirect(self.success_url)
            return redirect(self.success_url)
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {
            'form':form, 
            'title': 'Cambiar Contraseña',
            'info': 'Cambiar Contraseña',
            'perfil':Perfil.objects.get(pk=request.user.pk)
            })
        

###-- Acceder al perfil del usuario que esta registrado --###
def detailUserRegister(request,pk):
    perfil = Perfil.objects.get(pk=pk)
    template_name = 'users/perfil.html'
    context = {
        'perfil':perfil,
        'title': f'Perfil de Usuario {perfil.usuario}'
    }
    return render(request, template_name, context)