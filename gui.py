import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QRect
from exceptions import *

# with open('data.txt', 'w+') as f:
#     for item in dir(QMainWindow):
#         f.write("\n{}".format(item))

def _checkCoordinateTuple(tp, desired_length=4):
    return (tp and type(tp) == tuple and len(tp) == desired_length)

class Window(QMainWindow):
    def __init__(self, window_xywh=None, window_title="", window_icon=None):
        super(Window, self).__init__()
        
        # Set window size/coordinates
        if _checkCoordinateTuple(window_xywh):
            self.setGeometry(QRect(*window_xywh))
        else: # default setup
            self.setGeometry(QRect(400, 200, 900, 600))# x, y, w, h
        
        # Set window icon
        if window_icon and os.path.exists(window_icon):
            self.setWindowIcon(QIcon(window_icon))
            self.setIconSize(QSize(25, 25))
        
        # Set window title
        self.setWindowTitle(window_title)
        self.show()


class PushButton(QPushButton):
    def __init__(self, button_xywh=None, button_text=None, button_icon=None, slot_list=[], parent=None):
        super(PushButton, self).__init__(parent=parent)
        self.button_icon = button_icon
        self.button_text = button_text
        self.button_xywh = button_xywh
        self.slot_list = slot_list
        self.parent = parent
        self.setup()
        self.show()

    def setup(self) -> None:
        self.setIcon(QIcon(self.button_icon))
        if self.button_text and type(self.button_text) == str:
            self.setText(self.button_text)
        if _checkCoordinateTuple(self.button_xywh):
            self.setGeometry(QRect(*self.button_xywh))
        self.setShortcut('+')
        for slot in self.slot_list:
            self.clicked.connect(slot)
        self.setToolTip("Add a record")


class InputBox(QInputDialog):
    def __init__(self, input_xywh=None, parent=None):
        super(InputBox, self).__init__(parent=parent)
        self.input_xywh = input_xywh
        self.parent = parent
        self.setup()
        self.show()

    def setup(self) -> None:
        if _checkCoordinateTuple(self.input_xywh):
            self.setGeometry(QRect(*self.input_xywh))

    def getInput(self) -> None:
        set_num, success = self.getText(self, 'input dialog', 'enter set number')
        if success:
            print("Set Num entered = {}".format(set_num))

