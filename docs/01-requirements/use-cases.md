# Casos de Uso por Entidad
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Fecha**: 2026-04-21  
**Fase PDCO**: PLAN  
**Skill activa**: 01-requirements

## Entidad: Colegio

### UC-001: Registrar colegio
- **Actor**: Usuario de consola
- **Precondición**: La aplicación está en ejecución.
- **Flujo principal**:
  1. El usuario selecciona la opción de registrar colegio.
  2. El sistema solicita nombre y tipo de colegio.
  3. El sistema crea el subtipo concreto correspondiente.
  4. El sistema confirma el registro.
- **Flujo alternativo**: Si el tipo es inválido, el sistema muestra un error y no registra el colegio.
- **Postcondición**: El colegio queda disponible en memoria.
- **Requerimientos relacionados**: RF-001, RF-006

### UC-004: Consultar colegios
- **Actor**: Usuario de consola
- **Precondición**: La aplicación está en ejecución.
- **Flujo principal**:
  1. El usuario selecciona la opción de ver colegios.
  2. El sistema muestra los colegios registrados con su tipo y cantidad de alumnos.
- **Flujo alternativo**: Si no hay colegios, el sistema informa que no existen registros.
- **Postcondición**: El usuario obtiene una vista del estado actual.
- **Requerimientos relacionados**: RF-004

## Entidad: Alumno

### UC-002: Registrar alumno
- **Actor**: Usuario de consola
- **Precondición**: Existe al menos un colegio registrado.
- **Flujo principal**:
  1. El usuario selecciona la opción de registrar alumno.
  2. El sistema solicita colegio, nombre, edad, grado y perfil.
  3. El sistema crea el subtipo concreto de alumno.
  4. El sistema asocia el alumno al colegio seleccionado.
- **Flujo alternativo**: Si el colegio no existe o algún dato es inválido, el sistema muestra un error.
- **Postcondición**: El alumno queda asociado al colegio.
- **Requerimientos relacionados**: RF-002, RF-006

### UC-003: Calcular matrícula
- **Actor**: Usuario de consola
- **Precondición**: Existe al menos un alumno registrado.
- **Flujo principal**:
  1. El usuario consulta el resumen de matrículas.
  2. El sistema obtiene el valor base desde el tipo de colegio.
  3. El sistema aplica el descuento según el perfil del alumno.
  4. El sistema muestra el valor final.
- **Flujo alternativo**: Si no existen matrículas, el sistema informa que no hay datos para mostrar.
- **Postcondición**: El usuario visualiza la evidencia del polimorfismo.
- **Requerimientos relacionados**: RF-003, RF-004

## Entidad: Persistencia

### UC-005: Guardar y cargar datos
- **Actor**: Usuario de consola
- **Precondición**: La aplicación está en ejecución.
- **Flujo principal**:
  1. El usuario selecciona guardar o cargar.
  2. El sistema serializa o deserializa colegios y alumnos.
  3. El sistema confirma el resultado de la operación.
- **Flujo alternativo**: Si el archivo está corrupto, el sistema lanza un error de integridad.
- **Postcondición**: El estado queda persistido o restaurado.
- **Requerimientos relacionados**: RF-005

