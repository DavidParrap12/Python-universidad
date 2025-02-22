import menuUsuario as mU
from tkinter import *
from tkinter import ttk

#crear la instancia de la clase RegistroUsuario
registro_usuario = mU.RegistroUsuario()

#Configurar la ventana principal
ventana = Tk()
ventana.geometry("400x400")
ventana.title("Menu Principal")

def abrir_menu_usuario():
    menu_usuario = Toplevel(ventana)
    menu_usuario.title("Menu Usuario")
    menu_usuario.geometry("400x400")
    
    Label(menu_usuario, text="Bienvenidos al sistema de gestion de Usuario").pack()

    Button(menu_usuario, text="Registrar Usuario", command=registro_usuario.registro).pack()
    Button(menu_usuario, text="Modificar Usuario", command=registro_usuario.modificarUsuario).pack()        
    Button(menu_usuario, text="Eliminar Usuario", command=registro_usuario.eliminarUsuario).pack()      
    Button(menu_usuario, text="Listar Usuarios", command=registro_usuario.listarUsuarios).pack()    
    
    
#Boton para abrir el menu de usuario
Button(ventana, text="Menu Usuario", command=abrir_menu_usuario).pack()

ventana.mainloop()

