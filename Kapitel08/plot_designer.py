from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel08/gui.ui",self)

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0,self.canvas) #über insertWidget kann die Pos in der VBox bestimmt werden

        self.button1.clicked.connect(self.plot1)
        self.button2.clicked.connect(self.plot2)

        self.show()

    def plot1(self):
            plt.clf()
            x = np.linspace(-5, 5, 8)
            y = x**2
            plt.plot(x,y,"bo-")
            plt.axis("equal")
            self.canvas.draw()

    def plot2(self):
        plt.clf()
        x = np.linspace(-2*np.pi,2*np.pi,20)
        y = np.sin(x)
        plt.plot(x,y,"ko-")
        plt.axis("equal")
        self.canvas.draw()


app = QApplication([])
window = Window()
app.exec()