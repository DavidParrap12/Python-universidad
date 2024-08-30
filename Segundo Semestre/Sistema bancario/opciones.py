import consignacion
def opcion (saldo):
    #Menu de opciones
    while True:
        menu = int(input("""Escriba el numero de la opcion que deseas
                1 - Consultar saldo
                2 - Retirar
                3 - Consignacion
                9 - Salir """))
        #Saldo total
        if menu == 1:
            print("Su saldo total es: $", saldo)
        elif menu == 2:
            #Valor a retirar
            valorARetirar = int(input("Ingrese el valor que deseas retirar: "))
            if saldo < valorARetirar:
                print("Valor insuficiente")
            else: 
                saldo = consignacion.retiro(saldo, valorARetirar)
                print(f"El saldo actualizado es: $ {saldo}")
        elif menu == 3:
            #Consignacion
            saldo = consignacion.consignacion(saldo)
            print(f"El saldo actualizado es: $ {saldo}")
            #Salida y despido
        elif menu == 9:
            print("Gracias por usar nuestro servicio!")
            break
        else:
            print("Opcion no valida, vuelve a intentarlo")