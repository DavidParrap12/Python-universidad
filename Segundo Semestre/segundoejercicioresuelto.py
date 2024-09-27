class CalificacionProducto():
    def __init__(self):
        self.calificacionTotal = 0
        self.numeroCalificacion = 0

    def ingresarCalificacion(self, nota):
        if nota>= 1 and nota <=5:
            self.calificacionTotal+=nota
            self.numeroCalificacion+=1
            print("Se ha ingresado la nota")
        else:
            print("nota no valida")

    def mostrarPromedio(self):
        if self.numeroCalificacion > 0 and self.numeroCalificacion > 0:
            return self.calificacionTotal / self.numeroCalificacion
        else:
            return False
def menu():
    print("Bienvenidos al conversor de moneda")
    calificaciones = CalificacionProducto()
    while True:

        opcion = int(input("1. Ingresar calificacion \n 2 mostrar resultado \n 3 salir "))
        if opcion == 1:
            nota = print("Ingrese la nota")
            calificaciones.ingresarCalificacion(nota)
        elif opcion == 2:
            promedio = calificaciones.mostrarPromedio()
            if promedio == False:
                print("promedio no se puede realizar debe tener al menos una nota")
                continue
            else:
                print("El resultado del promedio es: {promedio}")
        elif opcion ==3:
            del nuevaConversion
            break

menu()
