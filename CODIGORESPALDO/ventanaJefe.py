# Importar el modulo 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from turtle import color




def avisoConstruccion():
    messagebox.showerror(title = "EN CONSTRUCCION", message = "Modulo aún en construcción uwu")



# Crear la funcion para la ventana del Jefe de Ventas
def ventanaJefe():
    root = Tk()
    # Definir el tamaño
    root.geometry("1280x720")
    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente=Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )
    #FUNCIONES DE LOS BOTONES, SE LLAMAN CON "COMMAND"
    def abrirVentanaReportes():
        root.destroy()
        ventanaReportes()
    
    def abrirVentanaInventario():
        root.destroy()
        ventanaInventario()
    
    def cerrarSesion():
        root.destroy()
        login()
    # Añadir las imagenes
    bg = PhotoImage( file = "IMG/BG.png")
    root.configure(bg = "#2148c0")
    #quitar los bordes del programa
    root.overrideredirect(True)
    botoninventario=PhotoImage(file="IMG/BOTON INVENTARIO.png")
    botonreportes=PhotoImage(file="IMG/BOTON REPORTESSINFONDO.png")
    botoniniciarcerrar=PhotoImage(file="IMG/BOTON INICIARCERRAR DIA.png")
    botonvendedor=PhotoImage(file="IMG/BOTON VENDEDOR.PNG")
    botoncerrarsesion=PhotoImage(file="IMG/BOTON CERRAR SESION.PNG")
  
    # Mostrar las imagenes usando LABEL
    label1 = Label( root, image = bg, bg='#2148c0' )
    label1.place(x = 0,y = 0)

    botonlabel= Label(root,image=botoninventario)
    botonlabel2= Label(root,image=botonreportes)
    botonlabel3= Label(root, image=botoniniciarcerrar)
    botonlabel4= Label(root, image=botonvendedor)
    botonlabel5= Label(root, image=botoncerrarsesion)

    #Crear boton y asignar función correspondiente con "command"
    button=Button(root,image=botoninventario,borderwidth=0,bg='#2148c0', command=abrirVentanaInventario)
    button.place(x=155.31,y=145.32)

    button2=Button(root,image=botonreportes,borderwidth=0,bg='#2148c0', command=avisoConstruccion)
    button2.place(x=705,y=145)

    button3=Button(root,image=botoniniciarcerrar,borderwidth=0,bg='#2148c0', command=avisoConstruccion)
    button3.place(x=152.31,y=405.32)

    button4=Button(root,image=botonvendedor,borderwidth=0,bg='#2148c0', command=avisoConstruccion)
    button4.place(x=705,y=405.32)
    
    button5=Button(root,image=botoncerrarsesion,borderwidth=0,bg='#2148c0', command=cerrarSesion)
    button5.place(x=881,y=34)

    # Execute tkinter
    root.mainloop()

def ventanaInventario():
    root = Tk()
    # Definir el tamaño
    root.geometry("1280x720")
    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente=Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )
    # Añadir las imagenes
    bg = PhotoImage( file = "IMG/BG.png")
    root.configure(bg = "#2148c0")
    root.overrideredirect(True)

    #MODIFICAR LOS BOTONES PARA LA VENTANA REPORTES
    botonagregarproducto=PhotoImage(file="IMG/Group 5.png")
    botonborrarproducto=PhotoImage(file="IMG/borrarproducto.png")
    botonmodificarproducto=PhotoImage(file="IMG/modificarproducto.png")
    botonsalir=PhotoImage(file="IMG/botonsalir.png")
  
    # Mostrar las imagenes usando LABEL
    label1 = Label( root, image = bg, bg='#2148c0' )
    label1.place(x = 0,y = 0)

    botonlabel= Label(root,image=botonagregarproducto)
    botonlabel2= Label(root,image=botonborrarproducto)
    botonlabel3= Label(root, image=botonmodificarproducto)
    botonlabel4= Label(root, image=botonsalir)

    #definir funciones de los botones

    def salir():
        root.destroy()
        ventanaJefe()


    #Crear boton
    button=Button(root,image=botonagregarproducto,borderwidth=0,bg='#2148c0')
    button.place(x=149,y=145)

    button2=Button(root,image=botonborrarproducto,borderwidth=0,bg='#2148c0')
    button2.place(x=705,y=145)

    button3=Button(root,image=botonmodificarproducto,borderwidth=0,bg='#2148c0')
    button3.place(x=149,y=405)

    button4=Button(root,image=botonsalir,borderwidth=0,bg='#2148c0', command=salir)
    button4.place(x=705,y=405)
    

    # Execute tkinter
    root.mainloop()

def ventanaReportes():
    root = Tk()
    # Definir el tamaño
    root.geometry("1280x720")
    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente=Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )
    # Añadir las imagenes
    bg = PhotoImage( file = "IMG/BG.png")
    root.configure(bg = "#2148c0")
    root.overrideredirect(True)

    #AGREGAR LOS BOTONES PARA LA VENTANA REPORTES
    
  
    # Mostrar las imagenes usando LABEL
    label1 = Label( root, image = bg, bg='#2148c0' )
    label1.place(x = 0,y = 0)

    #AGREGAR LOS LABEL

    #CREAR BOTONES
   

    

    # Execute tkinter
    root.mainloop()

