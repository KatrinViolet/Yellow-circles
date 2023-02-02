import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import random


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.on_click)

        self.showCircle = False
        self.diameter = 0

    def on_click(self):
        self.diameter = random.randrange(25, 250, 5)
        self.showCircle = True
        self.update()
        pass

    def paintEvent(self, event):
        if self.showCircle is False:
            return

        painter = QPainter()

        painter.begin(self)
        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        painter.drawEllipse(250 - self.diameter//2, 250 - self.diameter//2, self.diameter, self.diameter)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle_form = Circle()
    circle_form.show()
    sys.exit(app.exec())
