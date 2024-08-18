#Solicitamos al usuario que elija 
usuario = input("Elije si quieres 'Asc' o 'Desc': ")

def orden (usuario):
    listado = [2,4,6,8,10,12]
    #De menor a mayor
    if usuario == 'Asc':
        for i in range(len(listado)):
            for d in range ( i + 1, len(listado)):
                if listado[i] > listado[d]:
                    listado[i], listado[d] = listado[d], listado[i]
        print(f"El orden de los numeros es de menor a mayor {listado}")
    #De mayor a menor
    elif usuario == 'Desc':
        for i in range(len(listado)):
            for d in range (i + 1, len(listado)):
                if listado[i] < listado[d]:
                    listado[i], listado[d] = listado[d], listado[i]
        print(f"El orden de los numeros es de mayor a menor {listado}")
    else:
        print("Opcion no valida")
        
orden(usuario)
        