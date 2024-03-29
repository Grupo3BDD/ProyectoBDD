# Generated by Django 4.2 on 2023-05-06 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCarrera', models.CharField(max_length=60, unique=True)),
                ('duracionPeriodos', models.IntegerField(blank=True, null=True)),
                ('clasificacion', models.CharField(max_length=20, null=True)),
                ('partida', models.CharField(max_length=20, null=True)),
                ('tipo_ciclo', models.CharField(choices=[('Trimestral', 'Trimestral'), ('Anual', 'Anual'), ('Bimestral', 'Bimestral'), ('Cuatrimestre', 'Cuatrimestre'), ('Semestral', 'Semestral')], default='Semestral', max_length=100)),
                ('habilitado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoCurso', models.CharField(max_length=60, unique=True)),
                ('nombreCurso', models.CharField(max_length=80, unique=True)),
                ('horasSemana', models.IntegerField(blank=True, null=True)),
                ('creditos', models.IntegerField(blank=True, null=True)),
                ('creditosObligatorios', models.IntegerField(blank=True, null=True)),
                ('with_laboratorio', models.BooleanField(default=False)),
                ('obligatorio', models.BooleanField(default=True)),
                ('areaTecnica', models.BooleanField(default=True)),
                ('habilitado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('cursoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.curso')),
                ('facultad_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='GradoAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado_academico', models.CharField(max_length=75)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='TipoJornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion_jorn', models.CharField(max_length=75)),
                ('plan_t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.jornada')),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.detallecurso')),
                ('prerrequisito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_pensum', models.CharField(max_length=60, unique=True)),
                ('year_inicio_vigencia', models.IntegerField(default='2023')),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad_ciclo', models.IntegerField()),
                ('examen_final', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('carreraId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoLaboratorio', models.CharField(max_length=60, unique=True)),
                ('horas_lab_sem', models.IntegerField(blank=True, null=True)),
                ('valido_semestres', models.IntegerField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('codeCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.curso')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePensumCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipociclo', models.CharField(choices=[('Primer Ciclo', 'Primer Ciclo'), ('Segundo Ciclo', 'Segundo Ciclo'), ('Tercer Ciclo', 'Tercer Ciclo'), ('Cuarto Ciclo', 'Cuarto Ciclo'), ('Quinto Ciclo', 'Quinto Ciclo'), ('Sexto Ciclo', 'Sexto Ciclo'), ('Septimo Ciclo', 'Septimo Ciclo'), ('Octavo Ciclo', 'Octavo Ciclo'), ('Noveno Ciclo', 'Noveno Ciclo'), ('Decimo Ciclo', 'Decimo Ciclo')], max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('codigo_pensum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.pensum')),
                ('cursoid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.curso')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCarrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('carreraId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.carrera')),
                ('grado_acad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pensum.gradoacademico')),
                ('type_jornada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pensum.tipojornada')),
            ],
        ),
    ]
