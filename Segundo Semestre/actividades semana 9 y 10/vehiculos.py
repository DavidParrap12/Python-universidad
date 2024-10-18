# Clase base
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
    # Mensaje con los atributos
    def __str__(self):
        return f"La marca del auto es: {self.__marca}, el modelo {self.__modelo}, y el año {self.__anio}"
    
    @property
    # Getters
    def get_Marca(self):
        return self.__marca
    def get_Modelo(self):
        return self.__modelo
    def get_Anio(self):
        return self.__anio

    # Setters
    def set_Marca(self, marca):
        self.__marca = marca
    def set_Modelo(self, modelo):
        self.__modelo = modelo
    def set_Anio(self, anio):
        self.__anio = anio
        
    #Clase heredera de vehiculo 
class VehiculoLujo(Vehiculo):
    def __init__(self, marca, modelo, anio, precio):
        super().__init__(marca, modelo, anio)
        self.__precio = precio
    
    def __str__(self):
        return f"La marca del auto es: {self.__marca}, el modelo {self.__modelo}, y el año {self.__anio}, con un valor de {self.__precio}"
    
    # setter
    def set_Precio(self, precio):
        self.__precio = precio
    @property
    # getter
    def get_Precio(self):
        return self.__precio

# Clase para que el sistema permita
class GestionVehiculos:
    def __init__(self):
        self.vehiculos = []
        self.vehiculosLujos = []
    
    def agregar_Vehiculos(self, vehiculo):
        self.vehiculos.append(vehiculo)
    
    def agregar_VehiculosLujo(self, vehiculosLujo):
        self.vehiculosLujos.append(vehiculosLujo)
        
    def registrar_Vehiculo(self):
        marca = input("Ingrese la marca del vehiculo ")
        modelo = int(input("Ingrese el modelo del vehiculo "))
        anio = int(input("Ingrese el año del vehiculo "))
        vehiculo = Vehiculo(marca, modelo, anio)
        
        self.agregar_Vehiculos(vehiculo)
        print("Vehiculo registrado correctamente")
        
    def mostrar_Vehiculo(self):
        for vehiculo in self.vehiculos:
            print(vehiculo)
    
    def registrar_VehiculoLujo(self):
        marca = input("Ingrese la marca del vehiculo de lujo ")
        modelo = int(input("Ingrese el modelo del vehiculo de lujo "))
        anio = int(input("Ingrese el año del vehiculo de lujo "))
        precio = int(input("Ingrese el precio del vehiculo de lujo: "))
        vehiculoLujo = VehiculoLujo(marca, modelo, anio, precio)
        
        self.agregar_Vehiculos(vehiculoLujo)
        print("Vehiculo registrado correctamente")
        
    def mostrar_VehiculoLujo(self):
        for vehiculoLujo in self.vehiculosLujos:
            print(vehiculoLujo)

    def menu(self):
        while True:
            print("-----BIENVENIDOS AL CONCESIONARIO DE VEHICULOS-----")
            print(""" Selecciona la opcion que deseas usar 
                1. Registrar Vehiculos
                2. Registrar Vehiculos de lujo
                3. Mostrar todos los vehiculos
                4. Mostrar los vehiculos de lujo con su precio
                5. Salir """)
            op = int(input("Marca la opcion que deseas "))
            if op == 1:
                self.registrar_Vehiculo()
            elif op == 2:
                self.registrar_VehiculoLujo()
            elif op == 3:
                self.mostrar_Vehiculo()
            elif op == 4:
                self.mostrar_VehiculoLujo()
            else:
                print("Gracias por usar el concesionario de vehiculos")
                break

gestionSystem = GestionVehiculos()
gestionSystem.menu()
