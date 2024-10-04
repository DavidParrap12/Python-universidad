#Herencia sin iniciador
#Clase base
class Nadador:
    def nadar(self):
        return"Nadando"

class Volador:
    def volar(self):
        return "Volando"
    
class Comer:
    def comer(self):
        return "comiendo"
    
#Clase derivada hereda tres clases   
class Pato(Nadador, Volador, Comer):
    def hacer_sonido(self):
        return "Cuac"

# Imprimimos las clases
#Uso de las clases    
print("**************************************************")
mi_pato = Pato()
print(mi_pato.nadar())
print(mi_pato.volar())
print(mi_pato.hacer_sonido())
print(mi_pato.comer())