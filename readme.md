# Nexus - Project management software
### 🚧 En construcción 🚧
<br>

📼 Video de demostración:
https://youtu.be/caPNqiQ5PRc

## Nexus es una aplicación web para la gestión de proyectos de software, y la administración de tickets en equipos de desarrollo.

Esta aplicación les permite a los usuarios crear proyectos, y gestionar tickets utilizando una <b>metodología de desarrollo ágil</b> similar a Scrum o Kanban, en donde se tiene 
un backlog de tickets o tareas a realizar (<b>tickets nuevos</b>), se eligen cuáles son las tareas que se van a desarrollar en este sprint (<b>tickets en desarrollo</b>), y luego esos tickets se archivan como <b>tickets cerrados.</b>

<br>

#### Tecnologías utilizadas:
- HTML, CSS, Javascript.
- Django.
- PostgreSQL (producción), MySQLite (desarrollo).
- Implementado con Docker en un VPS.

<br>

#### Características de Nexus:
### - Crear proyectos con logos, descripciones, y archivos importantes (como documentación, listado de requerimientos del software, etc.).

### - Gestión de tickets que corresponden a un proyecto:
- Al crear un nuevo ticket, se le asignará el estado NUEVO.
- Un desarrollador puede seleccionar un ticket para asignárselo a si mismo, cambiando el estado a ASIGNADO.
- Cuando el desarrollador comienza a resolver ese ticket, el estado del mismo cambiará a EN DESARROLLO.
- Una vez que el ticket se haya resuelto, se cambiará el estado a CERRADO, y será archivado.

### - Autenticación y autorización de usuarios con distintos roles:

<b>Project Manager:</b>
- Puede ver todos los proyectos que están cargados en el sistema, pero sólo puede editar los proyectos de los que forma parte.
- Puede asignar desarrolladores a sus proyectos, gestionar tickets, y realizar comentarios.
- Puede asignar un ticket a otro desarrollador.

<b>Desarrollador:</b>
- Tiene acceso al listado de tickets del proyecto, pudiendo seleccionar tickets para comenzar el desarrollo del mismo.
- Sólo puede trabajar sobre los tickets de los proyectos en los que él está asignado.
- Sólo puede asignarse tickets a sí mismo.
- Puede crear comentarios en tickets.

<b>Tester / QA:</b>
- Tiene la habilidad de crear tickets, y crear comentarios en los tickets creados por él.

<b>Admin:</b>
- Tiene la habilidad de gestionar los roles de los otros usuarios.
- Además, es el único que puede crear y borrar proyectos.
<br>

### - Carga de archivos relevantes para cada ticket (ej: screenshots de un bug)

### - Cada ticket tiene su propia sección de comentarios, para facilitar la comunicación entre desarrolladores y testers / QA.
