"""Interfaz de consola del Taller 6."""

from __future__ import annotations

from aplicacion.servicio_gestion_escolar import ServicioGestionEscolar


class ConsolaTaller6:
    """Orquesta la interacción con el usuario por consola."""

    def __init__(self, servicio: ServicioGestionEscolar) -> None:
        self._servicio = servicio

    def inicializar(self) -> None:
        """Carga datos si existe un archivo persistido."""
        if self._servicio.cargar_si_existe():
            print("Se cargaron los datos guardados desde el archivo TXT.")
            return
        print("No se encontraron datos previos. Se iniciará una sesión nueva.")

    def ejecutar(self) -> None:
        """Muestra el menú principal hasta que el usuario decida salir."""
        while True:
            self._mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()
            try:
                if opcion == "1":
                    self._registrar_colegio()
                elif opcion == "2":
                    self._registrar_alumno()
                elif opcion == "3":
                    self._mostrar_colegios()
                elif opcion == "4":
                    self._mostrar_alumnos_por_colegio()
                elif opcion == "5":
                    self._mostrar_resumen_matriculas()
                elif opcion == "6":
                    self._guardar_datos()
                elif opcion == "7":
                    self._cargar_datos()
                elif opcion == "8":
                    print("Saliendo de la aplicación.")
                    break
                else:
                    print("La opción seleccionada no es válida.")
            except ValueError as error:
                print(f"Error: {error}")

    @staticmethod
    def _mostrar_menu() -> None:
        print("\n===== Taller 6 - Gestión Escolar =====")
        print("1. Registrar colegio")
        print("2. Registrar alumno")
        print("3. Ver colegios")
        print("4. Ver alumnos por colegio")
        print("5. Ver resumen de matrículas")
        print("6. Guardar datos")
        print("7. Cargar datos")
        print("8. Salir")

    def _registrar_colegio(self) -> None:
        nombre = input("Ingrese el nombre del colegio: ").strip()
        print("Tipos de colegio disponibles:")
        print("1. Público")
        print("2. Privado")
        tipo = self._mapear_tipo_colegio(input("Seleccione el tipo: ").strip())
        colegio = self._servicio.registrar_colegio(nombre=nombre, tipo=tipo)
        print(f"Colegio registrado correctamente: {colegio.resumen()}")

    def _registrar_alumno(self) -> None:
        colegios = self._servicio.listar_colegios()
        if not colegios:
            print("Debe registrar al menos un colegio antes de crear alumnos.")
            return

        self._mostrar_colegios()
        colegio_id = input("Ingrese el identificador del colegio: ").strip().upper()
        nombre = input("Ingrese el nombre del alumno: ").strip()
        edad = self._leer_entero_positivo("Ingrese la edad del alumno: ")
        grado = input("Ingrese el grado del alumno: ").strip()
        print("Perfiles de alumno disponibles:")
        print("1. Regular")
        print("2. Becado")
        perfil = self._mapear_perfil_alumno(input("Seleccione el perfil: ").strip())
        alumno = self._servicio.registrar_alumno(
            colegio_id=colegio_id,
            nombre=nombre,
            edad=edad,
            grado=grado,
            perfil=perfil,
        )
        print(
            "Alumno registrado correctamente: "
            f"{alumno.identificador} - {alumno.nombre} ({alumno.perfil()})"
        )

    def _mostrar_colegios(self) -> None:
        colegios = self._servicio.listar_colegios()
        if not colegios:
            print("No hay colegios registrados.")
            return
        print("\nColegios registrados:")
        for colegio in colegios:
            print(f"- {colegio.resumen()}")

    def _mostrar_alumnos_por_colegio(self) -> None:
        colegios = self._servicio.listar_colegios()
        if not colegios:
            print("No hay colegios registrados.")
            return

        self._mostrar_colegios()
        colegio_id = input("Ingrese el identificador del colegio a consultar: ").strip()
        colegio = self._servicio.obtener_colegio(colegio_id.upper())
        if not colegio.alumnos:
            print("El colegio seleccionado todavía no tiene alumnos registrados.")
            return

        print(f"\nAlumnos del colegio {colegio.nombre}:")
        valor_base = colegio.costo_base_matricula()
        for alumno in colegio.alumnos:
            print(f"- {alumno.descripcion(valor_base)}")

    def _mostrar_resumen_matriculas(self) -> None:
        resumen = self._servicio.obtener_resumen_matriculas()
        if not resumen:
            print("No existen matrículas para mostrar.")
            return

        print("\nResumen de matrículas:")
        for registro in resumen:
            print(
                f"- {registro['colegio_nombre']} ({registro['colegio_tipo']}) | "
                f"{registro['alumno_nombre']} [{registro['perfil']}] | "
                f"Base: ${registro['valor_base']} | Final: ${registro['valor_final']}"
            )

    def _guardar_datos(self) -> None:
        self._servicio.guardar_datos()
        print("Los datos fueron guardados correctamente en el archivo TXT.")

    def _cargar_datos(self) -> None:
        colegios = self._servicio.cargar_datos()
        print(f"Se cargaron {len(colegios)} colegios desde el archivo TXT.")

    @staticmethod
    def _mapear_tipo_colegio(opcion: str) -> str:
        opciones = {"1": "PUBLICO", "2": "PRIVADO"}
        if opcion not in opciones:
            raise ValueError("Debe seleccionar 1 para público o 2 para privado.")
        return opciones[opcion]

    @staticmethod
    def _mapear_perfil_alumno(opcion: str) -> str:
        opciones = {"1": "REGULAR", "2": "BECADO"}
        if opcion not in opciones:
            raise ValueError("Debe seleccionar 1 para regular o 2 para becado.")
        return opciones[opcion]

    @staticmethod
    def _leer_entero_positivo(mensaje: str) -> int:
        valor = int(input(mensaje).strip())
        if valor <= 0:
            raise ValueError("Debe ingresar un número entero positivo.")
        return valor

