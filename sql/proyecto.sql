-- Universida San Carlos De Guatemala
-- Centro Universitario del Norte -CUNOR-
-- Facultad de Ingenieria
-- Juan Carlos Choc Xol 202041390 Ing. Sistemas

-- DROP DATABASE IF EXISTS "ControlDeCargasAcademicasCUNOR";
CREATE DATABASE "ControlDeCargasAcademicasCUNOR";


CREATE TABLE IF NOT EXISTS "Usuario"(
    idUsuario SERIAL PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Profesion VARCHAR(75),
    Acronimo VARCHAR(50),
    CUI CHAR(13) UNIQUE NOT NULL,
    NoPersonal CHAR(8) UNIQUE NOT NULL,
    Telefono CHAR(12) NOT NULL,
    CorreoElectronico VARCHAR(75) UNIQUE,
    Usuario CHAR(8) UNIQUE NOT NULL,
    Password CHAR(8) NOT NULL,
    Estado BOOLEAN DEFAULT TRUE,
    FechaCreacion TIMESTAMP DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS "Rol"(
    idRol SERIAL PRIMARY KEY,
    Rol VARCHAR(50) UNIQUE NOT NULL,
    Descripcion VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS "Area"(
    idArea SERIAL PRIMARY KEY,
    TituloArea VARCHAR(50) UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS "Puesto"(
    idPuesto SERIAL PRIMARY KEY,    
    TipoPuesto VARCHAR(50) UNIQUE NOT NULL,
    Escala CHAR(10),
    Estado BOOLEAN DEFAULT TRUE    
);


CREATE TABLE IF NOT EXISTS "Permiso"(
    idPermiso SERIAL PRIMARY KEY,
    idArea INT NOT NULL,
    TituloPermiso VARCHAR(75) UNIQUE NOT NULL,

    CONSTRAINT fk_area 
        FOREIGN KEY(idArea) 
            REFERENCES "Area"(idArea) 
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Usuario-Rol"(
    idUsuarioRol SERIAL PRIMARY KEY,
    idUsuario INT NOT NULL,
    idRol INT NOT NULL,

    CONSTRAINT fk_usuario
        FOREIGN KEY (idUsuario)
            REFERENCES "Usuario"(idUsuario)
                ON DELETE CASCADE,
    CONSTRAINT fk_rol
        FOREIGN KEY (idRol)
            REFERENCES "Rol"(idRol)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Rol-Permiso"(
    idRolPermiso SERIAL PRIMARY KEY,
    idPermiso INT NOT NULL,
    idRol INT NOT NULL,

    CONSTRAINT fk_permiso
        FOREIGN KEY (idPermiso)
            REFERENCES "Permiso"(idPermiso)
                ON DELETE CASCADE,
    CONSTRAINT fk_rol_permiso
        FOREIGN KEY (idRol)
            REFERENCES "Rol"(idRol)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Docente"(
    idDocente SERIAL PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Profesion VARCHAR(80) NOT NULL,
    Acronimo CHAR(20) NOT NULL,
    CorreoElectronico VARCHAR(75) UNIQUE NOT NULL,
    CUI CHAR(13) UNIQUE NOT NULL,
    Telefono CHAR(12) NOT NULL,
    NoPersonal CHAR(8) UNIQUE NOT NULL,
    Estado BOOLEAN DEFAULT TRUE,
    FechaCreacion TIMESTAMP DEFAULT current_timestamp

);


CREATE TABLE IF NOT EXISTS "Docente-Rol"(
    idDocenteRol SERIAL PRIMARY KEY,
    idDocente INT NOT NULL,
    idRol INT NOT NULL,

    CONSTRAINT fk_docente
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_docente_rol
        FOREIGN KEY (idRol)
            REFERENCES "Rol"(idRol)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "Docente-Puesto"(
    idDocenteRol SERIAL PRIMARY KEY,
    idDocente INT NOT NULL,
    idPuesto INT NOT NULL,

    CONSTRAINT fk_docente_puesto
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_docente_pPuesto
        FOREIGN KEY (idPuesto)
            REFERENCES "Puesto"(idPuesto)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "TipoDeCicloAcademico"(
    idTipoDeCicloAcademico SERIAL PRIMARY KEY,
    TipoDeCicloAcademico VARCHAR(50) UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS "AdministracionDeCarrera"(
    idCarrera SERIAL PRIMARY KEY,
    NombreCarrera VARCHAR(80) UNIQUE NOT NULL,
    DuracionDePeriodosMinutos INT,
    Clasificacion VARCHAR(50),
    Partida VARCHAR(50),
    idTipoDeCicloAcademico INT NOT NULL,
    Estado BOOLEAN DEFAULT TRUE,
    
    CONSTRAINT fk_cicloAcademicoACarrera
        FOREIGN KEY (idTipoDeCicloAcademico)
            REFERENCES "TipoDeCicloAcademico"(idTipoDeCicloAcademico)
                ON DELETE CASCADE

);


CREATE TABLE IF NOT EXISTS "DocenteTitular"(
    idDocenteTitular SERIAL PRIMARY KEY,
    idDocente INT NOT NULL,
    idCarrera INT NOT NULL,
    NoHoras NUMERIC(5,2) NOT NULL,
    Escala VARCHAR(50),

    CONSTRAINT fk_docente_titular
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_carrera_docenteTitular
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "TipoDeDocumento"(
    idTipoDocumento SERIAL PRIMARY KEY,
    TipoDeDocumento VARCHAR(50) UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS "PaisOrigen"(
    idPaisOrigen SERIAL PRIMARY KEY,
    NombrePais VARCHAR(80) UNIQUE NOT NULL
);

CREATE TYPE certificadoNacimiento AS ENUM('Libro','Acta','Folio','NaC');

CREATE TABLE IF NOT EXISTS "Estudiante"(
    idEstudiante SERIAL PRIMARY KEY,
    idTipoDocumento INT,
    NumeroDeDocumentacionIdentificacion CHAR(25) NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Carnet CHAR(20) NOT NULL,
    idPaisOrigen INT NOT NULL,
    Telefono CHAR(12) NOT NULL,
    FechaNacimiento DATE NOT NULL,
    CorreoElectronico VARCHAR(75) UNIQUE,
    CertificadoNacimiento certificadoNacimiento,
    Estado BOOLEAN DEFAULT TRUE,
    FechaCreacion TIMESTAMP DEFAULT current_timestamp,

    CONSTRAINT fk_tipoDocumentoEstudiante
        FOREIGN KEY (idTipoDocumento)
            REFERENCES "TipoDeDocumento"(idTipoDocumento)
                ON DELETE CASCADE,
    CONSTRAINT fk_paisOrigenEstudiante
        FOREIGN KEY (idPaisOrigen)
            REFERENCES "PaisOrigen"(idPaisOrigen)
                ON DELETE CASCADE

);


CREATE TABLE IF NOT EXISTS "Estudiante-Carrera"(
    idEstudianteCarrera SERIAL PRIMARY KEY,
    idEstudiante INT NOT NULL,
    idCarrera INT NOT NULL,

    CONSTRAINT fk_estudianteCarrera
        FOREIGN KEY (idEstudiante)
            REFERENCES "Estudiante"(idEstudiante)
                ON DELETE CASCADE,
    CONSTRAINT fk_carreraEstudiante
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "AdministracionEdificio"(
    idEdificio SERIAL PRIMARY KEY,
    NombreEdificio CHAR(10) UNIQUE NOT NULL,
    CantidadSalones INT NOT NULL,
    FechaCreacion TIMESTAMP DEFAULT current_timestamp,
    Niveles INT,
    Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS "ClasificacionSalon"(
    idClasificacion SERIAL PRIMARY KEY,
    Titulo VARCHAR(75) NOT NULL,
    Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS "AdministracionSalon"(
    idSalon SERIAL PRIMARY KEY,
    NumSalon INT NOT NULL,
    idEdificio INT NOT NULL,
    CapacidadEstudiantes INT NOT NULL,
    Estado BOOLEAN DEFAULT TRUE,
    idClasificacion INT NOT NULL,
    SeudoNombre CHAR(20) UNIQUE,

    CONSTRAINT fk_edificioSalon
        FOREIGN KEY (idEdificio)
            REFERENCES "AdministracionEdificio"(idEdificio)
                ON DELETE CASCADE,
    CONSTRAINT fk_clasificacionSalon
        FOREIGN KEY(idClasificacion)
            REFERENCES "ClasificacionSalon"(idClasificacion)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "Laboratorio"(
    CodigoLaboratorio INT PRIMARY KEY,
    NumHoraSemana INT,
    ValidoSemestre INT
);

CREATE TABLE IF NOT EXISTS "AdministracionCurso"(
    CodigoCurso INT PRIMARY KEY,
    NombreCurso VARCHAR(75) NOT NULL,
    NumHoras INT,
    ConLaboratorio BOOLEAN DEFAULT FALSE,
    CodigoLaboratorio INT,
    Estado BOOLEAN DEFAULT TRUE,
    CONSTRAINT fk_cursoLab
        FOREIGN KEY (CodigoLaboratorio)
            REFERENCES "Laboratorio"(CodigoLaboratorio)
                ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS "CarreraCurso"(
    idCarreraCurso SERIAL PRIMARY KEY,
    idCarrera INT NOT NULL,
    CodigoCurso INT NOT NULL,
    CONSTRAINT fk_carreraCurso
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE,
    CONSTRAINT fk_cursoCarrera
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "CoordinadorCarrera"(
    idCoordinador SERIAL PRIMARY KEY,
    idCarrera INT NOT NULL,
    idUsuario INT,
    idDocente INT,
    FechaCreacion TIMESTAMP DEFAULT current_timestamp,
    CONSTRAINT fk_carreraCoordinador
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE,
    CONSTRAINT fk_usuarioCoordinador
        FOREIGN KEY (idUsuario)
            REFERENCES "Usuario"(idUsuario)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteCoordinador
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "EncargadoArea"(
    idEncargado SERIAL PRIMARY KEY,
    idCarrera INT NOT NULL,
    idUsuario INT,
    idDocente INT,
    fechaCreacion TIMESTAMP DEFAULT current_timestamp,
    CONSTRAINT fk_carreraEncargado
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE,
    CONSTRAINT fk_usuarioEncargado
        FOREIGN KEY (idUsuario)
            REFERENCES "Usuario"(idUsuario)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteEncargad
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "GradoAcademico"(
    idGradoAcademico SERIAL PRIMARY KEY,
    tipoAcademico VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS "Plan"(
    idPlan SERIAL PRIMARY KEY,
    plan VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS "Jornada"(
    idJornada SERIAL PRIMARY KEY,
    jornada VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS "PlanJornada"(
    idPlanJornada SERIAL PRIMARY KEY,
    idPlan INT NOT NULL,
    idJornada INT NOT NULL,
    CONSTRAINT fk_planJornada
        FOREIGN KEY (idPlan)
            REFERENCES "Plan"(idPlan)
                ON DELETE CASCADE,
    CONSTRAINT fk_jornadaPlan
        FOREIGN KEY (idJornada)
            REFERENCES "Jornada"(idJornada)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "CarreraGradoAcademico"(
    idCarreraGradoAcademico SERIAL PRIMARY KEY,
    idCarrera INT NOT NULL,
    idGradoAcademico INT NOT NULL,
    CONSTRAINT fk_carreraGradoAcademico
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE,
    CONSTRAINT fk_gradoAcademicoCarrera
        FOREIGN KEY (idGradoAcademico)
            REFERENCES "GradoAcademico"(idGradoAcademico)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "CarreraPlanJornada"(
    idCarreraPlanJornada SERIAL PRIMARY KEY,
    idCarrera INT NOT NULL,
    idPlanJornada INT NOT NULL,
    CONSTRAINT fk_carreraPlanJornada
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE,
    CONSTRAINT fk_planJornadaCarrera
        FOREIGN KEY (idPlanJornada)
            REFERENCES "PlanJornada"(idPlanJornada)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Pensum"(
    CodigoPensum INT PRIMARY KEY,
    yearInicioVigencia INTEGER NOT NULL,
    ultimaUtilizacion INTEGER,
    fechaCreacion TIMESTAMP DEFAULT current_timestamp,
    descripcionGraduacion VARCHAR(200),
    cantidadCiclos INT NOT NULL,
    valorExamenFinal INT NOT NULL,
    Estado BOOLEAN DEFAULT TRUE,
    idCarrera INT NOT NULL,
    CONSTRAINT fk_carreraPensum
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "Ciclo"(
    idCiclo SERIAL PRIMARY KEY,
    ciclo VARCHAR(75) NOT NULL
);

CREATE TABLE IF NOT EXISTS "SeccionCurso"(
    idSeccionCurso SERIAL PRIMARY KEY,
    Seccion CHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS "DetalleCurso"(
    idDetalleCurso SERIAL PRIMARY KEY,
    CodigoCurso INT NOT NULL,
    NombreCurso VARCHAR(80) NOT NULL,
    Creditos INT NOT NULL,
    Obligatorio BOOLEAN DEFAULT FALSE,
    CreditosRequeridos INT DEFAULT 0,
    NumPeriodosSemana INT,
    CursoAreaTecnica BOOLEAN DEFAULT TRUE,
    idCiclo INT NOT NULL,
    idDocente INT NOT NULL,
    NoPersonal CHAR(8) NOT NULL,
    NombreDocente VARCHAR(75) NOT NULL,
    idSalon INT,
    idSalonLaboratorio INT,
    CodigoPensum INT,
    idSeccionCurso INT NOT NULL,
    CONSTRAINT fk_codigoCursoDetalleCurso
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_cicloDetalleCurso
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteDetalleCurso
        FOREIGN KEY(idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_salonDetalleCurso
        FOREIGN KEY(idSalon)
            REFERENCES "AdministracionSalon"(idSalon)
                ON DELETE CASCADE,
    CONSTRAINT fk_salonLabDetalleCurso
        FOREIGN KEY(idSalonLaboratorio)
            REFERENCES "AdministracionSalon"(idSalon)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoPensum
        FOREIGN KEY(CodigoPensum)
            REFERENCES "Pensum"(CodigoPensum)
                ON DELETE CASCADE,
    CONSTRAINT fk_seccionDetalleCurso
        FOREIGN KEY(idSeccionCurso)
            REFERENCES "SeccionCurso"(idSeccionCurso)
                ON DELETE CASCADE


);


CREATE TABLE IF NOT EXISTS "Prerrequisito"(
    idPrerrequisito SERIAL PRIMARY KEY,
    CodigoCurso INT NOT NULL,
    idDetalleCurso INT NOT NULL,

    CONSTRAINT fk_codigoCursoPrerrequisito
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "DetallePensum"(
    idDetallePensum SERIAL PRIMARY KEY,
    CodigoPensum INT NOT NULL,
    idDetalleCurso INT NOT NULL,
    CodigoCurso INT NOT NULL,
    Creditos INT NOT NULL,
    Obligatorio BOOLEAN NOT NULL,
    CreditosRequeridos INT NOT NULL,
    NombreCurso VARCHAR(80),
    Observaciones VARCHAR(200),
    NumPeriodosSemana INT NOT NULL,
    Estado BOOLEAN DEFAULT TRUE,
    CursoAreaTecnica BOOLEAN DEFAULT TRUE,
    idCiclo INT NOT NULL,
    
    CONSTRAINT fk_codigoPensumDetallePensum
        FOREIGN KEY (CodigoPensum)
            REFERENCES "Pensum"(CodigoPensum)
                ON DELETE CASCADE,
    CONSTRAINT fk_detalleCursoDetallePensum
        FOREIGN KEY (idDetalleCurso)
            REFERENCES "DetalleCurso"(idDetalleCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoCursoDetallePensum
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_cicloDetallePensum
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE
);


CREATE TYPE estado_cargaAcademica AS ENUM('Solicitado','No Aprobado','Aprobado','En Proceso');

CREATE TABLE IF NOT EXISTS "CargaAcademica"(
    idCargaAcademica SERIAL PRIMARY KEY,
    idCiclo INT NOT NULL,
    year INT NOT NULL,
    idEncargado INT NOT NULL,
    Estado estado_cargaAcademica,
    FechaEnvio TIMESTAMP DEFAULT current_timestamp,
    fechaAprobacion TIMESTAMP,

    CONSTRAINT fk_encargadoCargaAcademica
        FOREIGN KEY (idEncargado)
            REFERENCES "EncargadoArea"(idEncargado)
                ON DELETE CASCADE,
    CONSTRAINT fk_cicloCargaAcademica
        FOREIGN KEY(idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "DetalleCargaAcademica"(
    idDetalleCargaAcademica SERIAL PRIMARY KEY,
    idDetalleCurso INT NOT NULL,
    CodigoCurso INT NOT NULL,
    NombreCurso VARCHAR(80) NOT NULL,
    idDocente INT NOT NULL,
    NoPersonal CHAR(8) NOT NULL,
    NombreDocente VARCHAR(50) NOT NULL,
    CodigoPensum INT NOT NULL,
    idCiclo INT NOT NULL,

    CONSTRAINT fk_detalleCursoDetalleCargaAcademica
        FOREIGN KEY (idDetalleCurso)
            REFERENCES "DetalleCurso"(idDetalleCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoCursoDetalleCargaAcademica
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteDetalleCargaAcademica
        FOREIGN KEY(idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoPensumDetalleCargaAcademica
        FOREIGN KEY (CodigoPensum)
            REFERENCES "Pensum"(CodigoPensum)
                ON DELETE CASCADE,
    CONSTRAINT fk_cicloDetalleCargaAcademica
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE
);

CREATE TYPE diaC AS ENUM('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo');

CREATE TABLE IF NOT EXISTS "HorarioCursoLab"(
    idHorarioCurso SERIAL PRIMARY KEY,
    idSeccionCurso INT NOT NULL,
    Dia diaC,
    horaInicio TIME NOT NULL,
    horaFin TIME NOT NULL,
    Periodos INT NOT NULL,
    idSalon INT NOT NULL,
    CodigoCurso INT NOT NULL,
    idDocente INT NOT NULL,
    NombreDocente VARCHAR(70) NOT NULL,
    idCiclo INT NOT NULL,

    CONSTRAINT fk_seccionHorario
        FOREIGN KEY(idSeccionCurso)
            REFERENCES "SeccionCurso"(idSeccionCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_salonHorario
        FOREIGN KEY(idSalon)
            REFERENCES "AdministracionSalon"(idSalon)
                ON DELETE CASCADE,
    CONSTRAINT fk_cursoHorario
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteHorario
        FOREIGN KEY(idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_cicloHorario
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS "HorarioCiclo"(
    idHoraCiclo SERIAL PRIMARY KEY,
    Dia diaC,
    Hora TIME NOT NULL,
    idHorarioCurso INT NOT NULL,    
    idCiclo INT NOT NULL,
    CONSTRAINT fk_horarioCiCloHorarioCurso
        FOREIGN KEY (idHorarioCurso)
            REFERENCES "HorarioCursoLab"(idHorarioCurso)
                ON DELETE CASCADE,
    
    CONSTRAINT fk_cicloHorarioCiclo
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "HorarioCarrera"(
    idHorarioCarrera SERIAL PRIMARY KEY,
    idHorarioCurso INT,
    
    idCarrera INT,
    idHoraCiclo INT NOT NULL,
    CONSTRAINT fk_horarioCarreraHorarioCurso
        FOREIGN KEY (idHorarioCurso)
            REFERENCES "HorarioCursoLab"(idHorarioCurso)
                ON DELETE CASCADE,
    
    CONSTRAINT fk_cicloHorarioCarrera
        FOREIGN KEY (idHoraCiclo)
            REFERENCES "HorarioCiclo"(idHoraCiclo)
                ON DELETE CASCADE,
    CONSTRAINT fk_carreraHorrarioCarrera
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS "Contratacion"(
    idContratacion SERIAL PRIMARY KEY,
    year INT NOT NULL,
    idCiclo INT NOT NULL,
    Inicio DATE NOT NULL,
    Fin DATE NOT NULL,
    CONSTRAINT fk_cicloContratacion
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Plaza"(
    idPlaza SERIAL PRIMARY KEY,
    idContratacion INT NOT NULL,
    idPuesto INT NOT NULL,    
    idDocente INT NOT NULL,
    NoPersonal CHAR(8),
    Nombre VARCHAR(50),
    TotalDehoras INT,
    CONSTRAINT fk_contratacionPlaza
        FOREIGN KEY(idContratacion)
            REFERENCES "Contratacion"(idContratacion)
                ON DELETE CASCADE,
    CONSTRAINT fk_puestoPlaza
        FOREIGN KEY(idPuesto)
            REFERENCES "Puesto"(idPuesto)
                ON DELETE CASCADE,
    CONSTRAINT fk_docentePlaza
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "DetallePlaza"(
    idDetallePlaza SERIAL PRIMARY KEY,
    idPlaza INT NOT NULL,
    CodigoCurso INT NOT NULL,
    NombreCurso VARCHAR(80) NOT NULL,
    HorasCurso INT NOT NULL,
    CONSTRAINT fk_plazaDetallePlaza
        FOREIGN KEY (idPlaza)
            REFERENCES "Plaza"(idPlaza)
                ON DELETE CASCADE,
    CONSTRAINT fk_cursoDetallePlaza
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "HorarioContratacion"(
    idHorarioContratacion SERIAL PRIMARY KEY,
    idPlaza INT NOT NULL,
    idDocente INT NOT NULL,
    NombreDocente VARCHAR(70) NOT NULL,
    Dia diaC,
    HoraInicio TIME NOT NULL,
    HoraFin TIME NOT NULL,

    CONSTRAINT fk_plazaHorarioContratacion
        FOREIGN KEY (idPlaza)
            REFERENCES "Plaza"(idPlaza)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteHorarioContratacion
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "ControlAsignacionCurso"(
    idControlAsignacionCurso SERIAL PRIMARY KEY,
    idCiclo INT NOT NULL,
    idCarrera INT NOT NULL,
    FechaCreacion TIMESTAMP DEFAULT current_timestamp,
    FechaInicio DATE NOT NULL,
    HoraInicio TIME NOT NULL,
    FechaFinalizacion DATE NOT NULL,
    HoraFinalizacion TIME NOT NULL,
    CONSTRAINT fk_cicloControlAsignacionCurso
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE,
    CONSTRAINT fk_carreraControlAsignacionCurso
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "AsignacionCursoLaboratorio"(
    idAsignacionCursoLab SERIAL PRIMARY KEY,
    idEstudiante INT NOT NULL,
    idCarrera INT NOT NULL,
    NombreCompleto VARCHAR(100),
    Carnet CHAR(12) NOT NULL,
    Promedio NUMERIC(10,2),
    Telefono CHAR(12),
    Plan VARCHAR(75),
    FechaAsignacion DATE,

    CONSTRAINT fk_estudianteAsignCursoLab
        FOREIGN KEY (idEstudiante)
            REFERENCES "Estudiante"(idEstudiante)
                ON DELETE CASCADE,
    CONSTRAINT fk_carreraAsignCursoLab
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE
);

CREATE TYPE tipo AS ENUM('Normal','Congelado','Optativo','Obligatorio');
CREATE TABLE IF NOT EXISTS "DetalleAsignacionCurso"(
    idDetalleAsignCurso SERIAL PRIMARY KEY,
    idAsignacionCursoLab INT,
    CodigoCurso INT,
    CodigoPensum INT,
    idCiclo INT NOT NULL,
    NombreCurso VARCHAR(75),
    Tipo tipo,
    idDocente INT,
    Docente VARCHAR(80),
    idSeccionCurso INT,
    Asignado BOOLEAN DEFAULT TRUE,
    idDetalleCurso INT,
    CodigoLaboratorio INT,

    CONSTRAINT fk_asignCursoLabDetalleAsignCurso
        FOREIGN KEY (idAsignacionCursoLab)
            REFERENCES "AsignacionCursoLaboratorio"(idAsignacionCursoLab)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoCursoDetalleAsignCurso
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_pensumDetalleAsignCurso
        FOREIGN KEY (CodigoPensum)
            REFERENCES "Pensum"(CodigoPensum)
                ON DELETE CASCADE,
    CONSTRAINT fk_cicloDetalleAsignCurso
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteDetalleAsignCurso
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_seccionDetalleAsignCurso
        FOREIGN KEY (idSeccionCurso)
            REFERENCES "SeccionCurso"(idSeccionCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_detalleCursoDetalleAsignCurso
        FOREIGN KEY (idDetalleCurso)
            REFERENCES "DetalleCurso"(idDetalleCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoLabDetalleAsignCurso
        FOREIGN KEY (CodigoLaboratorio)
            REFERENCES "Laboratorio"(CodigoLaboratorio)
);

CREATE TABLE IF NOT EXISTS "Equivalencia"(
    idEquivalencia SERIAL PRIMARY KEY,
    CodigoPensum INT,
    idCiclo INT,
    CodigoCurso INT,
    NombreCurso VARCHAR(75),
    Tipo tipo,
    idDocente INT,
    NombreDocente VARCHAR(80),
    idSeccionCurso INT,
    idCarrera INT,
    CodigoLaboratorio INT,
    idDetalleCurso INT,

    CONSTRAINT fk_carreraEquivalencia
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoCursoEquivalencia
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_pensumEquivalencia
        FOREIGN KEY (CodigoPensum)
            REFERENCES "Pensum"(CodigoPensum)
                ON DELETE CASCADE,
    CONSTRAINT fk_cicloEquivalencia
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteEquivalencia
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_seccionEquivalencia
        FOREIGN KEY (idSeccionCurso)
            REFERENCES "SeccionCurso"(idSeccionCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_detalleCursoEquivalencia
        FOREIGN KEY (idDetalleCurso)
            REFERENCES "DetalleCurso"(idDetalleCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoLabEquivalencia
        FOREIGN KEY (CodigoLaboratorio)
            REFERENCES "Laboratorio"(CodigoLaboratorio)


);


CREATE TABLE IF NOT EXISTS "Notas"(
    idNota SERIAL PRIMARY KEY,
    idCarrera INT,
    idAsignacionCursoLab INT,
    idDetalleAsignCurso INT,
    CodigoCurso INT,
    CodigoPensum INT,
    idDocente INT,
    Docente VARCHAR(80),
    idEstudiante INT,
    NombreEstudiante VARCHAR(80),
    CodigoLaboratorio INT,
    NombreCurso VARCHAR(80),

    CONSTRAINT fk_carreraNota
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoCursoNota
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_pensumNota
        FOREIGN KEY (CodigoPensum)
            REFERENCES "Pensum"(CodigoPensum)
                ON DELETE CASCADE,
    CONSTRAINT fk_asignCursoLabNota
        FOREIGN KEY (idAsignacionCursoLab)
            REFERENCES "AsignacionCursoLaboratorio"(idAsignacionCursoLab)
                ON DELETE CASCADE,
    CONSTRAINT fk_docenteNota
        FOREIGN KEY (idDocente)
            REFERENCES "Docente"(idDocente)
                ON DELETE CASCADE,
    CONSTRAINT fk_detalleAsignCursonNota
        FOREIGN KEY (idDetalleAsignCurso)
            REFERENCES "DetalleAsignacionCurso"(idDetalleAsignCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_estudianteNota
        FOREIGN KEY (idEstudiante)
            REFERENCES "Estudiante"(idEstudiante)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoLabEstudiante
        FOREIGN KEY (CodigoLaboratorio)
            REFERENCES "Laboratorio"(CodigoLaboratorio)

    
);

CREATE TABLE IF NOT EXISTS "AdministracionCursoCicloActivo"(
    idAdminCursoCiclo SERIAL PRIMARY KEY,
    idCarrera INT,
    CodigoCurso INT,
    TotalNota NUMERIC(10,2),
    year INT,
    idCiclo INT,

    CONSTRAINT fk_carreraAdministracionCursoCicloActivo
        FOREIGN KEY (idCarrera)
            REFERENCES "AdministracionDeCarrera"(idCarrera)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoCursoAdministracionCursoCicloActivo
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,    
    CONSTRAINT fk_cicloEquivalencia
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE    
);

CREATE TABLE IF NOT EXISTS "DetalleActividadCurso"(
    idDetalleActividadCurso SERIAL PRIMARY KEY,
    idAdminCursoCiclo INT,
    NombreActividad VARCHAR(80),
    CantidadSubActividad INT,
    NotaActividad NUMERIC(10,2),

    CONSTRAINT fk_adminCursoCicloDetalleActividadCurso
        FOREIGN KEY (idAdminCursoCiclo)
            REFERENCES "AdministracionCursoCicloActivo"(idAdminCursoCiclo)
                ON DELETE CASCADE
    
);

CREATE TABLE IF NOT EXISTS "TipoActa"(
    idTipoActa SERIAL PRIMARY KEY,
    TipoCiclo VARCHAR(50)
);

CREATE TYPE solicitud AS ENUM('Aprobada','NoAprobada');

CREATE TABLE IF NOT EXISTS "ActasCiclo"(
    idActa SERIAL PRIMARY KEY,
    idTipoActa INT,
    FechaCreacion TIMESTAMP DEFAULT current_timestamp,
    Solicitud solicitud,

    CONSTRAINT fk_tipoActaCiclo
        FOREIGN KEY (idTipoActa)
            REFERENCES "TipoActa"(idTipoActa)
                ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS "DetalleActa"(
    idDetalleActa SERIAL PRIMARY KEY,
    idActa INT,
    idAdminCursoCiclo INT,
    idEstudiante INT,
    NombreEstudiante VARCHAR(80),
    Carnet VARCHAR(20),
    CodigoCurso INT,
    idNota INT,
    NotaPromocion NUMERIC(10,2),

    CONSTRAINT fk_actaDetalleActa
        FOREIGN KEY (idActa)
            REFERENCES "ActasCiclo"(idActa)
                ON DELETE CASCADE,
    CONSTRAINT fk_adminCursoCicloDetalleActa
        FOREIGN KEY (idAdminCursoCiclo)
            REFERENCES "AdministracionCursoCicloActivo"(idAdminCursoCiclo)
                ON DELETE CASCADE,
    CONSTRAINT fk_estudianteDetalleActa
        FOREIGN KEY (idEstudiante)
            REFERENCES "Estudiante"(idEstudiante)
                ON DELETE CASCADE,
    CONSTRAINT fk_codigoCursoDetalleActa
        FOREIGN KEY (CodigoCurso)
            REFERENCES "AdministracionCurso"(CodigoCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_notaDetalleActa
        FOREIGN KEY (idNota)
            REFERENCES "Notas"(idNota)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "AdministracionLaboratorioCurso"(
    idAdminLabCurso SERIAL PRIMARY KEY,
    year INT,
    idCiclo INT,

    CONSTRAINT fk_cicloAdminLabCurso
        FOREIGN KEY (idCiclo)
            REFERENCES "Ciclo"(idCiclo)
                ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS "DetalleActividadLabCurso"(
    idDetalleActividadLabCurso SERIAL PRIMARY KEY,
    idAdminLabCurso INT,
    NombreActividad VARCHAR(100),
    CantidadSubActividad INT,
    NotaActividad NUMERIC(10,2),

    CONSTRAINT fk_adminLabCursoDetalleActividadLabCurso
        FOREIGN KEY (idAdminLabCurso)
            REFERENCES "AdministracionLaboratorioCurso"(idAdminLabCurso)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "SubActividad"(
    idSubActividad SERIAL PRIMARY KEY,
    idDetalleActividadCurso INT,
    idDetalleActividadLabCurso INT,
    SubActividad VARCHAR(150),
    Descripcion VARCHAR(200),
    ValorNeto NUMERIC(10,2),
    ValorNominal NUMERIC(10,2),
    TotalNota NUMERIC(10,2),

    CONSTRAINT fk_detalleActividadSubActividad
        FOREIGN KEY (idDetalleActividadCurso)
            REFERENCES "DetalleActividadCurso"(idDetalleActividadCurso)
                ON DELETE CASCADE,
    CONSTRAINT fk_detalleActividadLabSubActividad
        FOREIGN KEY (idDetalleActividadLabCurso)
            REFERENCES "DetalleActividadLabCurso"(idDetalleActividadLabCurso)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "DetalleNota"(
    idDetalleNota SERIAL PRIMARY KEY,
    idNota INT NOT NULL,
    PrimerExamen NUMERIC(10,2),
    SegundoExamen NUMERIC(10,2),
    TercerExamen NUMERIC(10,2),
    Zona NUMERIC(10,2),
    ExamenFinal NUMERIC(10,2),
    NotaPromocion NUMERIC(10,2),
    CalificacionFinalEnLetras VARCHAR(150),
    idAdminCursoCiclo INT,
    idAdminLabCurso INT,

    CONSTRAINT fk_notaDetalleNota
        FOREIGN KEY (idNota)
            REFERENCES "Notas"(idNota)
                ON DELETE CASCADE,
    CONSTRAINT fk_adminCursoCicloActivoDetalleNota
        FOREIGN KEY (idAdminCursoCiclo)
            REFERENCES "AdministracionCursoCicloActivo"(idAdminCursoCiclo)
                ON DELETE CASCADE,
    CONSTRAINT fk_asigCursoLabDetalleNota
        FOREIGN KEY (idAdminLabCurso)
            REFERENCES "AdministracionLaboratorioCurso"(idAdminLabCurso)
                ON DELETE CASCADE
);
