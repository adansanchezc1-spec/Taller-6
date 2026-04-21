# Arquitectura del Sistema
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Fecha**: 2026-04-21  
**Fase PDCO**: PLAN → DEVELOPMENT  
**Skill activa**: 02-architecture

## Estilo arquitectónico seleccionado
Se seleccionó una **arquitectura monolítica por capas** porque el taller es pequeño, requiere alta claridad académica y no necesita complejidad adicional como microservicios o hexagonal completa.

## Capas y responsabilidades

| Capa | Responsabilidad | Componentes |
|------|-----------------|-------------|
| Presentación | Interacción con el usuario por consola | `ConsolaTaller6`, `app.py` |
| Aplicación | Orquestación de casos de uso | `ServicioGestionEscolar` |
| Dominio | Reglas de negocio y polimorfismo | `Colegio`, `Alumno`, factorías |
| Infraestructura | Persistencia en archivo plano | `RepositorioTXT` |

## Interfaces públicas principales
- `Colegio`, `ColegioPublico`, `ColegioPrivado`
- `Alumno`, `AlumnoRegular`, `AlumnoBecado`
- `ServicioGestionEscolar`
- `RepositorioInstitucional`
- `RepositorioTXT`

## Decisiones de diseño
- La herencia se usa únicamente donde hay variación real de comportamiento.
- El polimorfismo reemplaza condicionales por tipo en el cálculo de matrícula.
- La consola no conoce el formato TXT ni la reconstrucción de objetos.
- La persistencia usa discriminadores de tipo para restaurar subclases.

## Validación SOLID por componente

### ServicioGestionEscolar
- **S**: Coordina casos de uso sin mezclar consola ni archivo.
- **O**: Se puede extender con nuevos tipos a través de factorías.
- **L**: Trabaja con `Colegio` y `Alumno` sin depender del subtipo concreto.
- **I**: Consume una interfaz de persistencia pequeña y cohesiva.
- **D**: Depende de `RepositorioInstitucional`, no de `RepositorioTXT`.

### RepositorioTXT
- **S**: Solo resuelve persistencia TXT.
- **O**: Nuevos repositorios pueden implementarse sin tocar el servicio.
- **L**: Sustituye correctamente a `RepositorioInstitucional`.
- **I**: Implementa únicamente el contrato necesario.
- **D**: Su dependencia concreta queda encapsulada en infraestructura.

