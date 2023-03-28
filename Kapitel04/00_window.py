from PyQt5.QtWidgets import *

class Hauptfenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.show()

app = QApplication([])
win = Hauptfenster()
app.exec()