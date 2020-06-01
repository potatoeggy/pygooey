import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Calc(QWidget):
	def __init__(self):
		super().__init__()
		self.main = QVBoxLayout()

		self.displayBox = QWidget()
		self.displayLayout = QHBoxLayout()
		self.display = QLineEdit()
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)
		self.displayLayout.addWidget(self.display)
		self.displayBox.setLayout(self.displayLayout)

		self.inputBox = QWidget()
		self.inputLayout = QGridLayout()
		self.buttons = [QPushButton(str(i)) for i in range(1, 10)]
		self.zeroButton = QPushButton("0")
		self.dotButton = QPushButton(".")
		for i in range(len(self.buttons)):
			self.inputLayout.addWidget(self.buttons[len(self.buttons)-i-1], i / 3, 3 - i % 3)
			self.buttons[i].clicked.connect(self.numButton(i+1))
		self.zeroButton.clicked.connect(self.numButton(0))
		self.dotButton.clicked.connect(self.numButton(".")) # needs to be replaced
		self.inputLayout.addWidget(self.zeroButton, 3, 1)
		self.inputLayout.addWidget(self.dotButton, 3, 2)

		self.inputBox.setLayout(self.inputLayout)
		self.main.addWidget(self.displayBox)
		self.main.addWidget(self.inputBox)

		self.setLayout(self.main)

	def numButton(self, number):
		def miniButton(self):
			print(str(self)) # why is self = False self should be the class? there are no lambdas i give up
			self.display.setText(self.display.text() + str(number))
		return miniButton

if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Fusion")

	win = Calc()
	win.show()
	sys.exit(app.exec_())