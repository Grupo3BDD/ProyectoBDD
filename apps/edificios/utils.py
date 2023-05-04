from django.urls import reverse

def breadcrumb(edificios = True):
    return [
        {'title': 'Edificios', 'active': edificios, 'url': reverse('edificios:Edificio')}
    ]

