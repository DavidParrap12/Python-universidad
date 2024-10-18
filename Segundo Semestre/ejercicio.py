import math

class Figura:
    def area (self):
        pass

class Circulo(Figura):
    def __init__(self, radio) -> None:
        self.radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo(Circulo):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

def mostrar_area(figura):
    print(f"El area es: {figura.area()}")


circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

figuras = [circulo, rectangulo]

for figura in figuras:
    mostrar_area(figura)