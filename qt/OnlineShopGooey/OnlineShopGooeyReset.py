import sys
import random

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

def debug():
	print("reached here!")

class OnlineShopGooeyReset(QWidget): # for future gooey consider regenerating every part of the gui instead of storing it all in ram
	def __init__(self):
		super().__init__()

		self.names = []
		self.costs = []
		self.stock = []
		self.cart = []
		self.taxprovters = [0, 5, 12, 13, 15, 15, 5, 15, 5, 13, 15, 14.975, 11, 5]
		self.provters = ["(Select province/territory)", "Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland", "Northwest Territories", "Nova Scotia", "Nunavut Territory", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon Territory"]
		self.revenue = 0.0

		self.vertSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.mainMenu = QWidget()
		self.mainMenuButtons = [QPushButton("Manager"), QPushButton("Customer"), QPushButton("Exit")]
		self.mainMenuLabel = QLabel()
		self.mainMenuLabel.setPixmap(QPixmap("/media/Computing/python/qt/OnlineShopGooey/os.png")) # TODO: rename to relative because vscode isn't relative
		self.mainMenuLabel.setAlignment(Qt.AlignCenter)
		self.welcomeLabel = QLabel()
		self.welcomeLabel.setAlignment(Qt.AlignCenter)

		self.mainMenuLayout = QVBoxLayout()
		self.mainMenuLayout.addWidget(self.welcomeLabel)
		self.mainMenuLayout.addItem(self.vertSpacer)
		for i in self.mainMenuButtons:
			self.mainMenuLayout.addWidget(i)
			i.clicked.connect(self.rngTitle)
		
		self.mainMenuButtons[2].clicked.connect(exit) # really each panel should have its own class if possible as qwidgets, all enclosed in a qmainwindow
		
		self.mainMenuButtons[0].clicked.connect(self.manTrans)
		self.mainMenuLayout.addItem(self.vertSpacer)
		self.mainMenuLayout.addWidget(self.mainMenuLabel)
		self.mainMenu.setLayout(self.mainMenuLayout)

		self.manMenu = QWidget()
		self.manCategories = [QLabel("Name"), QLabel("Price"), QLabel("Stock")]
		self.manRevenue = QLabel("Revenue = $0.00")
		self.manNames = [QLineEdit() for i in range(10)]
		self.manPrices = [QLineEdit() for i in range(10)]
		self.manStocks = [QLineEdit() for i in range(10)]
		self.manButton = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		self.manButton.button(QDialogButtonBox.Ok).clicked.connect(self.manOk)
		self.manButton.button(QDialogButtonBox.Cancel).clicked.connect(self.manCancel)
		self.manLayout = QGridLayout()

		self.manLayout.addWidget(self.manRevenue, 0, 0)
		for i in range(3):
			self.manLayout.addWidget(self.manCategories[i], 1, i)
			self.manCategories[i].setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
		whyPythonAccumulator = 0
		for i in [self.manNames, self.manPrices, self.manStocks]:
			for j in range(10):
				self.manLayout.addWidget(i[j], j+2, whyPythonAccumulator)
			whyPythonAccumulator += 1
		self.manLayout.addWidget(self.manButton, 12, 2)
		self.manMenu.setLayout(self.manLayout)

		self.darkModeToggle = QToolButton()
		self.darkModeToggle.clicked.connect(self.toggleDarkMode)
		self.status = QStatusBar()
		self.status.addWidget(self.darkModeToggle)

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

		self.rngTitle()
		self.baseLayout = QVBoxLayout()
		self.setLayout(self.baseLayout)
		self.baseLayout.addWidget(self.mainMenu)
		self.baseLayout.addWidget(self.manMenu)
		self.baseLayout.addWidget(self.status)
		self.manMenu.setVisible(False)

	def toggleDarkMode(self):
		if self.isDark:
			app.setPalette(self.lightPalette)
		else:
			app.setPalette(self.darkPalette)

		self.isDark = not self.isDark
	
	def rngName(self): # return random store name
		names = ["Osrus", "OS R'US", "A store", "Canada Operating Systems", "eBay", "Piracy Enterprises", "GNU", "Arduino", "Raspberry", "Pi", "Xunil", "Microsoft", "Amazon"]
		return random.choice(names)
	
	def rngTitle(self): # set title and welcomeLabel
		self.welcomeLabel.setText("Welcome to " + self.rngName() + "!")
		self.setWindowTitle(self.rngName())

	def manTrans(self): # transition from main to manager
		self.mainMenu.setVisible(False)
		self.manMenu.setVisible(True)
		self.manRevenue.setText("Revenue = $%.2f" % self.revenue)
		# TODO: fill with elements in backend

	def manOk(self):
		# TODO: save to database
		check = False
		for box in self.manNames:
			try:
				temp = float(box.text())
				# TODO: parse and save everything else from categories
				f = open("man.conf", "w")
				for i in range(10):
					pass
				f.close()
			except ValueError:
				pass
				# tell user that things broke
		if check:
			self.manCancel()

	def manCancel(self):
		self.manMenu.setVisible(False)
		self.mainMenu.setVisible(True)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	win = OnlineShopGooeyReset()
	win.show()

	sys.exit(app.exec_())