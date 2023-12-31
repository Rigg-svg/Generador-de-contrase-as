import sqlite3

class DB():
    def __init__(self) :
        self.iniciarBaseDatos()

    def iniciarBaseDatos(self):
        conexion = sqlite3.connect("ventana/generador_contrasenas.db")
        
        cursor = conexion.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS credenciales (usuario TEXT, contrasena TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS contrasenas (contrasena TEXT)")

        cursor.close()
        conexion.close()

    def inciarSeccion(self):
        pass

    def registrarUsuario(self, usuario, contrasena):
        if self.verificarRegistro(usuario) == None:

            conexion = sqlite3.connect("ventana/generador_contrasenas.db")
            cursor = conexion.cursor()

            query = "INSERT INTO credenciales (usuario, contrasena) VALUES (?, ?)"
            cursor.execute(query, (usuario, contrasena))

            conexion.commit()
            conexion.close()

        else:
            print(f"El usuario {usuario} esta registrado")

    def verificarRegistro(self, usuario):
        conexion = sqlite3.connect("ventana/generador_contrasenas.db")
        cursor = conexion.cursor()

        query = ( "SELECT * FROM credenciales WHERE usuario = ?")
        cursor.execute(query, (usuario,))

        resultado = cursor.fetchone()

        conexion.close()

        return resultado
    
    def incriptar(self):
        pass

baseDatos = DB()

baseDatos.registrarUsuario("william123", "12345678")
#print(baseDatos.verificarRegistro("william123"))

