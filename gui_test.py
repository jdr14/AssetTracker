
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QDialogButtonBox
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from gui import *

# class Record:
# 	def __init__(id, name, price, quantity):



def main():
    app = QApplication(sys.argv)
    window = Window(
        window_xywh=(400, 200, 900, 600), 
        window_title="Lego price tracker",
        window_icon="images/mr_gold.png",
    )
    
    # inputBox = InputBox(
    # 	input_xywh=(
    # 		window.width()  - (window.width() / 10) - 60, 
    #         (window.height() / 10), 
    #         200, 
    #         40
    #     ),
    #     # parent=window
    # )
    
    # ID
    textEntryID = QLineEdit()
    textEntryID.setWindowTitle("Set ID or number")
    setNumLabel = QLabel("Set Number")
    # column1 = QVBoxLayout()
    # column1.addWidget(setNumLabel)
    # column1.addWidget(textEntryID)

    # Set Name
    textEntryName = QLineEdit()
    textEntryName.setWindowTitle("Set name")
    nameLabel = QLabel("Set Name")
    # column2 = QVBoxLayout()
    # column2.addWidget(nameLabel)
    # column2.addWidget(textEntryName)

    # Price
    textEntryPrice = QLineEdit()
    textEntryPrice.setWindowTitle("Price per 1 item")
    priceLabel = QLabel("Price")
    # column3 = QVBoxLayout()
    # column3.addWidget(priceLabel)
    # column3.addWidget(textEntryPrice)

    # Quantity
    textEntryQuantity = QLineEdit()
    textEntryQuantity.setWindowTitle("Quantity")
    quantityLabel = QLabel("Quantity")
    # column4 = QVBoxLayout()
    # column4.addWidget(quantityLabel)
    # column4.addWidget(textEntryQuantity)

    # addButton = PushButton(
    # 	button_xywh=(
    # 		window.width()  - (window.width() / 10), 
    #         (window.height() / 10), 
    #         40, 
    #         40
    #     ),
    # 	button_text="Add Record",
    # 	button_icon="images/google_icons/outline_add_black_24dp.png",
    # 	slot_list=[],
    # 	# parent=window
    # )
    # subtractButton = PushButton(
    # 	button_xywh=(
    # 		window.width()  - (window.width() / 10), 
    #         (window.height() / 10), 
    #         40, 
    #         40
    #     ),
    # 	button_text="Delete Record",
    # 	button_icon="images/google_icons/outline_remove_black_24dp.png",
    # 	slot_list=[inputBox.recordDelete],
    # 	# parent=window
    # )

    def getData():
    	print("{}".format((
    		textEntryID.text(), 
    		textEntryName.text(), 
    		textEntryPrice.text(), 
    		textEntryQuantity.text()
    	)))

    addButton = QPushButton()
    addButton.setGeometry(
    	    window.width()  - (window.width() / 10), 
            (window.height() / 10), 
            40, 
            40
    )
    addButton.setText("Add Record")
    addButton.setIcon(QIcon("images/google_icons/outline_add_black_24dp.png"))
    addButton.clicked.connect(getData)

    # buttonbox = QDialogButtonBox(QDialogButtonBox.NoButton, inputBox)
    # buttonbox.addButton(addButton, QDialogButtonBox.AcceptRole)
    # buttonbox.addButton(subtractButton, QDialogButtonBox.DestructiveRole)
    # buttonbox.accepted.connect(inputBox.recordAdd)
    # buttonbox.rejected.connect(inputBox.recordDelete
    grid = QGridLayout()
    grid.addWidget(setNumLabel,       0, 0)
    grid.addWidget(textEntryID,       1, 0)
    grid.addWidget(nameLabel,         0, 1)
    grid.addWidget(textEntryName,     1, 1)
    grid.addWidget(priceLabel,        0, 2)
    grid.addWidget(textEntryPrice,    1, 2)
    grid.addWidget(quantityLabel,     0, 3)
    grid.addWidget(textEntryQuantity, 1, 3)
    grid.addWidget(addButton, 1, 4)

    # hboxlayoutEntries = QHBoxLayout()

    # hboxlayoutEntries.addLayout(column1)
    # hboxlayoutEntries.addLayout(column2)
    # hboxlayoutEntries.addLayout(column3)
    # hboxlayoutEntries.addLayout(column4)

    window.setLayout(grid)

    sys.exit(app.exec_())


if __name__ == '__main__':
	main()