# Importar el modulo
import tkinter as tk
from validacion import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from turtle import color
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from inventariodao import Inventario


def login():
    # FUNCION PARA LO QUE HACE CUANDO SE RECIBE EL RESULTADO DE LA VALIDACION
    def llamadaValidacion(usuario, password):
        retornovalidacion = validacionLogin(usuario, password)
        a = retornovalidacion[0]
        b = retornovalidacion[1]
        if a == True and b == "jefe":
            entrarVentanaJefe()
        elif a == True and b == "vendedor":
            avisoConstruccion()
        elif a == False:
            messagebox.showerror(title="Login incorrecto",
                                 message="Usuario o contraseña incorrecta")

    # funcion para cerrar la ventana actual y abrir la funcion importada desde el archivo ventanajefe.py

    def entrarVentanaJefe():
        root.destroy()
        ventanaJefe()

    # Crear el objeto
    root = Tk()

    # Definir el tamaño
    root.geometry("1280x720")

    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente = Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )

    # Ingresar la función que para los entry cuando se haga click en ellos
    # se borre y se vuelva a escribir

    def haceClick(event):
        if entry.get() == 'Usuario':
            entry.delete(0, "end")
            entry.insert(0, '')

    def sacaElClick(event):
        if entry.get() == '':
            entry.insert(0, 'Usuario')

    def haceClickPassword(event):
        if entry2.get() == 'Contraseña':
            entry2.delete(0, "end")
            entry2.insert(0, '')
            entry2.config(show='*')

    def sacaElClickPassword(event):
        if entry2.get() == '':
            entry2.insert(0, 'Contraseña')
            entry2.config(show='')

    def ojo(event):
        entry2.config(show='')

    def ojo2(event):
        entry2.config(show='*')

    # Añadir las imagenes
    bg = PhotoImage(file="IMG/BG.png")
    # definir el color del fondo
    root.configure(bg="#2148c0")
    # borrar los bordes del programa
    root.overrideredirect(True)
    carrito = PhotoImage(file="IMG/CARRITO.png")
    boton = PhotoImage(file="IMG/Login btn.png")
    bordestexto = PhotoImage(file="IMG/Rectangle.png")
    botonsalir = PhotoImage(file="IMG/BOTON SALIR LOGIN.png")
    botonojo = PhotoImage(file="IMG/OJOPASSWORD 1.png")

    # Mostrar las imagenes usando LABEL
    label1 = Label(root, image=bg, bg='#2148c0')
    label1.place(x=0, y=0)

    label1 = Label(root, image=carrito, bg='#2148c0')
    label1.place(x=584, y=167)

    botonlabel = Label(root, image=boton)
    botonsalirlabel = Label(root, image=botonsalir)
    bordestexto_label = Label(root, image=bordestexto, bg='#2148c0')
    bordestexto_label.place(x=490, y=330)
    bordestexto2_label = Label(root, image=bordestexto, bg='#2148c0')
    bordestexto2_label.place(x=490, y=400)
    # Crear cajas de textos
    # dato: se debe de definir tk (import tkinter as tk)porque usando ttk, no funciona

    # ENTRY DE USUARIO
    entry = tk.Entry(root, bg='#2148c0', font=fuente, borderwidth=0,
                     foreground="white", insertbackground="white")
    entry.place(x=510, y=335, width=280, height=40,)
    entry.insert(0, 'Usuario')
    entry.bind('<FocusIn>', haceClick)
    entry.bind('<FocusOut>', sacaElClick)

    # ENTRY DE PASSWORD
    entry2 = tk.Entry(root, bg='#2148c0', font=fuente, borderwidth=0,
                      foreground="white", insertbackground="white")
    entry2.place(x=510, y=405, width=280, height=40)
    entry2.insert(0, 'Contraseña')
    entry2.bind('<FocusIn>', haceClickPassword)
    entry2.bind('<FocusOut>', sacaElClickPassword)

    def almacenar(event):
        usuario = entry.get()
        password = entry2.get()
        validacion(usuario, password)

    def almacenarButton():
        usuario = entry.get()
        password = entry2.get()
        llamadaValidacion(usuario, password)

    def salir():
        root.destroy()

    # Crear boton
    # en el boton se indica con "command" la funcion que ejecutará el boton
    button = Button(root, image=boton, borderwidth=0,
                    command=almacenarButton, background='#2148c0')
    button.place(x=491, y=483)
    buttonsalir = Button(root, image=botonsalir, borderwidth=0,
                         command=salir, background='#2148c0')
    buttonsalir.place(x=491, y=553)
    buttonojo = Button(root, image=botonojo,
                       borderwidth=0, background='#2148c0')
    buttonojo.place(x=749, y=412)
    buttonojo.bind('<Button-1>', ojo)
    buttonojo.bind('<ButtonRelease-1>', ojo2)
    root.bind('<Return>', almacenar)
    # Execute tkinter
    root.mainloop()


