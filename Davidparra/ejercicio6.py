anio = int (input("Ingrese el año de nacimiento "))

edadTotal = 2024 - anio

if edadTotal >= 18: 
    print("Usted ya es mayor de edad: " + "Su edad es: " + str (edadTotal))
else:
    print("Usted es menor de edad: " + "Su edad es: "+ str (edadTotal))