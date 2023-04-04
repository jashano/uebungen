import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ##########
        # LAYOUT #
        ##########

        # Fenster-Titel definieren:
        self.setWindowTitle("Signal Slot Demo")

        # Layout erstellen:
        layout = QVBoxLayout()

        # Widget-Instanzen erstellen:
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Widgets dem Layout hinzufügen:
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

        ############
        # CONNECTS #
        ############

        # Klick auf Button 1 ruft die Funktion button1_pressed() auf
        button1.clicked.connect(self.button1_clicked)

        # Klick auf Button 2 ruft die Funktion button1_pressed() auf
        button2.clicked.connect(self.button2_clicked)


    def button1_clicked(self):
        print("Der Button 1 wurde gedrückt")

    def button2_clicked(self):
        print("Der Button 2 wurde gedrückt")


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()