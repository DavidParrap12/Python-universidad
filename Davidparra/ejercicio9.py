edad = int (input("Ingrese su edad: "))
ingresosMensuales = int (input("Ingrese sus ingresos: "))

if edad >= 16 and ingresosMensuales >= 120000000:
    print("Debes pagar impuestos")
else: 
    print("No debes pagar impuestos")