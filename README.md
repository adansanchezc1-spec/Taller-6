Se busca desarrollar un sistema con estándares de ingeniería de software, aplicando buenas prácticas de desarrollo y un diseño adecuado de sistemas, incorporando algunos de los patrones de diseño estudiados en clase. El taller sigue los estándares de diseño e ingeniería de requerimientos definidos en el libro SWEBOK, y fue implementado en Python, cumpliendo las convenciones de estilo establecidas en PEP 8. El sistema integra el uso correcto de arquitecturas de software, los principios SOLID y las heurísticas de usabilidad de Nielsen, y contempla de manera explícita la prevención de antipatrones de diseño. Adicionalmente, el desarrollo contó con el apoyo de un agente de inteligencia artificial creado y estandarizado con buenas prácticas de IA aplicada al desarrollo de software, en el entorno de Visual Studio Code. El código fue sometido a un proceso de refactorización aplicando los criterios de refactorización y optimización definidos en el SWEBOK, y dicha refactorización se llevó a cabo en Codex. Por último, el proyecto contempla un manejo correcto de CI/CD en GitHub, gestionado dentro de la rama asignada por el docente.
Solución propuesta
El sistema se rediseñó como una aplicación modular con:
•	Dominio basado en clases abstractas y subclases concretas.
•	Servicios que orquestan casos de uso.
•	Persistencia TXT desacoplada mediante un repositorio.
•	Documentación completa siguiendo PDCO.
Dominio del problema
Gestión escolar básica y media: colegios, alumnos y matrícula académica.
3. Información del Programa
Propiedad	Valor
Lenguaje	Python 3.13
Paradigma	Programación Orientada a Objetos
Estándares	Clean Code · SOLID · PEP 8
Entidades centrales	Colegio, Alumno, RepositorioInstitucional
Subtipos	ColegioPublico, ColegioPrivado · AlumnoRegular, AlumnoBecado
Persistencia	Archivo TXT estructurado
Arquitectura	Monolítica por capas
Dominio	Gestión escolar

4. Condiciones y Restricciones
ID	Descripción
R-001	El lenguaje de implementación es Python 3.13.
R-002	La persistencia debe realizarse con archivo TXT.
R-003	Toda la documentación debe estar en español.
R-004	La evidencia de herencia y polimorfismo debe ser explícita.

5. Entidades, Atributos y Relaciones
5.1 Entidad: Colegio
Descripción: Institución académica que agrupa alumnos y define una matrícula base.
Atributos:
•	identificador
•	nombre
•	tipo (público/privado)
•	alumnos (lista)
Métodos clave:
•	costo_base_matricula()
•	agregar_alumno(alumno)
•	calcular_matricula(alumno)
5.2 Entidad: Alumno
Descripción: Estudiante asociado a un colegio y a un perfil académico.
Atributos:
•	identificador
•	nombre
•	edad
•	grado
•	perfil (regular/becado)
•	colegio_id
Métodos clave:
•	porcentaje_descuento()
•	calcular_valor_matricula(valor_base)
5.3 Entidad: RepositorioInstitucional
Descripción: Contrato de persistencia para guardar y recuperar colegios y alumnos.
Métodos:
•	existe_fuente()
•	guardar_colegios(colegios)
•	cargar_colegios()
