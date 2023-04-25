import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("Fenster")

        # Layout erstellen:
        layout = QVBoxLayout()
        layout_bottom = QHBoxLayout()

        # Widget-Instanzen erstellen:
        label = QLabel("Ist dieses Datum in Ordnung?")
        calendar = QCalendarWidget()
        button1 = QPushButton("Ja",)
        button2 = QPushButton("Nein",)
        button3 = QPushButton("Abbrechen",)

        # Widgets dem Layout hinzufügen:

        layout.addWidget(calendar)
        layout.addWidget(label)

        layout.addLayout(layout_bottom)
        
        layout_bottom.addWidget(button1)
        layout_bottom.addWidget(button2)
        layout_bottom.addWidget(button3)

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