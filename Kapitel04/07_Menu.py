import sys
from PyQt5.QtWidgets import *

# Fenster-Klasse: wird von QWindow vererbt
class MyWindow(QMainWindow):
    def __init__(self):      # Konstruktor
        super().__init__()   # Konstruktor Basis-Klasse
        self.setWindowTitle("Hello World")  # Fenster-Titel setzen
        self.show()  # Fenster anzeigen/sichtbar machen

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        editmenu = menubar.addMenu("Edit")
        viewmenu = menubar.addMenu("View")

        open = QAction("Open", self)
        save = QAction("Save", self)
        quit = QAction("Quit", self)

        quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" zuweisen, nur für MacOS relevant

        filemenu.addAction(open)
        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()


