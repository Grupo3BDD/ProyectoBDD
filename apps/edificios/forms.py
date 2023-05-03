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

        ]

        labels = {
            'nombreEdificio': 'Nombre del Edificio',
            'cantidadSalones': 'Cantidad de Salones',
            'niveles': 'Niveles',

        }

        widgets = {
            'nombreEdificio': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidadSalones': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'niveles': forms.TextInput(attrs={'class': 'form-control', 'type':'number' }),

        }

class editForm(forms.ModelForm):
    class Meta:
        model = Edificio

        fields = [
            'nombreEdificio',
            'estado',


        ]

        labels = {
            'nombreEdificio': 'Nombre del Edificio',
            'estado': 'Habilitado',


        }

        widgets = {
            'nombreEdificio': forms.TextInput(attrs={'class': 'form-control'}),
            #'estado': forms.CheckboxInput(
            #    attrs={'class': 'form-control', 'type':'checkbox', 'content':' ', 'border':'solid 1px #9e9e9e',
            #           'border-radius':'3px', 'width':'0.8em','height':'0.8em','position':'absolute','left':'0px',
            #           'top':'0.1em','transition':'all 0.2s', 'transform':'rotate(0deg)'}),

        }


class clasificacionForm(forms.ModelForm):
    class Meta:
        model = Clasificacion

        fields = [
            'tipo_salon_uso',



        ]

        labels = {
            'tipo_salon_uso': 'Nombre Clasificacion',



        }

        widgets = {
            'tipo_salon_uso': forms.TextInput(attrs={'class': 'form-control'}),
            #'estado': forms.CheckboxInput(
            #    attrs={'class': 'form-control', 'type':'checkbox'}),

        }

class editClasificacion(forms.ModelForm):
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
            #'estado': forms.CheckboxInput(
            #    attrs={'class': 'form-control', 'type':'checkbox'}),

        }

class salonForm(forms.ModelForm):
    class Meta:
        model = Salon

        fields = [
            'edificio',
            'clasificacion',
            'nombreSalon',
            'capacidadEstudiantes',




        ]

        labels = {
            'edificio': 'Edificio',
            'clasificacion': 'Clasificacion',
            'nombreSalon': 'Nombre del Salon',
            'capacidadEstudiantes': 'Capacidad de estudiantes',



        }

        widgets = {
            'edificio': forms.Select(attrs={'class': 'form-control select2'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control select2'}),
            'nombreSalon': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidadEstudiantes': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),


        }

class editSalon(forms.ModelForm):
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
            'nombreSalon': 'Nombre del Salon',
            'capacidadEstudiantes': 'Capacidad de estudiantes',
            'estado': 'Habilitado',


        }

        widgets = {
            #'edificio': forms.Select(attrs={'class': 'form-control select2'}),
            #'clasificacion': forms.Select(attrs={'class': 'form-control select2'}),
            'nombreSalon': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidadEstudiantes': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            #'estado': forms.CheckboxInput(
            #    attrs={'class': 'form-control', 'type':'checkbox'}),

        }
