#!/usr/bin/env python3

import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

def debug():
	print("Reached here!")

class Box(QWidget):
	def __init(self):
		super().__init__()

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.mainWin = Box()
		self.setCentralWidget(self.mainWin)

# this is way beyond your level
# this needs screen scraping

if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	win = MainWindow()
	win.show()

	sys.exit(app.exec_())
