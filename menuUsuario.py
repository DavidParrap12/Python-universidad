#Clase principal
class Usuario:
    # Contiene estos atributos
    def __init__(self, nombre, codigo, fechaNacimiento):
        # constructor
        self.__nombre = nombre
        self.__codigo = codigo
        self.__fechaNacimiento = fechaNacimiento

    # getters
    def getNombre(self):
        return self.__nombre

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

#clase para registrar usuarios
class RegistroUsuario:
    def __init__(self):
        self.crear = []

    def agregarUsuario(self, creado):
        self.crear.append(creado)

    # Registro del usuario
    def registro(self):
        nombre = input("Ingresa tu nombre: ")
        codigo = int(input("Ingresa tu codigo: "))
        fechaNacimiento = int(input("Ingresa tu año de nacimiento: "))
        
        creado = Usuario(nombre, codigo, fechaNacimiento)
        self.agregarUsuario(creado)
    
    # Funcion para modificar un usuario
    def modificarUsuario(self):
        codigo = int(input("Ingresa el codigo del usuario a modificar: "))
        for usuario in self.crear:
            if usuario.getCodigo() == codigo:
                cambio = int(input("""Que modificacion deseas realizar:
                1. Nombre
                2. Codigo
                3. Año de nacimiento """))
                if cambio == 1:
                    nuevo_nombre = input("Ingresa el nuevo nombre: ")
                    usuario.setNombre(nuevo_nombre)
                elif cambio == 2:
                    nuevo_codigo = int(input("Ingresa el nuevo codigo: "))
                    usuario.setCodigo(nuevo_codigo)
                elif cambio == 3:
                    nuevo_anio = int(input("Ingresa el nuevo año de nacimiento: "))
                    usuario.setFechaNacimiento(nuevo_anio)
                return
        print("Usuario no encontrado")
    
    # Funcion para eliminar un usuario
    def eliminarUsuario(self):
        codigo = int(input("Ingresa el codigo del usuario a eliminar: "))
        usuario_encontrado = False
        for usuario in self.crear:
            if usuario.getCodigo() == codigo:
                self.crear.remove(usuario)
                usuario_encontrado = True
                print("Usuario con codigo {codigo} eliminado. ")
                break
        if not usuario_encontrado:
            print("Usuario no encontrado")

    

    # Funcion para listar los usuarios
    def listarUsuarios(self):
        for usuario in self.crear:
            print(f"Nombre: {usuario.getNombre()}, Codigo: {usuario.getCodigo()}, Año de Nacimiento: {usuario.getFechaNacimiento()}")

    # Funcion para mostrar el menu de opciones
    def menuOpciones(self):
        salir = 5

        try:
            while salir == 5:
                opciones = int(input("""Elije la opcion que deseas realizar
                1. Registrar un usuario
                2. Modificar usuario
                3. Eliminar un usuario
                4. Listar usuarios
                5. Salir del sistema"""))
                if opciones == 1:
                    self.registro()
                elif opciones == 2:
                    self.modificarUsuario()
                elif opciones == 3:
                    self.eliminarUsuario()
                elif opciones == 4:
                    self.listarUsuarios()
                elif opciones == 5:
                    print("Saliendo")
                else:
                    print("Opción no válida")
        except ValueError:
            print("Opción no válida")

#registro_usuario = RegistroUsuario()







