#Herencia con Iniciador
#Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        #llama al constructor de la superclase con super().
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def descripcion(self):
        return f"{super().descripcion()} con {self.num_puertas} puertas"
    

class Conductor(Coche):
    def __init__(self,  marca, modelo, num_puertas,nombre, cedula):
        # Intenta con el super llamar todos los atributos de las otras clases
        #Se le coloca self a los atributos propios de la clase
        super().__init__(marca, modelo, num_puertas) 
        self.nombre = nombre
        self.cedula = cedula
    
    def descripcion(self):
        #Llama y une a las descripcion de vehiculo y coche
        return f"{super().descripcion()} puertas, con el conductor {self.nombre}, y numero de cedula {self.cedula}"
#creamos la variable, con los atributos asignados
mi_coche = Conductor("BMW", "Serie 3 G20", 4, "David", 100449325 )
# Llamos la variable, la descripcion realizada en la ultima clase
print(mi_coche.descripcion())