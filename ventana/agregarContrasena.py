import sys
#from main import ventana
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDialog

class agregarContraseña(QDialog):
    def __init__(self, contraseña):
        self.contraseña = contraseña
        super().__init__()
        self.setModal(True)
        self.inicilalizarIU()

        #self.show()

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

        self.generarInterfaz()

    def generarInterfaz(self):
        titulo_contrasena = QLabel(self)
        titulo_contrasena.setText("Contraseña")
        titulo_contrasena.move(225, 135)

        titulo_dispocicion = QLabel(self)
        titulo_dispocicion.setText("Dispocición")
        titulo_dispocicion.move(230, 245)

        campo_contrasena = QLineEdit(self)
        campo_contrasena.resize(100, 30)
        campo_contrasena.move(207, 157)
        campo_contrasena.setDisabled(True)
        campo_contrasena.setText(self.contraseña)
        campo_contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)
        campo_contrasena_styles = """
            QLineEdit {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """

        campo_contrasena.setStyleSheet(campo_contrasena_styles)

        campo_mensaje = QLineEdit(self)
        campo_mensaje.resize(200, 30)
        campo_mensaje.move(155, 266)

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


    def cancelar(self):
        self.close()

    def guardar(self):
        print(self.contraseña)


""" if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = agregarContraseña()
    sys.exit(app.exec()) """