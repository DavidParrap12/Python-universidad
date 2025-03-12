from collections import deque

clientes = deque()


while True:
    print("Bienvenido a la taquilla")
    menu = int(input("Ingresa la opcion que deseas: \n 1. Agregar \n 2. Orden de llegada \n 3. Mostrar cliente \n 4.Atender cliente  \n 5. salir "))
    if menu == 1:
        ingrese = input("Ingrese el cliente ")
        clientes.append(ingrese)
    elif menu == 2:
        print("El orden de llegada es: ", clientes)
    elif menu == 3:
        if not clientes:
            print("No hay clientes")
        else:
            for cliente in clientes:
                print(cliente)
    elif menu == 4:
        if not clientes:
            print("No hay clientes")
        else:
            pelicula = input("Que pelicula deseas ver ")
            print(f"Tique comprado con exito {pelicula}")
            clientes.popleft()
    else:
        print("Saliendo de la taquilleria") 
        break
        