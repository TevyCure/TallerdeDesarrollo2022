
import cx_Oracle

class Conexion:
    connection=None
    cursor=None

    @classmethod
    def getStartConnection(cls):
        #este ruta es la del ORACLE CLIENT
       cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\Neo_2\Desktop\UNIVERSIDAD\SEMESTRE 3\TALLER DE DESARROLLO DE APLICACIONES\IC")
       connect = cx_Oracle.connect(user="DAVID", password="TallerSistema2022", dsn="tallerdesarrollosistemasdiurno_high")
       cls.cursor = connect.cursor()
       cls.connection = connect
       

