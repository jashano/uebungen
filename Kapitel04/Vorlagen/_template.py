from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(540)
        self.setMinimumHeight(420)
        self.setWindowTitle("GUI-Programmierung")  # Fenster-Titel setzen
        self.show()  # Fenster anzeigen/sichtbar machen

        #layout erzeugen
        #layout = ... # QVBoxLayout, QHBoxLayout, QGridlayout, ...
        layout = QVBoxLayout()
        #layout_top = QFormLayout()
        #layout_bottom = QVBoxLayout()    

        # Widget-Instanzen erstellen:
        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.UhrzeitEdit = QTimeEdit
        self.birthdayEdit = QDateEdit()
        self.countryEdit = QComboBox()

        #Widgets Spezifizieren
        self.birthdayEdit.setDisplayFormat("dd/MM/yyyy") #besser wäre hier ISOnorm
        self.countryEdit.addItems(['Schweiz', 'Deutschland', 'Österreich'])
     
        #gui Elemente dem Layout hinzufügen

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()


app = QApplication([])
win = Fenster()
app.exec()