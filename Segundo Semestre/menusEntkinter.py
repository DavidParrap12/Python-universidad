# # importamos el tkinter
# import tkinter as tk

# def abrir_archivo():
#     print("Archivo Abierto")

# def cerrar_archivo():
#     print("Archivo cerrado")

# def help():
#     print("En que te puedo ayudar")
# def soporte():
#     print("Estas siendo enviado al soporte")
# ventana = tk.Tk()

# barra_menu = tk.Menu(ventana)
# menu_archivo = tk.Menu(barra_menu, tearoff=0)
# # despliega el menu hacia la derecha
# menu_archivo.add_command(label="Abrir", command=abrir_archivo) #crea el comando abrir
# menu_archivo.add_command(label="Cerrar", command=cerrar_archivo)
# # despliega el menu hacia abajo
# barra_menu.add_cascade(label="Archivo", menu=menu_archivo) #esta diciendo que abrir vaya dentro del archivo

# menu_ayuda = tk.Menu(barra_menu, tearoff=0)
# menu_ayuda.add_command(label="Help", command=help)
# menu_ayuda.add_command(label="Soporte", command=soporte)
# barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# ventana.config(menu=barra_menu)
# ventana.mainloop()

# from tkinter import *
# root = Tk()
# root.title("Mi editor")

# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Nuevo")
# filemenu.add_command(label="Abrir")
# filemenu.add_command(label="Guardar")
# filemenu.add_command(label="Guardar como")
# filemenu.add_separator() #crea una linea entre casillas
# filemenu.add_command(label="Salir", command=root.quit)
# menubar.add_cascade(label="Archivo", menu=filemenu)

# texto = Text(root)
# texto.pack(fill='both', expand=1)
# # padx,pady es el pading bd es el
# texto.config(padx=6, pady=4, bd=0, font=("Consolas", 12))

# root.config(menu=menubar)
# root.mainloop()

# Checkbox

# import tkinter as tk

# def mostrar_estado():
#     print("El checkbox está", "Marcado" if var.get() else "Desmarcado")

# ventana = tk.Tk()

# var = tk.BooleanVar()
# casilla = tk.Checkbutton(ventana, text="Acepta terminos", variable=var, onvalue=True, offvalue=False, command=mostrar_estado)
# casilla.pack()

# ventana.mainloop()

# import tkinter as tk

# def mostrar_seleccion(seleccion):
#     print("Has seleccionado:", seleccion.get())

# ventana = tk.Tk()
# ventana.title("Ejemplo de checkboxes")

# # Variable para almacenar el estado de cada checkbox
# opciones_seleccionadas = tk.StringVar()

# Radio button
# import tkinter as tk

# def seleccionar_forma(forma):
#     print("Has seleccionado:", forma)

# ventana = tk.Tk()
# ventana.title("Seleccion de formas")

# forma_seleccionada = tk.StringVar()

# tk.Radiobutton(ventana, text="Circulo", variable=forma_seleccionada, value="circulo", command=lambda: seleccionar_forma(forma_seleccionada.get())).pack()
# tk.Radiobutton(ventana, text="Cuadrado", variable=forma_seleccionada, value="cuadrado", command=lambda: seleccionar_forma(forma_seleccionada.get())).pack()
# tk.Radiobutton(ventana, text="Triangulo", variable=forma_seleccionada, value="triangulo", command=lambda: seleccionar_forma(forma_seleccionada.get())).pack()

# ventana.mainloop()

# import tkinter as tk
# import tkinter.messagebox as messagebox

# def mostrar_mensajes():
#     messagebox.showinfo("Mensage", "¡Hola Mundo!")

# ventana = tk.Tk()
# boton = tk.Button(ventana, text="Mostrar Mensage", command=mostrar_mensajes)
# boton.pack()

# ventana.mainloop()

# from tkinter import *
# from tkinter import messagebox as Messagebox

# def test():
#     Messagebox.showinfo("Hola", "Hola mundo")
#     Messagebox.showerror("Upa", "Error")
#     Messagebox.showwarning("Upa", "Advertencia")

# root = Tk()
# Button(root, text="Clicame", command=test).pack()

# root.mainloop()

# modelo de pregunta para que decidan si o no
# import tkinter as tk
# import tkinter.messagebox as messagebox
"toca copiarlo en la casa"

# # cuadro de dialogo
# import tkinter as tk
# import tkinter.filedialog as filedialog

# def abrir_archivo():
#     archivo = filedialog.askopenfilename()
#     print("Archivo seleccionado:", archivo)

# ventana = tk.Tk()
# boton = tk.Button(ventana, text="Abrir Archivo", command=abrir_archivo)
# boton.pack()

# ventana.mainloop()

# import tkinter as tk

# ventana = tk.Tk()

# lista_frutas = tk.Listbox(ventana)
# lista_frutas.insert(tk.END, "Manzana")
# lista_frutas.insert(tk.END, "Banana")
# lista_frutas.pack()

# ventana.mainloop()