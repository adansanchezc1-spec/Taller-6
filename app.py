class app:

    def __init__(self):
        self.colegios = []
    def agregar_colegio(self, colegio):
        self.colegios.append(colegio)
    def mostrar_colegios(self):
        print("Colegios en la aplicación:")
        for colegio in self.colegios:
            print(f"- {colegio.nombre}")
    def mostrar_alumnos_en_colegios(self):
        for colegio in self.colegios:
            colegio.mostrar_alumnos()
    def app_menu(self):
        while True:
            print("\nMenú de la Aplicación:")
            print("1. Agregar Colegio")
            print("2. Mostrar Colegios")
            print("3. Mostrar Alumnos en Colegios")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                nombre_colegio = input("Ingrese el nombre del colegio: ")
                nuevo_colegio = colegio(nombre_colegio)
                self.agregar_colegio(nuevo_colegio)
                print(f"Colegio '{nombre_colegio}' agregado.")
            elif opcion == "2":
                self.mostrar_colegios()
            elif opcion == "3":
                self.mostrar_alumnos_en_colegios()
            elif opcion == "4":
                print("Saliendo de la aplicación.")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")