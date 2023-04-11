
# URL
from django.shortcuts import render

def index(request):
    template = 'index.html'
    context = {
        'title':'Inicio',
    }
    return render(request, template, context)