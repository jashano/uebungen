import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("Mehrere Layouts")

        # Layout erstellen:
        layout_top = QVBoxLayout()
        layout_bottom = QHBoxLayout()

        # 3 Push-Buttons erzeugen:
        button1 = QPushButton("Hello")

        button2 = QPushButton("PyQt5")
        button3 = QPushButton("World")

        # Buttons dem ersten (vertikalen) Layout hinzufügen
        layout_top.addWidget(button1)

        # Restliche Buttons dem zweiten (horizontalen) Layout hinzufügen
        layout_bottom.addWidget(button2)
        layout_bottom.addWidget(button3)

        # Dem ersten Layout das zweite Layout hinzufügen!
        layout_top.addLayout(layout_bottom)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout_top)

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