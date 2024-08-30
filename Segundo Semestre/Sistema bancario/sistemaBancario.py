import opciones

nombre = 'David Parra'
tipoDeCuenta = 'Ahorro'
saldo = 100000
opcion = 0

print("BIENVENIDO AL BANCO")
print("*********************************")
print(f"Nombre del cliente: {nombre}")
print(f"Tipo de cuenta es: {tipoDeCuenta}")
print(f"Su saldo es: '$' {saldo}")
print("*********************************")


menu = opciones.opcion(saldo)