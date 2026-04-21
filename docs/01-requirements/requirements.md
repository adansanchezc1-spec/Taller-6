# Especificación de Requerimientos de Software
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Versión**: 1.0.0  
**Fecha**: 2026-04-21  
**Fase PDCO**: PLAN  
**Skill activa**: 01-requirements  
**Estándar de referencia**: IEEE 830 / ISO 29148

## Definición del problema

### ¿Qué problema resuelve?
El taller original no permitía evidenciar correctamente herencia, reutilización de código, polimorfismo, modularidad ni manejo de archivos. Además, mezclaba la lógica de negocio con la interacción por consola y presentaba errores de modelado en la jerarquía de colegios.

### ¿Cómo lo resuelve?
Se rediseñó como una aplicación de consola modular, con una capa de dominio basada en clases abstractas y subclases concretas, una capa de aplicación con servicios, persistencia en archivo TXT y documentación completa por fases PDCO.

### Dominio del problema
Educación básica y media, específicamente la gestión de colegios, alumnos y matrícula académica.

### Stakeholders
| Rol | Interés | Nivel de influencia |
|-----|---------|---------------------|
| Estudiante desarrollador | Entregar un taller correcto y documentado | Alto |
| Docente evaluador | Ver evidencia de POO, modularidad y archivos | Alto |
| Usuario final de consola | Registrar y consultar información escolar | Medio |

## Requerimientos funcionales

| ID | Descripción | Prioridad | Entidad | UC |
|----|-------------|-----------|---------|----|
| RF-001 | El sistema debe registrar colegios públicos y privados. | Alta | Colegio | UC-001 |
| RF-002 | El sistema debe registrar alumnos regulares y becados asociados a un colegio. | Alta | Alumno | UC-002 |
| RF-003 | El sistema debe calcular el valor de matrícula usando polimorfismo entre tipo de colegio y perfil de alumno. | Alta | Colegio, Alumno | UC-003 |
| RF-004 | El sistema debe listar colegios, alumnos por colegio y resumen de matrículas. | Alta | Colegio, Alumno | UC-004 |
| RF-005 | El sistema debe guardar y cargar la información en un archivo TXT estructurado. | Alta | Repositorio | UC-005 |
| RF-006 | El sistema debe validar entradas inválidas y mostrar mensajes claros en español. | Media | Sistema | UC-001, UC-002 |

## Requerimientos no funcionales

| ID | Tipo | Descripción | Métrica |
|----|------|-------------|---------|
| RNF-001 | Mantenibilidad | El sistema debe separar presentación, aplicación, dominio e infraestructura. | 4 capas definidas |
| RNF-002 | Calidad | El código Python debe seguir PEP 8. | 0 errores de compilación |
| RNF-003 | Persistencia | La información debe almacenarse en texto plano con formato legible. | Archivo `data/taller6.txt` |
| RNF-004 | Usabilidad | Todos los mensajes visibles deben estar en español. | 100% de textos en español |
| RNF-005 | Verificabilidad | La solución debe tener pruebas automatizadas con cobertura mínima de 80%. | >= 80% líneas y ramas |
| RNF-006 | Documentación | Cada fase PDCO debe dejar artefactos Markdown y trazabilidad JSON. | `docs/` + `metadata.json` |

## Restricciones

| ID | Descripción |
|----|-------------|
| R-001 | El lenguaje de implementación es Python 3.13. |
| R-002 | La persistencia debe realizarse con archivo TXT, no con base de datos. |
| R-003 | La documentación del proyecto debe quedar en español. |
| R-004 | La evidencia de herencia y polimorfismo debe ser explícita y evaluable. |

## Glosario

| Término | Definición |
|---------|-----------|
| Colegio público | Colegio con matrícula base subsidiada. |
| Colegio privado | Colegio con matrícula base privada. |
| Alumno regular | Alumno sin descuento en matrícula. |
| Alumno becado | Alumno con descuento del 50% sobre la matrícula base. |
| Repositorio | Componente encargado de persistir y recuperar datos. |

