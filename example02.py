"""
Time:2021/4/19 10:21
Author:中庸猿
奋斗不止，赚钱不停    
"""
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

