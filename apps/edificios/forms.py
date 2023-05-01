# FORMULARIO DE DJANGO
from django import forms

#MODELOS
from .models import Edificio, Salon, Clasificacion

#Formulario para los Edificios
class EdificioForm(forms.ModelForm):
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