from django.urls import reverse

def breadcrumb(cargas = True):
    return [
        {'title': 'Cargas', 'active': cargas, 'url': reverse('cargas:carga-list')}
    ]
