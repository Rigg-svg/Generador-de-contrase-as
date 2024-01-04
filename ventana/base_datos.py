import sqlite3
import bcrypt

#decoradores
""" def obtenerDatos(func):
    def wrapper(self, *args, **kwargs):
        resultado = func(*args, **kwargs)

        if resultado is not None:
            resultado = list(resultado)
            resultado.pop(1)
            resultado.pop(2)
            resultado = tuple(resultado)

        return resultado
    return resultado """

class DB():
    def __init__(self) :
        self.iniciarBaseDatos()

    def iniciarBaseDatos(self):
        conexion = sqlite3.connect("datos/generador_contrasenas.db")
        
        cursor = conexion.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS credenciales(
                        id INTEGER PRIMARY KEY, 
                        usuario TEXT, 
                        contrasena TEXT, 
                        salt TEXT
                        )
                        ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS contrasenas (
                        contrasena TEXT, 
                        mensaje TEXT, 
                        salt TEXT,
                        usuario_id INTEGER,
                        FOREIGN KEY (usuario_id) REFERENCES credenciales (id)
                        )
                        ''')

        cursor.close()
        conexion.close()

#Esta funcion solo se usa despues de usar la función "verificar registro" para saber si el usuario esta registrado en la base de datos
    def inciarSeccion(self, contrasena, contrasenaAlmacenada, usuario=None):

        return bcrypt.checkpw(contrasena.encode('utf-8'), contrasenaAlmacenada)

#Esta funcion solo se usa despues de usar la función "verificar registro" para saber si el usuario esta registrado en la base de datos
    def registrarUsuario(self, usuario, contrasena):
        
        contrasenaIncriptada, salt = self.incriptar(contrasena)

        conexion = sqlite3.connect("datos/generador_contrasenas.db")
        cursor = conexion.cursor()

        query = "INSERT INTO credenciales (usuario, contrasena, salt) VALUES (?, ?, ?)"
        cursor.execute(query, (usuario, contrasenaIncriptada, salt))

        conexion.commit()
        conexion.close()

    def guardarContraseña(self, contrasena_guardar, mensaje):
        
        conexion = sqlite3.connect("datos/generador_contrasenas.db")
        cursor = conexion.cursor()

        query = ("INSERT INTO contrasenas (contrasena, mensaje, salt, usuario_id) VALUES (?, ?, ?, ?)")
        cursor.execute(query, (contrasena_guardar, mensaje, self.salt, self.usuario_id))

        conexion.commit()
        conexion.close()
    
    def verificarRegistro(self, usuario):
        conexion = sqlite3.connect("datos/generador_contrasenas.db")
        cursor = conexion.cursor()

        query = ( "SELECT * FROM credenciales WHERE usuario = ?")
        cursor.execute(query, (usuario,))

        resultado = cursor.fetchone()

        if resultado is not None:
            self.usuario_id = resultado[0]
            self.usuario = resultado[1]
            self.salt = resultado[3]
        
        conexion.close()

        return resultado

    def incriptar(self, contrasena):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
        
        return hashed_password, salt

    def obtenerDatos(self):
        conexion = sqlite3.connect("datos/generador_contrasenas.db")
        cursor = conexion.cursor()

        query = "SELECT contrasena, mensaje FROM contrasenas WHERE usuario_id = ?"

        cursor.execute(query, (self.usuario_id,))

        resultado = cursor.fetchall()

        conexion.close()

        return resultado