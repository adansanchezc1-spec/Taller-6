# Documentación de Módulos y Componentes
**Proyecto**: Taller 6 - Gestión Escolar con POO  
**Fecha**: 2026-04-21  
**Fase PDCO**: DEVELOPMENT  
**Skill activa**: 03-development

## Punto de entrada
- `app.py`: instancia el repositorio, el servicio y la consola.

## Dominio
- `Colegio`: contrato abstracto para colegios.
- `ColegioPublico`: retorna tipo `PUBLICO` y matrícula base `50000`.
- `ColegioPrivado`: retorna tipo `PRIVADO` y matrícula base `150000`.
- `Alumno`: contrato abstracto para alumnos.
- `AlumnoRegular`: perfil `REGULAR`, descuento `0%`.
- `AlumnoBecado`: perfil `BECADO`, descuento `50%`.
- `FabricaColegios`: crea subtipos de colegio por discriminador.
- `FabricaAlumnos`: crea subtipos de alumno por discriminador.

## Aplicación
- `ServicioGestionEscolar.registrar_colegio(nombre, tipo)`: registra un colegio nuevo.
- `ServicioGestionEscolar.registrar_alumno(colegio_id, nombre, edad, grado, perfil)`: asocia un alumno a un colegio existente.
- `ServicioGestionEscolar.obtener_resumen_matriculas()`: produce la vista polimórfica de matrícula.
- `ServicioGestionEscolar.guardar_datos()` y `cargar_datos()`: coordinan persistencia.

## Infraestructura
- `RepositorioInstitucional`: contrato abstracto de persistencia.
- `RepositorioTXT`: implementación en texto plano con integridad referencial básica.

## Presentación
- `ConsolaTaller6.inicializar()`: carga datos si existe un archivo previo.
- `ConsolaTaller6.ejecutar()`: lanza el menú principal y despacha cada opción.

## Ejecución local
```bash
python app.py
```

## Ejecución de pruebas
```bash
python -m pytest --cov=aplicacion --cov=dominio --cov=infraestructura --cov=presentacion --cov-branch --cov-report=term
```

