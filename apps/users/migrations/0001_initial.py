# Generated by Django 4.2 on 2023-04-18 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaisOrigen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=95)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPuesto', models.CharField(max_length=100, unique=True)),
                ('escala', models.CharField(max_length=8, unique=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=75, unique=True)),
                ('Descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocumento', models.CharField(max_length=80)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_usuario', models.CharField(blank=True, choices=[('Usuario', 'Usuario'), ('Docente', 'Docente'), ('Estudiante', 'Estudiante')], default='Usuario', max_length=100, null=True)),
                ('profesion', models.CharField(blank=True, max_length=75, null=True)),
                ('acronimo', models.CharField(blank=True, max_length=75, null=True)),
                ('noDocumentoIdentificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('noPersonal', models.CharField(max_length=9, unique=True)),
                ('certificado_nacimiento', models.CharField(blank=True, choices=[('Libro', 'Libro'), ('Acta', 'Acta'), ('Folio', 'Folio')], max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('pais_origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.paisorigen')),
                ('puesto', models.ManyToManyField(blank=True, to='users.puesto')),
                ('rol', models.ManyToManyField(blank=True, to='users.rol')),
                ('tipoDocumento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.tipodocumento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
