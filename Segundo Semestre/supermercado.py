class Producto:
    def __init__(self, nombre, precioUnit, cantidad):
        self.nombre = nombre
        self.precioUnit = precioUnit
        self.cantidad = cantidad
        
    def precio_Total(self):
        return self.cantidad * self.precioUnit
    
Factura = []   

def ingreso_Productos():
    nombre= input("Ingrese el producto que desea comprar: ")
    precioUnit = float(input(f"Ingrese el precio por unidad de {nombre}: "))
    cantidad = int(input("Ingrese la cantidad que deseas comprar "))
        
    producto = Producto(nombre, precioUnit, cantidad) 
    Factura.append(producto)

def imprimir_factura():
    subtotal = 0
    print("\n ********FACTURA********")
    for producto in Factura:
        total_producto = Producto.precio_Total()
        print(f"{Producto.nombre}: {Producto.precio_unitario} x {Producto.cantidad} = {total_producto}")
        subtotal += total_producto
        
    iva = subtotal * 19
    total = subtotal + iva
    print(f"\nSubtotal: {subtotal}")
    print(f"IVA (13%): {iva}")
    print(f"Total a pagar: {total}\n")
        
def menu():
    print("Bienvenidos al supermercado")
    while True:
        opcion = int(input("1. Ingresar Producto \n 2 Imprimir factura \n 3 salir "))
        if opcion == 1:
            ingreso_Productos()
        elif opcion == 2:
            imprimir_factura()
        elif opcion ==3:
            print("Factura generada, gracias por usar nuestro servicio")
            break
        else:
            print("Opcion no valida")

menu()
