# conda install pyqt -y

import sys
from PyQt5.QtWidgets import *

# Fenster-Klasse: wird von QWindow vererbt
class MyWindow(QMainWindow):
    def __init__(self):      # Konstruktor
        super().__init__()   # Konstruktor Basis-Klasse

        #self.setGeometry(10,10,640,480)
        self.setMinimumWidth(540)
        self.setMinimumHeight(420)
        self.setWindowTitle("GUI-Programmierung")  # Fenster-Titel setzen
        self.show()  # Fenster anzeigen/sichtbar machen

        # Layout erstellen:
        layout = QVBoxLayout()
        layout_top = QFormLayout()
        layout_bottom = QVBoxLayout()    

        # Widget-Instanzen erstellen:
        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.birthdayEdit = QDateEdit()
        self.countryEdit = QComboBox()
        

        #WidgetSpezifikationen
        self.birthdayEdit.setDisplayFormat("dd/MM/yyyy")
        self.countryEdit.addItems(['Schweiz', 'Deutschland', 'Österreich'])


        # Layout füllen:
        layout_top.addRow("Vorname:", self.vornameLineEdit)
        layout_top.addRow("Name:", self.nameLineEdit)
        layout_top.addRow("Geburtstag:", self.birthdayEdit)
        layout_top.addRow("Adresse:", self.adresseLineEdit)
        layout_top.addRow("Postleitzahl:", self.plzLineEdit)
        layout_top.addRow("Ort:", self.ortLineEdit)
        layout_top.addRow("Land:", self.countryEdit)

        # Layouts anordnen
        layout.addLayout(layout_top)
        layout.addLayout(layout_bottom)

        # Buttons dem Layout hinzufügen
        button1 = QPushButton("Save")
        button1.clicked.connect(self.speichern)
        layout_bottom.addWidget(button1)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Menubar 
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        quit = QAction("Quit", self)

        save.setShortcut('Ctrl+S')
        save.triggered.connect(self.speichern)

        quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" zuweisen, nur für MacOS relevant
        quit.setShortcut('Ctrl+Q')
        quit.triggered.connect(self.close)
        filemenu.addAction(save)
        filemenu.addAction(quit)


# -----------------------------------------------------------------        

    def speichern(self):
         
        # inputdaten
        vorname = self.vornameLineEdit.text()
        nachname = self.nameLineEdit.text()
        addresse = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        geburtstag = self.birthdayEdit.text()
        land = self.countryEdit.currentText()

        # string mit inputwerten
        datenstring = f"{vorname},{nachname},{geburtstag},{plz},{ort},{addresse},{land}\n"

        # string in file speichern
        file = open('Kapitel04/output.txt', "a", encoding="utf-8")
        file.write(datenstring)
        file.close() 

# -----------------------------------------------------------------------------

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()