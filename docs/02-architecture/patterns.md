# Patrones y Principios Aplicados
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Fecha**: 2026-04-21  
**Fase PDCO**: PLAN → DEVELOPMENT  
**Skill activa**: 02-architecture

## Patrones GoF y GRASP aplicados

| Patrón | Ubicación | Justificación |
|--------|-----------|---------------|
| Factory Method | `FabricaColegios`, `FabricaAlumnos` | Construye subtipos concretos a partir de un discriminador textual. |
| Repository | `RepositorioInstitucional`, `RepositorioTXT` | Desacopla la lógica de negocio del mecanismo de persistencia. |
| Controller (GRASP) | `ServicioGestionEscolar` | Centraliza la coordinación de los casos de uso. |
| Creator (GRASP) | Factorías y servicio | El sistema crea objetos donde existe la información necesaria. |
| Polymorphism (GRASP) | Jerarquías `Colegio` y `Alumno` | Elimina lógica condicional por tipo durante el cálculo de matrícula. |
| Low Coupling / High Cohesion | Separación por capas | Reduce dependencias innecesarias entre consola, negocio y archivo. |

## Antipatrones detectados y corregidos
- Herencia incorrecta en `tipo_colegio.py`, donde se intentaba extender un módulo en lugar de una clase.
- Acoplamiento entre menú, reglas de negocio y almacenamiento.
- Nombres no alineados con PEP 8 y ausencia de abstracciones de dominio.
- Ausencia de un mecanismo claro para reutilización de código y sustitución de comportamiento.

## Resultado arquitectónico
La solución final deja una jerarquía coherente, extensible y fácil de evaluar, con herencia real, polimorfismo explícito y un repositorio TXT desacoplado.

