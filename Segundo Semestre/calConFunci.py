menu= int(input("""Seleccione la operacion que deseas realizar
            1. +
            2. -
            3. *
            4. / """))

numeroUno = int(input("Ingrese un numero "))
numeroDos = int(input("Ingrese un numero "))

def operacion(menu,numeroUno, numeroDos):
    if menu == 1:
        resultadoSuma = numeroUno + numeroDos
        print(f"El resultado de la suma es: {resultadoSuma} ")
        return resultadoSuma
    elif menu == 2:
        resultadoResta = numeroUno - numeroDos
        print(f"El resultado de la resta es: {resultadoResta} ")
        return resultadoResta
    elif menu == 3:
        resultadoMulti = numeroUno * numeroDos
        print(f"El resultado de la multiplicacion es: {resultadoMulti} ")
        resultadoMulti
    elif menu == 4:
        if numeroDos == 0:
            print("Operacion no valida")
        else:
            resultadoDivision = numeroUno / numeroDos
            print(f"El resultado de la division es: {resultadoDivision} ")
            return resultadoDivision
        
    else:
        print("Operacion no valida")


resultadoTotal = operacion(menu,numeroUno,numeroDos)