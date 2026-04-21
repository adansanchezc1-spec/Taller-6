# Bitácora de Desarrollo
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Fecha**: 2026-04-21  
**Fase PDCO**: DEVELOPMENT  
**Skill activa**: 03-development

## Registro de implementación

### DEV-001 - Reestructuración inicial
- Se reorganizó el proyecto en capas: `dominio`, `aplicacion`, `infraestructura` y `presentacion`.
- Se mantuvo `app.py` como punto de entrada liviano.

### DEV-002 - Modelo orientado a objetos
- Se implementó `Colegio` como clase abstracta con las subclases `ColegioPublico` y `ColegioPrivado`.
- Se implementó `Alumno` como clase abstracta con las subclases `AlumnoRegular` y `AlumnoBecado`.
- Se centralizó la validación de datos en los modelos del dominio.

### DEV-003 - Casos de uso
- Se creó `ServicioGestionEscolar` para registrar colegios, registrar alumnos, listar información y coordinar la persistencia.
- Se agregó generación de identificadores secuenciales `COL-XXX` y `ALU-XXX`.

### DEV-004 - Persistencia en archivo
- Se implementó `RepositorioTXT` con dos secciones: `[COLEGIOS]` y `[ALUMNOS]`.
- Se usó `Factory Method` para reconstruir subtipos desde el discriminador del archivo.

### DEV-005 - Interfaz de consola
- Se añadió un menú principal en español con opciones de alta, consulta, guardado y carga.
- Se agregaron mensajes claros para estados vacíos y errores de validación.

### DEV-006 - Calidad y pruebas
- Se incorporó `pytest` y `pytest-cov` como dependencias de desarrollo.
- Se automatizaron pruebas de dominio, aplicación, infraestructura y presentación.

