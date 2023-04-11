import sys
import urllib.parse
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Fenster-Klasse: wird von QWindow vererbt
class MyWindow(QMainWindow):
    def __init__(self):      # Konstruktor
        super().__init__()   # Konstruktor Basis-Klasse

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
        self.birthdayEdit.setDisplayFormat("dd/MM/yyyy") #besser wäre hier ISOnorm
        self.countryEdit.addItems(['Schweiz', 'Deutschland', 'Österreich'])


        # Layout füllen
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

        # Buttons dem Layout hinzufügen und ausführung zuweisen
        button1 = QPushButton("Auf Karte zeigen")
        button1.clicked.connect(self.karteoeffnen)
        button2 = QPushButton("Laden")
        button2.clicked.connect(self.dateiladen)
        button3 = QPushButton("Speichern")
        button3.clicked.connect(self.speichern)
        layout_bottom.addWidget(button1)
        layout_bottom.addWidget(button2)
        layout_bottom.addWidget(button3)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Menubar 
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        filemenu1 = menubar.addMenu("View")

        save = QAction("Speichern", self)
        quit = QAction("Beenden", self)
        karte = QAction("Karte", self)

        save.setShortcut('Ctrl+S')
        save.triggered.connect(self.speichern)

        quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" zuweisen, nur für MacOS relevant
        quit.setShortcut('Ctrl+Q')
        quit.triggered.connect(self.close)

        karte.triggered.connect(self.karteoeffnen)
        karte.setShortcut('Ctrl+M')

        filemenu.addAction(save)
        filemenu.addAction(quit)
        filemenu1.addAction(karte)


# -----------------------------------------------------------------        

    def speichern(self):
        # Inputdaten
        vorname = self.vornameLineEdit.text()
        nachname = self.nameLineEdit.text()
        adresse = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        geburtstag = self.birthdayEdit.text()
        land = self.countryEdit.currentText()

        # String mit inputwerten erstellen
        datenstring = f"{vorname},{nachname},{geburtstag},{plz},{ort},{adresse},{land}\n"

        #Dateiort definiereren
        location = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        filename, filter = QFileDialog.getSaveFileName(self,"Datei speichern",location,"Text (*.txt)")

        #Wenn File definiert, schreibe file.
        if filename:
            file = open(filename, "a", encoding="utf-8")
            file.write(datenstring)
            file.close()

# -----------------------------------------------------------------   

    def karteoeffnen(self):
        #Inputdaten
        adresse = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        land = self.countryEdit.currentText()

        #String mit inputwerten erstellen
        query = f"{adresse}, {plz} {ort}, {land}"

        #string mit urllib verändern wegen umlauten etc
        appendix = urllib.parse.quote(query)

        #link erzeugen und öffnen
        linkmap = f"http://maps.google.com/maps/place/{appendix}"
        QDesktopServices.openUrl(QUrl(linkmap))

# -----------------------------------------------------------------   

    def dateiladen(self):
        location = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        filename, filter = QFileDialog.getOpenFileName(self,"Datei öffnen",location,"Text (*.txt)")
        if (filename != ""):
        # Inhalt der Datei lesen
            with open(filename, "r", encoding="utf-8") as file:
              fileContent = file.read()

            # Inhalt in QTextEdit anzeigen
            textEdit = QTextEdit()
            textEdit.setText(fileContent)

            # QDialog erstellen und QTextEdit als zentrales Widget setzen
            dialog = QDialog(self)
            layout = QVBoxLayout()
            layout.addWidget(textEdit)
            dialog.setLayout(layout)

            #Fenstergestaltung
            dialog.setWindowTitle(filename)
            dialog.setMinimumWidth(800)
            dialog.setMinimumHeight(420)

            # Dialog anzeigen
            dialog.exec_()

# -----------------------------------------------------------------------------

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()