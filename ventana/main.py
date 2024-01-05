import sys
from script import *
from ventanaContrasena import *
from agregarContrasena import *
from base_datos import *

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette, QFont, QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QCheckBox, QLabel, QApplication, QLineEdit, QMessageBox, QFormLayout, QHBoxLayout, QSpacerItem, QSizePolicy


class ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicilalizarIU()

        self.inicioSeccionExitoso = False #saber si el usuario ya inicio sección
        self.ventana_misContraseñas = misContraseñas(self)#Crear la intancia para abrir la ventana "mis contraseñas"
        self.ventana_noRegistrado = ventanaError(self)#Crear una instancia de para mostrar la ventana Error, que no iniciado sección
        self.ventana_agregar = agregarContraseña(self) #Se pasa la clase del ventana principal (class ventana()) para crear una intancia de la ventana principal en la ventana de agregar a mis contraseñas
        self.usuario = ''

        self.showMaximized()

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

    def misContrasenas(self):
        if self.inicioSeccionExitoso:

            if self.ventana_misContraseñas.ventanaInicializada is not True:
                self.ventana_misContraseñas.inicilalizarIU()
                self.ventana_misContraseñas.addItemsTable()
                self.ventana_misContraseñas.showMaximized()#mazimar la ventana 'mis contraseñas'
                self.ventana_misContraseñas.ventanaInicializada = True
                self.showMinimized() #minimizar la 'ventana principal'

            else:
                self.ventana_misContraseñas.addItemsTable()
                self.ventana_misContraseñas.showMaximized() #mazimar la ventana 'mis contraseñas'
                self.showMinimized() #minimizar la 'ventana principal'
        else:
            self.ventana_noRegistrado.incializarVentana() #Abrir la ventana de error, si el usuario aún no ha iniciado sección

    def agregarContrasena(self):
        contraseña = self.mostrarContrasena.text() #obtener la contraseña que esta en el objeto QLineEdit

        if self.inicioSeccionExitoso is not True:
            self.ventana_noRegistrado.incializarVentana()

        else:
            if contraseña != "'Oprima el boton GENERAR'":
                self.ventana_agregar.inicilalizarIU()


#ventanas de error, ventana de rigsitrarce y iniciar sección
class ventanaError(QDialog):
    def __init__(self, ventanaPrincipal) :
        super().__init__()
        self.setModal(True)
        self.ventanaPrincipal = ventanaPrincipal

    def incializarVentana(self):
        self.setWindowIcon(QIcon("Icons/warning.png")) #Establecer el icono de la ventana
        paleta = self.palette() #Se debe crear un objeto paleta

        # Establecer el color de fondo deseado
        color_de_fondo = QColor(2, 179, 255)  #color de  fondo
        color_de_fondo.setAlphaF(0.5) #Establecer la transparencia al 50% (0 = 0% | 1 = 100%)

        paleta.setColor(QPalette.ColorRole.Window, color_de_fondo)
        self.setPalette(paleta)

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint) #Establecer que la ventana que contraponga antes la otras que esten abiertas

        self.setGeometry(300, 300, 300, 300)
        self.setMaximumSize(300, 300) #tamaño maximo en ancho y alto de la ventana
        self.setMinimumSize(300,300) #tamaño minimo en ancho y alto de la ventana
        self.setWindowTitle("ERROR")

        mensaje = QLabel("  ERROR DEBE REGISTRARCE O INICIAR SECCION\n ANTES DE PODER AGREGAR A SU CONTRASEÑAS", self)
        mensaje.move(25, 100)
        mensaje_styles = """
            QLabel {
                font-size: 10px;
                font-weight: bold;
                font-family: 'Roboto';
                color: #ffffff;
            }
        """

        mensaje.setStyleSheet(mensaje_styles)

        btn_cerrar = QPushButton("CERRAR", self)
        btn_cerrar.move(234, 25)
        btn_cerrar.resize(45, 18)
        btn_cerrar.clicked.connect(self.cerrarVentana)
        btn_cerrar_styles = """
            QPushButton{
                background-color: lightgray;
                border: 1px solid black;
                border-radius: 5px;
                color: #0E719C;
                font-size: 10px;
                font-family: 'Roboto';
                font-weight: bold;
            }
        """
        btn_cerrar.setStyleSheet(btn_cerrar_styles)

        btn_registrarce = QPushButton("REGISTRARCE", self)
        btn_registrarce.move(20, 245)
        btn_registrarce.resize(100, 20)
        btn_registrarce.clicked.connect(self.registrarce)
        btn_registrarce_styles = """
            QPushButton{
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 5px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """
        btn_registrarce.setStyleSheet(btn_registrarce_styles)

        btn_inciarSeccion = QPushButton("INICIAR SECCIÓN", self)
        btn_inciarSeccion.move(185, 245)
        btn_inciarSeccion.resize(100, 20)
        btn_inciarSeccion.clicked.connect(self.iniciarSeccion)
        btn_inciarSeccion_styles = """
            QPushButton{
                background-color: lightgray;
                border: 1.5px solid black;
                border-radius: 5px;
                color: #0E719C;
                font-family: 'Roboto';
            }
        """
        btn_inciarSeccion.setStyleSheet(btn_inciarSeccion_styles)

        warningIcon = QLabel(self)
        warningIcon.setPixmap(QIcon("Icons/warningSVG.svg").pixmap(64, 64))
        warningIcon.move(120, 150)

        self.show() #mostrar la ventana


    def registrarce(self):
        self.ventana_registrarce = ventanaRegistrarce(self)
        self.ventana_registrarce.iniciarVentana()

    def iniciarSeccion(self):
        self.ventana_iniciar_seccion = ventanaIniciarSeccion(self)
        self.ventana_iniciar_seccion.iniciarVentana()

    def cerrarVentana(self):
        self.close()

