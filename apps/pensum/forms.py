# FORMULARIO DE DJANGO
from django import forms

#MODELOS
from .models import *

#Formulario para los Cursos
class cursoForm(forms.ModelForm):
    class Meta:
        model = Curso

        fields = [
            'idCurso',
            'nombreCurso',
            'horasSemana',
            'carrera',
            'laboratorio',
            'codigo_lab',
            'horas_lab_sem',
            'valido_semestres',

        ]

        labels = {
            'idCurso': 'Código de curso',
            'nombreCurso': 'Nombre del curso',
            'horasSemana': 'Num. de horas a la semana',
            'carrera':'Carrera',
            'laboratorio': 'Con laboratorio',
            'codigo_lab': 'Código de laboratorio',
            'horas_lab_sem': 'Num. de horas a la semana',
            'valido_semestres': 'Valido por',

        }

        widgets = {
            'idCurso': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreCurso': forms.TextInput(attrs={'class': 'form-control'}),
            'horasSemana': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'carrera':forms.CheckboxSelectMultiple(attrs = { 'type': 'checkbox'}),
            'codigo_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'horas_lab_sem': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'valido_semestres': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),

        }


# Formulario para la edición de Cursos
class editCurso(forms.ModelForm):
    class Meta:
        model = Curso

        fields = [
            'idCurso',
            'nombreCurso',
            'horasSemana',
            'carrera',
            'laboratorio',
            'codigo_lab',
            'horas_lab_sem',
            'valido_semestres',
            'habilitado',

        ]

        labels = {
            'idCurso': 'Código de curso',
            'nombreCurso': 'Nombre del curso',
            'horasSemana': 'Num. de horas a la semana',
            'carrera': 'Carrera',
            'laboratorio': 'Con laboratorio',
            'codigo_lab': 'Código de laboratorio',
            'horas_lab_sem': 'Num. de horas a la semana',
            'valido_semestres': 'Valido por',
            'habilitado': 'Habilitado',

        }

        widgets = {
            'idCurso': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreCurso': forms.TextInput(attrs={'class': 'form-control'}),
            'horasSemana': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'carrera': forms.CheckboxSelectMultiple(attrs = { 'type': 'checkbox'}),
            'codigo_lab': forms.TextInput(attrs={'class': 'form-control'}),
            'horas_lab_sem': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'valido_semestres': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),

        }

#Formulario para las Carreras
class carreraForm(forms.ModelForm):
    class Meta:
        model = Carrera

        fields = [
            'idCarrera',
            'nombreCarrera',
            'duracionPeriodos',
            'clasificacion',
            'partida',
            'tipo_ciclo',
            #'encargado_area',

        ]

        labels = {
            'idCarrera': 'Código de la carrera',
            'nombreCarrera': 'Nombre de la carrera',
            'duracionPeriodos': 'Duración de los períodos en minutos',
            'clasificacion':'Clasificación',
            'partida': 'Partida',
            'tipo_ciclo': 'Tipo de ciclo académico'

        }

        widgets = {
            'idCarrera': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreCarrera': forms.TextInput(attrs={'class': 'form-control'}),
            'duracionPeriodos': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'partida': forms.TextInput(attrs={'class': 'form-control'}),

        }

#Formulario para la edición de Carreras
class editCarrera(forms.ModelForm):
    class Meta:
        model = Carrera

        fields = [
            'idCarrera',
            'nombreCarrera',
            'duracionPeriodos',
            'clasificacion',
            'partida',
            'habilitado',
            'tipo_ciclo',

        ]

        labels = {
            'idCarrera': 'Código de la carrera',
            'nombreCarrera': 'Nombre de la carrera',
            'duracionPeriodos': 'Duración de los períodos en minutos',
            'clasificacion':'Clasificación',
            'partida': 'Partida',
            'habilitado': 'Habilitado',
            'tipo_ciclo': 'Tipo de ciclo académico'

        }

        widgets = {
            'idCarrera': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreCarrera': forms.TextInput(attrs={'class': 'form-control'}),
            'duracionPeriodos': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'partida': forms.TextInput(attrs={'class': 'form-control'}),


        }