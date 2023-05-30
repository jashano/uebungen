from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel08/uebung8.ui",self)
        
        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0,self.canvas) #über insertWidget kann die Pos in der VBox bestimmt werden

        self.button1.clicked.connect(self.plot)

        self.comboBox.addItems(["Rot","Blau","Grün"])
        
        self.show()

    def plot(self):
        plt.clf()

        colourCurve = self.comboBox.currentText()
        if colourCurve == "Rot":
            color = "r"
        elif colourCurve == "Blau":
            color = "b"
        elif colourCurve == "Grün":
            color = "g"

        AnzahlPunkte = self.spinBox.value()
        Minimum = self.doubleSpinBox.value()
        Maximum = self.doubleSpinBox_2.value()

        xx = self.lineEdit.text()
        try:
            x = eval(xx)
        except:
            QMessageBox.critical(self, "Fehler", "Überprüef dini ihgab, Tschutsch!", QMessageBox.Ok)
            return
    
        f = np.poly1d(x)
        x = np.linspace(Minimum,Maximum,AnzahlPunkte)
        y = f(x)
        plt.plot(x,y,color+"o-")

        plt.axis("equal")
        self.canvas.draw()
        
            
    

app = QApplication([])
window = Window()
app.exec()