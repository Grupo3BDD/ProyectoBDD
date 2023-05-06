# FORMULARIO DE DJANGO
from django import forms

#MODELOS
from .models import *

#Formulario para los Cursos
class cursoForm(forms.ModelForm):
    class Meta:
        model = Curso

        fields = [
            'codigoCurso',
            'nombreCurso',
            'horasSemana',
            'creditos',
            'creditosObligatorios',
            'with_laboratorio',
            'obligatorio',
            'areaTecnica',


        ]

        labels = {

            'codigoCurso':'Código del curso',
            'nombreCurso':'Nombre del curso',
            'horasSemana':'Num. de horas a la semana',
            'creditos':'Créditos',
            'creditosObligatorios':'Créditos necesarios',
            'with_laboratorio':'Con laboratorio:',
            'obligatorio':'Obligatorio',
            'areaTecnica':'Área Técnica',


        }

        widgets = {
            'codigoCurso': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreCurso': forms.TextInput(attrs={'class': 'form-control'}),
            'horasSemana': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'creditos': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'creditosObligatorios': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),

        }

#Formulario para la edición de Cursos
class editCurso(forms.ModelForm):
    class Meta:
        model = Curso

        fields = [
            'codigoCurso',
            'nombreCurso',
            'horasSemana',
            'creditos',
            'creditosObligatorios',
            'with_laboratorio',
            'obligatorio',
            'areaTecnica',
            'habilitado',

        ]

        labels = {

            'codigoCurso':'Código del curso',
            'nombreCurso':'Nombre del curso',
            'horasSemana':'Num. de horas a la semana',
            'creditos':'Créditos',
            'creditosObligatorios':'Créditos necesarios',
            'with_laboratorio':'Con laboratorio:',
            'obligatorio':'Obligatorio',
            'areaTecnica':'Área Técnica',
            'habilitado':'Habilitado',

        }

        widgets = {
            'codigoCurso': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreCurso': forms.TextInput(attrs={'class': 'form-control'}),
            'horasSemana': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'creditos': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'creditosObligatorios': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),

        }


# Formulario para las Carreras
class carreraForm(forms.ModelForm):
    class Meta:
        model = Carrera

        fields = [

            'nombreCarrera',
            'duracionPeriodos',
            'clasificacion',
            'partida',
            'tipo_ciclo',
            'encargado_area',
            'coordinador_acad',


        ]

        labels = {

            'nombreCarrera':'Nombre de la carrera',
            'duracionPeriodos':'Duración de los períodos',
            'clasificacion':'Clasificación',
            'partida':'Partida',
            'tipo_ciclo':'Tipo de ciclo académico',
            'encargado_area':'Encargado de área',
            'coordinador_acad':'Coordinador académico',


        }

        widgets = {
            'nombreCarrera': forms.TextInput(attrs={'class': 'form-control'}),
            'duracionPeriodos': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'partida': forms.TextInput(attrs={'class': 'form-control'}),
            #'tipo_ciclo',
            'encargado_area': forms.Select(attrs={'class': 'form-control select2'}),
            'coordinador_acad': forms.Select(attrs={'class': 'form-control select2'}),

        }


# Formulario para la edición de Carreras
class editCarrera(forms.ModelForm):
    class Meta:
        model = Carrera

        fields = [

            'nombreCarrera',
            'duracionPeriodos',
            'clasificacion',
            'partida',
            'tipo_ciclo',
            'encargado_area',
            'coordinador_acad',
            'habilitado',

        ]

        labels = {

            'nombreCarrera': 'Nombre de la carrera',
            'duracionPeriodos': 'Duración de los períodos',
            'clasificacion': 'Clasificación',
            'partida': 'Partida',
            'tipo_ciclo': 'Tipo de ciclo académico',
            'encargado_area': 'Encargado de área',
            'coordinador_acad': 'Coordinador académico',
            'habilitado': 'Habilitado',

        }

        widgets = {
            'nombreCarrera': forms.TextInput(attrs={'class': 'form-control'}),
            'duracionPeriodos': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'partida': forms.TextInput(attrs={'class': 'form-control'}),
            # 'tipo_ciclo',
            'encargado_area': forms.Select(attrs={'class': 'form-control select2'}),
            'coordinador_acad': forms.Select(attrs={'class': 'form-control select2'}),

        }


class detalleCursoForm(forms.ModelForm):
    class Meta:
        model = DetalleCurso

        fields = [

            'cursoId',
            'facultad_carrera',
        ]


<<<<<<< HEAD
        ]
=======
>>>>>>> 847d593d66ff5d2296dd8c395352614af9585342

#-------------
# Formulario para pensum
class pensumForm(forms.ModelForm):
    class Meta:
        model = Pensum

        fields = [

            'codigo_pensum',
            'year_inicio_vigencia',
            'descripcion',
            'cantidad_ciclo',
            'examen_final',

            'carreraId',

            'carreraId'

        ]

        labels = {


            'cursoId': 'Código del curso',
            'facultad_carrera': 'Carrera',
<<<<<<< HEAD

        


=======
>>>>>>> 847d593d66ff5d2296dd8c395352614af9585342
            'codigo_pensum':'Codigo',
            'year_inicio_vigencia':'Año de inicio de vigencia',
            'descripcion':'Descripcion del proceso de graduacion',
            'cantidad_ciclo':'Cantidad de ciclos',
            'examen_final':'Valor del examen final',
            'carreraId':'Carrera de Facultad',

        }

        widgets = {
            'codigo_pensum': forms.TextInput(attrs={'class': 'form-control'}),
            'year_inicio_vigencia': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_ciclo': forms.TextInput(attrs={'class': 'form-control','type':'number'}),
            'examen_final': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'carreraId':forms.Select(attrs={'class':'form-control'})


        }
<<<<<<< HEAD

# Formulario para la edición de Carreras
=======
# Formulario para la edición de Pensums
>>>>>>> 847d593d66ff5d2296dd8c395352614af9585342

class editPensum(forms.ModelForm):
    class Meta:
        model = Pensum

        fields = [

            'codigo_pensum',
            'year_inicio_vigencia',
            'descripcion',
            'cantidad_ciclo',
            'examen_final',
            'carreraId',
            'estado',

        ]

        labels = {

            'codigo_pensum':'Codigo',
            'year_inicio_vigencia':'Año de inicio de vigencia',
            'descripcion':'Descripcion del proceso de graduacion',
            'cantidad_ciclo':'Cantidad de ciclos',
            'examen_final':'Valor del examen final',
            'carreraId':'Carrera de Facultad',
            'estado':'Habilitado',

        }

        widgets = {
            'codigo_pensum': forms.TextInput(attrs={'class': 'form-control'}),
            'year_inicio_vigencia': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_ciclo': forms.TextInput(attrs={'class': 'form-control','type':'number'}),
            'examen_final': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'carreraId':forms.Select(attrs={'class':'form-control'})


        }
<<<<<<< HEAD
=======

>>>>>>> 847d593d66ff5d2296dd8c395352614af9585342
