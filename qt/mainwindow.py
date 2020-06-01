import sys
import random

from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import Qt, Slot

class MyWidget(QWidget):
	def __init__(self):
		super().__init__() # run higher constructor

		self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"] # array

		self.button = QPushButton("Click me!") # new JButton("Text")
		self.text = QLabel("Hello World") # new JLabel("Text")
		self.text.setAlignment(Qt.AlignCenter) # setAlignment

		self.layout = QVBoxLayout() # new BoxLayout
		self.layout.addWidget(self.text) # you add stuff to layouts, not the other way around it seems
		self.layout.addWidget(self.button)
		self.setLayout(self.layout) # setLayout

		self.button.clicked.connect(self.magic) # addActionListener

	@Slot() # think of it like actionPerformed but not really
	def magic(self):
		self.text.setText(random.choice(self.hello)) # setText

if __name__ == "__main__":
	app = QApplication(sys.argv) # special init thing

	widget = MyWidget() # make a new instance of itself
	widget.resize(800, 600) # ideally i want to avoid this
	widget.show() # setVisible true

	sys.exit(app.exec_()) # exit on destroy