def avisoConstruccion():
    messagebox.showerror(title="EN CONSTRUCCION",
                         message="Modulo aún en construcción uwu")


# Crear la funcion para la ventana del Jefe de Ventas
def ventanaJefe():
    root = Tk()
    # Definir el tamaño
    root.geometry("1280x720")
    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente = Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )
    # FUNCIONES DE LOS BOTONES, SE LLAMAN CON "COMMAND"

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
    bg = PhotoImage(file="IMG/BG.png")
    root.configure(bg="#2148c0")
    # quitar los bordes del programa
    root.overrideredirect(True)
    botoninventario = PhotoImage(file="IMG/BOTON INVENTARIO.png")
    botonreportes = PhotoImage(file="IMG/BOTON REPORTESSINFONDO.png")
    botoniniciarcerrar = PhotoImage(file="IMG/BOTON INICIARCERRAR DIA.png")
    botonvendedor = PhotoImage(file="IMG/BOTON VENDEDOR.PNG")
    botoncerrarsesion = PhotoImage(file="IMG/BOTON CERRAR SESION.PNG")

    # Mostrar las imagenes usando LABEL
    label1 = Label(root, image=bg, bg='#2148c0')
    label1.place(x=0, y=0)

    botonlabel = Label(root, image=botoninventario)
    botonlabel2 = Label(root, image=botonreportes)
    botonlabel3 = Label(root, image=botoniniciarcerrar)
    botonlabel4 = Label(root, image=botonvendedor)
    botonlabel5 = Label(root, image=botoncerrarsesion)

    # Crear boton y asignar función correspondiente con "command"
    button = Button(root, image=botoninventario, borderwidth=0,
                    bg='#2148c0', command=abrirVentanaInventario)
    button.place(x=155.31, y=145.32)

    button2 = Button(root, image=botonreportes, borderwidth=0,
                     bg='#2148c0', command=avisoConstruccion)
    button2.place(x=705, y=145)

    button3 = Button(root, image=botoniniciarcerrar,
                     borderwidth=0, bg='#2148c0', command=avisoConstruccion)
    button3.place(x=152.31, y=405.32)

    button4 = Button(root, image=botonvendedor, borderwidth=0,
                     bg='#2148c0', command=avisoConstruccion)
    button4.place(x=705, y=405.32)

    button5 = Button(root, image=botoncerrarsesion,
                     borderwidth=0, bg='#264ECA', command=cerrarSesion)
    button5.place(x=881, y=34)

    # Execute tkinter
    root.mainloop()


