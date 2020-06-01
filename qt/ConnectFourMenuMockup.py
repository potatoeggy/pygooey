import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.main = QVBoxLayout()
		self.title = QLabel("Connect 4")
		self.title.setAlignment(Qt.AlignCenter)

		self.boxWidget = QWidget()
		self.box = QGridLayout()
		self.labels = [QLabel("Name:") for i in range(2)]
		self.tfs = [QLineEdit("Player " + str(i)) for i in range(1, 3)]
		self.cpuSelect = [QLabel("Player type:") for i in range(2)]
		self.cpuBox = [QComboBox() for i in range(2)]
		for i in self.cpuBox:
			i.addItem("Human")
			i.addItem("Computer (easy)")
			i.addItem("Computer (medium)")
			i.addItem("Computer (hard)")
			i.addItem("Computer (impossible)")

		for i in range(2):
			self.box.addWidget(self.labels[i], i, 0)
			self.box.addWidget(self.tfs[i], i, 1)
			self.box.addWidget(self.cpuSelect[i], i, 2)
			self.box.addWidget(self.cpuBox[i], i, 3)

		self.moreButtons = [QPushButton("Start game"), QPushButton("Options"), QPushButton("Exit")]

		self.boxWidget.setLayout(self.box)

		self.main.addWidget(self.title)
		self.main.addWidget(self.boxWidget)
		for i in self.moreButtons:
			self.main.addWidget(i)
		self.setLayout(self.main)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Fusion")

	win = MainWindow()
	win.show()
	sys.exit(app.exec_())