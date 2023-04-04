# conda install pyqt -y

import sys
from PyQt5.QtWidgets import *

# Fenster-Klasse: wird von QWindow vererbt
class MyWindow(QMainWindow):
    def __init__(self):      # Konstruktor
        super().__init__()   # Konstruktor Basis-Klasse

        #self.setGeometry(10,10,640,480)
        self.setMinimumWidth(640)
        self.setMinimumHeight(480)

        self.setWindowTitle("Hello World")  # Fenster-Titel setzen
        self.show()  # Fenster anzeigen/sichtbar machen

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()