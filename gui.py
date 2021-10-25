from os import getcwd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtGui

# with open("data.txt", 'w+') as f:
#     for item in dir(QMainWindow):
#         f.write("\n{}".format(item))

class Window(QMainWindow):
    def __init__(self, window_xywh=None, window_title=""):
        super().__init__()
        
        if window_xywh:
            self.setGeometry(*window_xywh)
        else: # default setup
            self.setGeometry(400, 200, 900, 600) # x, y, w, h

        self.setWindowTitle(window_title)
        self.setWindowIcon(QtGui.QIcon('{}/mr_gold.png'.format(getcwd())))
        self.show()


# class Button(QWidget):
#     def __init__()