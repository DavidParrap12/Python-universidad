try:
    #r es para lectura
    archivo = open("C:\Users\IBA-S01-LT-033\Documents\Davidparra\saludo.txt", "r")
    contenido = archivo.read()

except FileNotFoundError:
    print("No se encontro ningun archivo ")
else:
    print("El archivo fue encontrado ")
    print(contenido)
finally:
    print("Se termino la lectura")
