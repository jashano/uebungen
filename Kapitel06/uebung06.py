from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import sys
import urllib.parse

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel06/showmap.ui", self)
        self.setWindowTitle("Main Window - [Preview]")
        self.show()
        
        self.button.clicked.connect(self.buttonclick)

    def buttonclick(self):
        lon = self.lineEdit.text()
        lat = self.lineEdit_2.text()

        #String mit inputwerten erstellen
        query = f"{lon}, {lat}"

        #string mit urllib verändern wegen umlauten etc
        appendix = urllib.parse.quote(query)

        #link erzeugen und öffnen
        linkmap = f"http://maps.google.com/maps/place/{appendix}"
        QDesktopServices.openUrl(QUrl(linkmap))


app = QApplication([])
win = UIFenster()
app.exec()