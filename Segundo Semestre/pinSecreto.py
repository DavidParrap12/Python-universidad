pinSecreto = 4567


for _ in range(1,4):
    pinSolicitado = int(input("Ingrese el pin "))
    
    if pinSolicitado == pinSecreto:
        print("Acceso permitido")
        break
    else: 
        if _ < 3:
            print("Intentos realizados: ", _)
        else:
            print("Llamando a la policia")