#Clase simple y no tiene metodo solo atributo
"""class MyClass:
    x = 5
print(MyClass)"""
#init(primer parametro define y recibe, adquiere un valor de los parametros) se puede hacer iniciar una lista vacia con corchetes
class Persona:
    def __init__(self, name, age):
        #Llama el parametro
        self.name = name
        self.age = age

#variable p1 con un valor tipo Persona
p1 = Persona("David", 21) #es una instacia
#otra manera
#p2 = Persona(name="Juan", age= 25)

print(p1.name)

#funcion str: representa texto 

class Persona:
    def __init__(self, name, age):
        #Llama el parametro
        self.name = name
        self.age = age

#variable p1 con un valor tipo Persona
    def __str__(self):
        #me retorna un texto
        return f"{self.name}, {self.age}"
p1 = Persona("David", 21) #es una instacia
print(p1)

"""atributos sin parentesis, metodo con parentesis"""