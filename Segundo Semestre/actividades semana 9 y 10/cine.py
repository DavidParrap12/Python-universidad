class Cuenta:
    def __init__(self, numCuenta, saldo):
        self.__numCuenta = numCuenta
        self.__saldo = saldo
    
    def __str__(self):
        return f"El numero de cuenta es {self.__numCuenta} con un saldo total de {self.__saldo}"
    
    @property
    # setter
    def setNumCuenta(self, numCuenta):
        self.__numCuenta = numCuenta
    def setSaldo(self, saldo):
        self.__saldo = saldo
    
    # Getter
    def getNumCuenta(self):
        return self.__numCuenta
    def getSaldo(self):
        return self.__saldo

class CuentaCorriente(Cuenta):
    def __init__(self, numCuenta, saldo=0, sobreGiro=0):
        super().__init__(numCuenta, saldo)
        self.__sobreGiro = sobreGiro
    
    def  __str__(self):
        return f"El numero de cuenta es {self.__numCuenta} con un saldo total de {self.__saldo}"

    @property
    def getSobreGiro(self):
        return self.__sobreGiro
    
    def setSobreGiro(self, sobreGiro):
        self.__sobreGiro = sobreGiro
        
class SistemaCuentas:
    def __init__(self):
        self.cuentas = []
        self.cuentasCorriente = []
        
    def agregarCuentas(self, cuenta):
        self.cuentas.append(cuenta)
        
    
        
    def registrarCuenta(self):
        print("BIENVENIDOS AL SISTEMA DE REGISTRO DE CUENTA")
        numCuenta = int(input("Ingrese el numero de la cuenta: "))
        saldo = float(input("Ingresa el saldo inicial: "))
        cuenta = Cuenta(numCuenta, saldo)
        self.agregarCuentas(cuenta)
        print("Cuenta registrada con exito! ")
        
    def mostrarCuenta(self):
        for cuenta in self.cuentas:
            print(cuenta)
    
    def agregarCuentaCorriente(self, cuentaCorriente):
        self.cuentasCorriente.append(cuentaCorriente)
        
    def registrarCuentaCorriente(self):
        print("BIENVENIDOS AL SISTEMA DE REGISTRO DE CUENTA")
        numCuenta = int(input("Ingrese el numero de la cuenta: "))
        saldo = float(input("Ingresa el saldo inicial: "))
        sobreGiro = float(input("Ingrese el limite de sobregiro: "))
        cuentaCorriente = CuentaCorriente(numCuenta, saldo, sobreGiro)
        self.agregarCuentaCorriente(cuentaCorriente)
        print("Cuenta registrada con exito! ")
        
    def mostrarCuentaCorriente(self):
        for cuentaCorriente in self.cuentasCorriente:
            print(cuentaCorriente)
    
    def actualizarSaldoYSobregiro(self):
        numCuenta = int(input("Ingrese el número de cuenta para actualizar: "))
        for cuenta in self.cuentas:
            if cuenta.getNumCuenta() == numCuenta:
                nuevo_saldo = float(input("Ingrese el nuevo saldo: "))
                cuenta.setSaldo(nuevo_saldo)
                print("Saldo actualizado.")
                return
        for cuentaCorriente in self.cuentasCorriente:
            if cuentaCorriente.getNumCuenta() == numCuenta:
                nuevo_saldo = float(input("Ingrese el nuevo saldo: "))
                nuevo_sobregiro = float(input("Ingrese el nuevo límite de sobregiro: "))
                cuentaCorriente.setSaldo(nuevo_saldo)
                cuentaCorriente.setSobreGiro(nuevo_sobregiro)
                print("Saldo y sobregiro actualizados.")
                return
        print("Cuenta no encontrada.")
        
        
    def menu(self):
        while True:
            print("BIENVENIDOS AL SISTEMA DE GESTION DEL CINE")
            print("Selecciona la opcion que deseas realizar \n 1. Registrar cuenta \n 2. Registrar cuenta corriente \n 3. Mostrar cuenta \n 4. Mostrar cuentas corriente \n 5. Actualizar saldo y el limite de sobregiro  \n 6. Salir")
            opcion = int(input("Ingresa la opcion: "))
            if opcion == 1:
                self.registrarCuenta()
            elif opcion == 2:
                self.cuentasCorriente()
            elif opcion == 3:
                self.mostrarCuenta()
            elif opcion == 4:
                self.mostrarCuentaCorriente()
            elif opcion == 5:
                self.actualizarSaldo()
            else:
                print("Gracias por usarnos")

sistema = SistemaCuentas()
sistema.menu()