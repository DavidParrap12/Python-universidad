#Herencia sin iniciador
#Clase base
class Nadador:
    def nadar(self):
        return"Nadando"

class Volador:
    def volar(self):
        return "Volando"
#Clase derivada hereda dos clases base   
class Pato(Nadador, Volador):
    def hacer_sonido(self):
        return "Cuac"
    
class Paloma(Volador):
    def ruido(self):
        return "cucurrucucu "
    
#Uso de las clases    
mi_paloma = Paloma()
print(mi_paloma.volar())
print(mi_paloma.ruido())
print("**************************************************")
mi_pato = Pato()
print(mi_pato.nadar())
print(mi_pato.volar())
print(mi_pato.hacer_sonido())
