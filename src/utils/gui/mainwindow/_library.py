import time
from pathlib import Path

import msgpack
from PySide6.QtCore import QRunnable, Slot
from PySide6.QtWidgets import QFrame, QPushButton

from src import log
from src.utils.file_processing import cache_library
from src.utils.game_config import parse_game_config, set_game_config_value
from src.utils.game_utils import launch_game
from src.utils.spreadsheet import parse_mod_list

from ..funcs import Worker, clear_layout


def refresh_library(self):
	'''
	Fetches all of the mods from the library.msgpack file and adds them 
	'''
	library_path = Path.cwd() / 'cache' / 'library.msgpack'
	mod_list_path = Path.cwd() / 'cache' / 'mod_list.msgpack'
	if not library_path.exists():
		cache_library()

	with open(library_path, 'rb') as f:
		msgpack_data = f.read()
		self.library = msgpack.unpackb(msgpack_data)

	if mod_list_path.exists():
		self.mod_list = parse_mod_list()

	layout = self.ui.libraryModScrollAreaWidgetContents.layout()
	self.selected_game = None
	clear_layout(self, layout)

	for key in self.library.keys():
		index = list(self.library.keys()).index(key)

		nickname = self.library[key]['info']['nickname']
		if nickname == '':
			name = key
		else:
			name = nickname

		button = QPushButton(name)
		button.setObjectName(f'libraryModButton{index}')
		button.setCheckable(True)
		button.setFlat(True)
		button.setStyleSheet('QPushButton { text-align: left; padding: 4px; padding-left: 8px; }')
		button.clicked.connect(self.button_action)
		layout.addWidget(button)

		log.info(f'index: {index}')
		log.info(f'button: {button}')
		if index == 0:
			self.selected_game = button

	separator = QFrame()
	layout.addWidget(separator)
	select_game(self)

def recache_library(self):
	worker = Worker(cache_library)
	worker.signal.finished.connect(lambda: refresh_library(self))
	self.threadpool.start(worker)

def select_game(self):
	if self.selected_game is not None:
		self.selected_game.setChecked(False)
	# if there's no sender that means the function was not run from a button click and most likely from the library being refreshed
	if self.sender() is not None:
		self.selected_game = self.sender()
	else:
		self.selected_game.setChecked(True)

	self.ui.libraryModInfoName.setText(self.selected_game.text())

def start_game_process(self):
	index = int(self.selected_game.objectName().removeprefix('libraryModButton'))
	game_name = list(self.library.keys())[index]

	if game_name == 'base':
		game_path = Path.cwd() / 'base'
	else:
		game_path = Path.cwd() / 'mods' / game_name

	launch_game(game_path)

def cleanup_game(self, game_path: Path) -> None:
	config_data = parse_game_config(game_path)
	
	playtime = config_data['info']['playtime'] + time.time() - config_data['info']['date_last_played']
	set_game_config_value(game_path, 'playtime', playtime)
	set_game_config_value(game_path, 'date_last_played', time.time()) 


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