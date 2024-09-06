"""class Personasy:
    def __init__(pepito, name, age):
        pepito.name = name
        pepito.age = age

    def myfunc(pepita):
        print("Hello my name is " + pepita.name)"""

#p1 = Personasy("David", 21)
#p1.myfunc() 

#modificar atributos
"""class Personasy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Personasy("David", 21)
p2 = Personasy("Juan", 17)
p2.age = 50
print(p1.age)
print(p2.age)
"""
#Eliminar (vaciar) atributos del objeto mas no de la clase

"""class Personasy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Personasy("David", 21)
p2 = Personasy("Juan", 17)

del p2.age
print(p1.age)
#Imprime error y elimino el p2 la edad
print(p2.age)"""

#del: eliminando el objeto 

"""class Personasy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Personasy("David", 21)
p2 = Personasy("Juan", 17)

del p2
print(p1.age)
#Imprime error y elimino el p2 la edad
print(p2)"""