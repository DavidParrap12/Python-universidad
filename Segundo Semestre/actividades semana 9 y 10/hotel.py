class Habitacion:
    def __init__(self, numHabitaciones, capacidad):
        self.__numHabitaciones = numHabitaciones
        self.__capacidad = capacidad
    
    def __str__(self):
        return f"Numero de habitaciones son: {self.__numHabitaciones}, con capacidad para {self.__capacidad}"
    
    # Getter
    def getNumHabitaciones(self):
        return self.__numHabitaciones
    def getCapacidad(self):
        return self.__capacidad
    
    # Setter
    def setNumHabitaciones(self, numHabitaciones):
        self.__numHabitaciones = numHabitaciones
    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad

class HabitacionVip(Habitacion):
    def __init__(self, numHabitaciones, capacidad, serviciosExtras):
        super().__init__(numHabitaciones, capacidad)
        self.__serviciosExtras = serviciosExtras
    
    def __str__(self):
        return f"Numero de habitacion que agendas: {self.__numHabitaciones}, con capacidad para {self.__capacidad}, con servicios {self.__serviciosExtras}"
    
    def getServExtras(self):
        return self.__serviciosExtras
    
    # Setter
    def setServExtras(self, serviciosExtras):
        self.__serviciosExtras = serviciosExtras
    
class SistemaReservas:
    def __init__(self):
        self.servicios = []
        self.serviciosExtra = []
        
    def agregarServicios(self, servicio):
        self.servicios.append(servicio)
    
    def registrarHabitaciones(self):
        numHabitaciones = int(input("Ingresa el numero de Habitacion que deseas "))
        capacidad = int(input("Ingresa la capacidad que deseas "))
        servicio = Habitacion(numHabitaciones, capacidad)
        
        self.agregarServicios(servicio)
        print("Habitacion reservada con exito!")
    
    def mostrarHabitaciones(self):
        for servicio in self.servicios:
            print(servicio)
        
    def agregarServiciosExtra(self, serviciosEx):
        self.serviciosExtra.append(serviciosEx)
    
    def registrarHabitacionesVip(self):
        numHabitaciones = int(input("Ingresa el numero de Habitacion que deseas "))
        capacidad = int(input("Ingresa la capacidad que deseas "))
        serviciosExtras = input("Ingrese que mas contiene el servicio extra ")
        servicioEx = HabitacionVip(numHabitaciones, capacidad, serviciosExtras)
        
        self.agregarServicios(servicioEx)
        print("Habitacion reservada con exito!")
    
    def mostrarHabitacionesVip(self):
        for servicioEx in self.serviciosExtra:
            print(servicioEx)
        
    def menu(self):
        while True:
            print("-----BIENVENIDOS AL SISTEMA DE RESERVAS DE HOTEL-----")
            print("Selecciona la opcion que deseas \n 1. Registrar habitaciones \n 2. Registrar habitaciones Vip \n 3. Mostrar todas las habitaciones \n 4. Mostrar habitaciones VIP \n 5. Salir")
            opcion = int(input("Marca la opcion: "))
            if opcion == 1:
                self.registrarHabitaciones()
            elif opcion == 2:
                self.registrarHabitacionesVip()
            elif opcion == 3:
                self.mostrarHabitaciones()
            elif opcion == 4:
                self.mostrarHabitacionesVip()
            else:
                print("Saliendo del sistema")
                break

sistemaRe = SistemaReservas()
sistemaRe.menu()