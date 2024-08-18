#Mostramos los productos disponibles
print ("Bienvenidos a la maquina exprendedora ")
print("""Los productos que tenemos son: 
    1. Agua $1500
    2. Coca Cola $2000
    3. Cerveza $3500
    4. Pizza $8000
    5. Donut $4000 """)
#Solicitamos al cliente que seleccione el producto y ingrese el valor
cliente = int(input("Seleccione que producto desea comprar "))
dineroCliente = int(input("Ingrese la cantidad con la que va a pagar "))
#Hacemos la funcion para que haga el calculo y demas
def precios (cliente, dineroCliente):
    productos = {1: 1500, 2: 2000, 3: 3500, 4: 8000, 5: 4000}
    if cliente in productos:
        #Buscara el valor seleccionado que el cliente elija
        precioProductos = productos[cliente]
        if dineroCliente >= precioProductos:
            total = dineroCliente - precioProductos
            return(f"Compra exitosa, sus devueltas son: {total}" )
        else:
            return("Valor insuficiente ")
    else:
        print("Producto no valido")
#Mostramos el valor total de la funcion precios
precioTotal = precios(cliente, dineroCliente)
print (precioTotal)