import tkinter as gui
from tkinter import ttk
from SQL import conexion
from frames import informacion, Agregar, borrar
import clases.usuario as usu
import getpass


def inicio(cnxn, correo):

    usuario = conexion.rellenar(cnxn, correo)
    menu = gui.Tk()
    menu.title('Menu')
    menu.geometry('600x300')

    menu.columnconfigure(0, weight=1)

    panel = ttk.Notebook(menu)
    panel.grid(sticky=(gui.N, gui.S, gui.E, gui.W), padx = 0, pady = 0)

    cuadro1 = ttk.Frame(panel)
    panel.add(cuadro1, text = 'Informacion')
    
    cuadro2 = ttk.Frame(panel)
    panel.add(cuadro2, text = 'Agregar')

    cuadro3 = ttk.Frame(panel)
    panel.add(cuadro3, text = 'Borrar')

    data = conexion.todo(cnxn)

    tree = ttk.Treeview(cuadro1, columns = ('correo'))
    tree.heading('#0', text = 'Nickname')
    tree.heading('correo', text = 'correo')

    for a in data:
        tree.insert('',gui.END, text=a[1], values=(a[2]))

    b = usu.usuario()
    
    informacion.informacion(cuadro1, usuario, correo, tree, conexion, cnxn)
    Agregar.menuAgregar(cuadro2, conexion,cnxn, b, tree)
    borrar.inicio(cuadro3, conexion, cnxn, tree)

    
    menu.mainloop()



def insertar(cnxn, nick, correo, pas):
    h = usu.usuario()
    
    h.set_Nickname(nick.get())
    h.set_Correo(correo.get())
    h.set_pasw(pas.get())
    
    if h.get_Nickname() == '' or h.get_Correo() == '' or h.get_pasw() == '':
        Agregar.loginError()
    else:
        a = conexion.insertar(cnxn, h.get_Nickname(), h.get_Correo(), h.get_pasw())
        Agregar.loginAccept()
        

def Agregar_emergente(cnxn):

    menu = gui.Tk()
    menu.title('Agregar')
    menu.geometry('300x300')

    
    menu.columnconfigure(0, weight = 3)
    menu.columnconfigure(1, weight = 3)
    menu.columnconfigure(2, weight = 3)
    menu.columnconfigure(3, weight = 3)
    menu.columnconfigure(4, weight = 3)

    b = ttk.Label(menu, text = 'Nickname')
    b.grid(column = 1, row = 1)

    c = ttk.Entry(menu)
    c.grid(column = 2, row = 1)

    d = ttk.Label(menu, text = 'correo')
    d.grid(column = 1, row = 2)

    e = ttk.Entry(menu)
    e.grid(column = 2, row = 2)

    f = ttk.Label(menu, text = 'Contraseña')
    f.grid(column = 1, row = 3)

    g = ttk.Entry(menu, show = '*')
    g.grid(column = 2, row = 3)

    h = ttk.Button(menu, text = 'Agregar', command = lambda: insertar(cnxn, c, e, g ) ) 
    h.grid(column = 3, row = 4)

    menu.mainloop()

    



if __name__ == '__inicio__':
    inicio()
