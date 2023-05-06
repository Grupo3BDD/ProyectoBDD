import os

def main():
    ruta = [
        'python manage.py dumpdata users.User --format=json --indent=4 > apps/users/fixtures/User.json',
        'python manage.py dumpdata users.Rol --format=json --indent=4 > apps/users/fixtures/Rol.json',
        'python manage.py dumpdata users.Permiso --format=json --indent=4 > apps/users/fixtures/Permiso.json',
        'python manage.py dumpdata users.Puesto --format=json --indent=4 > apps/users/fixtures/Puesto.json',
        'python manage.py dumpdata users.PaisOrigen --format=json --indent=4 > apps/users/fixtures/PaisOrigen.json',
        'python manage.py dumpdata users.TipoDocumento --format=json --indent=4 > apps/users/fixtures/TipoDocumento.json',

        'python manage.py dumpdata users.UsuarioRol --format=json --indent=4 > apps/users/fixtures/UsuarioRol.json',
        'python manage.py dumpdata users.EncargadoArea --format=json --indent=4 > apps/users/fixtures/EncargadoArea.json',
        'python manage.py dumpdata users.CoordinadorAcademico --format=json --indent=4 > apps/users/fixtures/CoordinadorAcademico.json',
        'python manage.py dumpdata users.Estudiante --format=json --indent=4 > apps/users/fixtures/Estudiante.json',
        'python manage.py dumpdata users.Docente --format=json --indent=4 > apps/users/fixtures/Docente.json',

        'python manage.py dumpdata edificios.Edificio --format=json --indent=4 > apps/edificios/fixtures/Edificio.json',
        'python manage.py dumpdata edificios.Clasificacion --format=json --indent=4 > apps/edificios/fixtures/Clasificacion.json',
        'python manage.py dumpdata edificios.Salon --format=json --indent=4 > apps/edificios/fixtures/Salon.json',

        'python manage.py dumpdata cargas.Carga --format=json --indent=4 > apps/cargas/fixtures/Carga.json',
        'python manage.py dumpdata cargas.CargaAcademicaDetalle --format=json --indent=4 > apps/cargas/fixtures/CargaAcademicaDetalle.json',

        'python manage.py dumpdata pensum.GradoAcademico --format=json --indent=4 > apps/pensum/fixtures/GradoAcademico.json',
        'python manage.py dumpdata pensum.Jornada --format=json --indent=4 > apps/pensum/fixtures/Jornada.json',
        'python manage.py dumpdata pensum.TipoJornada --format=json --indent=4 > apps/pensum/fixtures/TipoJornada.json',
        'python manage.py dumpdata pensum.Carrera --format=json --indent=4 > apps/pensum/fixtures/Carrera.json',
        'python manage.py dumpdata pensum.DetalleCarrera --format=json --indent=4 > apps/pensum/fixtures/DetalleCarrera.json',
        'python manage.py dumpdata pensum.Curso --format=json --indent=4 > apps/pensum/fixtures/Curso.json',
        'python manage.py dumpdata pensum.DetalleCurso --format=json --indent=4 > apps/pensum/fixtures/DetalleCurso.json',
        'python manage.py dumpdata pensum.Prerequisito --format=json --indent=4 > apps/pensum/fixtures/Prerequisito.json',
        'python manage.py dumpdata pensum.Laboratorio --format=json --indent=4 > apps/pensum/fixtures/Laboratorio.json',
        'python manage.py dumpdata pensum.Pensum --format=json --indent=4 > apps/pensum/fixtures/Pensum.json',
        'python manage.py dumpdata pensum.DetallePensumCurso --format=json --indent=4 > apps/pensum/fixtures/DetallePensumCurso.json',

    ]

    ruta1=[
        'python manage.py loaddata User.json',
        'python manage.py loaddata Rol.json',
        'python manage.py loaddata Permiso.json',
        'python manage.py loaddata Puesto.json',
        'python manage.py loaddata PaisOrigen.json',
        'python manage.py loaddata TipoDocumento.json',
        'python manage.py loaddata UsuarioRol.json',
        'python manage.py loaddata EncargadoArea.json',
        'python manage.py loaddata CoordinadorAcademico.json',
        'python manage.py loaddata Estudiante.json',
        'python manage.py loaddata Docente.json',

        'python manage.py loaddata Edificio.json',
        'python manage.py loaddata Clasificacion.json',
        'python manage.py loaddata Salon.json',

        'python manage.py loaddata Carga.json',
        'python manage.py loaddata CargaAcademicaDetalle.json',

        'python manage.py loaddata GradoAcademico.json',
        'python manage.py loaddata Jornada.json',
        'python manage.py loaddata TipoJornada.json',
        'python manage.py loaddata Carrera.json',
        'python manage.py loaddata DetalleCarrera.json',
        'python manage.py loaddata Curso.json',
        'python manage.py loaddata DetalleCurso.json',
        'python manage.py loaddata Prerequisito.json',
        'python manage.py loaddata Laboratorio.json',
        'python manage.py loaddata Pensum.json',
        'python manage.py loaddata DetallePensumCurso.json',
    ]
    print('Bienvenidooo')

    decide = int(input(f'''
    1) Crear un respaldo
    2) Cargar Respaldo
    
    '''))

    if decide ==1:
        for crearR in ruta:
            os.system(crearR)
        os.system('cls')
    elif decide ==2:
        for carga in ruta1:
            os.system(carga)
        os.system('cls')
    else:
        print('Dato erroneo...')

if __name__=='__main__':
    main()