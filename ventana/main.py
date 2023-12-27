import typing, sys
from script import *
from ventanaContrasena import *
from agregarContrasena import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette, QFont
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QApplication, QLineEdit


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
        color_de_fondo.setAlphaF(0.5) #Establecer la transparencia al 50% (0 = 0% | 1 = 100%)
        
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

        #Mensaja del footer
        mensaje = QLabel(self)
        mensaje.setText("Si no seleciona ninguna de las opciones, la contraseña solo se generara en letras minusculas")
        mensaje.move(30, 350)
        mensaje_styles = """
            QLabel{
                font-family: 'Roboto';
                font-size: 10px;
                font-weight: bold;
            }
        """
        mensaje.setStyleSheet(mensaje_styles)

        #Campo donde se mostrara la contraseña
        self.mostrarContrasena = QLineEdit(self)
        self.mostrarContrasena.setDisabled(True)
        self.mostrarContrasena.setText("'Oprima el boton GENERAR'")
        self.mostrarContrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mostrarContrasena.resize(150, 25)
        self.mostrarContrasena.move(250, 180)
        mostrarContrasena_styles = """
            QLineEdit {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
                font-size: 11px;
            }
        """
        self.mostrarContrasena.setStyleSheet(mostrarContrasena_styles)

        #boton para copiar la contraseña
        btn_copiar = QPushButton(self)
        btn_copiar.setText("COPIAR")
        btn_copiar.resize(50, 25)
        btn_copiar.move(410, 180)
        btn_copiar_styles = """
            QPushButton {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """
        btn_copiar.setStyleSheet(btn_copiar_styles)

        btn_copiar.clicked.connect(self.copiar)

        #Boton para agregar la contraseña a mis contraseñas
        btn_agregar_Miscontrasenas = QPushButton(self)
        btn_agregar_Miscontrasenas.setText("Agregar a mis contraseñas")
        btn_agregar_Miscontrasenas.resize(210, 25)
        btn_agregar_Miscontrasenas.move(250, 220)
        btn_agregar_Miscontrasenas_styles = """ 
            QPushButton {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """
        btn_agregar_Miscontrasenas.setStyleSheet(btn_agregar_Miscontrasenas_styles)
        btn_agregar_Miscontrasenas.clicked.connect(self.agregarContrasena)

        #Boton para generar un nueva contraseña
        btn_generar = QPushButton(self)
        btn_generar.setText("GENERAR")
        btn_generar.resize(75, 30)
        btn_generar.move(310, 260)
        btn_generar_styles = """
            QPushButton {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """
        btn_generar.setStyleSheet(btn_generar_styles)

        btn_generar.clicked.connect(self.generar)

        #Boton para ir a la sección de mis contraseñas
        btn_misContrasenas = QPushButton(self)
        btn_misContrasenas.setText("Mis contraseñas")
        btn_misContrasenas.resize(75, 25)
        btn_misContrasenas.move(410, 20)
        btn_misContrasenas_styles = """
            QPushButton {
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 8px;
                color: #0E719C;
                font-family: 'Roboto';
                font-size: 10px;
            }
        """
        btn_misContrasenas.setStyleSheet(btn_misContrasenas_styles)
        btn_misContrasenas.clicked.connect(self.misContrasenas)

    def generar(self): #Boton para generar contraseña
        
        opcionMayus = self.checkbox_mayus.isChecked()
        opcionSimbols = self.checkbox_simbols.isChecked()
        opcionNumbers = self.checkbox_numbers.isChecked()

        contraseña = generarContrasena(opcionMayus, opcionSimbols, opcionNumbers)
        
        self.mostrarContrasena.setText(contraseña)
        self.mostrarContrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def copiar(self): #Boton que copia la contraseña en el portapapeles

        portapapeles = QApplication.clipboard() #Crea una intancia del portapapeles del sistema usando el metodo .clipboard

        contraseña = self.mostrarContrasena.text() #.text() se usa para obtener el texto de un objeto QLineEdit().

        #El if es para solo copiar si se ha generado una contraseña. De lo contrario copiaria el texto que cumple la funcion de placeholder en el objeto QTextEdit

        if contraseña != "'Oprima el boton GENERAR'":
            # Copiar el texto al portapapeles
            portapapeles.setText(contraseña)
            print(contraseña)

    def misContrasenas(self):
        self.ventana_misContraseñas = misContraseñas()
        self.ventana_misContraseñas.show()

    def agregarContrasena(self):
        contraseña = self.mostrarContrasena.text() #obtener la contraseña que esta en el objeto QLineEdit

        if contraseña != "'Oprima el boton GENERAR'":
            self.ventana_agregar = agregarContraseña(self) #Se pasa la clase del ventana principal (class ventana()) para crear una intancia de la ventana principal en la ventana de agregar a mis contraseñas 
            self.ventana_agregar.show()
    
    def maximizar_ventana_principal(self):
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = ventana()
    sys.exit(app.exec())