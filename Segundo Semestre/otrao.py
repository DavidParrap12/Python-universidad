import tkinter as tk
from tkinter import messagebox, simpledialog

class Contacto:
    def __init__(self, nombre, telefono, email="", direccion=""):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, telefono):
        self.contactos = [contacto for contacto in self.contactos if contacto.telefono != telefono]

    def buscar_contacto(self, consulta):
        return [
            contacto for contacto in self.contactos 
            if consulta.lower() in contacto.nombre.lower() or 
               consulta in contacto.telefono
        ]

class AplicacionAgenda:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.geometry("500x450")
        self.agenda = Agenda()

    def iniciar(self):
        self.raiz.title("Agenda Telefónica")

        tk.Label(self.raiz, text="Búsqueda:").pack()
        self.entrada_busqueda = tk.Entry(self.raiz, width=50)
        self.entrada_busqueda.pack()
        
        tk.Button(self.raiz, text="Buscar", command=self.buscar_contactos).pack()

        self.lista_resultados = tk.Listbox(self.raiz, width=70)
        self.lista_resultados.pack()

        self.area_detalles = tk.Text(self.raiz, height=4, width=70, state=tk.DISABLED)
        self.area_detalles.pack()

        tk.Button(self.raiz, text="Agregar Contacto", command=self.dialogo_agregar_contacto).pack()
        tk.Button(self.raiz, text="Eliminar Contacto", command=self.dialogo_eliminar_contacto).pack()

        self.lista_resultados.bind('<<ListboxSelect>>', self.mostrar_detalles_contacto)

        self.raiz.mainloop()

    def buscar_contactos(self):
        consulta = self.entrada_busqueda.get()
        resultados = self.agenda.buscar_contacto(consulta)
        
        self.lista_resultados.delete(0, tk.END)
        for contacto in resultados:
            self.lista_resultados.insert(tk.END, str(contacto))

    def dialogo_agregar_contacto(self):
        nombre = simpledialog.askstring("Agregar Contacto", "Ingrese nombre:")
        telefono = simpledialog.askstring("Agregar Contacto", "Ingrese teléfono:")
        email = simpledialog.askstring("Agregar Contacto", "Ingrese email (opcional):") or ""
        direccion = simpledialog.askstring("Agregar Contacto", "Ingrese dirección (opcional):") or ""

        contacto = Contacto(nombre, telefono, email, direccion)
        self.agenda.agregar_contacto(contacto)
        messagebox.showinfo("Éxito", "Contacto agregado exitosamente")
        self.buscar_contactos()

    def dialogo_eliminar_contacto(self):
        telefono = simpledialog.askstring("Eliminar Contacto", "Ingrese teléfono:")
        if not telefono:
            return

        self.agenda.eliminar_contacto(telefono)
        messagebox.showinfo("Éxito", "Contacto eliminado")
        self.buscar_contactos()

    def mostrar_detalles_contacto(self, evento):
        if not self.lista_resultados.curselection():
            return

        indice = self.lista_resultados.curselection()[0]
        contacto_str = self.lista_resultados.get(indice)
        contacto = next((c for c in self.agenda.contactos if str(c) == contacto_str), None)

        if contacto:
            self.area_detalles.config(state=tk.NORMAL)
            self.area_detalles.delete(1.0, tk.END)
            self.area_detalles.insert(tk.END, f"Nombre: {contacto.nombre}\n")
            self.area_detalles.insert(tk.END, f"Teléfono: {contacto.telefono}\n")
            self.area_detalles.insert(tk.END, f"Email: {contacto.email}\n")
            self.area_detalles.insert(tk.END, f"Dirección: {contacto.direccion}")
            self.area_detalles.config(state=tk.DISABLED)

# Forma de ejecutar
open = AplicacionAgenda()
open.iniciar()