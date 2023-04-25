from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel06/demo.ui", self)
        self.show()

        self.helloButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        print("hello22!!!")


app = QApplication([])
win = UIFenster()
app.exec()