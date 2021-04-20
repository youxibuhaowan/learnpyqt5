"""
Time:2021/4/19 15:19
Author:中庸猿
奋斗不止，赚钱不停    
"""
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QGridLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()
        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('布局2')
        self.show()


    def create_ui(self):
        label1 = QLabel('用户名')
        label2 = QLabel('密码')

        # 1.创建布局盒子对象
        # # box = QHBoxLayout(self)
        # box = QHBoxLayout(self)
        #
        # # 2.添加标签
        # box.addWidget(label1)
        # box.addWidget(label2)
        # box.addStretch(1)

        # QGridLayout
        box1 = QGridLayout(self)

        # # 添加标签
        # btn1 = QPushButton('1')
        # btn2 = QPushButton('2')
        # btn3 = QPushButton('3')
        # btn4 = QPushButton('4')
        # btn5 = QPushButton('5')
        # btn6 = QPushButton('6')
        #
        # # 网格布局.addWidget(控件，行号，列好，行合并数，列合并数)
        # box1.addWidget(btn1, 1, 1)
        # box1.addWidget(btn2, 1, 2)
        # box1.addWidget(btn3, 1, 3)
        # box1.addWidget(btn4, 2, 1)
        # box1.addWidget(btn5, 2, 2, 1, 2)
        # box1.addWidget(btn6, 3, 1, 2, 1)

        btns = []
        controls1 = ['+', '=', '.', '-', '*', '/', 'Close,', 'Bck', 'cls']
        controls2 = ['0', '3', '2', '1', '6', '5', '4', '9', '8', '7']
        for i in range(20):
            if i == 2:
                btns.append('1')
                continue
            elif i < 4:
                btns.append((QPushButton(controls1.pop())))
                continue
            elif i%4 == 3:
                btns.append((QPushButton(controls1.pop())))
            elif i > 16:
                btns.append(QPushButton(controls1.pop()))
            else:
                btns.append(QPushButton(controls2.pop()))

        # print(btns)
        box1.addWidget(QPushButton('111'), 0, 0, 1, 4)
        for i in range(20):
            if i == 2:
                continue
            box1.addWidget(btns[i], int(i//4+2), int(i%4))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())