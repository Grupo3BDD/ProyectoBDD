
# URL
from django.shortcuts import render

# Modelos
from apps.users.models import Perfil


def index(request):
    template = 'index.html'
    
    context = {
        'title':'Inicio',
        'perfil':Perfil.objects.get(pk=request.user.pk)
    }
    return render(request, template, context)