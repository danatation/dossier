from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel

from utils.dirs import check_ddms_tree
from gui import mainwindow_ui

import logging as log
log.basicConfig(level=log.NOTSET)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = mainwindow_ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Doki Doki Mod Swapper')

		# Initializing all of the buttons
		attributes = vars(self.ui)
		for attribute_name, attribute in attributes.items():
			if isinstance(attribute, QPushButton):
				attribute.clicked.connect(self.action)

		self.setup_text('modNameLabel')

	def action(self):
		''' Determines what a button should do '''
		sender = self.sender()
		sender_name = sender.objectName()

		if sender_name == "modPlayButton":
			check_ddms_tree()
		else:
			self.na_action()

	def na_action(self):
		''' Fallback function '''
		log.info(f' This button has not been asigned a function!')

	def setup_text(self, object_name) -> None:
		if object_name == 'modNameLabel':
			self.ui.modNameLabel.setText('Exit Music Refdux')