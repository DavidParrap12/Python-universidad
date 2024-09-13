#Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "El animal hace un sonido"
    
class Perro(Animal):
    def hablar(self):
        return "Guau"
        #Llama al nombre de la funcion init
mi_perro = Perro("Rex")
#dice primero nombre del perro y despues retorna guau
print(f"{mi_perro.nombre} dice {mi_perro.hablar()}")