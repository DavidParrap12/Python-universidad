#Trabajar con conjuntos en Python. Mutables es con set para trabajarlo
conjunto = {1,2,3,4,5} #definicion de un conjuntos
print(type(conjunto)) 
print(conjunto) 
conjunto.add(6) #Agregar un elemento al conjunto
conjunto.add(6) #No se puede agregar un elemento repetido
conjunto.add("Hola como vas")
print(conjunto)

conjunto2 = set([1,2,3,4,5])#Otra forma de definir un conjunto
print(conjunto2)

conjunto3=set([2,4,5,6,7,8,9,0])
print(conjunto3)

conjunto.remove(6)#Eliminar un elemento del conjunto
conjunto.remove("Hola como vas")
print(conjunto)

#Union de conjuntos
union=conjunto.union(conjunto)
print(union)

#Interseccion de conjuntos
interseccion = conjunto.intersection(conjunto3)
print(interseccion)

#Diferencia de conjuntos
diferencia = conjunto.difference(conjunto3)
print(diferencia)