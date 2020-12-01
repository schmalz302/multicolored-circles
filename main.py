import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QColor,  QPainter
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Разноцветные круги')
        self.pushButton = QPushButton('Круг', self)
        self.pushButton.move(0, 570)
        self.a = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.a = True
        self.repaint()
        self.a = False

    def paintEvent(self, event):
        if self.a:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            a = randint(0, 300)
            qp.drawEllipse(400 - int(0.5 * a), 300 - int(0.5 * a), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())