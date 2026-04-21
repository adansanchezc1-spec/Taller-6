# Resultados de Pruebas
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Fecha de ejecución**: 2026-04-21  
**Fase PDCO**: CONTROL  
**Skill activa**: 04-testing

## Comando ejecutado
```bash
python -m pytest --cov=aplicacion --cov=dominio --cov=infraestructura --cov=presentacion --cov-branch --cov-report=term
```

## Resumen ejecutivo

| Métrica | Valor | Umbral | Estado |
|---------|-------|--------|--------|
| Tests totales | 16 | - | Informativo |
| Tests pasados | 16 | 100% | Cumple |
| Tests fallidos | 0 | 0 | Cumple |
| Cobertura de líneas | 97% | 80% | Cumple |
| Cobertura de ramas | 92% | 80% | Cumple |
| Tiempo de ejecución | 0.95 s | < 30 s | Cumple |

## Resultado por capa

| Capa | Cobertura reportada |
|------|---------------------|
| Aplicación | 97% |
| Dominio | 95% a 100% según módulo |
| Infraestructura | 95% |
| Presentación | 98% |

## Hallazgos
- No se detectaron fallos funcionales en la suite final.
- La persistencia TXT conserva correctamente los tipos concretos al recargar.
- La consola maneja estados vacíos, validaciones y flujo principal correctamente.

## Conclusión
La solución cumple el objetivo académico del taller y supera el umbral mínimo de calidad definido para la fase CONTROL.

