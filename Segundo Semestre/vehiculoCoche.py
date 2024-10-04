# clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
# set y get de marca
    @property
    def getMarca(self):
        return self.__marca
    def setMarca(self, marca):
        self.__marca = marca
    # get y set de modelo
    @property
    def getModelo(self):
        return self.__modelo
    def setModelo(self, modelo):
        self.__modelo = modelo
        
        
    def descripcion(self):
        return f"{self.__marca} {self.__modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        #llama al constructor de la superclase con super().
        super().__init__(marca, modelo)
        self.__num_puertas = num_puertas
        
    @property
    def getNumPuertas(self):
        return self.__num_puertas
    def setNumPuertas(self, num_puertas):
        self.__num_puertas = num_puertas

    def descripcion(self):
        return f"{super().descripcion()} con {self.__num_puertas} puertas"
    
mi_Coche = Coche("BMW", "Serie 3 G20", 4)
print(mi_Coche.descripcion())