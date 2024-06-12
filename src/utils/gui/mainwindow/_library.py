from pathlib import Path
from src import log
import atexit, subprocess, time

from PySide6.QtCore import QThreadPool, QProcess, Signal
from PySide6.QtWidgets import QPushButton, QFrame
import msgpack

from src.utils.file_processing import cache_library
from src.utils.spreadsheet import parse_mod_list
from src.utils.game_config import parse_game_config, set_game_config_value
from src.utils.game_utils import launch_game
from src.utils.game_info import get_resolved_game_path
from ..funcs import clear_layout

def refresh_library(self):
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
			button.clicked.connect(self.button_action)
			layout.addWidget(button)

		separator = QFrame()
		layout.addWidget(separator)

def select_game(self):
	if self.selected_game != None:
		self.selected_game.setChecked(False)
	self.selected_game = self.sender()

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
	config_path = game_path / 'game' / 'config.toml'
	config_data = parse_game_config(game_path)
	
	playtime = config_data['info']['playtime'] + time.time() - config_data['info']['date_last_played']
	set_game_config_value(game_path, 'playtime', playtime)
	set_game_config_value(game_path, 'date_last_played', time.time()) 