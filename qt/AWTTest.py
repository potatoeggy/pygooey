import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class AWTTest(QWidget): # class AWTTest extends JFrame
	def __init__(self): # constructor
		super().__init__() # call QWidget constructor
		self.main = QVBoxLayout() # Layouts in Qt are both Frames and Layouts in Swing
		self.child1 = QHBoxLayout() # horizontal box layout
		self.child2 = QHBoxLayout()

		self.label = QLabel("Label1") # JLabel
		self.te = QLineEdit("TextField1") # JTextField
		self.buttons = [QPushButton("Button 1"), QPushButton("Button 2"), QPushButton("Button 3")] # JButton array
		self.darkModeButton = QToolButton() # dark mode button
		self.darkModeButton.clicked.connect(self.toggleDarkMode) # addActionListener

		self.main.addLayout(self.child1) # panels are layouts
		self.main.addLayout(self.child2)

		for i in [self.label, self.te, self.darkModeButton]:
			self.child1.addWidget(i) # add to layout

		for i in self.buttons:
			self.child2.addWidget(i)

		self.setLayout(self.main) # setLayout
		self.isDark = False

		self.darkPalette = QPalette() # stylesheets exist but they crash vscode for whatever reason
		self.darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
		self.darkPalette.setColor(QPalette.WindowText, Qt.white)
		self.darkPalette.setColor(QPalette.Base, QColor(25, 25, 25))
		self.darkPalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
		self.darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
		self.darkPalette.setColor(QPalette.ToolTipText, Qt.white)
		self.darkPalette.setColor(QPalette.Text, Qt.white)
		self.darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
		self.darkPalette.setColor(QPalette.ButtonText, Qt.white)
		self.darkPalette.setColor(QPalette.BrightText, Qt.red)
		self.darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
		self.darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
		self.darkPalette.setColor(QPalette.HighlightedText, Qt.black)

		self.lightPalette = QGuiApplication.palette()

	def toggleDarkMode(self):
		if self.isDark:
			app.setPalette(self.lightPalette)
		else:
			app.setPalette(self.darkPalette)
		self.isDark = not self.isDark


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Fusion")

	win = AWTTest()
	win.show()
	sys.exit(app.exec_())
