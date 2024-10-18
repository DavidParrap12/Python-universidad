"""Enunciado: Diseña un sistema para gestionar una biblioteca. Crea una clase Libro que contenga los atributos 
título, autor y número de páginas. La clase Ebook hereda de Libro y agrega el formato del libro (por ejemplo, "PDF", "EPUB"). 
Usa setters y getters para manipular los atributos. Implementa un menú que permita:
Registrar libros.
Registrar ebooks.
Mostrar todos los libros y ebooks.
Modificar el formato de un ebook registrado.
Clases involucradas:
Libro: título, autor, número de páginas.
Ebook: hereda de Libro y añade formato.
"""
# Clase base
class Libro:
    def __init__(self, titulo, autor, num_Paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__num_Paginas = num_Paginas
    
    def descripcion(self):
        return f"Titulo del libro {self.__titulo}, autor {self.__autor}, y numero de paginas {self.__num_Paginas}"
    
    # getter
    @property
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getNum_Pag(self):
        return self.__num_Paginas
    
    # setter
    def setTitulo(self, titulo):
        self.__titulo = titulo
    def setAutor(self, autor):
        self.__autor = autor
    def setNum_Pag(self, num_paginas):
        self.__num_Paginas = num_paginas
        
# Clase heredera de libro  
class Ebook(Libro):
    def __init__(self, titulo, autor, num_Paginas, formato):
        super().__init__(titulo, autor, num_Paginas)
        self.__formato = formato
        
    
    def descripcion(self):
        return f"{self.descripcion}, en el formato {self.__formato}"
    
    # setter
    def getFormato(self):
        return self.__formato
    
    # setter
    def setFormato(self, formato):
        self.__formato = formato
    # Clase para ejecutar todo 
class SistemaGestionBiblioteca:  
    
    def __init__(self):
        self.libros = []
        self.ebooks = []
    # agregamos libros
    def agregar_Libros(self, libro):
        self.libros.append(libro)
    # registramos los libros
    def registrar_libros(self):
        titulo = input("Ingrese el titulo del libro")
        autor = input("Ingrese el autor del libro")
        num_Paginas = int(input("Ingrese la cantidad de paginas que contiene el libro"))
        libro = Libro(titulo, autor, num_Paginas)
        
        self.agregar_Libros(libro)
        print("libro registrado correctamente")
    # agregamos ebooks
    def agregbooks(self, ebook):
        self.ebooks.append(ebook)
    # registramos los ebooks
    def registrar_ebooks(self):
        titulo = input("Ingrese el titulo del ebook")
        autor = input("Ingrese el autor del ebook")
        num_Paginas = int(input("Ingrese la cantidad de paginas que contiene el ebook"))
        formato = input("Ingrese el formato del ebook (PDF, EPUB, etc...)")
        ebook = Ebook(titulo, autor, num_Paginas, formato)
        
        self.agrebooks(ebook)
        print("Ebook registrado correctamente")
        # mostramos los libros y ebooks
    def mostrar_liEbooks(self):
        for libro in self.libros:
            print(libro.descripcion())
        for ebook in self.ebooks:
            print (ebook.descripcion())
    
    def modificar_formato_ebook(self):
        titulo = input("Ingrese el título del ebook cuyo formato desea modificar: ")
        encontrado = False
        for ebook in self.ebooks:
            if ebook.titulo == titulo:
                nuevo_formato = input("Ingrese el nuevo formato (PDF, EPUB, etc.): ")
                ebook.formato = nuevo_formato
                print(f"Formato del ebook '{titulo}' actualizado correctamente.\n")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el ebook con el título '{titulo}'.\n")

    def menu(self):
        while True:
            op = print("Selecciona la opcion que deseas \n 1. Registrar libros \n 2. Registrar ebooks \n 3. Mostrar todos los libros y ebooks \n 4. Modificar el formato de un ebook \n 5. Salir")
            if op == 1:
                self.registrar_libros()
            elif op == 2:
                self.registrar_ebooks()
            elif op == 3:
                self.mostrar_liEbooks()
            elif op == 4:
                self.modificar_formato_ebook()
            else:
                print("Saliendo del Sistema de Gestion De La Biblioteca")
                break

SystemBiblioteca = SistemaGestionBiblioteca()
SystemBiblioteca.menu()