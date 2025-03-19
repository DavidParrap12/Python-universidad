# -*- coding: utf-8 -*-
"""
Sistema de Gestión de Supermercado
interfaz gráfica para un sistema de gestión de supermercado
que incluye inicio de sesión, gestión de listas de compras y administración de colas.
"""
from tkinter import *
from tkinter import messagebox, simpledialog
from backend import SistemaAcceso, ListaSupermercado, GestorColas

class AplicacionAcceso:
    """Clase que maneja la ventana de inicio de sesión y acceso al sistema principal."""
    
    def __init__(self, raiz):
        """ raiz: Ventana principal de Tkinter"""
        self.raiz = raiz
        self.raiz.title("Sistema de Acceso")
        self.raiz.geometry("300x150")
        
        # Inicializa sistema backend
        self.sistema_acceso = SistemaAcceso()
        
        # Crea elementos de la interfaz gráfica
        self.marco = Frame(raiz)
        self.marco.pack(pady=20)
        
        # Usuario
        Label(self.marco, text="Usuario:").grid(row=0, column=0, padx=5, pady=5)
        self.usuario = Entry(self.marco)
        self.usuario.grid(row=0, column=1, padx=5, pady=5)
        
        # Contraseña
        Label(self.marco, text="Clave:").grid(row=1, column=0, padx=5, pady=5)
        self.clave = Entry(self.marco, show="*")
        self.clave.grid(row=1, column=1, padx=5, pady=5)
        
        # Botón de acceso
        self.boton_acceso = Button(self.marco, text="Ingresar", command=self.verificar_acceso)
        self.boton_acceso.grid(row=2, column=0, columnspan=2, pady=10)

    def verificar_acceso(self):
        """Verifica las credenciales de usuario y gestiona los intentos fallidos."""
        usuario = self.usuario.get()
        clave = self.clave.get()
        
        if self.sistema_acceso.verificar_credenciales(usuario, clave):
            messagebox.showinfo("Éxito", "¡Acceso exitoso!")
            self.raiz.destroy()
            self.mostrar_ventana_principal()
        else:
            if self.sistema_acceso.ha_excedido_intentos():
                messagebox.showerror("Error", "Máximo de intentos alcanzado. La aplicación se cerrará.")
                self.raiz.destroy()
            else:
                restantes = self.sistema_acceso.obtener_intentos_restantes()
                messagebox.showerror("Error", f"Credenciales inválidas. Intentos restantes: {restantes}")
                self.usuario.delete(0, END)
                self.clave.delete(0, END)

    def mostrar_ventana_principal(self):
        """Muestra la ventana principal del sistema de gestión."""
        ventana_principal = Tk()
        ventana_principal.title("Sistema de Gestión de Supermercado")
        ventana_principal.geometry("800x600")
        
        # Etiqueta de bienvenida
        Label(ventana_principal, text="Bienvenido al Sistema de Gestión de Supermercado", 
            font=("Arial", 14)).pack(pady=10)
        
        # Inicializa gestores
        self.gestor_listas = ListaSupermercado()
        self.gestor_colas = GestorColas()
        
        # Crea barra de menú
        barra_menu = Menu(ventana_principal)
        ventana_principal.config(menu=barra_menu)
        
        # Crea menú de Listas
        menu_listas = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Listas Supermercado", menu=menu_listas)
        
        # Agrega opciones del menú Listas
        menu_listas.add_command(label="Nueva Lista", command=lambda: self.crear_nueva_lista(ventana_principal))
        menu_listas.add_command(label="Ver Listas", command=lambda: self.ver_listas(ventana_principal))
        menu_listas.add_command(label="Editar Lista", command=lambda: self.editar_lista(ventana_principal))
        menu_listas.add_command(label="Eliminar Lista", command=lambda: self.eliminar_lista(ventana_principal))
        menu_listas.add_separator()
        
        # Crea menú de Colas
        menu_colas = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Sistema de Colas", menu=menu_colas)
        
        # Agrega opciones del menú Colas
        menu_colas.add_command(label="Cola de Cajas", command=lambda: self.gestionar_cola_cajas(ventana_principal))
        menu_colas.add_command(label="Cola de Atención al Cliente", command=lambda: self.gestionar_cola_servicio(ventana_principal))
        menu_colas.add_command(label="Cola de Entregas", command=lambda: self.gestionar_cola_entregas(ventana_principal))
        menu_colas.add_command(label="Ver Estado de Colas", command=lambda: self.ver_estado_colas(ventana_principal))
        
        menu_listas.add_command(label="Salir", command=ventana_principal.destroy)

        # Área de contenido principal
        self.marco_principal = Frame(ventana_principal)
        self.marco_principal.pack(fill=BOTH, expand=True, padx=20, pady=20)

    def crear_nueva_lista(self, ventana):
        """ Crea una nueva lista de compras. """
        nombre = simpledialog.askstring("Nueva Lista", "Nombre de la lista:")
        if nombre:
            ventana_items = Toplevel(ventana)
            ventana_items.title("Agregar Artículos")
            ventana_items.geometry("400x300")

            marco_items = Frame(ventana_items)
            marco_items.pack(pady=20)

            texto_items = Text(marco_items, height=10, width=40)
            texto_items.pack()
            Label(marco_items, text="Ingrese un artículo por línea").pack()

            def guardar_items():
                """Guarda los artículos de la lista en el gestor."""
                items = texto_items.get("1.0", END).strip().split("\n")
                id_lista = self.gestor_listas.agregar_lista(nombre, items)
                messagebox.showinfo("Éxito", "¡Lista creada exitosamente!")
                ventana_items.destroy()

            Button(marco_items, text="Guardar", command=guardar_items).pack(pady=10)

    def ver_listas(self, ventana):
        """ Muestra todas las listas existentes."""
        listas = self.gestor_listas.obtener_todas_listas()
        ventana_vista = Toplevel(ventana)
        ventana_vista.title("Ver Listas")
        ventana_vista.geometry("500x400")

        for id_lista, datos_lista in listas.items():
            marco = Frame(ventana_vista)
            marco.pack(fill=X, padx=10, pady=5)
            Label(marco, text=f"Lista: {datos_lista['nombre']}", font=("Arial", 12, "bold")).pack(anchor=W)
            for item in datos_lista['articulos']:
                Label(marco, text=f"- {item}").pack(anchor=W)
            Label(marco, text="-"*50).pack(fill=X)

    def editar_lista(self, ventana):
        """ Edita una lista existente."""
        listas = self.gestor_listas.obtener_todas_listas()
        if not listas:
            messagebox.showinfo("Info", "No hay listas para editar")
            return

        id_lista = simpledialog.askinteger("Editar Lista", "ID de la lista a editar:")
        if id_lista in listas:
            datos_lista = self.gestor_listas.obtener_lista(id_lista)
            ventana_edicion = Toplevel(ventana)
            ventana_edicion.title(f"Editar Lista: {datos_lista['nombre']}")
            ventana_edicion.geometry("400x300")

            var_nombre = StringVar(value=datos_lista['nombre'])
            Entry(ventana_edicion, textvariable=var_nombre).pack(pady=5)

            texto_items = Text(ventana_edicion, height=10, width=40)
            texto_items.pack(pady=5)
            texto_items.insert("1.0", "\n".join(datos_lista['articulos']))

            def guardar_cambios():
                """Guarda los cambios realizados en la lista."""
                nuevo_nombre = var_nombre.get()
                nuevos_items = texto_items.get("1.0", END).strip().split("\n")
                self.gestor_listas.actualizar_lista(id_lista, nuevo_nombre, nuevos_items)
                messagebox.showinfo("Éxito", "¡Lista actualizada!")
                ventana_edicion.destroy()

            Button(ventana_edicion, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)
        else:
            messagebox.showerror("Error", "Lista no encontrada")

    def eliminar_lista(self, ventana):
        """Elimina una lista existente."""
        id_lista = simpledialog.askinteger("Eliminar Lista", "ID de la lista a eliminar:")
        if id_lista is not None:
            if self.gestor_listas.eliminar_lista(id_lista):
                messagebox.showinfo("Éxito", "¡Lista eliminada exitosamente!")
            else:
                messagebox.showerror("Error", "Lista no encontrada")

    def gestionar_cola_cajas(self, ventana):
        """Gestiona la cola de cajas de pago."""
        ventana_cola = Toplevel(ventana)
        ventana_cola.title("Cola de Cajas")
        ventana_cola.geometry("400x300")
        
        marco = Frame(ventana_cola)
        marco.pack(pady=20)
        
        def agregar_cliente():
            """Agrega un nuevo cliente a la cola de cajas."""
            cliente = simpledialog.askstring("Nuevo Cliente", "Nombre del cliente:")
            if cliente:
                self.gestor_colas.agregar_a_cajas(cliente)
                actualizar_estado()
        
        def siguiente_cliente():
            """Procesa al siguiente cliente en la cola."""
            cliente = self.gestor_colas.siguiente_cliente_cajas()
            if cliente:
                messagebox.showinfo("Siguiente Cliente", f"Atendiendo a: {cliente}")
                actualizar_estado()
            else:
                messagebox.showinfo("Cola Vacía", "No hay clientes en espera")
        
        def actualizar_estado():
            """Actualiza la información del estado de la cola."""
            tamaño = self.gestor_colas.obtener_tamaños_colas()["cajas"]
            etiqueta_estado.config(text=f"Clientes en espera: {tamaño}")
        
        Button(marco, text="Agregar Cliente", command=agregar_cliente).pack(pady=5)
        Button(marco, text="Siguiente Cliente", command=siguiente_cliente).pack(pady=5)
        etiqueta_estado = Label(marco, text="Clientes en espera: 0")
        etiqueta_estado.pack(pady=10)

    def gestionar_cola_servicio(self, ventana):
        """Gestiona la cola de atención al cliente."""
        ventana_cola = Toplevel(ventana)
        ventana_cola.title("Cola de Atención al Cliente")
        ventana_cola.geometry("400x300")
        
        marco = Frame(ventana_cola)
        marco.pack(pady=20)
        
        def agregar_caso():
            """Agrega un nuevo caso a la cola de atención."""
            asunto = simpledialog.askstring("Nuevo Caso", "Descripción del caso:")
            if asunto:
                self.gestor_colas.agregar_a_atencion(asunto)
                actualizar_estado()
        
        def siguiente_caso():
            """Procesa el siguiente caso en la cola."""
            caso = self.gestor_colas.siguiente_caso_atencion()
            if caso:
                messagebox.showinfo("Siguiente Caso", f"Atendiendo caso: {caso}")
                actualizar_estado()
            else:
                messagebox.showinfo("Cola Vacía", "No hay casos pendientes")
        
        def actualizar_estado():
            """Actualiza la información del estado de la cola."""
            tamaño = self.gestor_colas.obtener_tamaños_colas()["atencion"]
            etiqueta_estado.config(text=f"Casos pendientes: {tamaño}")
        
        Button(marco, text="Registrar Caso", command=agregar_caso).pack(pady=5)
        Button(marco, text="Siguiente Caso", command=siguiente_caso).pack(pady=5)
        etiqueta_estado = Label(marco, text="Casos pendientes: 0")
        etiqueta_estado.pack(pady=10)

    def gestionar_cola_entregas(self, ventana):
        """Gestiona la cola de entregas a domicilio."""
        ventana_cola = Toplevel(ventana)
        ventana_cola.title("Cola de Entregas")
        ventana_cola.geometry("400x300")
        
        marco = Frame(ventana_cola)
        marco.pack(pady=20)
        
        def agregar_entrega():
            """Agrega una nueva entrega a la cola."""
            direccion = simpledialog.askstring("Nueva Entrega", "Dirección de entrega:")
            if direccion:
                self.gestor_colas.agregar_a_entregas(direccion)
                actualizar_estado()
        
        def siguiente_entrega():
            """Procesa la siguiente entrega en la cola."""
            entrega = self.gestor_colas.siguiente_entrega()
            if entrega:
                messagebox.showinfo("Siguiente Entrega", f"Entrega a: {entrega}")
                actualizar_estado()
            else:
                messagebox.showinfo("Cola Vacía", "No hay entregas pendientes")
        
        def actualizar_estado():
            """Actualiza la información del estado de la cola."""
            tamaño = self.gestor_colas.obtener_tamaños_colas()["entregas"]
            etiqueta_estado.config(text=f"Entregas pendientes: {tamaño}")
        
        Button(marco, text="Nueva Entrega", command=agregar_entrega).pack(pady=5)
        Button(marco, text="Procesar Entrega", command=siguiente_entrega).pack(pady=5)
        etiqueta_estado = Label(marco, text="Entregas pendientes: 0")
        etiqueta_estado.pack(pady=10)

    def ver_estado_colas(self, ventana):
        """Muestra el estado actual de todas las colas."""
        tamaños = self.gestor_colas.obtener_tamaños_colas()
        mensaje_estado = f"""Estado actual de las colas:

    Cajas: {tamaños['cajas']} clientes
    Atención al Cliente: {tamaños['atencion']} casos
    Entregas: {tamaños['entregas']} pedidos"""
        messagebox.showinfo("Estado de Colas", mensaje_estado)

"""Llamamos la aplicaciom¿n"""
if __name__ == "__main__":
    raiz = Tk()
    app = AplicacionAcceso(raiz)
    raiz.mainloop()