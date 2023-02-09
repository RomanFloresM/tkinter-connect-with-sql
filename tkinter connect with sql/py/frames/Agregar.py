import tkinter as gui
from tkinter import ttk



    

def loginAccept():
    b = gui.Tk()
    b.title('Exito')
    b.geometry('200x200')

    c = ttk.Label(b, text = 'registro Completado')
    c.pack()

    d = ttk.Button(b, text = 'Cerrar', command = lambda: b.destroy())
    d.pack()

def loginError():
    b = gui.Tk()
    b.title('Error')
    b.geometry('200x200')

    c = ttk.Label(b, text = 'intenta de nuevo')
    c.pack()

    d = ttk.Button(b, text = 'Cerrar', command = lambda: b.destroy())
    d.pack()

    b.mainloop()

def treeinsert(tree, nick, correo):
    tree.insert('',gui.END, text=nick, values=(correo))
    


def insertar(cnxn, nick, correo, pas, h, conexion, tree):
    
    h.set_Nickname(nick.get())
    h.set_Correo(correo.get())
    h.set_pasw(pas.get())
    
    if h.get_Nickname() == '' or h.get_Correo() == '' or h.get_pasw() == '':
        loginError()
    else:
        a = conexion.insertar(cnxn, h.get_Nickname(), h.get_Correo(), h.get_pasw())
        treeinsert(tree, h.get_Nickname(), h.get_Correo())
        nick.insert(0,'')
        correo.insert(0,'')
        pas.insert(0,'')
        loginAccept()

    

def menuAgregar(cuadro2, conexion, cnxn, usu, tree):
    
    
    cuadro2.columnconfigure(0, weight = 4)
    cuadro2.columnconfigure(1, weight = 4)
    cuadro2.columnconfigure(2, weight = 4)
    cuadro2.columnconfigure(3, weight = 4)
    cuadro2.columnconfigure(4, weight = 4)

    b = ttk.Label(cuadro2, text = 'Nickname')
    b.grid(column = 1, row = 1)

    c = ttk.Entry(cuadro2)
    c.grid(column = 2, row = 1)

    d = ttk.Label(cuadro2, text = 'correo')
    d.grid(column = 1, row = 2)

    e = ttk.Entry(cuadro2)
    e.grid(column = 2, row = 2)

    f = ttk.Label(cuadro2, text = 'Contraseña')
    f.grid(column = 1, row = 3)

    g = ttk.Entry(cuadro2, show = '*')
    g.grid(column = 2, row = 3)

    h = ttk.Button(cuadro2, text = 'Agregar', command = lambda: insertar(cnxn, c, e, g, usu,conexion, tree ) ) 
    h.grid(column = 3, row = 4)

        


if __name__ == '__agregar__':
    menuAgregar()
