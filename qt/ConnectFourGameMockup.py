import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.main = QVBoxLayout()

		self.statusWidget = QWidget()
		self.status = QHBoxLayout()
		self.statusWidget.setLayout(self.status)
		self.topButtons = [QPushButton("Save and quit"), QPushButton("New game"), QPushButton("Undo action")]
		self.topLabels = [QLabel("Vincent's turn!"), QLabel("00:10 remaining")]
		self.topLabels[1].setAlignment(Qt.AlignRight)
		self.topLabels[0].setAlignment(Qt.AlignCenter)
		for i in self.topButtons:
			self.status.addWidget(i)
		for i in self.topLabels:
			self.status.addStretch()
			self.status.addWidget(i)
		# screw it i'm not doing extra work
		
		
		self.main.addWidget(self.statusWidget)
		self.setLayout(self.main)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Fusion")

	win = MainWindow()
	win.show()
	sys.exit(app.exec_())