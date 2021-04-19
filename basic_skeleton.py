"""
Time:2021/4/19 9:58
Author:中庸猿
奋斗不止，赚钱不停    
"""

from PyQt5.QtWidgets import QApplication, QWidget
import sys

# 1.创建APP对象(应用程序对象)
app = QApplication(sys.argv)

# 2.创建窗口
window = QWidget()

# 3.设置窗口的大小和位置
# window.setGeometry(x, y, w, h)
window.setGeometry(0, 0, 800, 600)

# 设置窗口标题
window.setWindowTitle('基于tushare的股票分析')

# 显示窗口
window.show()

# 3.启动程序
sys.exit(app.exec_())
