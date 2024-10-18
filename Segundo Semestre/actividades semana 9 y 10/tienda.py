class Producto:
    def __init__(self, nombre, precio, cantidadInventario):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidadInventario = cantidadInventario
    
    def __str__(self):
        return f"Nombre del producto es {self.__nombre}, con un valor de {self.__precio} cantidad {self.__cantidadInventario}"
    
    property
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    def getInventario(self):
        return self.__cantidadInventario

    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPrecio(self, precio):
        self.__precio = precio
    def setCantidadInventario(self, cantidadInventario):
        self.__cantidadInventario = cantidadInventario
    
class ProductoPerecedero:
    def __init__(self, nombre, precio, cantidadInventario, fechaCaducidad):
        super().__init__(nombre, precio, cantidadInventario)
        self.__fechaCaducidad = fechaCaducidad
    
    def __str__(self):
        return f"Nombre del producto es {self.__nombre}, con un valor de {self.__precio} cantidad {self.__cantidadInventario} con caducidad de {self.__fechaCaducidad}"
        