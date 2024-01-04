from base_datos import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import  QPushButton, QLabel, QLineEdit, QDialog

class agregarContraseña(QDialog):
    def __init__(self, ventanaPrincipal):
        super().__init__()
        self.setModal(True)
        self.ventanaPrincipal = ventanaPrincipal #Intanciar el objeto de la clase ventana del arhivo 'main'
        self.baseDatos = DB()


    def inicilalizarIU(self):
        self.setWindowTitle("Guardar nueva contraseña")
        self.setGeometry(500,500,500,500)
        self.setMaximumSize(500, 500) #tamaño maximo en ancho y alto de la ventana
        self.setMinimumSize(500,500) #tamaño minimo en ancho y alto de la ventana

        paleta = self.palette() #Se debe crear un objeto paleta

        # Establecer el color de fondo deseado
        color_de_fondo = QColor(2, 179, 255)  #color de  fondo
        color_de_fondo.setAlphaF(0.5) #Establecer la transparencia al 50% (0 = 0% | 1 = 100%)
        
        paleta.setColor(QPalette.ColorRole.Window, color_de_fondo)
        self.setPalette(paleta)

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint) #Permite que la ventana quede por encima de las otras

        self.generarInterfaz()

        self.show()

    def generarInterfaz(self):
        #Crear instancia del campo de la contraseña del arhivo main. Para saber cual es el valor del campo
        contraseña = self.ventanaPrincipal.mostrarContrasena.text()

        titulo_contrasena = QLabel(self)
        titulo_contrasena.setText("Contraseña")
        titulo_contrasena.move(225, 135)

        titulo_dispocicion = QLabel(self)
        titulo_dispocicion.setText("Dispocición")
        titulo_dispocicion.move(230, 245)

        self.campo_contrasena = QLineEdit(self)
        self.campo_contrasena.resize(110, 30)
        self.campo_contrasena.move(207, 157)
        self.campo_contrasena.setDisabled(True)
        self.campo_contrasena.setText(contraseña)#mostrar la contraseña en pantalla
        self.campo_contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)
        campo_contrasena_styles = """
            QLineEdit {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """

        self.campo_contrasena.setStyleSheet(campo_contrasena_styles)

        self.campo_mensaje = QLineEdit(self)
        self.campo_mensaje.resize(200, 30)
        self.campo_mensaje.move(155, 266)

        btn_guardar = QPushButton(self)
        btn_guardar.setText("Guardar")
        btn_guardar.resize(100, 30)
        btn_guardar.move(208 ,366)
        btn_guardar.clicked.connect(self.guardar)
        btn_guardar_styles = """ 
            QPushButton {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """

        btn_guardar.setStyleSheet(btn_guardar_styles)

        btn_cancelar = QPushButton(self)
        btn_cancelar.setText("Cancelar")
        btn_cancelar.resize(100, 30)
        btn_cancelar.move(395, 15)
        btn_cancelar.clicked.connect(self.cancelar)
        btn_cancelar_styles = """ 
            QPushButton {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """

        btn_cancelar.setStyleSheet(btn_cancelar_styles)

        self.ventanaPrincipal.showMinimized() #minimiza la ventana principal
        self.showMaximized() #muestra la ventana maximizada

    def guardar(self):
        mensaje = self.campo_mensaje.text() #obtener el texto del campo mensaje
        contraseña = self.campo_contrasena.text() #obtemer el texto del campo contraseña
        usuario = self.usuario = self.ventanaPrincipal.usuario #obtener el nombre del usuario que inicio sección

        self.baseDatos.verificarRegistro(usuario)
        self.baseDatos.guardarContraseña(contraseña, mensaje)

        self.close()

    def cancelar(self):
        self.close()