import tkinter as gui
from tkinter import ttk


def buscar(a, conexion, cnxn, tree):

    b = conexion.buscar(cnxn, a.get())
    tree.delete(*tree.get_children())

    tree.heading('#0', text='Nickname')
    tree.heading('correo', text='Correo')

    for c in b:
        tree.insert('',gui.END, text = c[0], values=(c[1]))
    

def informacion(cuadro1, usuario, correo, tree, conexion, cnxn):

    cuadro1.columnconfigure(0, weight = 4)
    cuadro1.columnconfigure(1, weight = 4)
    cuadro1.columnconfigure(2, weight = 0)

    labelCuadro1 = ttk.Label(cuadro1, text = 'Nickname: ' + usuario[1])
    labelCuadro1.grid(column = 0, row = 0, sticky = gui.W)

    labelCuadro2 = ttk.Label(cuadro1, text = 'Correo: ' + correo)
    labelCuadro2.grid(column = 1, row = 0, sticky = gui.W)

    a = ttk.Entry(cuadro1)
    a.grid(column = 0, row = 1, sticky = gui.W)

    b = ttk.Button(cuadro1, text = 'buscar', command = lambda: buscar(a, conexion, cnxn, tree))
    b.grid(column = 1, row = 1, sticky = gui.W)

    tree.grid(column = 0, row = 2)

if __name__ == '__informacion__':
    informacion()
