from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        #layout erzeugen
        #layout = ... # QVBoxLayout, QHBoxLayout, QGridlayout, ...

        #gui Elemente erstellen
     
        #gui Elemente dem Layout hinzufügen

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()


app = QApplication([])
win = Fenster()
app.exec()