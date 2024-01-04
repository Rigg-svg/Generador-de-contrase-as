from base_datos import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QApplication, QTableWidget, QDialog, QHeaderView, QTableWidgetItem

class misContraseñas(QDialog):
    def __init__(self, ventanaPrincipal):
        super().__init__()
        self.setModal(True) #El usuario no puede interactuar con la otras ventanas. Asta que cierre esta
        self.ventanaPrincipal = ventanaPrincipal
        self.baseDatos = DB()
        self.ventanaInicializada = False

    def inicilalizarIU(self):
        self.setWindowTitle("Mis contraseñas")
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
        self.generarTabla() #Se llama el metodo para crear el objeto tabla. Se crea como instancia : self.tabla

        main_layout = QVBoxLayout()

        btn_regresar = QPushButton("Regresar")
        btn_regresar.setFixedSize(100, 30)
        btn_regresar.clicked.connect(self.regresar)

        main_layout.addStretch(1)
        main_layout.addWidget(self.tabla, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) #Centar la tabla en el Layout
        main_layout.addStretch(1)
        main_layout.addWidget(btn_regresar, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) #Centar el boton
        

        self.setLayout(main_layout)

        #self.finished.connect(self.eliminarDiseño)

    def generarTabla(self):

        self.tabla = QTableWidget(40,2) #Crear un widget tabla con 2 filas y dos columnas
        self.tabla.setFixedSize(400, 200) #Establcer un tamaño fijo de tabla

        self.tabla.cellClicked.connect(self.slot_cell_clicked) 

        self.tabla.setHorizontalHeaderLabels(["Contraseña", "Disposición"]) #Establecer los header de la columnas
        
        header = self.tabla.horizontalHeader() #Obtener el Header de la tabla

        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch) #Hacer que la tabla ocupe le espacio restante.

    def addItemsTable(self): #Funcion para agregar los items a la tabla

        usuario = self.ventanaPrincipal.usuario
        self.baseDatos.verificarRegistro(usuario)

        datos = self.baseDatos.obtenerDatos()

        for row, item in enumerate(datos): 
            contraseña, mensaje = item

            itemContraseña = QTableWidgetItem(contraseña)
            itemMensaje = QTableWidgetItem(mensaje)

            self.tabla.setItem(row, 0, itemContraseña)
            self.tabla.setItem(row, 1, itemMensaje)

    def slot_cell_clicked(self, row, col):
        item = self.tabla.item(row, col)

        if item is not None:
            portapapeles = QApplication.clipboard()
            portapapeles.setText(item.text())

    def regresar(self):#Funcion del boton (btn_regrsar)
        self.close()