# Generated by Django 4.2 on 2023-05-06 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cargas', '0001_initial'),
        ('pensum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargaacademicadetalle',
            name='cursoid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.curso'),
        ),
    ]
