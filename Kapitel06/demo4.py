from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel06/demo2.ui", self)
        self.show()

        self.button.clicked.connect(self.buttonclick)

    def buttonclick(self):
        txt = self.lineEdit.text()
        print("hello22!!!", txt)


app = QApplication([])
win = UIFenster()
app.exec()