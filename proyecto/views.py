
# URL
from django.shortcuts import render

# Modelos
from apps.users.models import User
from django.db.models import Q 

# from django.contrib.auth.models import User



# SETTINGS OF PROJECT
from proyecto.settings import MEDIA_URL, STATIC_URL

def index(request):
    template = 'index.html'  

    context = {
        'title':'Inicio',
        
    }
    return render(request, template, context)