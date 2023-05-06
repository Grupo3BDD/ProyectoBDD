from django import forms
from django.forms import ModelForm, DateInput, NumberInput
from .models import Carga


class CargaForm(ModelForm):
    tipo_ciclo = [
        ('Primer Ciclo', 'Primer Ciclo'),
        ('Segundo Ciclo', 'Segundo Ciclo'),
        ('Tercer Ciclo', 'Tercer Ciclo'),
        ('Cuarto Ciclo', 'Cuarto Ciclo'),
        ('Quinto Ciclo', 'Quinto Ciclo'),
        ('Sexto Ciclo', 'Sexto Ciclo'),
        ('Septimo Ciclo', 'Septimo Ciclo'),
        ('Octavo Ciclo', 'Octavo Ciclo'),
        ('Noveno Ciclo', 'Noveno Ciclo'),
        ('Decimo Ciclo', 'Decimo Ciclo'),
    ]

    ciclo_acad = forms.ChoiceField(
        choices=tipo_ciclo,
        required=True,
        label='Ciclo Academico',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Carga
        fields = [
            'year', 'ciclo_acad', 'carreraId'
        ]
        labels = {
            'year': 'Año',
            'carreraId': 'Nombre de la carrera'


        }
        
