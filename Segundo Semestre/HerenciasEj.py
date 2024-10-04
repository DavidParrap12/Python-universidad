#Herencia basica
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def Hablar(self):
        return "El animal hace un sonido"
    
class Perro(Animal):
    #funcion hablar con el ruido a hacer
    def Hablar(self):
        return "guau"
    
class Gato(Animal):
    def Hablar(self):
        return "Miau"
    
#Llamos las clases Perro y gato con los atributos de hablar y nombre
mi_Gato = Gato("Tom")
print(f"{mi_Gato.nombre} dice {mi_Gato.Hablar()}")
mi_perro = Perro("Rex")
print(f"{mi_perro.nombre} dice {mi_perro.Hablar()}")