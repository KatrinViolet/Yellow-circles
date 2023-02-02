import sys
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        # set windows size
        self.resize(482, 600)
        # create button
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(170, 490, 141, 31))
        self.pushButton.setText("Click me")
        self.pushButton.clicked.connect(self.on_click)

        self.showCircle = False
        self.diameter = 0
        self.color_choice = Qt.white

    def on_click(self):
        self.diameter = random.randrange(25, 250, 5)
        self.color_choice = random.choice([Qt.yellow, Qt.red, Qt.green, Qt.magenta, Qt.blue, Qt.black])
        self.showCircle = True
        self.update()
        pass

    def paintEvent(self, event):
        if self.showCircle is False:
            return

        painter = QPainter()

        painter.begin(self)
        painter.setPen(QPen(self.color_choice, 8, Qt.SolidLine))
        painter.drawEllipse(250 - self.diameter // 2, 250 - self.diameter // 2, self.diameter, self.diameter)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle_form = Circle()
    circle_form.show()
    sys.exit(app.exec())
