# Plan de Pruebas
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Versión**: 1.0.0  
**Fecha**: 2026-04-21  
**Fase PDCO**: CONTROL  
**Skill activa**: 04-testing

## Alcance
Pruebas unitarias de dominio, aplicación, infraestructura y presentación por consola.

## Estrategia
- Framework: `pytest 8.4.1`
- Cobertura: `pytest-cov 6.2.1`
- Patrón principal: AAA
- Cobertura objetivo: mínimo 80% en líneas y ramas

## Casos de prueba

| ID | Módulo | Método o flujo | Tipo | RF |
|----|--------|----------------|------|----|
| TC-001 | Dominio | Polimorfismo de colegios | Happy path | RF-001, RF-003 |
| TC-002 | Dominio | Polimorfismo de alumnos | Happy path | RF-002, RF-003 |
| TC-003 | Aplicación | Registro en colegio inexistente | Error | RF-002 |
| TC-004 | Dominio | Validación de datos inválidos | Edge case | RF-006 |
| TC-005 | Infraestructura | Roundtrip TXT con subtipos | Happy path | RF-005 |
| TC-006 | Infraestructura | Alumno huérfano en archivo | Error | RF-005 |
| TC-007 | Presentación | Flujo principal del menú | Happy path | RF-001 a RF-005 |
| TC-008 | Presentación | Estados vacíos de consola | Edge case | RF-004 |
| TC-009 | Presentación | Validaciones estáticas de menú | Error | RF-006 |

## Criterios de aceptación
- [x] Cobertura de líneas mayor o igual a 80%
- [x] Cobertura de ramas mayor o igual a 80%
- [x] 0 pruebas fallidas
- [x] Suite ejecutada en menos de 30 segundos

