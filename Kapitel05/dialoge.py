from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("layout")

        #layout erzeugen ------------------------------------------------------------
        layout = QVBoxLayout()

        #menubar erstellen ----------------------------------------------------------

        #gui Elemente erstellen -----------------------------------------------------
        button1 = QPushButton("Info")
        button2 = QPushButton("About")
        button3 = QPushButton("Warnig")
        button4 = QPushButton("Question")
        button5 = QPushButton("Load")
        button6 = QPushButton("Save")
        button7 = QPushButton("Zahl")
        button8 = QPushButton("Auswahl")
        button9 = QPushButton("Text")
        button0 = QPushButton("Weiteres...")
     
        #gui Elemente dem Layout hinzufügen -----------------------------------------
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(button8)
        layout.addWidget(button9)
        layout.addWidget(button0)


        #layout hinzufügen ----------------------------------------------------------

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        # Fenster anzeigen ----------------------------------------------------------

        self.show()
        self.raise_()

        # Connects erstellen --------------------------------------------------------
        button1.clicked.connect(self.info)
        button2.clicked.connect(self.about)
        button3.clicked.connect(self.warning)
        button4.clicked.connect(self.question)
        button5.clicked.connect(self.load)
        button6.clicked.connect(self.save)
        button7.clicked.connect(self.zahl)
        button8.clicked.connect(self.auswahl)
        button9.clicked.connect(self.texteingabe)
        button0.clicked.connect(self.weiteres)

    

    

    #Konstruktor Menubefehle --------------------------------------------------------


    #Konstruktor Widgets ------------------------------------------------------------
    def info(self):
        QMessageBox.information(self, "Titel", "Text")


    def about(self):
        pass

    def warning(self):
        QMessageBox.warning(self, "Titel", "Kann nicht gespeichert werden")

    def question(self):
        antwort = QMessageBox.question(self, "Titel", "Hallo?", QMessageBox.Ok, QMessageBox.Cancel)

        if antwort == QMessageBox.Yes:
            QMessageBox.about(self, "Antwort", "Ja")
        
        else:
            QMessageBox.about(self, "Antwort", "Nein")

    def load(self):
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Python Files (*.py)")

        if filename != "":
            print(filename)
            #hier werden Befehle für Operationen angegeben
        else:
            print("abgebrochen")

        print(filter)

    def save(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text Datei (*.txt)")
        print(filename)

    def zahl(self):
        zahl, ok = QInputDialog.getDouble(self, "Titel", "Geben sie eine Zahl ein",10,5,15)
        if ok:
            if zahl == 12:
                print("richtig")
            else:
                print("falsch")
        else:
            print("abgebrochen")

    def auswahl(self):
        farbe, ok = QInputDialog.getItem(self, "Auswahl", "Was ist deine Lieblingsfarbe?", ["rot", "blau", "gelb", "orange"], 1, True)
        if ok:
            print(farbe)

    def texteingabe(self):
        text, ok = QInputDialog.getText(self,"Titel","Bitte Text eingeben",QLineEdit.Normal,"") #QLineEdit.Password existiert auch
        if ok:
            print(text)

    def weiteres(self):
        color = QColorDialog.getColor()
        print(color.red(),color.green(),color.blue())
        #font=QFontDialog.getFont()


app = QApplication([])
win = Fenster()
app.exec()