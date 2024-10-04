Amigos = []
class Amigo:
    def __init__(self, nombre, correo, telefono, instagram):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__instagram = instagram
        
        @property
        def getNombre(self):
            return self.__nombre
        def setNombre(self, nombre):
            self.__nombre = nombre
        
        @property
        def getCorreo(self):
            return self.__correo
        def setCorreo(self,correo):
            self.__correo = correo
            
        @property
        def getTelefono(self):
            return self.__telefono
        
        def set_Telefono(self,telefono):
            self.__telefono = telefono
        
        @property
        def getInstagram(self):
            return self.__instagram
        def setInstagram(self,instagram):
            self.__instagram = instagram
            
    def ingresar_Datos(self):
        self.__nombre = input("Ingrese su nombre: ")
        self.__correo = input("Ingrese su correo: ")
        self.__telefono = int(input("Ingrese su numero telefonico: "))
        self.__instagram = input("Ingrese su usuario de Ig: ")


nuevo_Amigo = Amigo("", "", 0, "")
nuevo_Amigo.ingresar_Datos()

Amigos.append(nuevo_Amigo)

for amigo in Amigos:
    print(f"Nombre: {amigo.get__nombre()}, Correo: {amigo.get_correo()}, Teléfono: {amigo.get_telefono()}, Instagram: {amigo.get_instagram()}")