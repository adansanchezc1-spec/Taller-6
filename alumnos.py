class alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"{self.nombre}, Edad: {self.edad}"  
    def __repr__(self):
        return self.__str__()  
    def alumno_menu(self):
        print("Menú de Alumnos:")
        print("1. Agregar Alumno")
        print("2. Mostrar Alumnos")
        print("3. Salir")