estudiantes = []

while True: 
    nombre = input("Ingresa el nombre del estudiante (o 'salir' para detenerse): ").strip().lower()
    if nombre == 'salir':
        break
    apellido = input("Ingresa el apellido del estudiante: ").strip()
    try:
        edad = int(input("Ingresa la edad del estudiante: ").strip())
    except ValueError:
        print("La edad debe ser un número entero. Inténtalo de nuevo.")
        continue
    
    estudiantes.append({'nombre': nombre, 'apellido': apellido, 'edad': edad})
    
print("\n Informacion del estudiante:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}, Edad: {estudiante['edad']}")