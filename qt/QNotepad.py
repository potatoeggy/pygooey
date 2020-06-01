import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.editor = QPlainTextEdit()
		self.setCentralWidget(self.editor)
		
		monospace = QFontDatabase.systemFont(QFontDatabase.FixedFont)
		monospace.setPointSize(12)
		self.editor.setFont(monospace)
		self.path = None

		self.menu = QMenuBar()
		self.fileMenu = QMenu("File")
		self.newAction = QAction("New")
		self.openAction = QAction("Open")
		self.saveAction = QAction("Save")
		self.saveAsAction = QAction("Save as...")
		for i in [self.newAction, self.openAction, self.saveAction, self.saveAsAction]:
			self.fileMenu.addAction(i)

		self.editMenu = QMenu("Edit")
		self.toolsMenu = QMenu("Tools")
		self.helpMenu = QMenu("Help")
		for i in [self.fileMenu, self.editMenu, self.toolsMenu, self.helpMenu]:
			self.menu.addMenu(i)
		self.setMenuBar(self.menu)

		self.status = QStatusBar()
		self.setStatusBar(self.status)


if __name__ == "__main__":
	app = QApplication(sys.argv)

	win = MainWindow()
	win.resize(600, 400)
	win.show()
	sys.exit(app.exec_())