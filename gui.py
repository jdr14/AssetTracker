import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

# with open("data.txt", 'w+') as f:
#     for item in dir(QMainWindow):
#         f.write("\n{}".format(item))

class Window(QMainWindow):
    def __init__(self, window_xywh=None, window_title="", window_icon=None):
        super().__init__()
        
        # Set window size/coordinates
        if window_xywh:
            self.setGeometry(*window_xywh)
        else: # default setup
            self.setGeometry(400, 200, 900, 600) # x, y, w, h
        
        # Set window icon
        if window_icon and os.path.exists(window_icon):
            self.setWindowIcon(QIcon(window_icon))
            self.setIconSize(QSize(25, 25))
        
        # Set window title
        self.setWindowTitle(window_title)
        self.show()


# class Button(QWidget):
#     def __init__()