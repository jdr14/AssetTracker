import sys
from copy import deepcopy
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QDialogButtonBox
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtWidgets import QScrollArea, QSizePolicy, QGroupBox
from PyQt5.QtGui import QIcon, QPalette, QFont
from PyQt5.QtCore import Qt
from gui import *

# class Record:
# 	def __init__(id, name, price, quantity):

def main():
    app = QApplication(sys.argv)
    window = Window(
        window_xywh=(400, 200, 600, 500), 
        window_title="Lego price tracker",
        window_icon="images/mr_gold.png",
    )
    
    font = QFont()
    font.setBold(True)

    _label_height = 15
    # ID
    textEntryID = QLineEdit()
    textEntryID.setFixedWidth(30)
    recordLabel = QLabel("ID")
    recordLabel.setFixedHeight(_label_height)
    recordLabel.setAlignment(Qt.AlignCenter)
    recordLabel.setFont(font)

    # Set Number
    textEntrySetNum = QLineEdit()
    setNumLabel = QLabel("Set Number")
    setNumLabel.setFixedHeight(_label_height)
    setNumLabel.setAlignment(Qt.AlignCenter)
    setNumLabel.setFont(font)

    # Set Name
    textEntryName = QLineEdit()
    nameLabel = QLabel("Set Name")
    nameLabel.setFixedHeight(_label_height)
    nameLabel.setAlignment(Qt.AlignCenter)
    nameLabel.setFont(font)

    # Price
    textEntryPrice = QLineEdit()
    priceLabel = QLabel("Set Price")
    priceLabel.setFixedHeight(_label_height)
    priceLabel.setAlignment(Qt.AlignCenter)
    priceLabel.setFont(font)

    # Quantity
    textEntryQuantity = QLineEdit()
    quantityLabel = QLabel("Set Quantity")
    quantityLabel.setFixedHeight(_label_height)
    quantityLabel.setAlignment(Qt.AlignCenter)
    quantityLabel.setFont(font)

    heading = QGridLayout()
    heading.addWidget(recordLabel,       0, 0)
    heading.addWidget(textEntryID,       1, 0)
    heading.addWidget(setNumLabel,       0, 1)
    heading.addWidget(textEntrySetNum,   1, 1)
    heading.addWidget(nameLabel,         0, 2)
    heading.addWidget(textEntryName,     1, 2)
    heading.addWidget(priceLabel,        0, 3)
    heading.addWidget(textEntryPrice,    1, 3)
    heading.addWidget(quantityLabel,     0, 4)
    heading.addWidget(textEntryQuantity, 1, 4)
    headingGroupBox = QGroupBox()
    headingGroupBox.setLayout(heading)

    # Create a scroll view to display the records added in 
    scrollview = QScrollArea()
    scrollview.setStyleSheet("background: tan")

    # Define a slot to connect to once button is clicked
    def addRecord():
    	print("{}".format((
    		textEntrySetNum.text(), 
    		textEntryName.text(), 
    		textEntryPrice.text(), 
    		textEntryQuantity.text()
    	)))
        # scrollview.add
    
    def deleteRecord():
        print("Delete record")


    # Create an add button
    addButton = QPushButton()
    addButton.setGeometry(
    	    window.width()  - (window.width() / 10), 
            (window.height() / 10), 
            40, 
            40
    )
    # Add some styling for the button
    addButton.setText("Add Record")
    addButton.setIcon(QIcon("images/google_icons/outline_add_black_24dp.png"))
    addButton.clicked.connect(addRecord)
    addButton.setStyleSheet("border: 2px solid black; background-color: #64ed32")
    
    deleteButton = QPushButton()
    deleteButton.setGeometry(
            window.width()  - (window.width() / 10), 
            (window.height() / 10), 
            40, 
            40
    )
    deleteButton.setText("Delete Record")
    deleteButton.setIcon(QIcon("images/google_icons/outline_remove_black_24dp.png"))
    deleteButton.clicked.connect(deleteRecord)
    deleteButton.setStyleSheet("border: 2px solid black; background-color: #f23a3a")

    # Create a grid which will be the parent layout for all widgets
    grid = QGridLayout()
    grid.setSpacing(20)
    grid.addWidget(headingGroupBox,   0, 0, 2, 6)
    grid.addWidget(addButton, 0, 6)         # add button
    grid.addWidget(deleteButton, 1, 6)      # delete button
    grid.addWidget(scrollview, 3, 0, 10, 7) # scrollview

    window.setLayout(grid)

    sys.exit(app.exec_())


if __name__ == '__main__':
	main()