productos = [
    {"nombre": "Yuca", "precio": 2500, "cantidad": 20 },
    {"nombre": "Platano", "precio": 1500, "cantidad": 30 },
    {"nombre": "Aguacate", "precio": 3000, "cantidad": 10 }
]

for producto in productos:
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    
paises = {
    "Pais": {"Colombia": "Bogota", "Poblacion": 50_000_000, "Moneda": "COP"},
    "Pais": {"Brasil": "Brasilia", "Poblacion": 200_000_000, "Moneda": "BRL"},
    "Pais": {"Chile": "Santiago de chile", "Poblacion": 20_000_000, "Moneda": "CLP"}
}

for pais in paises.items:
    print(f"Pais {pais}, Capital: {paises[pais]['Capital']}, Poblacion: {paises[pais]['Poblacion']}, Moneda: {paises[pais]['Moneda']}")