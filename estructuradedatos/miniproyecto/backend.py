# -*- coding: utf-8 -*-
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
    """Clase que maneja la autenticación de usuarios y control de intentos."""
    def __init__(self):
        """Inicializa el sistema de acceso con valores predeterminados."""
        self.intentos = 0
        self.cola_usuarios = Queue()
        self.usuario_valido = "admin"
        self.clave_valida = "123"
        self.max_intentos = 3

    def verificar_credenciales(self, usuario, clave):
        """
        Verifica si las credenciales proporcionadas son válidas.
        Args:
            usuario: Nombre de usuario
            clave: Contraseña
        """
        # Registrar el intento de acceso
        self.cola_usuarios.put((usuario, clave))
        
        # Verificar credenciales
        if usuario == self.usuario_valido and clave == self.clave_valida:
            return True
        else:
            self.intentos += 1
            return False
    
    def obtener_intentos_restantes(self):
        """
        Calcula los intentos restantes antes del bloqueo.
        
        Returns:
            int: Número de intentos restantes
        """
        return self.max_intentos - self.intentos
    
    def ha_excedido_intentos(self):
        """
        Determina si se ha excedido el número máximo de intentos.
        
        Returns:
            bool: True si se excedió el límite, False en caso contrario
        """
        return self.intentos >= self.max_intentos


class ListaSupermercado:
    """
    Clase que gestiona la creación y mantenimiento de listas de compras.
    """
    def __init__(self):
        """Inicializa el gestor de listas de supermercado."""
        self.listas = {}
        self.id_actual = 1

    def agregar_lista(self, nombre, articulos):
        """
        Agrega una nueva lista de compras.
        
        Args:
            nombre: Nombre de la lista
            articulos: Lista de artículos
            
        Returns:
            int: ID de la lista creada
        """
        self.listas[self.id_actual] = {"nombre": nombre, "articulos": articulos}
        self.id_actual += 1
        return self.id_actual - 1

    def obtener_todas_listas(self):
        """
        Obtiene todas las listas almacenadas.
        
        Returns:
            dict: Diccionario con todas las listas
        """
        return self.listas

    def obtener_lista(self, id_lista):
        """
        Obtiene una lista específica por su ID.
        
        Args:
            id_lista: ID de la lista a obtener
            
        Returns:
            dict: Datos de la lista o None si no existe
        """
        return self.listas.get(id_lista)

    def actualizar_lista(self, id_lista, nombre, articulos):
        """
        Actualiza una lista existente.
        
        Args:
            id_lista: ID de la lista a actualizar
            nombre: Nuevo nombre de la lista
            articulos: Nueva lista de artículos
            
        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario
        """
        if id_lista in self.listas:
            self.listas[id_lista] = {"nombre": nombre, "articulos": articulos}
            return True
        return False

    def eliminar_lista(self, id_lista):
        """
        Elimina una lista existente.
        
        Args:
            id_lista: ID de la lista a eliminar
            
        Returns:
            bool: True si la eliminación fue exitosa, False en caso contrario
        """
        if id_lista in self.listas:
            del self.listas[id_lista]
            return True
        return False


class GestorColas:
    """
    Clase que gestiona las diferentes colas del supermercado.
    """
    def __init__(self):
        """Inicializa las colas del sistema."""
        self.cola_cajas = Queue()
        self.cola_atencion = Queue()
        self.cola_entregas = Queue()

    def agregar_a_cajas(self, cliente):
        """
        Agrega un cliente a la cola de cajas.
        
        Args:
            cliente: Nombre o identificador del cliente
        """
        self.cola_cajas.put(cliente)

    def siguiente_cliente_cajas(self):
        """
        Obtiene el siguiente cliente en la cola de cajas.
        
        Returns:
            str: Cliente a atender o None si la cola está vacía
        """
        return self.cola_cajas.get() if not self.cola_cajas.empty() else None

    def agregar_a_atencion(self, caso):
        """
        Agrega un caso a la cola de atención al cliente.
        
        Args:
            caso: Descripción del caso
        """
        self.cola_atencion.put(caso)

    def siguiente_caso_atencion(self):
        """
        Obtiene el siguiente caso en la cola de atención.
        
        Returns:
            str: Caso a atender o None si la cola está vacía
        """
        return self.cola_atencion.get() if not self.cola_atencion.empty() else None

    def agregar_a_entregas(self, pedido):
        """
        Agrega un pedido a la cola de entregas.
        
        Args:
            pedido: Información del pedido a entregar
        """
        self.cola_entregas.put(pedido)

    def siguiente_entrega(self):
        """
        Obtiene la siguiente entrega en la cola.
        
        Returns:
            str: Entrega a procesar o None si la cola está vacía
        """
        return self.cola_entregas.get() if not self.cola_entregas.empty() else None

    def obtener_tamaños_colas(self):
        """
        Obtiene el tamaño actual de todas las colas.
        
        Returns:
            dict: Diccionario con el tamaño de cada cola
        """
        return {
            "cajas": self.cola_cajas.qsize(),
            "atencion": self.cola_atencion.qsize(),
            "entregas": self.cola_entregas.qsize()
        }