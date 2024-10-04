import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow




class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.make_flag.clicked.connect(self.run)


    def foo(self):
        print(self.text())

    def run(self):
        color_group_1.buttonClicked.connect(foo)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MyWidget()
    a.show()
    sys.exit(app.exec())
