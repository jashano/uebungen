from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)

        self.x = QLineEdit("[1,2,3,4,5]")
        self.y = QLineEdit("[1,4,9,16,24]")

        button = QPushButton("Plot")

        layout.addWidget(self.canvas)
        layout.addWidget(self.x)
        layout.addWidget(self.y)
        layout.addWidget(button)

        centre = QWidget()
        centre.setLayout(layout)

        self.setCentralWidget(centre)
        self.show()

        button.clicked.connect(self.plot)
    
    def plot(self):
        xx = self.x.text()
        yy = self.y.text()
        try:
            x_eval = eval(xx)
            y_eval = eval(yy)
        except:
            QMessageBox.critical(self, "Fehler", "Gib Zahle für x und y, Man ey!", QMessageBox.Ok)
            return
        try:
            plt.plot(x_eval, y_eval, "ko-")
            plt.axis("equal")
            self.canvas.draw()
        except:
            QMessageBox.critical(self, "Fehler", "Was bisch du för ne tschaupi!", QMessageBox.Ok)

app = QApplication([])
window = Window()
app.exec()