"""
Time:2021/4/20 10:42
Author:中庸猿
奋斗不止，赚钱不停    
"""
import sys


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QSpinBox


# 事件绑定三要素：xxx 发生什么就做xxx
# 事件源 发生事件 就执行某个操作
# 绑定程序： 事件源.事件.connect(操作对应的函数)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('图书管理系统首页')
        self.show()

    def create_ui(self):
        btn1 = QPushButton('确定', self)
        btn1.move(50, 10)
        # 按钮点击事件
        btn1.clicked.connect(self.btnation)

        input1 = QLineEdit(self)
        self.input1.setPlaceholderText('请输入手机号')
        self.input1.move(50, 70)
        # 输入框改变事件
        self.input1.textChanged.connect(self.input_text_action)


        num_input = QSpinBox(self)



    def btnation(self):
        print('按钮被点击')

    def input_text_action(self, value):
        print('输入框内容改变', value)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())






