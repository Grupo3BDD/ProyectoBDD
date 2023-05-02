# FORMULARIO DE DJANGO
from django import forms

#MODELOS
from .models import Edificio, Salon, Clasificacion

#Formulario para los Edificios
class edificioForm(forms.ModelForm):
    class Meta:
        model = Edificio

        fields = [
            'nombreEdificio',
            'cantidadSalones',
            'niveles',
            'estado',


        ]

        labels = {
            'nombreEdificio': 'Nombre del Edificio',
            'cantidadSalones': 'Cantidad de Salones',
            'niveles': 'Niveles',
            'estado': 'Habilitado',


        }

        widgets = {
            'nombreEdificio': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidadSalones': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'niveles': forms.TextInput(attrs={'class': 'form-control', 'type':'number' }),
            'estado': forms.CheckboxInput(
                attrs={'class': 'form-control', 'type':'boolean'}),

        }

class clasificacionForm(forms.ModelForm):
    class Meta:
        model = Clasificacion

        fields = [
            'tipo_salon_uso',
            'estado',


        ]

        labels = {
            'tipo_salon_uso': 'Nombre Clasificacion',
            'estado': 'Habilitado',


        }

        widgets = {
            'tipo_salon_uso': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(
                attrs={'class': 'form-control', 'type':'boolean'}),

        }

class salonForm(forms.ModelForm):
    class Meta:
        model = Salon

        fields = [
            'edificio',
            'clasificacion',
            'nombreSalon',
            'capacidadEstudiantes',
            'estado',



        ]

        labels = {
            'edificio': 'Edificio',
            'clasificacion': 'Clasificacion',
            'nombreSalon': 'Niveles',
            'capacidadEstudiantes': 'Capacidad de estudiantes',
            'estado': 'Habilitado',


        }

        widgets = {
            'edificio': forms.Select(attrs={'class': 'form-control select2'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control select2'}),
            'nombreSalon': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidadEstudiantes': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'estado': forms.CheckboxInput(
                attrs={'class': 'form-control', 'type':'boolean'}),

        }
