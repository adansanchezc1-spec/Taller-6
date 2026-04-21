class colegio:
    def __init__(self, nombre,tipo):
        self.nombre = nombre
        self.alumnos = []
        self.tipo =tipo 

    def __str__(self):
        return f"Colegio: {self.nombre}, Alumnos: {len(self.alumnos)}"

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_alumnos(self):
        print(f"Alumnos en el colegio {self.nombre}:")
        for alumno in self.alumnos:
            print(f"- {alumno.nombre}, Edad: {alumno.edad}")
            