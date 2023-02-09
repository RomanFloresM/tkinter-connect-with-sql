import pyodbc 

def borrar(cnxn, word):
    with cnxn.cursor() as cursor:
        query = 'exec examSpEliminarUsuario ?;'
        a = [word]
        b = cursor.execute(query, a)

        return b

def buscar(cnxn, word):
    with cnxn.cursor() as cursor:
        query = 'exec examSpConsultaUsuario ?;'
        a = [word]
        data = cursor.execute(query, a)
        b = []
        for c in data:
            b.append(c)
        return b

def insertar(cnxn, nick, correo, pas):
    with cnxn.cursor() as cursor:
        query = 'exec examSpInsertarUsuario ?, ?, ?;'
        data = [nick, correo, pas]
        a = cursor.execute(query,data)
        return a

def todo(cnxn):
    with cnxn.cursor() as cursor:
        query = 'select id, Nickname, Correo from examusuario2 with(nolock) where estatus = 1;'
        data = cursor.execute(query)
        a = []
        for b in data:
            a.append(b)
        return a            

def rellenar(cnxn, correo):
    with cnxn.cursor() as cursor:
        query = 'select id, Nickname, registrofecha from examusuario2 with(nolock) where correo = ?;'
        data = [correo]
        buscar = cursor.execute(query, data)
        for a in buscar:
            return a

def intento(cnxn, user, passw):
    bandera = None
    with cnxn.cursor() as cursor:
        query = 'exec examSpConsultacorreo ?,  ?'
        data = [user, passw]
        buscar  = cursor.execute(query, data)
        for a in buscar:
            bandera = int(a[0])

    return bandera
        

def cnxn():
    direccion_servidor = '127.0.0.1'
    nombre_bd = 'prueba'
    nombre_usuario = 'rmflores'
    password = 'prueba1234'
    try:
        cnxn  = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
        return cnxn
    except Exception as e:
        print('error: ',e)





if __name__ == '__conexion__':
    cnxn()
