import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("Grid Layout")

        # Layout erstellen:
        layout = QGridLayout()

        # Widget-Instanzen erstellen:
        nameLabel = QLabel("Name:")
        nameLine = QLineEdit()
        addressLabel = QLabel("Address:")
        addressText = QTextEdit()

        # Widgets mit Grid-Koordinaten dem Layout hinzufügen
        layout.addWidget(nameLabel, 0, 0)
        layout.addWidget(nameLine, 0, 1)
        layout.addWidget(addressLabel, 1, 0, Qt.AlignTop)
        layout.addWidget(addressText, 1, 1)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()