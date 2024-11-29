import tkinter as tk
from tkinter import messagebox, simpledialog

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"

class Libro:
    def __init__(self, titulo, autor, isbn, año):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año = año

    def __str__(self):
        return f"{self.titulo} de {self.autor} (ISBN: {self.isbn}, {self.año})"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, isbn):
        self.libros = [libro for libro in self.libros if libro.isbn != isbn]

    def buscar_libro(self, consulta):
        return [
            libro for libro in self.libros 
            if consulta.lower() in libro.titulo.lower() or 
               consulta.lower() in libro.autor.nombre.lower() or 
               consulta == libro.isbn
        ]

class AplicacionBiblioteca:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.geometry("500x400")
        self.biblioteca = Biblioteca()

    def iniciar(self):
        self.raiz.title("Sistema de Gestión de Biblioteca")

        tk.Label(self.raiz, text="Búsqueda:").pack()
        self.entrada_busqueda = tk.Entry(self.raiz, width=50)
        self.entrada_busqueda.pack()
        
        tk.Button(self.raiz, text="Buscar", command=self.buscar_libros).pack()

        self.lista_resultados = tk.Listbox(self.raiz, width=70)
        self.lista_resultados.pack()

        tk.Button(self.raiz, text="Agregar Libro", command=self.dialogo_agregar_libro).pack()
        tk.Button(self.raiz, text="Eliminar Libro", command=self.dialogo_eliminar_libro).pack()

        self.raiz.mainloop()

    def buscar_libros(self):
        consulta = self.entrada_busqueda.get()
        resultados = self.biblioteca.buscar_libro(consulta)
        
        self.lista_resultados.delete(0, tk.END)
        for libro in resultados:
            self.lista_resultados.insert(tk.END, str(libro))

    def dialogo_agregar_libro(self):
        titulo = simpledialog.askstring("Agregar Libro", "Ingrese título:")
        if not titulo:
            return

        nombre_autor = simpledialog.askstring("Agregar Libro", "Ingrese nombre del autor:")
        nacionalidad_autor = simpledialog.askstring("Agregar Libro", "Ingrese nacionalidad del autor:")
        
        isbn = simpledialog.askstring("Agregar Libro", "Ingrese ISBN:")
        año_str = simpledialog.askstring("Agregar Libro", "Ingrese año de publicación:")

        try:
            año = int(año_str)
            autor = Autor(nombre_autor, nacionalidad_autor)
            libro = Libro(titulo, autor, isbn, año)
            self.biblioteca.agregar_libro(libro)
            messagebox.showinfo("Éxito", "Libro agregado exitosamente")
        except ValueError:
            messagebox.showerror("Error", "Año inválido")

    def dialogo_eliminar_libro(self):
        isbn = simpledialog.askstring("Eliminar Libro", "Ingrese ISBN del libro:")
        if not isbn:
            return

        self.biblioteca.eliminar_libro(isbn)
        messagebox.showinfo("Éxito", "Libro eliminado")
        self.buscar_libros()

# Forma de ejecutar
open = AplicacionBiblioteca()
open.iniciar()