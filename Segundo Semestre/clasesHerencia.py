class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo 
    #comodin es propety convierte el metodo en un atributo, solamente para los getters
    @property
    def getMarca(self):
        return self.__marca
        
    
    def setMarca(self,marca):
        self.__marca = marca

    @property
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, modelo):
        self.__modelo = modelo
        
#mostramos get and set de marca
nuevo = Vehiculo("nunu", "uhiaus")
print(nuevo.getMarca)
nuevo.setMarca("nana")
print(nuevo.getMarca)

#mostramos get and set de modelo
print(nuevo.getModelo)
nuevo.setModelo("urus")
print(nuevo.getModelo)