# Refactoring Log
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Fecha**: 2026-04-21  
**Fase PDCO**: OPERATIONS  
**Skill activa**: 05-maintenance

## Refactorizaciones realizadas

### REF-001: Separación por capas
- **Módulo**: proyecto completo
- **Smell detectado**: mezcla de UI, negocio y datos
- **Técnica aplicada**: Extract Class + Separation of Concerns
- **SOLID corregido**: S - Single Responsibility Principle
- **Resultado**: aparición de capas `dominio`, `aplicacion`, `infraestructura`, `presentacion`

### REF-002: Corrección del modelo de herencia
- **Módulo**: `tipo_colegio.py` y modelo institucional
- **Smell detectado**: herencia sobre módulo y ausencia de subtipos útiles
- **Técnica aplicada**: Replace Conditional/Incorrect Hierarchy with Polymorphism
- **SOLID corregido**: L - Liskov Substitution Principle
- **Resultado**: subclases concretas y sustituibles

### REF-003: Persistencia desacoplada
- **Módulo**: nuevo repositorio TXT
- **Smell detectado**: sistema sin manejo real de archivos
- **Técnica aplicada**: Introduce Repository
- **SOLID corregido**: D - Dependency Inversion Principle
- **Resultado**: el servicio depende de una abstracción de persistencia

### REF-004: Calidad y verificabilidad
- **Módulo**: pruebas automatizadas
- **Smell detectado**: ausencia total de regresión automática
- **Técnica aplicada**: Introduce Test Suite
- **Resultado**: 16 pruebas exitosas con cobertura superior al objetivo

