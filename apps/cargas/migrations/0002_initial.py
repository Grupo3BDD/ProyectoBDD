# Generated by Django 4.2 on 2023-05-05 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pensum', '0001_initial'),
        ('cargas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargaacademicadetalle',
            name='cursoid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.curso'),
        ),
    ]
