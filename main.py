import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
import math
class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle_form = Circle()
    circle_form.show()
    sys.exit(app.exec())