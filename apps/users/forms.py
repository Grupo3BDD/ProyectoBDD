
# FORMULARIO DE DJANGO
from django import forms

# MODELOS
from .models import User

# LIBRERIA QUE SE ENCARGA DE CREAR USUARIOS
from django.contrib.auth.forms import UserCreationForm


### -- FORMULARIO PARA CREAR Y REGISTRAR USUARIOS--#
class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        required=True
    )

    email = forms.EmailField(
        label="Correo Electronico",
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}),
        required=True

    )

    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required=True,


    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required=True,


    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'username'

        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

        }


### -- FORMULARIO PARA CAMBIAR LA CONTRASEÑA --###
class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='NUEVA CONTRASEÑA: ',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required=True,


    )
    password2 = forms.CharField(
        label='CONFIRMAR CONTRASEÑA: ',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required=True,


    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Contraseña no coinciden')
        return password2


class CreateUserForm(UserCreationForm):
    USER_TYPE = [
            ('Usuario', 'Usuario'),
        ('Docente', 'Docente'),
        ('Estudiante', 'Estudiante')
    ]
    certificado_nacimiento = [
        ('Libro', 'Libro'),
        ('Acta', 'Acta'),
        ('Folio', 'Folio')
    ]

    tipo_usuario = forms.ChoiceField(
        choices=USER_TYPE,
        required = False,
        label='Tipo de Usuario',
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    
    certificado_nacimiento = forms.ChoiceField(
        choices=certificado_nacimiento,
        required = False,
        label='Tipo de Certificado de Nacimiento',
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        required=True
    )

    email = forms.EmailField(
        label="Correo Electronico",
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}),
        required=True

    )

    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required=True,


    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required=True,


    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'tipo_usuario',
            'profesion',
            'acronimo',
            'tipoDocumento',
            'noDocumentoIdentificacion',
            'certificado_nacimiento',
            'telefono',
            'pais_origen',
            'imagen',
            
            

        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'profesion': 'Profesion',
            'acronimo': 'Acronimo de la Profesion',
            'tipoDocumento': 'Tipo de Documento de Identificacion',
            'noDocumentoIdentificacion': 'Numero de Documento de Identificacion',
            
            'telefono': 'Telefono',
            'pais_origen': 'Pais de Origen',
            'imagen': 'Imagen',
            
            
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','name':'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','name':'last_name'}),
            
            'profesion': forms.TextInput(attrs={'class': 'form-control','name':'profesion'}),
            'acronimo': forms.TextInput(attrs={'class': 'form-control','name':'profesion'}),
            'tipoDocumento': forms.Select(attrs={'class': 'form-control','name':'profesion'}),
            'noDocumentoIdentificacion': forms.TextInput(attrs={'class': 'form-control','name':'profesion'}),
            
            'telefono': forms.TextInput(attrs={'class': 'form-control','name':'profesion'}),
            'pais_origen': forms.Select(attrs={'class': 'form-control','name':'profesion'}),
            'imagen':forms.FileInput(attrs={'type':'checkbox', 'name':'image', 'type':'file', 'accept':'image', 'class':'form-control'}),
            

        }