#***************************************************************************************
class ventanaRegistrarce(QDialog):
    def __init__(self, ventanaPadre):
        super().__init__()
        self.baseDatos = DB()
        self.ventanaPadre = ventanaPadre
        self.setModal(True)

    def iniciarVentana(self):
        paleta = self.palette() #Se debe crear un objeto paleta

        # Establecer el color de fondo deseado
        color_de_fondo = QColor(2, 179, 255)  #color de  fondo
        color_de_fondo.setAlphaF(0.5) #Establecer la transparencia al 50% (0 = 0% | 1 = 100%)

        paleta.setColor(QPalette.ColorRole.Window, color_de_fondo)
        self.setPalette(paleta)

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint) #Establecer que la ventana que contraponga antes la otras que esten abiertas

        self.setGeometry(300,300,300,220)
        self.setMaximumSize(300, 300) #tamaño maximo en ancho y alto de la ventana
        self.setMinimumSize(300,300) #tamaño minimo en ancho y alto de la ventana
        self.setWindowTitle("REGISTRARCE")

        self.widgets()

        self.show()

    def widgets(self):
        main_layout = QFormLayout()

        labelInput1 = QLabel("Nombre de usuario:")
        self.inputBox1 = QLineEdit()

        labelInput2 = QLabel("Contraseña:")
        self.inputBox2 = QLineEdit()

        labelInput3 = QLabel("Repita contraseña:")
        self.inputBox3 = QLineEdit()

        btn_registrarse = QPushButton("REGISTRARSE")
        btn_registrarse.clicked.connect(self.registrarUsuario)

        main_layout.setVerticalSpacing(30)

        main_layout.addRow(labelInput1, self.inputBox1)
        main_layout.addRow(labelInput2, self.inputBox2)
        main_layout.addRow(labelInput3, self.inputBox3)
        main_layout.addRow(btn_registrarse)

        self.setLayout(main_layout)

    def registrarUsuario(self):
        usuario, contraseña, contraseña2 = self.inputBox1.text(), self.inputBox2.text(), self.inputBox3.text()
        
        if contraseña != contraseña2:
            QMessageBox.warning(self, 
                                "REGISTRAR USUARIO", 
                                f"Las contraseñas no coinciden", 
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
            
        elif contraseña == contraseña2:

            if self.baseDatos.verificarRegistro(usuario) == None:

                self.baseDatos.registrarUsuario(usuario, contraseña)
                QMessageBox.information(self, 
                                "REGISTRAR USUARIO", 
                                f"Usuario:  {usuario} ¡REGISTRADO EXITOXAMENTE!", 
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
                self.close()

            else:
                QMessageBox.warning(self, 
                                "REGISTRAR USUARIO", 
                                f"El usuario '{usuario}' ya se encuentra registrado", 
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)

#***************************************************************************************
class ventanaIniciarSeccion(QDialog):
    def __init__(self, ventanaPadre):
        super().__init__()
        self.baseDatos = DB()
        self.ventanaPadre = ventanaPadre
        self.setModal(True)


    def iniciarVentana(self):
        paleta = self.palette() #Se debe crear un objeto paleta

        # Establecer el color de fondo deseado
        color_de_fondo = QColor(2, 179, 255)  #color de  fondo
        color_de_fondo.setAlphaF(0.5) #Establecer la transparencia al 50% (0 = 0% | 1 = 100%)

        paleta.setColor(QPalette.ColorRole.Window, color_de_fondo)
        self.setPalette(paleta)

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint) #Establecer que la ventana que contraponga antes la otras que esten abiertas

        self.setGeometry(300,300,300,220)
        self.setMaximumSize(300, 300) #tamaño maximo en ancho y alto de la ventana
        self.setMinimumSize(300,300) #tamaño minimo en ancho y alto de la ventana
        self.setWindowTitle("INICIAR SECCIÓN")

        self.widgets()

        self.show()

    def widgets(self):
        main_layout = QFormLayout()

        labelInput1 = QLabel("Nombre de usuario:")
        self.inputBox1 = QLineEdit()

        labelInput2 = QLabel("Contraseña:")
        self.inputBox2 = QLineEdit()

        btn_inciarSeccion = QPushButton("INICIAR SECCIÓN")
        btn_inciarSeccion.clicked.connect(self.iniciarSeccion)

        checkboxContrasena = QCheckBox()
        checkboxContrasena.setText("ver contraseña")

        btn_regresar = QPushButton("REGRESAR")
        btn_regresar.clicked.connect(self.regresar)

        main_layout.setVerticalSpacing(30)

        self.setContentsMargins(0, 40, 0, 40)

        layoutContrasena = QHBoxLayout()
        layoutContrasena.addWidget(labelInput2)
        layoutContrasena.addSpacing(49)
        layoutContrasena.addWidget(self.inputBox2)

        layoutContrasena_checkbox = QVBoxLayout()
        layoutContrasena_checkbox.addLayout(layoutContrasena)
        #layoutContrasena_checkbox.addSpacing(10)
        layoutContrasena_checkbox.addWidget(checkboxContrasena)

        main_layout.addRow(labelInput1, self.inputBox1)
        main_layout.addRow(layoutContrasena_checkbox)

        main_layout.addRow(btn_inciarSeccion)
        main_layout.addRow(btn_regresar)

        self.setLayout(main_layout)

    def iniciarSeccion(self):
        usuario, contraseña = self.inputBox1.text(), self.inputBox2.text()

        contraseñaAlmacenada = self.baseDatos.verificarRegistro(usuario) #La funcion devulve un tupla con 4 valores

        if contraseñaAlmacenada:
        
            if self.baseDatos.inciarSeccion(contraseña, contraseñaAlmacenada[2]):
                QMessageBox.information(self,
                                        "INICIAR SECCIÓN",
                                        "¡INICIO DE SECCIÓN EXITOSO! Ahora puede ingresar a su sección en el boton mis contraseñas",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.ventanaPadre.ventanaPrincipal.inicioSeccionExitoso = True
                self.ventanaPadre.ventanaPrincipal.usuario = usuario #Usuario que inicio sección
                self.close()

            else:
                QMessageBox.warning(self,
                                "INICIAR SECCIÓN",
                                "La contraseña o el usuario son incorrectos",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            QMessageBox.warning(self,
                                "INICIAR SECCIÓN",
                                f"El usuario '{usuario} no esta registrado'",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

    def regresar(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = ventana()
    sys.exit(app.exec())