
-- UNIVERSIDAD SAN CARLOS DE GUATEMALA
-- FACULTAD DE INGENIERIA 
-- BASE DE DATOS 1
-- CONSULTAS REALIZADAS EN EL MOTOR DE BASE DE DATOS DE POSTGRES

-- Obtenemos todos los datos que tienen el rol de administrador
SELECT usuario.first_name AS "Nombre",  rol.rol AS "Rol"
FROM users_user usuario 
JOIN users_usuariorol roles ON roles."userId_id" = usuario.id
JOIN users_rol rol ON   roles.rolid_id = rol.id;


-- Muestra El nombre del Salon con su respectivo edificio
SELECT e."nombreEdificio", s."nombreSalon" from edificios_edificio e
JOIN edificios_salon s ON s."edificio_id" = e.id;


-- Obteniendo  el nombre de la carrera relacionada con el pensum
SELECT carrera."nombreCarrera" AS " NOMBRE DE LA CARRERA",  pensum."codigo_pensum" AS "CODIGO DE PENSUM"
FROM pensum_carrera carrera
JOIN pensum_pensum pensum ON pensum."carreraId_id" = carrera.id; 


