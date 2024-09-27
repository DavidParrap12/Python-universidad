class ConversorMoneda:
    def __init__(self):
        self.cantidad = 0
        self.moneda = ""

    def ingresarCambio (self):
        self.cantidad = int(input("Ingrese la cantidad de dinero a cambiar: $ "))
        self.moneda = input("Ingrese la moneda a convertir USD, EUR, MXN, JPY, GBP ")
        return True
    
    def convertirMoneda (self):
        if self.moneda == "USD":
            return self.cantidad * 4173
        elif self.moneda == "EUR":
            return self.cantidad * 4637
        elif self.moneda == "MXN":
            return self.cantidad * 214
        elif self.moneda == "JPY":
            return self.cantidad * 28.88
        elif self.moneda == "GBP":
            return self.cantidad * 5530
        else: 
            return False
def menu():
    print("Bienvenidos al conversor de moneda")
    nuevaConversion = ConversorMoneda()
    while True:

        opcion = int(input("1. Ingresar cambio \n 2 realizar conversion \n 3 salir "))
        if opcion == 1:
            print("Seleccione su valor de conversion a pesos \n USD=4173 \n EUR = 4637 \n MXN = 214 \n JPY = 28.88 \n GBP = 5530")
            nuevaConversion.ingresarCambio()
        elif opcion == 2:
            response = nuevaConversion.convertirMoneda
            if response == False:
                print("La moneda no esta disponible")
                continue
            else:
                print("El resultado de la conversion es: {response}")
        elif opcion ==3:
            del nuevaConversion
            break

menu()