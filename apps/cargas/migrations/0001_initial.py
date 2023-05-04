# Generated by Django 4.2 on 2023-05-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DecimalField(decimal_places=0, max_digits=5)),
                ('ciclo_acad', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('Solicitado', 'Solicitado'), ('En proceso', 'En proceso'), ('Aprobado', 'Aprobado'), ('No aprobado', 'No aprobado')], default='En proceso', max_length=255)),
                ('fecha_envio', models.DateField()),
                ('fecha_aprob', models.DateField()),
            ],
        ),
    ]