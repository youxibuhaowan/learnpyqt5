"""
Time:2021/4/19 14:29
Author:中庸猿
奋斗不止，赚钱不停    
"""
import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('布局1')
        self.show()


    def create_ui(self):
        # 0.设置背景颜色
        bg_pa = QPalette()
        bg_pa.setColor(self.backgroundRole(), QColor(200, 200, 200))
        self.setPalette(bg_pa)
        self.setAutoFillBackground(True)

        # 1.绝对定位 - 通过move方法直接设置标签的坐标
        # 缺点，当你的窗口发生变化，他永远在固定的位置
        # username = QLabel('用户名', self)
        # username.move(100, 10)

        # 2.Layout盒子
        # QVBoxLayout
        # 1）创建布局对象并且和窗口进行关联
        box = QVBoxLayout(self)
        # 设置间距
        box.setContentsMargins(0, 0, 0, 0)

        # box1 = QVBoxLayout(self)
        # box = QVBoxLayout()
        # self.setLayout(box)

        label1 = QLabel('用户名:', self)
        label2 = QLabel('密码:', self)
        # 2）将需要垂直布局的空间添加到布局盒子中
        box.addWidget(label1)
        box.addWidget(label2)
        box.addStretch(1)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

















