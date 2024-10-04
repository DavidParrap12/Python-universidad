Amigos = []
class Amigo:
    def __init__(self, nombre, correo, telefono, instagram):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__instagram = instagram
        
        @property
        def get_Nombre(self):
            return self.__nombre
        def setNombre(self, nombre):
            self.__nombre = nombre
        
        @property
        def get_Correo(self):
            return self.__correo
        def set_Correo(self,correo):
            self.__correo = correo
            
        @property
        def get_Telefono(self):
            return self.__telefono
        
        def set_Telefono(self,telefono):
            self.__telefono = telefono
        
        @property
        def get_Instagram(self):
            return self.__instagram
        def set_Instagram(self,instagram):
            self.__instagram = instagram
            
def ingresar_Datos(self):
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    telefono = int(input("Ingrese su numero telefonico: "))
    instagram = input("Ingrese su usuario de Ig: ")


nuevo_Amigo = Amigo(nombre, correo, telefono, instagram)
nuevo_Amigo.ingresar_Datos()

Amigos.append(nuevo_Amigo)

for amigo in Amigos:
    print(f"Nombre: {amigo.get_nombre()}, Correo: {amigo.get_correo()}, Teléfono: {amigo.get_telefono()}, Instagram: {amigo.get_instagram()}")
