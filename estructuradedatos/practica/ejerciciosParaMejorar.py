productos = [
    {"nombre": "Yuca", "precio": 2500, "cantidad": 20 },
    {"nombre": "Platano", "precio": 1500, "cantidad": 30 },
    {"nombre": "Aguacate", "precio": 3000, "cantidad": 10 }
]

for producto in productos:
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    
paises = {
    "Colombia": {"Capital": "Bogota", "Poblacion": 50_000_000, "Moneda": "COP"},
    "Brasil": {"Capital": "Brasilia", "Poblacion": 200_000_000, "Moneda": "BRL"},
    "Chile": {"Capital": "Santiago de chile", "Poblacion": 20_000_000, "Moneda": "CLP"}
}

#pais nos devuelve los paises y datos nos devuelve los datos de cada pais
for pais, datos in paises.items():
    print(f"Pais {pais}, Capital: {datos ['Capital']}, Poblacion: {datos ['Poblacion']}, Moneda: {datos ['Moneda']}")