class Vehiculos:
    def __init__(self,marca,modelo,anio,color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio 
        self.color = color

    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.anio}, {self.color}"

marcaAl = Vehiculos("BMW", "Serie 3 G20", 2019, "Blanco")


def main():
    salir = 7
    while True:

        menu = int(input(""" Seleccione la opcion
            1. encender
            2. apagar
            3. pitar
            4. girar
            5. cambiarMarcha
            6. info
            7. salir """))
        if menu == 2:
            print("Apagando el carro") 
        elif menu == 3:
            print("Carro pitando")
        elif menu == 4:
            print("Girando")
        elif menu == 6:
            print(marcaAl)
        elif menu == 5:
            menuDos = int(input(""" Elige a que marcha quieres ir
                            1. 1ª Marcha
                            2. 2ª Marcha
                            3. 3ª Marcha
                            4. 4ª Marcha
                            5. 5ª Marcha
                            6. Reversa """))
            if menuDos == 1:
                print("El carro va en primera")
            elif menuDos ==2:
                print("El carro va en segunda")
            elif menuDos ==3:
                print("El carro va en tercera")
            elif menuDos ==4:
                print("El carro va en cuarta")
            elif menuDos ==5:
                print("El carro va en quinta")
            else:
                print("El carro esta en reversa")
        elif menu == 1:
            print("Enciendiendo el carro") 
        else:
            break
            
main()