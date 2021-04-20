"""
Time:2021/4/19 16:26
Author:中庸猿
奋斗不止，赚钱不停    
"""

import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout


class TopView(QWidget):
    def __init__(self):
        super(TopView, self).__init__()
        self.create_ui()
        self.setGeometry(0, 0, 800, 150)
        self.show()


    def create_ui(self):
        # 1.设置背景颜色
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QColor(200, 0, 0))
        self.setPalette(pal)
        self.autoFillBackground()


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()
        self.setGeometry(200, 200, 800, 600)
        self.show()

    def create_ui(self):
        box = QVBoxLayout(self)
        box1 = QHBoxLayout(self)

        # 1.顶部
        top_view = TopView()
        top_view.setStyleSheet('')
        box.addWidget(top_view)

        # 2.底部
        bottom_view = QHBoxLayout()
        # 在一个布局结构中添加新的布局结构
        box.addLayout(bottom_view)

        left_view = 2










if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())