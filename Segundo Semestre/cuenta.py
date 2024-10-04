# clase base
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
        
    #get y set de titular
    @property
    def getTitular(self):
        return self.__titular
    def setTitular(self, titular):
        self.__titular = titular
    # get y set de cantidad
    @property
    def getCantidad(self):
        return self.__cantidad
    def setCantidad(self, cantidad):
        self.__cantidad = cantidad
    
    # funcion para depositar
    def depositar(self, saldo):
        saldo = int(input("Ingrese la cantidad que deseas depositar "))
        if saldo > self.__cantidad:
            self.__cantidad += saldo    
            print(f"Han sido depositados $ {saldo} \n Saldo actual es: $ {self.__cantidad}.")
        else:
            print("Monto insuficiente")
    # funcion para retirar
    def retirar (self, saldo):
        saldo = int(input("Ingrese la cantidad que deseas retirar "))
        if saldo <= self.__cantidad:
            self.__cantidad -= saldo
            print(f"Se han retirado de su cuenta {saldo}. \n Saldo actual es: $ {self.__cantidad} ")
        else:
            print("Monto insuficiente")
    #  funcion para consultar saldo
    def consultar_Saldo (self):
        return f"Saldo actual es: ${self.__cantidad}"
     
titular = input("Ingrese el nombre del usuario ")
cuenta = Cuenta(titular, 0)   
def menu ():
    while True:
        opcion = int(input("ELIGE LA OPCION QUE DESEAS REALIZAR \n 1. Consultar saldo \n 2. Retirar saldo \n 4. Depositar saldo \n 3. Salir "))
        if opcion == 1:
            cuenta.consultar_Saldo()
        elif opcion == 2:
            cuenta.retirar()
        elif opcion == 3:
            print("Saliendo del cajero")
        else:
            cuenta.depositar()
            break
            

menu()
print(cuenta.consultar_Saldo())
        