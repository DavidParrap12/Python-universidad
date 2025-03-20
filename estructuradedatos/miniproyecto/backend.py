"""
Backend del Sistema de Gestión de Supermercado
----------------------------------------------
implementa las clases de backend para el sistema:
- SistemaAcceso: Maneja la autenticación de usuarios
- ListaSupermercado: Gestiona las listas de compras
- GestorColas: Administra las diferentes colas del supermercado
"""

from queue import Queue

class SistemaAcceso:
    """Esta clase se encarga de ver si el usuario puede entrar al sistema o no."""
    def __init__(self):
        """Arranca el sistema con valores por defecto."""
        self.intentos = 0
        self.cola_usuarios = Queue()
        self.usuario_valido = "admin"
        self.clave_valida = "123"
        self.max_intentos = 3

    def verificar_credenciales(self, usuario, clave):
        """Mira si el usuario y la clave son correctos."""
        # Guardamos el intento
        self.cola_usuarios.put((usuario, clave))
        
        # Vemos si es válido
        if usuario == self.usuario_valido and clave == self.clave_valida:
            return True
        else:
            self.intentos += 1
            return False
    
    def obtener_intentos_restantes(self):
        """Cuenta cuántos intentos le quedan al usuario."""
        return self.max_intentos - self.intentos
    
    def ha_excedido_intentos(self):
        """Mira si ya se pasó del límite de intentos."""
        return self.intentos >= self.max_intentos


class ListaSupermercado:
    """Esta clase maneja las listas de compras del supermercado."""
    def __init__(self):
        """Arranca con una lista vacía."""
        self.listas = {}
        self.id_actual = 1

    def agregar_lista(self, nombre, articulos):
        """Añade una nueva lista de compras."""
        self.listas[self.id_actual] = {"nombre": nombre, "articulos": articulos}
        self.id_actual += 1
        return self.id_actual - 1

    def obtener_todas_listas(self):
        """Devuelve todas las listas que tenemos."""
        return self.listas

    def obtener_lista(self, id_lista):
        """ Busca una lista por su número."""
        return self.listas.get(id_lista)

    def actualizar_lista(self, id_lista, nombre, articulos):
        """Cambia una lista que ya existe."""
        if id_lista in self.listas:
            self.listas[id_lista] = {"nombre": nombre, "articulos": articulos}
            return True
        return False

    def eliminar_lista(self, id_lista):
        """Borra una lista que ya no queremos."""
        if id_lista in self.listas:
            del self.listas[id_lista]
            return True
        return False


class GestorColas:
    """Esta clase maneja las filas de gente en el supermercado."""
    def __init__(self):
        """Crea las colas vacías."""
        self.cola_cajas = Queue()
        self.cola_atencion = Queue()
        self.cola_entregas = Queue()

    def agregar_a_cajas(self, cliente):
        """Mete a un cliente en la fila para pagar."""
        self.cola_cajas.put(cliente)

    def siguiente_cliente_cajas(self):
        """Llama al siguiente cliente para pagar."""
        return self.cola_cajas.get() if not self.cola_cajas.empty() else None

    def agregar_a_atencion(self, caso):
        """Añade un problema a la fila de atención al cliente."""
        self.cola_atencion.put(caso)

    def siguiente_caso_atencion(self):
        """Saca el siguiente problema de la fila de atención."""
        return self.cola_atencion.get() if not self.cola_atencion.empty() else None

    def agregar_a_entregas(self, pedido):
        """ Mete un pedido a la fila de entregas."""
        self.cola_entregas.put(pedido)

    def siguiente_entrega(self):
        """Saca el siguiente pedido para entregar."""
        return self.cola_entregas.get() if not self.cola_entregas.empty() else None

    def obtener_tamaños_colas(self):
        """Cuenta cuánta gente hay en cada fila."""
        return {
            "cajas": self.cola_cajas.qsize(),
            "atencion": self.cola_atencion.qsize(),
            "entregas": self.cola_entregas.qsize()
        }