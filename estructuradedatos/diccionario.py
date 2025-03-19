#Manejo de diccionarios en python. Mutables
empleado = {"IdCliente": 1, "Nombre": "David", "Apellido": "Parra", "Edad": 22}
print(type(empleado))
print(empleado)

productos = {"Manzana": 1,"Peras": 3,"Mangos": 1200,
             "Bananos": 500, "Naranjas": 1000,
            }

print("Inventario Inicial :", productos)

#Adicionar un nuevo producto al inventario
productos.update({"Granadilla": 5000})
print("Inventario despues de agregar Granadilla :", productos)

#Obtener las claves, valores y pares clave-valor
print("Claves del inventario", productos.keys())
print("Valor del inventario", productos.values())
print("Elementos del inventario", productos.items())

#Obtener la cantidad del producto
producto = "Manzanas"
cantidad = productos.get(producto, "Producto no encontrado ")
print(f"La cantidad de {producto}, es: {cantidad}")

#Eliminar un producto 
producto_eliminado = "Plátanos"
cantidad_elimnidada = productos.pop(producto_eliminado, "Producto no encontrado")
print(f"Se elimino {producto_eliminado}, Cantidad eliminada: {cantidad_elimnidada}")
print("Inventario despues de eliminar plátanos:", productos)

#Eliminar un par clave-valor aleatorio
clave, valor = productos.popitem()
print(f"Se elimino el producto {clave}, con cantidad {valor}")
print("Inventario despues de elminiar un producto aleatorio", producto)

#Vaciar el inventario
productos.clear()