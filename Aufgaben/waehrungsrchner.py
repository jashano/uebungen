from PyQt5.QtWidgets import *

class Währungsumrechner(QMainWindow):
    def __init__(self):
        super().__init__()

        # GUI-Elemente erstellen
        self.chf_label = QLabel('Schweizer Franken:')
        self.chf_edit = QLineEdit()
        self.euro_label = QLabel('Euro:')
        self.euro_edit = QLineEdit()
        self.euro_edit.setReadOnly(True)  # Euro-Feld schreibgeschützt machen
        self.umrechnen_button = QPushButton('Umrechnen')
        self.umrechnen_button.clicked.connect(self.umrechnen)

        # Layout erstellen und Elemente hinzufügen
        layout = QVBoxLayout()
        layout.addWidget(self.chf_label)
        layout.addWidget(self.chf_edit)
        layout.addWidget(self.euro_label)
        layout.addWidget(self.euro_edit)
        layout.addWidget(self.umrechnen_button)

        # Fenstereinstellungen
        self.setLayout(layout)
        self.setWindowTitle('Währungsumrechner')
        self.show()

    def umrechnen(self):
        # Wechselkurs abrufen und Umrechnung durchführen
        chf = float(self.chf.text())
        wechselkurs = 0.8760 #Was ein Umrechnungskurs, Halleluja
        euro = round(chf * wechselkurs, 2)

        # Ergebnis im Euro-Feld anzeigen
        self.euro_edit.setText(str(euro))


if __name__ == '__main__':
    app = QApplication([])
    w = Währungsumrechner()
    app.exec_()