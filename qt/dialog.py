# 27 April 2020
# Introduction to Qt

import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog): # class
	def __init__(self, parent=None): # constructor
		super(Form, self).__init__(parent) # call higher constructor
		self.setWindowTitle("Woot!") # setTitle
		self.edit = QLineEdit("What's your name?") # JTextField
		self.button = QPushButton("Say your name!") # JButton
		self.button.clicked.connect(self.helloConsole)

		layout = QVBoxLayout() # BoxLayout
		layout.addWidget(self.edit) # Component.addLayout but backwards
		layout.addWidget(self.button)

		self.setLayout(layout) # setLayout
	
	def helloConsole(self):
		print("Hello, " + self.edit.text()) # apparently the following works too: print("Hello, %s" % self.edit.text())

if __name__ == "__main__": # make sure this isn't being run from something else
	app = QApplication(sys.argv) # i think this is like a backend

	form = Form() # Minesweeper minesweeper = new Minesweeper()
	form.show() # setVisible(true)

	sys.exit(app.exec_()) # kill i think