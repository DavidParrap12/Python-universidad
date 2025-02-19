class Usuario:
    # Contiene estos atributos
    def __init__(self, nombre, codigo, fechaNacimiento):
        # constructor
        self.__nombre = nombre
        self.__codigo = codigo
        self.__fechaNacimiento = fechaNacimiento

    # getters
    @property
    def getNombre(self):
        return  self.__nombre
    def getCodigo(self):
        return self.__codigo
    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    
    # setters
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setCodigo(self, codigo):
        self.__codigo = codigo
    def setFechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento

class RegistroUsuario:
    def __init__(self):
        self.crear = []

    def agregarUsuario(self, creado):
        self.crear.append(creado)

    # Registro del usuario
    def registro(self):
        nombre = input("Ingresa tu nombre ")
        codigo = int(input("Ingresa tu codigo! "))
        fechaNacimiento = int(input("Ingresa tu año de nacimiento "))
        
        creado = Usuario(nombre, codigo, fechaNacimiento)
        self.agregarUsuario(creado)
    
    def eliminarUsuario(self):
        self.crear.clear()


    def menuOpciones(self):
        salir = 'No'

        while salir == 'No':
            opciones = int(input("""Elije la opcion que deseas realizar
            1. Registrar un usuario
            2. Modificar usuario
            3. eliminar un usuario
            4. salir """)) 
            if opciones == 1:
                self.registro()
            elif opciones == 2:
                cambio = int(input("""Que modificacion deseas realizar:
                1. nombre
                2. codigo
                3. Año de nacimiento"""))
                if cambio == 1:
                    self.crear[0] = input("Ingresa el nombre que deseas modificar ")
                elif cambio ==2:
                    self.crear[1] = int(input("Ingresa el codigo que deseas modificar "))
                elif cambio == 3:
                    self.crear[2] = int(input("Ingresa el año que deseas modificar "))
                else:
                    return
            elif opciones == 4:
                opcion = int(input("Deseas salir? \n 1. Si \n 2. No "))
                if opcion == 1:
                    print("Saliendo")
                else:
                    return
            else:
                self.eliminarUsuario()

SystemUsuario = RegistroUsuario()
SystemUsuario.menuOpciones()

                   
        
    
        
        
        
