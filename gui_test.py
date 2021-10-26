
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import *


def main():
    app = QApplication(sys.argv)
    window = Window(
        window_xywh=(400, 200, 900, 600), 
        window_title="Lego price tracker",
        window_icon="images/mr_gold.png",
    )

    inputBox = InputBox(
    	input_xywh=(
    		window.width()  - (window.width() / 10) - 60, 
            (window.height() / 10), 
            200, 
            40
        ),
        parent=window
    )

    button = PushButton(
    	button_xywh=(
    		window.width()  - (window.width() / 10), 
            (window.height() / 10), 
            40, 
            40
        ),
    	button_text="",
    	button_icon="images/google_icons/outline_add_circle_outline_black_24dp.png",
    	slot_list=[inputBox.getInput],
    	parent=window
    )

    sys.exit(app.exec_())


if __name__ == '__main__':
	main()