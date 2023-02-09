import tkinter as gui
from tkinter import ttk
import clases.usuario as usu
import SQL.conexion as cone
import inicio 
import getpass




def loginError():
    b = gui.Tk()
    b.title('Error')
    b.geometry('200x200')

    c = ttk.Label(b, text = 'intenta de nuevo')
    c.pack()

    d = ttk.Button(b, text = 'Cerrar', command = lambda: b.destroy())
    d.pack()

    b.mainloop()


def ingreso(usuario,correo,passw, cnxn, a): 
    usuario.set_Correo(correo.get())
    usuario.set_pasw(passw.get())
        
    if cone.intento(cnxn, usuario.get_Correo(), usuario.get_pasw()) == 1:
        a.destroy()
        inicio.inicio(cnxn, usuario.get_Correo())
    else:
        loginError()


def login(cnxn):
    
    a = gui.Tk()
    a.title("log in")
    a.geometry("500x100")
    
    a.columnconfigure(0, weight = 3)
    a.columnconfigure(1, weight = 3)
    a.columnconfigure(2, weight = 3)
    a.columnconfigure(3, weight = 5)

    b = ttk.Label(a, text = 'login')
    b.grid(column = 2, row = 0, sticky = gui.W)

    c = ttk.Label(a, text = 'Usuario')
    c.grid(column = 1, row = 1, sticky = gui.E)
    
    d = ttk.Entry()
    d.grid(column = 3, row = 1, sticky = gui.W)

    e = ttk.Label(a, text = 'Contraseña')
    e.grid(column = 1, row = 2, sticky = gui.E)
    
    f = ttk.Entry(show = '*')
    f.grid(column = 3, row = 2, sticky = gui.W)

    
    h = usu.usuario()
    d.insert(0,'prueba1@prueba.com')
    f.insert(0,'prueba1')

    g = ttk.Button(text = 'log in', command = lambda: ingreso(h,d,f, cnxn, a) )
    g.grid(column = 1, row = 3)

    i = ttk.Button(text = 'Agregar', command = lambda: inicio.Agregar_emergente(cnxn) )
    i.grid(column= 3, row = 3)

        

    
    a.mainloop()

def main():
    cnxn2 = cone.cnxn()
    if str(type(cnxn2)) == "<class 'pyodbc.Connection'>":
        login(cnxn2)
    else :
        print(type(cone.cnxn()))

if __name__ == '__main__':
    main()
