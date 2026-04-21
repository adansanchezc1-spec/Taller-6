# Changelog
Formato basado en Keep a Changelog.

## [1.0.0] - 2026-04-21

### Added
- Arquitectura por capas para el Taller 6.
- Jerarquía de colegios públicos y privados.
- Jerarquía de alumnos regulares y becados.
- Servicio de gestión escolar desacoplado.
- Persistencia en archivo TXT con secciones `[COLEGIOS]` y `[ALUMNOS]`.
- Suite de pruebas automatizadas con `pytest`.
- Documentación PDCO completa en español.

### Changed
- `app.py` pasó de contener lógica mezclada a ser un entrypoint liviano.
- Los archivos `colegio.py`, `alumnos.py` y `tipo_colegio.py` quedaron como compatibilidad con el nuevo diseño.

### Fixed
- Error de herencia inválida en `tipo_colegio.py`.
- Inconsistencias de firma en la creación de colegios.
- Falta de modularidad y ausencia de persistencia real.

