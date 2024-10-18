class Vehiculo:
    def moverse(self):
        pass

class Coche(Vehiculo):
    def moverse(self):
        return "El coche se desplaza por carretera"
    
class Barco(Vehiculo):
    def moverse(self):
        return "El barco navega por el agua"
    
class Avion(Vehiculo):
    def moverse(self):
        return "El avion se desplaza por el aire"
    
def describir_movimiento(vehiculo):
    print(vehiculo.moverse())

vehiculos = [Coche(), Barco(), Avion()]

for vehiculo in vehiculos:
    describir_movimiento(vehiculo)
