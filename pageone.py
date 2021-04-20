"""
Time:2021/4/20 9:44
Author:中庸猿
奋斗不止，赚钱不停    
"""

from datetime import date
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QCheckBox, QCommandLinkButton, QDialogButtonBox, \
    QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QComboBox, QFontComboBox, QDateEdit, QColorDialog, \
    QDial, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QPushButton
import sys

# QPushButton{color: #008000;background-color: #FFFF00;font-size: 20px;border: 1px solid #FF0000; border-radius: 8px;width: 100px; height: 40px;}
# color - 文字颜色
# background-color - 背景颜色
# font-size - 字体大小
# border - 边框，宽度、样式、颜色
# border-radius - 边框圆角大小
# width - 宽度
# height - 高度

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('图书管理系统首页')
        self.show()

    def create_ui(self):
        # 设置窗口背景颜色
        self.setStyleSheet('QWidgt{background-color: rgb(205, 193, 168);}')

        # pa = QPalette()
        # pa.setColor()


        box = QHBoxLayout(self)

        box1 = QVBoxLayout()

        box.addStretch(1)
        box.addLayout(box1)
        box.addStretch(1)

        # 标题
        box4 = QHBoxLayout()
        title_label = QLabel('千峰图书管理系统', self)
        title_label.setStyleSheet('QLabel{color: rgb(91, 64, 37);font-size: 30px; font-weight:900;}')

        box4.addStretch(1)
        box4.addWidget(title_label)
        box4.addStretch(1)
        # 输入账号密码
        box2 = QGridLayout()
        username = QLabel('用户名:')
        username.setStyleSheet('QLabel{color: rgb(95, 60, 55);font-size: 20px; font-weight:500;}')
        username_input = QLineEdit(self)
        username_input.setStyleSheet('QLineEdit{width:100px; height:30px;color: rgb(255, 60, 55);border-radius: 8px;}')

        pw = QLabel('密  码:')
        pw.setStyleSheet('QLabel{color: rgb(95, 60, 55);font-size: 20px; font-weight:500;}')
        pw_input = QLineEdit(self)
        pw_input.setStyleSheet('QLineEdit{width:100px; height:30px;color: rgb(255, 60, 55);border-radius: 8px;}')

        # 登录和退出按钮
        box3 = QHBoxLayout()
        btn1 = QPushButton('登录', self)
        btn1.setStyleSheet('QPushButton{width:100px; height:30px;color: rgb(255, 250, 255);border-radius: 6px;background-color: rgb(91, 64, 37)}')
        btn2 = QPushButton('退出', self)
        btn2.setStyleSheet('QPushButton{width:100px; height:30px;color: rgb(255, 250, 255);border-radius: 6px;background-color: rgb(91, 64, 37)}')
        box3.addWidget(btn1)
        box3.addStretch(1)
        box3.addWidget(btn2)

        box2.addWidget(username, 1, 1)
        box2.addWidget(username_input, 1, 2)
        box2.addWidget(pw, 2, 1)
        box2.addWidget(pw_input, 2, 2)




        box1.addStretch(3)
        box1.addLayout(box4)
        box1.addStretch(3)
        box1.addLayout(box2)
        box1.addStretch(3)
        box1.addLayout(box3)
        box1.addStretch(20)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
