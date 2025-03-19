#Son un tipo de dato que permite almacenar varios elementos inmutables
lista = (1,2,3, "David Parra", [23,23,56])

print(type(lista))
print(lista)
print(lista[3]) #Acceder a un elemento de la tupla
print(lista[4] [2])
print(len(lista))

nombres = ("David", "Parra", "Pardo")

print(lista+nombres)#concatenar tuplas
print(nombres*3) #Repetir tuplas

print("David" not in nombres, "El nombre existe") #verific si un elemento está en la dupla

#nombres[0]="Harold" #No se puede modificar una tupla

