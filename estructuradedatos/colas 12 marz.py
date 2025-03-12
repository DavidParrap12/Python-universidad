from collections import deque

#crear cola vacia
cola= deque()
#agregar elementos
cola.append("A")
cola.append("B")
cola.append("C")
cola.append("D")
cola.append("E")
cola.append("F")

print("cola despues de encolar:", cola)

#eliminar el primer elemento
elemento = cola.popleft()
print("elemento eliminado:", elemento)
print("cola despues de eliminar", cola)

#obtener el primer elemento
if cola:
    print("primer elemento (front):", cola[0])
#obtener el ultimo elemento
if cola:
    print("ultimo elemento(rear):", cola[-1])
#verificar que a cola este vacia 
print("la cola esta vacia?", len(cola) == 0)
#obtener el tamaño de la cola
print("tamaño de la cola:", len(cola))
