class Concierto:
    def __init__(self, boleta):
        self.boleta = boleta
    
    def vender(self):
        self.boleta.tarifa()

class General:
    def tarifa (self):
        print(150000)
    
class Plateada:
    def tarifa(self):
        print(300000)

class Vip:
    def tarifa(self):
        print(1000000)


def menu():
    while True:
        print("Bienvenido a la boleteria del concierto")
        print("Selecciona la tarifa que deseas comprar: \n 1. General \n 2. Plateada \n 3. Vip \n 4. Salie")
        op = int(input("Ingrese la opcion "))
        if op == 1:
            bg = General()
            con = Concierto(bg)
            con.vender()
        elif op == 2:
            bp = Plateada()
            con = Concierto(bp)
            con.vender()
        elif op == 3:
            bv = Vip()
            con = Concierto(bv)
            con.vender()
        else:
            print("Saliendo del menu ")
            break

menu()

    
    
