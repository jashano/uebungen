import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("QVBoxLayout Demo")

        # Layout erstellen:
        layout = QVBoxLayout()

        # Widget-Instanzen erstellen:
        label = QLabel("Hello World")
        edit = QLineEdit()
        button = QPushButton("Ok")

        # Widgets dem Layout hinzufügen:
        layout.addWidget(label)
        layout.addWidget(edit)
        layout.addWidget(button)

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