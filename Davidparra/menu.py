#Configuracion para el menu de opciones
salida = 2
while salida == 2:
    menu = int(input("""Seleccione una opcion del menu
                 1. Ingresar
                 2. Crear
                 3. Salir """))
    #Empece por la parte de salida
    if menu == 3:
        salida = int(input("Deseas salir 1. Si 2. No "))
    #Esta es la opcion para crear el usuario
    elif menu == 2:
        print("Recuerde que el usuario es solo con letras, no se permite con caracteres ni numeros")
        ingresarUsuario = input("Ingrese su nombre ")
        print("Recuerde que la contraseña es solo con numero, no se permite caracteres ni letras")
        ingresarContraseña = int(input("Ingrese la contraseña "))

    #esta es la parte de ingresar
    else:
        usuario = input("Ingrese al sistema con su usuario ")
        clave = int(input("Ingrese la contraseña "))
        intentos = 0
        if usuario != usuario:
            intentos +=1
            print("Usuario no validado ")
        else:
            print("Usuario validado ")
        if clave != clave:
            intentos +=1
            print("Contraseña no valida")
        else: 
            print("Contraseña es valida")
        
       
        
        
    
        