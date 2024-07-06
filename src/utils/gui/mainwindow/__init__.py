import importlib

from PySide6.QtWidgets import QMainWindow

from .library import refresh_library

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		mainwindow_ui = importlib.import_module('src.qt.mainwindow_ui')
		self.ui = mainwindow_ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Dossier')

		refresh_library(self)