# Generated by Django 4.2 on 2023-05-06 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default='2023')),
                ('ciclo_acad', models.CharField(choices=[('Primer Ciclo', 'Primer Ciclo'), ('Segundo Ciclo', 'Segundo Ciclo'), ('Tercer Ciclo', 'Tercer Ciclo'), ('Cuarto Ciclo', 'Cuarto Ciclo'), ('Quinto Ciclo', 'Quinto Ciclo'), ('Sexto Ciclo', 'Sexto Ciclo'), ('Septimo Ciclo', 'Septimo Ciclo'), ('Octavo Ciclo', 'Octavo Ciclo'), ('Noveno Ciclo', 'Noveno Ciclo'), ('Decimo Ciclo', 'Decimo Ciclo')], max_length=100)),
                ('estado', models.CharField(choices=[('Solicitado', 'Solicitado'), ('En proceso', 'En proceso'), ('Aprobado', 'Aprobado'), ('No aprobado', 'No aprobado')], default='En proceso', max_length=255)),
                ('fecha_envio', models.DateField(auto_now_add=True)),
                ('fecha_aprob', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CargaAcademicaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('cargaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargas.carga')),
            ],
        ),
    ]
