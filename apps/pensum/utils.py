from django.urls import reverse

def breadcrumb(pensums = True):
    return [
        {'title': 'Pensums', 'active': pensums, 'url': reverse('pensums:Curso')}
    ]
