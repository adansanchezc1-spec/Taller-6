# ADR-001 - Arquitectura por capas con persistencia TXT

## Estado
Aprobado

## Contexto
El taller necesitaba evidenciar principios de POO y modularidad sin introducir complejidad innecesaria. La solución original mezclaba presentación, lógica y modelado.

## Decisión
Adoptar una arquitectura monolítica por capas con:
- Dominio basado en herencia y polimorfismo.
- Servicio de aplicación como coordinador.
- Repositorio TXT como infraestructura.
- Consola desacoplada de la persistencia.

## Consecuencias
- Se mejora la evaluabilidad académica del diseño.
- La solución queda lista para extender nuevos tipos sin reescribir el servicio.
- La persistencia se mantiene simple y visible para fines didácticos.

