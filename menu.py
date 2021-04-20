"""
Time:2021/4/20 15:14
Author:中庸猿
奋斗不止，赚钱不停    
"""


# 如果想要在窗口上添加菜单，那么窗口类型必须是QMainWindow火QMainWindow的子类
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu


# 第一步，让窗口类继承QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('图书管理系统首页')
        self.show()

    def create_ui(self):
        # 第二部，添加各种菜单
        # 1.获取菜单栏
        menubar = self.menuBar()

        # 2.在菜单栏上添加菜单
        file_menu = menubar.addMenu('File')
        # menubar.setNativeMenuBar(False)  Mac电脑加
        edit_menu = menubar.addMenu('Edit')

        # 3.在菜单上添加选项
        fa1 = QAction('New Project', self)
        # 给选项绑定事件
        fa1.triggered.connect(self.new_project)

        fa2 = QAction(QIcon('files/logo.jpg'), 'open', self)
        fa2.triggered.connect(self.open_action)
        # 给选项添加快快捷键
        fa2.setShortcut('ctrl+o')

        # 添加子菜单
        file_p_menu = QMenu('子菜单1', self)
        file_menu.addMenu(file_p_menu)

        fp3 = QAction('子菜单里面的内容1', self)
        fp4 = QAction('子菜单里面的内容2', self)
        file_p_menu.addActions([fp3,fp4])


        # 将选项添加到菜单上
        file_menu.addActions([fa1, fa2])


    def new_project(self):
        print('创建新的file')

    def open_action(self):
        print('打开新的工程')


    # 在窗口上点击鼠标右键的时候会被自动调用
    def contextMenuEvent(self, event) -> None:
        # 创建菜单对象
        right_menu = QMenu(self)

        # 在右键菜单上添加选项或者子菜单
        a1 = QAction('copy', self)
        a2 = QAction('cut', self)
        a3 = QAction('pash', self)
        right_menu.addActions([a1, a2, a3])

        # 让菜单下显示在当前窗口鼠标所在位置
        right_menu.exec_(self.mapToGlobal(event.pos()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())














