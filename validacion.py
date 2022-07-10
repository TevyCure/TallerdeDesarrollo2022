from conexion import Conexion


def validacionLogin(usuario, clave):
    try:      
        #se hace un select en los usuarios
        Conexion.cursor.execute("SELECT USUARIO FROM LOGIN")
        #con fetchall se hace una lista con todo lo obtenido de usuarios
        rows = Conexion.cursor.fetchall()
        usuarios = []
        for row in rows:
            usuarios.append(row[0])
        print(usuarios)
        Conexion.cursor.execute("SELECT CONTRASENHA FROM LOGIN")
        rows = Conexion.cursor.fetchall()
        contrasenhas = []
        for row in rows:
            contrasenhas.append(row[0])
        Conexion.cursor.execute("SELECT TIPO FROM LOGIN")
        rows = Conexion.cursor.fetchall()
        tipo = []
        for row in rows:
            tipo.append(row[0])

        validacionuser = 0
        validacionpass = 0
        for i in usuarios:
            if i == usuario:
                validacionuser += 1
                print(i)
                print(usuario)
                print(validacionuser)
                posicion = (usuarios.index(i))
        if contrasenhas[posicion] == clave:
            validacionpass += 1
            print(contrasenhas[posicion])
            print(clave)
            print(validacionpass)
            print(tipo[posicion])

        if validacionpass == 1 and validacionuser == 1:
            return [True, tipo[posicion]]

        else:
            return [False,0]

    except:
        return [False,0]
