import colegio
import tipo_colegio


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
                tipo_colegio_eleccion =input("Seleccione 1 si el colegio es privado o 2 si el colegio es público")
                if tipo_colegio_eleccion =="1":
                    colegio.tipo = tipo_colegio.col_privado.gestion()
                elif tipo_colegio_eleccion =="2":
                    colegio.tipo = tipo_colegio.col_publico.gestion()
            elif opcion == "2":
                self.mostrar_colegios()
            elif opcion == "3":
                self.mostrar_alumnos_en_colegios()
            elif opcion == "4":
                print("Saliendo de la aplicación.")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")

        def main():
            app_instance = app()
            app_instance.app_menu()