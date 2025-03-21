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

estudiantes = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o 'salir' para detenerse): ").strip().lower()
    if nombre == 'salir':
        break
    
    apellido = input("Ingresa el apellido del estudiante: ").strip()
    try:
        edad = int(input("Ingresa la edad del estudiante: ").strip())
    except ValueError:
        print("La edad debe ser un número entero. intentalo de nuevo")
        continue
    
    estudiantes[nombre]={"apellido": apellido, "edad": edad}
    
print("\n Informacion del estudiante:")
for estudiante, datos in estudiantes.items():
    print(f"Nombre: {estudiante.capitalize()}, Apellido {datos['apellido']}, Edad: {datos['edad']} ")
    
