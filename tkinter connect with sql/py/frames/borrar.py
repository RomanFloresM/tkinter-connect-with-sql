import tkinter as gui
from tkinter import ttk
import copy



def aborlito(tree, data):
    tree.delete(*tree.get_children())
    tree.heading('#0', text = 'Nickname')
    tree.heading('correo', text = 'correo')

    for b in data:
        tree.insert('',gui.END, text=b[1], values=(b[2]))

def eliminar(tree, conexion, cnxn, treeB):
    try:

        a = tree.focus()

    except IndexError:
        print("Debe seleccionar un elemento.")

    else:
        b = tree.item(a)
        c = str(b.get('values', 'error'))
        c = c.replace("['", '')
        c = c.replace("']", '')
        conexion.borrar(cnxn, c)
        
        data = conexion.todo(cnxn)
        aborlito(tree, data)
        aborlito(treeB, data)

def buscar(a, conexion, cnxn, tree):

    b = conexion.buscar(cnxn, a.get())
    tree.delete(*tree.get_children())

    tree.heading('#0', text='Nickname')
    tree.heading('correo', text='Correo')

    for c in b:
        tree.insert('',gui.END, text = c[0], values=(c[1]))




def inicio(cuadro3, conexion, cnxn, treeB):
    cuadro3.columnconfigure(0, weight = 4)
    cuadro3.columnconfigure(1, weight = 4)
    cuadro3.columnconfigure(2, weight = 4)

    a = ttk.Entry(cuadro3)
    a.grid(column = 0, row = 0)

    data = conexion.todo(cnxn)
    
    tree = ttk.Treeview(cuadro3, columns = ('correo'))

    aborlito(tree, data)

    c = ttk.Button(cuadro3, text = 'Buscar', command = lambda: buscar(a, conexion, cnxn, tree))
    c.grid(column = 1, row = 0)

    tree.grid(column = 0, row = 1)

    d = ttk.Button(cuadro3, text = 'Eliminar', command = lambda: eliminar(tree, conexion, cnxn, treeB) )
    d.grid(column = 1, row = 2)


if __name__ == 'main':
    inicio()
