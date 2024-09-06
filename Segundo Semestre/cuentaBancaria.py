#=0 quiere decir que empieza desde 0 el valor 
class CuentaBancaria:
    def __init__(self, titular, saldo =0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, depostio):
        self.saldo += depostio
        print(f"Se han adicionado {depostio}. Saldo actual: {self.saldo}€. ")
    
    def retirar(self, depostio):
        if depostio <= self.saldo:
            self.saldo -= depostio
            print(f"Se han retirado {depostio}. Saldo actual: {self.saldo}€.")
        else:
            print("No tienes suficiente saldo para retirar esa cantidad.")
    
    def consultar_saldo(self):
        return f"Saldo actual: {self.saldo}€."
    
cuenta = CuentaBancaria(nombre, depostio)
nombre = input("Ingrese su nombre")
depostio = float(input("Ingrese el valor"))
cuenta.depositar(depostio)
cuenta.retirar(depostio)
print(cuenta.consultar_saldo)
cuenta2 = CuentaBancaria("Valeria", 60000)
cuenta2.depositar(10000)
print(cuenta2.consultar_saldo)
    