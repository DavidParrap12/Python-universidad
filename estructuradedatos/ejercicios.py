"""#tuplas
diasSemana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
print(diasSemana[2]) #Miercoles

#diasSemana[3] = "Fiesta"

listaUno = {1,2,3,4,5,6}
print(listaUno)
listaDos = {4,5,6,7,8,9}
print(listaDos)

union = listaUno.union(listaDos)
print(union) 

interseccion = listaUno.intersection(listaDos)
print(interseccion)

diferencia = listaUno.difference(listaDos)
print(diferencia) # {1, 2, 3}

infoEstudiantes = {"Nombre": "Pepito", "Edad": 81, "Curso": 11}

infoEstudiantes.update({"Edad": 22})
print(infoEstudiantes) 

infoEstudiantes.update({"Nota": 5})
print("agregado nota: ", infoEstudiantes)"""

estudiantes = {
    "estudiante1" : 
        "nombre" : "",
        "apellido": "",
        "edad": 0,
    
}

def agregar_estudiantes():
    agregar[estudiantes]

print(estudiantes.keys())
