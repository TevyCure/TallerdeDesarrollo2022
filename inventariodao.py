from conexion import Conexion
from tkinter import messagebox
import ventanas
import cx_Oracle

class Inventario:
    def __init__(self):
        self.__oracle = Conexion()

    @property
    def oracle(self):
        return self.__oracle

    def getAllBBDD(self):
        try:

            # se hace un select en los productos
            Conexion.cursor.execute("SELECT * FROM PRODUCTO")
            # con fetchall se hace una lista con todo lo obtenido de usuarios
            rows = Conexion.cursor.fetchall()
            return rows
        except:
            pass

    def searchInventarioBBDD(self, busqueda):
        try:
            # se hace un select en los productos que contengan la descripcion
            Conexion.cursor.execute(
                f"SELECT * FROM PRODUCTO WHERE DESCRIPCION like '%{busqueda}%'")
            # con fetchall se hace una lista con todo lo obtenido de usuarios
            rows = Conexion.cursor.fetchall()
            print(rows)
            return rows
        except:
            pass

    def searchCodigoBBDD(self, busqueda):
        try:
            # se hace un select en los productos que contengan la descripcion
            Conexion.cursor.execute(
                f"SELECT * FROM PRODUCTO WHERE CODIGO_SKU = {busqueda}")
            # con fetchall se hace una lista con todo lo obtenido de usuarios
            rows = Conexion.cursor.fetchall()

            return rows
        except:
            pass

    def agregarElemento(self, datos):
        try:
            print("hola")
            print(datos)
            Conexion.cursor.execute(
                "insert into PRODUCTO(CODIGO_SKU,DESCRIPCION,VALOR_UNITARIO) values(:1,:2,:3)", datos)
            Conexion.connection.commit()
            messagebox.showinfo(
                message="Elemento agregado correctamente", title="Elemento agregado")
            return True

        except:
            pass

    def eliminarElemento(self, codigo_sku):
        try:
            codigo_sku = int(codigo_sku)
            print(codigo_sku)
            Conexion.cursor.execute(
                "delete from PRODUCTO where CODIGO_SKU=:1", [codigo_sku])
            Conexion.connection.commit()
            messagebox.showinfo(
                message="Elemento eliminado correctamente", title="Elemento eliminado")
            return True
        except:
            error_obj, = cx_Oracle.IntegrityError.args
            print("Customer ID already exists")
            print("Error Code:", error_obj.code)
            print("Error Message:", error_obj.message)
    
    def modificarElemento(self,code,descript,precio):
        try:
            code=int(code)
            precio=int(precio)
            print(code)
            print(descript)
            print(precio)
            Conexion.cursor.execute("update PRODUCTO set CODIGO_SKU=:1,DESCRIPCION=:2,VALOR_UNITARIO=:3 where CODIGO_SKU=:1", [code,descript,precio] )
            Conexion.connection.commit()
            messagebox.showinfo(
            message="Elemento modificado correctamente", title="Elemento Modificado")
            return True
        except:
            pass