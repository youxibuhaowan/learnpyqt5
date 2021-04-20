"""
Time:2021/4/20 11:27
Author:中庸猿
奋斗不止，赚钱不停    
"""
import sys

from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_ui()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('图书管理系统首页')
        self.show()

    def create_ui(self):
        # 1.设置窗口图标
        icon = QIcon('files/download.jpg')
        self.setWindowIcon(icon)
        # 2.显示图片
        image_label = QLabel(self)
        pix = QPixmap('files/logo.jpg')
        image_label.setPixmap(pix)

        # 2. 显示图片
        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 800, 450)
        self.bgpix = QPixmap('files/logo.jpg')
        self.bg_label.setPixmap(self.bgpix)


    # 在窗口的大小发送改变的时候会被自动调用
    def resizeEvent(self, a0) -> None:
        # 获取到最新的窗口大小
        w_size = self.size()

        # 对原图进行缩放
        image = QImage('files/logo.jpg')
        new_image = image.scaled(w_size.width(), w_size.height())
        pix = QPixmap.fromImage(new_image)

        # 将显示图片的label进行缩放
        self.bg_label.setGeometry(0, 0, w_size.width(), w_size.height())
        self.bg_label.setPixmap(pix)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
