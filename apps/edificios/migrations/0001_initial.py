# Generated by Django 4.2 on 2023-05-06 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_salon_uso', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEdificio', models.CharField(max_length=60)),
                ('cantidadSalones', models.IntegerField(blank=True, null=True)),
                ('niveles', models.IntegerField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSalon', models.CharField(max_length=60)),
                ('capacidadEstudiantes', models.IntegerField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edificios.clasificacion')),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edificios.edificio')),
            ],
        ),
    ]
