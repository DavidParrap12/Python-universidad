class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def agregar_arista(self, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append(destino)
            self.vertices[destino].append(origen)

def menu_arbol():
    arbol = ArbolBinario()
    while True:
        print("\n=== MENÚ ÁRBOL BINARIO ===")
        print("1. Insertar nodo")
        print("2. Mostrar árbol")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            valor = int(input("Ingrese el valor a insertar: "))
            arbol.insertar(valor)
            print("Nodo insertado correctamente")
        elif opcion == "2":
            # Aquí se podría implementar la visualización del árbol
            print("Función de mostrar árbol pendiente de implementar")
        elif opcion == "3":
            break

def menu_grafo():
    grafo = Grafo()
    while True:
        print("\n=== MENÚ GRAFO ===")
        print("1. Agregar vértice")
        print("2. Agregar arista")
        print("3. Mostrar grafo")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            vertice = input("Ingrese el nombre del vértice: ")
            grafo.agregar_vertice(vertice)
            print("Vértice agregado correctamente")
        elif opcion == "2":
            origen = input("Ingrese el vértice origen: ")
            destino = input("Ingrese el vértice destino: ")
            grafo.agregar_arista(origen, destino)
            print("Arista agregada correctamente")
        elif opcion == "3":
            print("Grafo actual:", grafo.vertices)
        elif opcion == "4":
            break

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Árbol Binario")
        print("2. Grafo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_arbol()
        elif opcion == "2":
            menu_grafo()
        elif opcion == "3":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu_principal()
