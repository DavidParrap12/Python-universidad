numeroIngresadoPrimero = int(input("Ingrese un numero: "))
numeroIngresadoSegundo = int(input("Ingrese el segundo: "))

if numeroIngresadoSegundo == 0:
    print("No se puede dividir por cero")
else:
    print(numeroIngresadoPrimero / numeroIngresadoSegundo)