import importlib
from pathlib import Path

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QMainWindow, QPushButton, QTabWidget

from src import log
from src.utils.game_info import get_resolved_game_path
from src.utils.gui import importdialog

from ..funcs import connect_attributes
from ._library import GameWorker, recache_library, refresh_library, select_game


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		mainwindow_ui = importlib.import_module('src.qt.mainwindow_ui')
		self.ui = mainwindow_ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Dossier')

		connect_attributes(self, connect_qtabwidget=True)
		self.library = {}
		self.mod_list = {}
		self.selected_game: QPushButton
		self.threadpool = QThreadPool()

		# refresh_library(self)
		# recache_library(self)

	def button_action(self):
		# sender = self.sender().objectName()
		
		# if sender == 'libraryModInfoPlay':
		# 	index = int(self.selected_game.objectName().removeprefix('libraryModButton'))
		# 	game_name = list(self.library.keys())[index]

		# 	if game_name == 'base':
		# 		game_path = Path.cwd() / 'base'
		# 	else:
		# 		game_path = Path.cwd() / 'mods' / game_name

		# 	worker = GameWorker(get_resolved_game_path(game_path))
		# 	self.threadpool.start(worker)

		# elif 'libraryModButton' in sender:
		# 	select_game(self)

		# elif sender == 'libraryImportButton':
		# 	dialog = importdialog.Ui_Dialog()
		# 	try:
		# 		dialog.exec()
		# 	finally:
		# 		recache_library(self)

		# else:
		# 	log.info(f'Button clicked! ({sender})')
		...

	def tab_action(self):
		# sender = self.sender().currentWidget().objectName()
		# if sender == 'libraryTab':
		# 	refresh_library(self)
		# 	recache_library(self)
		# else:
		# 	log.info(f'Tab changed! ({sender})')
		...