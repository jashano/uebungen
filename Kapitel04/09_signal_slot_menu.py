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
        open.triggered.connect(self.menu_open)
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" (für MacOS)

        filemenu.addAction(open)
        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

    def menu_open(self):
        print("Menu Open wurde gewählt...")

    def menu_save(self):
        print("Menu Save wurde gewählt...")

    def menu_quit(self):
        print("Menu Quit wurde gewählt...")
        self.close()  # Hauptfenster schliessen = beenden!

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()


