from django import forms
from django.forms import ModelForm, DateInput, NumberInput
from .models import Carga, ModCarga

class CargaForm(ModelForm):
    class Meta: 
        model = Carga
        fields = '__all__'
        widgets = {
            'year': NumberInput(attrs = {'type': 'number'}),
            'fecha_envio': DateInput(attrs = {'type': 'date'}),
            'fecha_aprob': DateInput(attrs = {'type': 'date'})
        }

class ModCargaForm(ModelForm):

    class Meta:
        model = ModCarga
        fields = [
            'pensum',
            'codigo',
            'curso',
            'num_personal',
            'docente'

        ]

        labels = {
            'pensum': 'Pensum',
            'codigo': 'Código',
            'curso': 'Curso',
            'num_personal': 'No. Personal',
            'docente': 'Docente'


        }

        widgets = {
            'pensum': forms.Select(attrs={'class': 'form-control select2'}),
            'codigo': forms.Select(attrs={'class': 'form-control select2'}),
            'curso': forms.Select(attrs={'class': 'form-control select2'}),
            'num_personal': forms.Select(attrs={'class': 'form-control select2'}),
            'docente': forms.Select(attrs={'class': 'form-control select2'}),

        }
