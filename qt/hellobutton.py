# 27 April 2020
# Introduction to Qt

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot

@Slot()
def hello_console():
	print("Hello, console!")

win = QApplication(sys.argv)

button = QPushButton("Hello?")
button.clicked.connect(hello_console)

button.show()
win.exec_()