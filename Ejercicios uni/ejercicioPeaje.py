tipoVehiculo = (input("Ingrese el tipo de vehiculo: 4 ,6 , moto o cuatriMoto: "))

try:
    tipoVehiculo = int(tipoVehiculo)
except: 
    tipoVehiculo = tipoVehiculo.lower()
    
    
peaje = 0
peajeMoto = 25000

if tipoVehiculo == 4:
    peaje = 50000
    print("El valor del peaje es de: " + str(peaje))
elif tipoVehiculo == 6:
    peaje = 65000
    print("El valor del peaje es de: " + str(peaje))
elif tipoVehiculo == "moto":
    print("El valor del peaje es de: " + str(peajeMoto))
elif tipoVehiculo == "cuatriMoto":
    numeroPersonas = input("ingrese el numero de personas")
    peajeNP = 10000 * numeroPersonas
    print("El valor del peaje es de: " + str(peajeNP))
else: 
    print("Tipo de vehiculo no reconocido.")
