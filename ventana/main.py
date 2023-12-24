import typing, sys
from script import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette, QFont
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QApplication, QTextEdit


class ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicilalizarIU()

        self.show()

    def inicilalizarIU(self):
        self.setWindowTitle("Generador de contraseñas")
        self.setGeometry(500,500,500,500)
        self.setMaximumSize(500, 500) #tamaño maximo en ancho y alto de la ventana
        self.setMinimumSize(500,500) #tamaño minimo en ancho y alto de la ventana

        paleta = self.palette() #Se debe crear un objeto paleta

        # Establecer el color de fondo deseado
        color_de_fondo = QColor(2, 179, 255)  #color de  fondo
        color_de_fondo.setAlphaF(0.5) #Establecer la transparencia al 50% (0 = 0% - 1 = 100%)
        
        paleta.setColor(QPalette.ColorRole.Window, color_de_fondo)
        self.setPalette(paleta)

        self.generarInterfaz()

    def generarInterfaz(self):
        #geometry (500,500,500,500)

        titulo = QLabel(self)
        titulo.setText("GENERADOR DE CONTRASEÑAS")
        titulo.setFont(QFont('Roboto', 14))
        titulo.move(120, 80)
        paleta = titulo.palette()
        
        # Establecer el color del texto deseado
        color_de_texto = QColor(255, 255, 255)  # color del texto
        paleta.setColor(QPalette.ColorRole.WindowText, color_de_texto)

        # Aplicar la paleta actualizada a la etiqueta
        titulo.setPalette(paleta)

        #checkboxes
        #mayus
        self.checkbox_mayus = QCheckBox(self)
        self.checkbox_mayus.setText("Mayusculas")
        self.checkbox_mayus.setFont(QFont('Roboto', 12))
        self.checkbox_mayus.move(50, 180)

        #numbers
        self.checkbox_numbers = QCheckBox(self)
        self.checkbox_numbers.move(50, 220)
        self.checkbox_numbers.setText("Numeros")
        self.checkbox_numbers.setFont(QFont('Roboto', 12)) 

        #simbolos
        self.checkbox_simbols = QCheckBox(self)
        self.checkbox_simbols.move(50, 260)
        self.checkbox_simbols.setText("Simbolos")
        self.checkbox_simbols.setFont(QFont('Roboto', 12)) 


        mensaje = QLabel(self)
        mensaje.setText("Si no seleciona ninguna de las opciones, la contraseña solo se generara en letras minusculas")
        mensaje.setFont(QFont('Roboto', 8))
        mensaje.move(30, 350)

        self.mostrarContrasena = QTextEdit(self)
        self.mostrarContrasena.setDisabled(True)
        self.mostrarContrasena.setText("Contraseña Generada")
        self.mostrarContrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mostrarContrasena.resize(150, 25)
        self.mostrarContrasena.move(250, 200)


        btn_generar = QPushButton(self)
        btn_generar.setText("Generar")
        btn_generar.resize(75, 30)
        btn_generar.move(310, 250)
        btn_generar.clicked.connect(self.generar)

        btn_copiar = QPushButton(self)
        btn_copiar.setText("Copiar")
        btn_copiar.resize(50, 25)
        btn_copiar.move(410, 200)
        btn_copiar.clicked.connect(self.copiar)

    def generar(self): #Boton para generar contraseña
        
        opcionMayus = self.checkbox_mayus.isChecked()
        opcionSimbols = self.checkbox_simbols.isChecked()
        opcionNumbers = self.checkbox_numbers.isChecked()

        contraseña = generarContrasena(opcionMayus, opcionSimbols, opcionNumbers)
        
        self.mostrarContrasena.setText(contraseña)
        self.mostrarContrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def copiar(self): #Boton que copia la contraseña en el portapapeles

        portapapeles = QApplication.clipboard() #Crea una intancia del portapapeles del sistema usando el metodo .clipboard

        contraseña = self.mostrarContrasena.toPlainText() #.toPlainTexT() se usa para obtener el texto de un objeto QTextEdit.

        #El if es para solo copiar si se ha generado una contraseña. De lo contrario copiaria el texto que cumple la funcion de placeholder en el objeto QTextEdit

        if contraseña != "Contraseña Generada":
            # Copiar el texto al portapapeles
            portapapeles.setText(contraseña)
            print(contraseña)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = ventana()
    sys.exit(app.exec())