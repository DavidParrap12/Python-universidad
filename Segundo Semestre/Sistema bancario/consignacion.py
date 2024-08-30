def consignacion (saldo):
    print("¿Cual es el valor que deseas consignar?")
    valorAConsignar = int(input("Ingrese la cantidad "))
    saldo += valorAConsignar
    return saldo

def retiro (saldo, valorARetirar):
    saldo = saldo - valorARetirar
    return saldo 


