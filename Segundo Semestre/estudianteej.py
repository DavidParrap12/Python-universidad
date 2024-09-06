class Estudiantes: 
    def __init__(self, nombre):
        self.nombre = nombre
        #[Para listas vacias]
        self.calificaciones = []

    def agregar_calificaciones (self, calificaciones):
        #append significa agregar
        self.calificaciones.append(calificaciones)
        print(f"Calificacion {calificaciones} añadida para {self.nombre}")

    def quitar_calificaciones(self):
        #pop para eliminar uno en especifico
        self.calificaciones.pop(2)
    
        

    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0
        # si tiene self algo if self.calificaciones
        
estudiante = Estudiantes("David Parra")
estudiante.agregar_calificaciones(90)
estudiante.agregar_calificaciones(98)
estudiante.agregar_calificaciones(85)
print(f"Promedio de {estudiante.nombre}: {estudiante.promedio()}")