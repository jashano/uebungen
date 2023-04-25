import sys
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Währungsumrechner')
        self.setMinimumWidth(540)

        layout = QVBoxLayout()
        layout_top = QFormLayout()
        layout_bottom = QVBoxLayout()

        self.chf_edit = QLineEdit()
        self.euro_edit = QLineEdit()
        self.euro_edit.setReadOnly(True)
        self.umrechnen_button = QPushButton('Umrechnen')
        self.umrechnen_button.clicked.connect(self.umrechnen)

        
        layout_top.addRow("Schweizer Franken:",self.chf_edit)
        layout_top.addRow("Euro:",self.euro_edit)
        layout.addLayout(layout_top)
        layout.addLayout(layout_bottom)
        layout_bottom.addWidget(self.umrechnen_button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

    def umrechnen(self):
        franken = float(self.chf_edit.text())
        wechselkurs = 0.8760 #Was ein Umrechnungskurs, Halleluja
        euro = round(franken * wechselkurs, 2)
        self.euro_edit.setText(str(euro))

def main():
    app = QApplication(sys.argv)
    mainwindow = Fenster()   
    mainwindow.raise_()
    app.exec_()

if __name__ == '__main__':
    main()