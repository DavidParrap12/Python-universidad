def todas (preguntaUno,preguntaDos,preguntaTres,preguntaCuatro,preguntaQuinta):
    #Colocamos las variables de las distintas casas
    gryffindor = 0
    hufflepuff = 0
    ravenclaw = 0
    slytherin = 0
    
    #Procesamos las preguntas
    if preguntaUno == 1:
        gryffindor +=1
    elif preguntaUno == 2:
        hufflepuff +=1
    elif preguntaUno == 3:
        ravenclaw +=1
    elif preguntaUno == 4:
        slytherin +=1
    else:
        print("Opcion no valida en la primera pregunta")
    
    if preguntaDos == 1:
        gryffindor +=1
    elif preguntaDos == 2:
        ravenclaw +=1
    elif preguntaDos == 3:
        slytherin +=1
    elif preguntaDos == 4:
        hufflepuff +=1
    else:
        print("Opcion no valida en la segunda pregunta")
        
    if preguntaTres == 1:
        hufflepuff +=1
    elif preguntaTres == 2:
        ravenclaw +=1
    elif preguntaTres == 3:
        slytherin +=1
    elif preguntaTres == 4:
        gryffindor +=1
    else:
        print("Opcion no valida en la tercera pregunta")
        
    if preguntaCuatro == 1:
        gryffindor +=1
    elif preguntaTres == 2:
        ravenclaw +=1
    elif preguntaTres == 3:
        slytherin +=1
    elif preguntaTres == 4:
        hufflepuff +=1
    else:
        print("Opcion no valida en la cuarta pregunta")
    
    if preguntaQuinta == 1:
        ravenclaw +=1
    elif preguntaTres == 2:
        gryffindor +=1
    elif preguntaTres == 3:
        hufflepuff +=1
    elif preguntaTres == 4:
        slytherin +=1
    else:
        print("Opcion no valida en la quinta pregunta")        
    #Definimos a que casa pertenece el usuario    
    puntosTotal = max(gryffindor,hufflepuff,ravenclaw,slytherin)
    if puntosTotal == gryffindor:
        return "Tu casa es Gryffindor!"
    elif puntosTotal == hufflepuff:
        return "Tu casa es Hufflepuff!"
    elif puntosTotal == ravenclaw:
        return "Tu casa es Ravenclaw!"
    elif puntosTotal == slytherin:
        return "Tu casa es Ravenclaw!"

#Preguntas para el usuario
print("Primera pregunta")
preguntaUno = int(input("""Como te definirías
                    1. 'Valiente', 'gryffindor',
                    2. 'Leal' 'hufflepuff',
                    3. 'Sabio' 'ravenclaw',
                    4. 'Ambicioso' 'slytherin' """))
print("Segunda Pregunta")
preguntaDos = int(input("""Cual es tu clase favorita?
                    1. 'Vuelo' 'gryffindor'
                    2. 'Pociones' 'ravenclaw'
                    3. 'Defensa contra las artes oscuras' 'slytherin'),
                    4. 'Animales fantásticos' 'hufflepuff' """))
print("Tercera Pregunta")
preguntaTres = int(input("""¿Dónde pasarías más tiempo?
                    1. 'Invernadero' 'hufflepuff'
                    2. 'Biblioteca' 'ravenclaw'
                    3. 'En la sala común' 'slytherin'
                    4. 'Explorando' 'gryffindor' """))
print("Cuarta Pregunta")                            
preguntaCuatro = int(input("""¿Cuál es tu color favorito?
                    1. 'Rojo' 'gryffindor'
                    2. 'Azul' 'ravenclaw'
                    3. 'Verde' 'slytherin'
                    4. 'Amarillo' 'hufflepuff' """))
print("Quinta Pregunta")
preguntaQuinta = int(input("""¿Cuál es tu mascota?
                    1. 'Sapo' 'ravenclaw'
                    2. 'Lechuza' 'gryffindor'
                    3. 'Gato' 'hufflepuff'
                    4. 'Serpiente' 'slytherin' """))

resultadoTotal = todas (preguntaUno,preguntaDos,preguntaTres,preguntaCuatro,preguntaQuinta)
print(resultadoTotal)