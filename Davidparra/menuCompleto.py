salida = 2
while salida == 2:
try:
    opcion = int(input("""menu 
                        1. Peaje 
                        2. Conversor 
                        3. Calculadora 
                        4. Salir
                        Por favor ingresa la opcion """))
except Exception as error:
        print("Señor usuario para seleccionar una opcion del menu debe digitar un numero ", type(error))
else: 
    if opcion == 4:
        salida = int(input("Desea Salir? 1.si 2.no "))
#except Exception as Error: 
        #print("Debes ingresar la opcion 1 o 2, no texto", Error)

    elif opcion == 1:
        tipoVehiculo = int (input("Ingrese su tipo de vehiculo: 1. Carro 4, 2. Carro 6, 3. Moto, 4.Cuatrimoto "))
        peaje = 0
        peajeMoto = 25000

        #Calculamos el valor del peaje
        if tipoVehiculo == 1:
            peaje = 50000 * 4
            print("El valor del peaje es de: " + str (peaje))
        elif tipoVehiculo == 2:
            peaje = 65000 * 6
            print("El valor del peaje es de: " + str (peaje))
        elif tipoVehiculo == 3:
            print("El valor de su peaje es de: " + str (peajeMoto)) 
        elif tipoVehiculo == 4:
            #Solicitamos al usuario el numero de personas
            numeroPersonas = int (input("Ingrese el numero de personas"))
            peaje = 10000 * numeroPersonas
            print("El valor del peaje es: " + str (peaje))
        else:
            print("El tipo de vehiculo no esta en la lista")
    elif opcion == 3:
        #Solicitamos al usuario que ingrese los numeros
        numeroUno = int(input("Ingrese un numero "))
        numeroDos = int(input("Ingrese otro numero "))
        #Solicitamos al usuario que elija la operacion que desea realizar
        operacion = input("Que operacion desea realizar + suma,- resta ,* multiplicacion o / division ")
        #esto seria como el front de la funcion
        if operacion == '+':
            sumaTotal = numeroUno + numeroDos
            print("La suma es: ", sumaTotal)
        elif operacion == '-':
            restaTotal = numeroUno + numeroDos
            print("La resta es: ", restaTotal)
        elif operacion == '*':
            multi = numeroUno * numeroDos
            print("La multiplicacion es: ", multi)
        else:
            if numeroDos != 0:
                divisionTotal = numeroUno* numeroDos
                print("La division es: ", divisionTotal)
            else:
                 print("Division no realizada, el divisor debe ser diferente a 0 ")
    else:
        salidaConversor = 2
        while salidaConversor == 2:
            conversorMenu = int(input(""" Elija una conversion que desea: 
                1. Pesos a Dolares
                2. Kilogramos a Gramos
                3. Kilometros a Millas
                4. Salir """))
                
            if conversorMenu == 4:
                salidaConversor = int(input("Desea salir 1. Si 2. No "))
            elif conversorMenu == 1:
                pesosADolares = int(input("Ingrese los pesos que desea convertir "))
                dolares = 4067.45
                totalConvertidos = pesosADolares * 1 / dolares
                print("La conversion de pesos a dolares es de: ", totalConvertidos)
            elif conversorMenu == 2:
                kilogramos = int(input("Ingrese los kilogramos que deseas convertir: "))
                kilosAGramos = kilogramos * 1000
                print("La conversion de kilogramos a gramos es de: ", kilosAGramos)
            else:
                kilometros = int(input("Ingrese los kilometros que desea convertir a millas: "))
                kilometrosAMillas = kilometros / 1.609
                print("La converson de kilometros a Millas es de: ", kilometrosAMillas)