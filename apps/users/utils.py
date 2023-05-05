from django.urls import reverse

def breadcrumb_usuarios(usuarios = True):
    return [
        {'title': 'Usuarios', 'active': usuarios, 'url': reverse('users:usuario')}
    ]

def breadcrumb_docente(docente = True):
    return [
        {'title': 'Docentes', 'active': docente, 'url': reverse('users:docente')}
    ]

def breadcrumb_estudiante(estudiante = True):
    return [
        {'title': 'Estudiantes', 'active': estudiante, 'url': reverse('users:estudiante')}
    ]