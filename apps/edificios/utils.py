from django.urls import reverse

def breadcrumb(edificios = True):
    return [
        {'title': 'Edificios', 'active': edificios, 'url': reverse('edificios:Edificio')}
    ]

#def breadcrumb(salones = True):
#    return [
#        {'title': 'Salones', 'active': salones, 'url': reverse('edificios:Salon')}
#    ]