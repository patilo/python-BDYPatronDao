import sys
import psycopg2 as bd
from logger_base import log

#esta clase administra la conexion  la base de datos
#corrobora los valores, ip, bd y password para conectarnos
#a pgadmin4 o por consola
class Conexion:
    _DATABASE = 'Proyecto'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None


    @classmethod #creamos el metodo para obtener la conexion con los metodos de la clase
    def obtenerConexion(cls): #creamos el metodo y recibiimos el parametro de cls
        if cls._conexion is None: #consultamos si existe el objeto conexion
            try:  #probamos la conexion con los metodos de la clase y creamos la variable cls._conexion
                cls._conexion = bd.connect(host = cls._HOST,
                                           user = cls._USERNAME,
                                           password = cls._PASSWORD,
                                           database = cls._DATABASE,
                                           port = cls._DB_PORT)
                log.debug(f'conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e: #capturamos e imprimimos si existe la conexion o la excepcion
                log.error(f'ocurrio la excepcion: {e}')
                sys.exit()
                #en caso de existir una excepcion nos salimos del programa para analizar el error
        else:
            return cls._conexion

    @classmethod #creamos el metodo de cursor, recordar que este dispara la conexion
    def obtenerCursor(cls): #creamos  el metodo para obtener el cursor
        if cls._cursor is None: #preguntamos si ya esta disparado el cursor
            try:
                cls._cursor = cls.obtenerConexion().cursor() #creamos la variable cursor en caso que no exista y tengamos la conexion
                log.debug(f'se disparo el cursor {cls._cursor}')
                return cls._cursor #retornamos la conexion disparada por el cursor 
            except Exception as e:
                log.error(f'ocurrio la excepcion: {e}')
                sys.exit()
        else:
            return cls._cursor

#aqui probamos si esta conectando con nuestra br, nos abrira el mensaje
#en el log o de forma bugeada ya que estamos usando log.debug
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
