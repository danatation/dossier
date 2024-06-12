from pathlib import Path
import importlib
from src import log

from PySide6.QtCore import QThreadPool, QThread, Slot, QRunnable
from PySide6.QtWidgets import QMainWindow, QPushButton, QTabWidget, QFrame
import msgpack

from src.utils.file_processing import cache_library
from src.utils.spreadsheet import parse_mod_list
from src.utils.gui import importdialog
from src.utils.game_utils import launch_game
from src.utils.game_info import get_resolved_game_path
from ._library import refresh_library, select_game, start_game_process, cleanup_game
from ..funcs import clear_layout, connect_attributes

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
		self.selected_game = None
		self.threadpool = QThreadPool()

		refresh_library(self)
		self.recache_library()

	def button_action(self):
		sender = self.sender().objectName()
		
		if sender == 'libraryModInfoPlay':
			index = int(self.selected_game.objectName().removeprefix('libraryModButton'))
			game_name = list(self.library.keys())[index]

			if game_name == 'base':
				game_path = Path.cwd() / 'base'
			else:
				game_path = Path.cwd() / 'mods' / game_name

			worker = GameWorker(get_resolved_game_path(game_path))
			self.threadpool.start(worker)
		elif 'libraryModButton' in sender:
			select_game(self)
		elif sender == 'libraryImportButton':
			dialog = importdialog.Ui_Dialog()
			dialog.exec()
		else:
			log.info(f'Button clicked! ({sender})')

	def tab_action(self):
		sender = self.sender().currentWidget().objectName()
		if sender == 'libraryTab':
			refresh_library(self)
			self.recache_library()
		else:
			log.info(f'Tab changed! ({sender})')

	def recache_library(self):
		worker = FunctionWorker(cache_library)
		self.threadpool.start(worker)
		refresh_library(self)

class FunctionWorker(QRunnable):
	def __init__(self, fn):
		super(FunctionWorker, self).__init__()
		self.fn = fn
	@Slot()
	def run(self):
		self.fn()

class GameWorker(QRunnable):
	def __init__(self, game_path: Path):
		super(GameWorker, self).__init__()
		self.game_path = game_path

	@Slot()
	def run(self):
		try:
			launch_game(self.game_path)
		finally:
			cleanup_game(self, self.game_path)