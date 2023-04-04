import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        # Fenster-Titel definieren:
        self.setWindowTitle("Signal Slot Demo")

        # Layout erstellen:
        layout = QVBoxLayout()

        # Widget-Instanzen erstellen:
        self.button = QPushButton("Button 1")
        self.lineedit = QLineEdit()
        self.checkbox = QCheckBox("Bla")
        self.radio1 = QRadioButton("Radio 1")
        self.radio2 = QRadioButton("Radio 2")
        self.checkbox.setCheckState(Qt.CheckState.Checked)  # oder Unchecked
        self.calendar = QCalendarWidget()
        self.combobox = QComboBox()
        self.combobox.addItems(["Erstes Item", "Zweites Item", "Drittes Item"])

        # Widgets dem Layout hinzufügen:
        layout.addWidget(self.button)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.calendar)
        layout.addWidget(self.combobox)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    def createConnects(self):
        self.button.clicked.connect(self.button_clicked)
        self.lineedit.textChanged.connect(self.lineedit_update)
        self.checkbox.stateChanged.connect(self.checkbox_changed)
        self.radio1.toggled.connect(self.radio1_toggled)
        self.radio2.toggled.connect(self.radio2_toggled)
        self.calendar.clicked.connect(self.calendar_clicked)
        self.combobox.currentIndexChanged.connect(self.combobox_indexchange)


    def button_clicked(self):
        print("Der Button wurde gedrückt")

    def lineedit_update(self, txt):
        print("LineEdit Update:", txt)

    def checkbox_changed(self, state):
        if state == Qt.CheckState.Checked:
            print("checkbox is checked")
        elif state == Qt.CheckState.Unchecked:
            print("checkbox is unchecked")

    def radio1_toggled(self, checked):
        print("Radio1", checked)

    def radio2_toggled(self, checked):
        print("Radio2", checked)

    def calendar_clicked(self, date):
        print(date)

    def combobox_indexchange(self, index):
        print(index)

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()

