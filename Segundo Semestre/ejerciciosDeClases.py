class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def __str__(self):
        return f"{self.nombre},{self.edad},{self.ocupacion}"

persona = Persona("David", 21, "Desarrollador")
print(persona)


