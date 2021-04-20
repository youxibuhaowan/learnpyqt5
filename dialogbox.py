"""
Time:2021/4/20 16:04
Author:中庸猿
奋斗不止，赚钱不停    
"""
# 第一步，让窗口类继承QMainWindow
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('图书管理系统首页')
        self.show()

    def create_ui(self):
        message_btn = QPushButton('确定', self)
        message_btn.move(50, 30)
        message_btn.clicked.connect(self.show_message_box)

    def show_message_box(self):
        print('显示消息框！')
        # QMessageBox.消息类型()
        # 消息框（information、question、warning、critical、about）
        result = QMessageBox.information(self, '无情的催债机器', '该交钱了', QMessageBox.Ok)
        print(result)

        result = QMessageBox.question(self, '问题', '是否删除该数据', QMessageBox.Cancel, QMessageBox.Close)
        print(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())