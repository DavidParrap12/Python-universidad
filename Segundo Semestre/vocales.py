#Definimos la funcion 
def contador (cadena):
    vocales = "aeiouAEIOU"
    contadorVocales = 0

    for letras in cadena:
        if letras in vocales:
            contadorVocales +=1
    return contadorVocales

#Solicitamos al usuario que ingrese el texto
cadena = input("Ingrese el texto ")

#Convertimos el contador en una sola variable
totalVocales = contador(cadena)
print(f"Total de vocales son: {totalVocales}")