from django.shortcuts import render

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

#MODELOS
from .models import Edificio, Salon, Clasificacion

#FORMULARIOS
#from. forms

# Decoradores
#from .decoradores import *

# FORMS
#from .forms import RegistroForm



# Create your views here.
