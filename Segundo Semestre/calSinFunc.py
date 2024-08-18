menu= int(input("""Seleccione la operacion que deseas realizar
            1. +
            2. -
            3. *
            4. / """))

numeroUno = int(input("Ingrese un numero "))
numeroDos = int(input("Ingrese un numero "))

if menu == 1:
    resultado = numeroUno + numeroDos
    print("El resultado de la suma es: ", resultado)
elif menu == 2:
    resultado = numeroUno - numeroDos
    print("El resultado de la resta es: ", resultado)
elif menu == 3:
    resultado = numeroUno * numeroDos
    print("El resultado de la multiplicacion es: ", resultado)
elif menu == 4:
    if numeroDos == 0:
        print("Operacion no valida")
    else: 
        resultado = numeroUno / numeroDos
        print("El resultado de la division es: ", resultado)
else:
    print("Operacion no valida")