
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QDialogButtonBox
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtWidgets import QScrollArea, QSizePolicy
from PyQt5.QtGui import QIcon
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

    _label_height = 15
    # ID
    textEntryID = QLineEdit()
    setNumLabel = QLabel("Set Number")
    setNumLabel.setFixedHeight(_label_height)
    setNumLabel.setAlignment(Qt.AlignCenter)

    # Set Name
    textEntryName = QLineEdit()
    nameLabel = QLabel("Set Name")
    nameLabel.setFixedHeight(_label_height)
    nameLabel.setAlignment(Qt.AlignCenter)

    # Price
    textEntryPrice = QLineEdit()
    priceLabel = QLabel("Price")
    priceLabel.setFixedHeight(_label_height)
    priceLabel.setAlignment(Qt.AlignCenter)

    # Quantity
    textEntryQuantity = QLineEdit()
    quantityLabel = QLabel("Quantity")
    quantityLabel.setFixedHeight(_label_height)
    quantityLabel.setAlignment(Qt.AlignCenter)
    
    # Create a scroll view to display the records added in 
    scrollview = QScrollArea()

    recordLabel = QLabel("ID")
    recordLabel.setFixedHeight(_label_height)
    recordLabel.setAlignment(Qt.AlignCenter)

    def getData():
    	print("{}".format((
    		textEntryID.text(), 
    		textEntryName.text(), 
    		textEntryPrice.text(), 
    		textEntryQuantity.text()
    	)))
        # scrollview.add

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
    grid.setSpacing(20)
    grid.addWidget(setNumLabel,       0, 0)
    grid.addWidget(textEntryID,       1, 0)
    grid.addWidget(nameLabel,         0, 1)
    grid.addWidget(textEntryName,     1, 1)
    grid.addWidget(priceLabel,        0, 2)
    grid.addWidget(textEntryPrice,    1, 2)
    grid.addWidget(quantityLabel,     0, 3)
    grid.addWidget(textEntryQuantity, 1, 3)
    grid.addWidget(addButton, 1, 4)

    grid.addWidget(scrollview, 3, 0, 10, 5)

    # hboxlayoutEntries = QHBoxLayout()

    # hboxlayoutEntries.addLayout(column1)
    # hboxlayoutEntries.addLayout(column2)
    # hboxlayoutEntries.addLayout(column3)
    # hboxlayoutEntries.addLayout(column4)

    window.setLayout(grid)

    sys.exit(app.exec_())


if __name__ == '__main__':
	main()