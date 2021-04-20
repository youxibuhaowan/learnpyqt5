"""
Time:2021/4/19 10:21
Author:中庸猿
奋斗不止，赚钱不停    
"""
from datetime import date
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QCheckBox, QCommandLinkButton, QDialogButtonBox, \
    QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QComboBox, QFontComboBox, QDateEdit, QColorDialog, \
    QDial, QSlider
from PyQt5.QtWidgets import QLabel, QPushButton
import sys


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('基于tushare的股票操作')
        self.show()

    def create_ui(self):
        # 1.文字标签
        # QLabel(显示的文字, 父标签/放到哪个窗口上)
        label1 = QLabel('用户名:', self)
        # 一般不常用的移动坐标
        label1.move(50, 10)

        # 2.按钮
        btn1 = QPushButton('登录', self)
        btn1.move(50, 50)
        # css语法：选择器{属性1：属性值1; 属性2：属性值2;..}
        # color - 字体颜色，对应的值：颜色单词， rbg(255, 0, 0)
        #
        btn1.setStyleSheet('QPushButton{}')
        btn2 = QRadioButton('男', self)
        btn2.move(50, 100)
        btn3 = QCheckBox('篮球', self)
        btn3.move(50, 150)
        btn4 = QCommandLinkButton('hello', 'hellowword', self)
        btn4.move(50, 200)

        b1 = QDialogButtonBox.StandardButton.Ok
        b2 = QDialogButtonBox.StandardButton.Cancel
        btn5 = QDialogButtonBox(b2, self)
        btn5.move(50, 300)

        # 3.输入框
        input1 = QLineEdit(self)
        input1.move(150, 10)
        input2 = QLineEdit('admin', self)
        input2.move(150, 50)
        input1.setText('张三')
        # 富文本
        input3 = QTextEdit('张三', self)
        input3.move(50, 300)
        # 设置成只读
        input3.setReadOnly(True)
        # 只能显示纯文本
        input4 = QPlainTextEdit(self)
        input4.move(300, 10)
        # 输入数值
        input5 = QSpinBox(self)
        input5.move(100, 100)
        input5.setMinimum(10)
        input5.setMaximum(20)
        input5.setValue(15)
        print(input5.value())  # 获取当前值
        # 输入小数
        input6 = QDoubleSpinBox(self)
        input6.move(100, 150)
        # 下拉菜单
        input7 = QComboBox(self)
        input7.addItems(['item1', 'item2'])
        input7.move(150, 200)
        print(input7.currentText())  # 获取当前选中的选项，适用input8
        input8 = QFontComboBox(self)
        input8.move(350, 300)
        input8.setCurrentIndex(2)
        print(input8.currentText())
        label1.setFont(input8.currentFont())
        # 日期选择
        input9 = QDateEdit(date.today(), self)
        input9.move(300, 400)
        # 选择颜色
        input10 = QColorDialog(self)
        input10.move(400, 400)
        # input10.show()

        input11 = QDial(self)
        input11.move(300, 200)

        input12 = QSlider(self)
        input12.move(430, 350)
        input12.setMaximum(100)
        input12.setMinimum(-100)
        input12.setValue(20)
        input12.setOrientation(Qt.Horizontal) # 设置为水平方向


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

