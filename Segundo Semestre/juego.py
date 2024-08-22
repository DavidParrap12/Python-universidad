import random
jugadorA = 1
jugadorB = 2

vidaTotalA = 50
vidaTotalB = 50 
#Para seleccionar que jugador va a jugar primero
jugadorAleatorio = random.choice([jugadorA, jugadorB])

print(jugadorAleatorio)
    
def ataque(jugadorAleatorio, vidaTotalA, vidaTotalB):
    if jugadorAleatorio == jugadorA:
        print("Turno del jugador A")
        turnoA = int(input("Jugador A: Diga el numero del 1-5 "))
        turnoB = int(input("Jugador B: Diga el numero del 1-5 "))
        if turnoA != turnoB:
            vidaTotalB -=10
            print("Jugador b pierde 10 puntos, vidas restantes:  ", vidaTotalB)
        elif turnoA == turnoB:
            print("Jugador B bloqueo el ataque")
        else:
            print("Numero no valido")
        return vidaTotalA, vidaTotalB
    else:
        print("Turno del jugador B")
        turnoA = int(input("Jugador A: Diga el numero del 1-5 "))
        turnoB = int(input("Jugador B: Diga el numero del 1-5 "))
        if turnoB != turnoA:
            vidaTotalA -=10
            print("Jugador A pierde 10 puntos, vidas restantes: ", vidaTotalA)
        elif turnoB == turnoA:
            print("Jugador B bloqueo el ataque")
        else:
            print("Numero no valido")
    
    jugadorAleatorio = jugadorA + jugadorB - jugadorAleatorio
    return vidaTotalA, vidaTotalB, jugadorAleatorio

while vidaTotalA > 0 and vidaTotalB >0:
    vidaTotalA, vidaTotalB = ataque(jugadorAleatorio, vidaTotalA, vidaTotalB)
        
            

if vidaTotalA > 0:
    print("Jugador A ha ganado")
else:
    print("Jugador B ha ganado")

