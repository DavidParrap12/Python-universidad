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
    

class Electrico(Coche):
    def __init__(self,  marca, modelo, num_puertas,bateria):
        super().__init__(marca, modelo, num_puertas) 
        self.bateria = bateria
    
    def descripcion(self):
        return f"{super().descripcion()} puertas con bateria {self.bateria}"

mi_coche = Electrico("BMW", "Serie 3 G20", 4, 3800)
print(mi_coche.descripcion())