def ventanaInventario():
    def getAll():
        productos = Inventario()
        elementos = productos.getAllBBDD()
        count = 0
        for elemento in elementos:
            tv.insert(parent='', index='end', iid=count, text="", values=(
                elemento[1], elemento[2], elemento[3], elemento[4]))
            count += 1

    def buscarInventario(event):
        # FUNCION DE BUSQUEDA

        products = Inventario()
        busqueda = searchEntry.get().upper()
        # limpiar la tabla
        for elemento in tv.get_children():
            tv.delete(elemento)

        # llamamos a la función searchInventario y le entregamos el parametro a buscar
        # en search se guarda en forma de lista los resultados
        search = products.searchInventarioBBDD(busqueda)
        count = 0
        # con este for asignamos los elementos de la lista a las columnas
        for elemento in search:
            tv.insert(parent='', index='end', iid=count, text="", values=(
                elemento[1], elemento[2], elemento[3], elemento[4]))
            count += 1

    def salirInventario():
        root.destroy()
        ventanaJefe()

    def modalAgregar():
        def buscarCodigo(event):
            inventario = Inventario()
            busqueda = codigoEntry.get()
            search = inventario.searchCodigoBBDD(busqueda)

            if search != []:
                a = search[0]
                if descripcionEntry.get() != a[1]:
                    descripcionEntry.delete(0, "end")
                    descripcionEntry.insert(0, a[2])
                precioEntry.insert(0, a[3])
                categoriaEntry.insert(0, a[4])

        def agregarElement():
            inventario = Inventario()
            elementos = []
            codigo = codigoEntry.get()
            descripcion = descripcionEntry.get()
            precio = precioEntry.get()
            categoria = categoriaEntry.get()

            elementos.append(codigo)
            elementos.append(descripcion)
            elementos.append(precio)
            ''' elementos.append(categoria) '''
            print(elementos)
            validador = inventario.agregarElemento(elementos)
            if validador == True:
                ventana_nueva.destroy()
                products = Inventario()
                search = products.getAllBBDD()
                count = 0
                for elemento in tv.get_children():
                    tv.delete(elemento)
                # con este for asignamos los elementos de la lista a las columnas
                for elemento in search:
                    tv.insert(parent='', index='end', iid=count, text="", values=(
                        elemento[1], elemento[2], elemento[3], elemento[4]))
                    count += 1

        # se crea la especie de modal para agregar elementos,Toplevel()
        ventana_nueva = Toplevel()
        ventana_nueva.title("Agregar Producto")
        ventana_nueva.geometry("720x640")
        ventana_nueva.configure(bg="#2148C0")
        canvas = Canvas(ventana_nueva, width=0, height=0, bg="#2148C0")

        fuente = Font(
            family="Montserrat",
            size=18,
            weight="normal",
        )
        formAgregar = PhotoImage(file="IMG/formularioAGREGAR.png")
        formAgregar_label = Label(
            ventana_nueva, image=formAgregar, bg="#2148C0")
        formAgregar_label.place(x=38, y=10)
        # agregamos los entry para cada uno de los campos
        codigoEntry = tk.Entry(ventana_nueva, font=fuente,
                               borderwidth=0, foreground="blue", insertbackground="blue")
        codigoEntry.place(x=250, y=15, width=400, height=30)
        codigoEntry.bind('<Key>', buscarCodigo)

        descripcionEntry = tk.Entry(ventana_nueva, font=fuente,
                                    borderwidth=0, foreground="blue", insertbackground="blue")
        descripcionEntry.place(x=250, y=105, width=400, height=30)

        precioEntry = tk.Entry(ventana_nueva, font=fuente,
                               borderwidth=0, foreground="blue", insertbackground="blue")
        precioEntry.place(x=250, y=195, width=400, height=30)

        categoriaEntry = tk.Entry(ventana_nueva, font=fuente,
                                  borderwidth=0, foreground="blue", insertbackground="blue")
        categoriaEntry.place(x=250, y=285, width=400, height=30)

        botonEnviar = PhotoImage(
            file="IMG/botonEnviar.jpg")

        botonLimpiar = PhotoImage(
            file="IMG/botonLimpiar.jpg")

        botonVolver = PhotoImage(
            file="IMG/botonVolver.jpg")

        botonEnv = Button(ventana_nueva, image=botonEnviar, borderwidth=0,
                          background='#2148c0', command=agregarElement)
        botonEnv_label = Label(ventana_nueva, image=botonEnviar)
        botonEnv.place(x=480, y=555)

        botonLimp = Button(ventana_nueva, image=botonLimpiar, borderwidth=0,
                           background='#2148c0')
        botonLimp_label = Label(ventana_nueva, image=botonLimpiar)
        botonLimp.place(x=280, y=555)

        botonVolv = Button(ventana_nueva, image=botonVolver, borderwidth=0,
                           background='#2148c0', command=ventana_nueva.destroy)
        botonVolv_label = Label(ventana_nueva, image=botonVolver)
        botonVolv.place(x=80, y=555)

        ventana_nueva.mainloop()

    def deleteItem():
        inventario = Inventario()
        hola = tv.selection()
        for i in hola:
            print(tv.item(i, 'values'))
            item = tv.item(i, 'values')

            validador = inventario.eliminarElemento(item[0])

        if validador == True:

            products = Inventario()
            search = products.getAllBBDD()
            count = 0
            for elemento in tv.get_children():
                tv.delete(elemento)
            # con este for asignamos los elementos de la lista a las columnas
            for elemento in search:
                tv.insert(parent='', index='end', iid=count, text="", values=(
                    elemento[1], elemento[2], elemento[3], elemento[4]))
                count += 1

    def modalModificarItem():

        def modificarItem():
            codigo = codigoEntry.get()
            descripcion = descripcionEntry.get()
            precio = precioEntry.get()
            categoria = categoriaEntry.get()
            validador = inventario.modificarElemento(codigo,descripcion,precio)
            print(validador)
            if validador == True:
                ventana_nueva.destroy()
                products = Inventario()
                search = products.getAllBBDD()
                count = 0
                for elemento in tv.get_children():
                    tv.delete(elemento)
                    # con este for asignamos los elementos de la lista a las columnas
                for elemento in search:
                    tv.insert(parent='', index='end', iid=count, text="", values=(
                    elemento[1], elemento[2], elemento[3], elemento[4]))
                    count += 1
                    
        inventario = Inventario()
        elementModify = tv.selection()
        listaElement = []
        for i in elementModify:
            print(tv.item(i, 'values'))
            item = tv.item(i, 'values')
            for n in item:
                listaElement.append(n)
        print(listaElement)
        

        # se crea la especie de modal para agregar elementos,Toplevel()
        ventana_nueva = Toplevel()
        ventana_nueva.title("Modificar Producto")
        ventana_nueva.geometry("720x640")
        ventana_nueva.configure(bg="#2148C0")
        canvas = Canvas(ventana_nueva, width=0, height=0, bg="#2148C0")

        fuente = Font(
            family="Montserrat",
            size=18,
            weight="normal",
        )
        formAgregar = PhotoImage(file="IMG/formularioAGREGAR.png")
        formAgregar_label = Label(
            ventana_nueva, image=formAgregar, bg="#2148C0")
        formAgregar_label.place(x=38, y=10)
        # agregamos los entry para cada uno de los campos
        codigoEntry = tk.Entry(ventana_nueva, font=fuente,
                               borderwidth=0, foreground="blue", insertbackground="blue")
        codigoEntry.place(x=250, y=15, width=400, height=30)

        descripcionEntry = tk.Entry(ventana_nueva, font=fuente,
                                    borderwidth=0, foreground="blue", insertbackground="blue")
        descripcionEntry.place(x=250, y=105, width=400, height=30)

        precioEntry = tk.Entry(ventana_nueva, font=fuente,
                               borderwidth=0, foreground="blue", insertbackground="blue")
        precioEntry.place(x=250, y=195, width=400, height=30)

        categoriaEntry = tk.Entry(ventana_nueva, font=fuente,
                                  borderwidth=0, foreground="blue", insertbackground="blue")
        categoriaEntry.place(x=250, y=285, width=400, height=30)

        botonEnviar = PhotoImage(
            file="IMG/botonEnviar.jpg")

        botonLimpiar = PhotoImage(
            file="IMG/botonLimpiar.jpg")

        botonVolver = PhotoImage(
            file="IMG/botonVolver.jpg")

        botonEnv = Button(ventana_nueva, image=botonEnviar, borderwidth=0,
                          background='#2148c0', command=modificarItem)
        botonEnv_label = Label(ventana_nueva, image=botonEnviar)
        botonEnv.place(x=480, y=555)

        botonLimp = Button(ventana_nueva, image=botonLimpiar, borderwidth=0,
                           background='#2148c0')
        botonLimp_label = Label(ventana_nueva, image=botonLimpiar)
        botonLimp.place(x=280, y=555)

        botonVolv = Button(ventana_nueva, image=botonVolver, borderwidth=0,
                           background='#2148c0', command=ventana_nueva.destroy)
        botonVolv_label = Label(ventana_nueva, image=botonVolver)
        botonVolv.place(x=80, y=555)

        codigoEntry.insert(0, listaElement[0])
        descripcionEntry.insert(0, listaElement[1])
        precioEntry.insert(0, listaElement[2])
        categoriaEntry.insert(0, listaElement[3])

        ventana_nueva.mainloop()

    root = Tk()

    root.geometry("1280x720")
    root.configure(bg="#2148C0")
    root.overrideredirect(True)
    style = ttk.Style()
    style.theme_use('alt')
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=(
        'Montserrat', 11))  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", background="white", font=(
        'Montserrat', 13, 'bold'), foreground="#244bc5")  # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {
                 'sticky': 'nswe'})])  # Remove the borders
    # define el tamaño del "canvas"
    canvas = Canvas(
        root,
        bg="#2148C0",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file="IMG/image_1.png")
    image_1 = canvas.create_image(
        541.0,
        541.0,
        image=image_image_1
    )
    # botones y sus respectivas ubicaciones "place"
    button_image_1 = PhotoImage(
        file="IMG/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=salirInventario,
        relief="flat", bg='#2148c0'
    )
    button_1.place(
        x=1005.0,
        y=33.0,
        width=228.0,
        height=90.0
    )

    button_image_2 = PhotoImage(
        file="IMG/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=modalModificarItem,
        relief="flat", bg='#2148c0'
    )
    button_2.place(
        x=686.3004760742188,
        y=33.0,
        width=222.6995391845703,
        height=90.0
    )

    button_image_3 = PhotoImage(
        file="IMG/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=modalAgregar,
        relief="flat", bg='#2148c0'
    )
    button_3.place(
        x=49.0,
        y=36.0,
        width=226.0,
        height=90.0
    )

    button_image_4 = PhotoImage(
        file="IMG/button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=deleteItem,
        relief="flat", bg='#2148c0'
    )
    button_4.place(
        x=369.0,
        y=36.0,
        width=226.0,
        height=90.0,
    )

    # entry para la barra de busqueda

    bordesbarra = PhotoImage(file="IMG/INPUTBUSQUEDAINVENTARIO.png")
    bordesbarra_label = Label(root, image=bordesbarra, bg='#2148c0')
    bordesbarra_label.place(x=49, y=135)

    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente = Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )
    searchEntry = tk.Entry(root, bg='#2148c0', font=fuente,
                           borderwidth=0, foreground="white", insertbackground="white")
    searchEntry.place(x=113, y=141, width=1000, height=30,)
    searchEntry.bind('<Key>', buscarInventario)

    tv = ttk.Treeview(root, columns=(1, 2, 3, 4, 5),
                      show="headings", style="mystyle.Treeview")
    tv.pack()
    tv.place(
        x=49.0,
        y=200.0,
        width=1182,
        height=500
    )

    # AGREGA SCROLLBAR AL TREEVIEW
    vsb = ttk.Scrollbar(tv, orient="vertical", command=tv.yview)
    vsb.pack(side='right', fill='y')
    tv.configure(yscrollcommand=vsb.set)

    # HEADINGS DEL TREEVIEW
    headings = ["CODIGO(SKU)", "DESCRIPCION", "PRECIO", "CATEGORIA"]
    tv.heading(1, text=headings[0])
    tv.heading(2, text=headings[1])
    tv.heading(3, text=headings[2])
    tv.heading(4, text=headings[3])

    # no se porque, pero al momento de agregar stretch=NO, se puede usar la opcion
    # width para controlar el ancho de la columna
    tv.column(1, anchor=CENTER, stretch=NO, width=135)
    tv.column(2, anchor=CENTER, stretch=NO, width=500)
    tv.column(3, anchor=CENTER, stretch=NO, width=250)
    tv.column(4, anchor=CENTER, stretch=NO, width=300)

    # ordenar al momento de hacer click un heading --- FALTAAA


# recibir elementos de la base de datos y guardarlos en una lista
    productos = Inventario()
    elementos = productos.getAllBBDD()
    count = 0
    for elemento in elementos:
        tv.insert(parent='', index='end', iid=count, text="", values=(
            elemento[1], elemento[2], elemento[3], elemento[4]))
        count += 1
    root.resizable(False, False)
    root.mainloop()


def ventanaReportes():
    root = Tk()
    # Definir el tamaño
    root.geometry("1280x720")
    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente = Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )
    # Añadir las imagenes
    bg = PhotoImage(file="IMG/BG.png")
    root.configure(bg="#2148c0")
    root.overrideredirect(True)

    # AGREGAR LOS BOTONES PARA LA VENTANA REPORTES

    # Mostrar las imagenes usando LABEL
    label1 = Label(root, image=bg, bg='#2148c0')
    label1.place(x=0, y=0)

    # AGREGAR LOS LABEL

    # CREAR BOTONES

    # Execute tkinter
    root.mainloop()
