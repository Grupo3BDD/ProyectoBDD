from django import forms
from django.forms import ModelForm, DateInput, NumberInput
from .models import Carga

class CargaForm(ModelForm):
    class Meta: 
        model = Carga
        fields = '__all__'
        widgets = {
            'year': NumberInput(attrs = {'type': 'number'}),
            'fecha_envio': DateInput(attrs = {'type': 'date'}),
            'fecha_aprob': DateInput(attrs = {'type': 'date'})
        }