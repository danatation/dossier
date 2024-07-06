from pathlib import Path
from typing import cast

import msgpack
from PySide6.QtWidgets import QPushButton

from src import log
from ..funcs import clear_layout


def refresh_library(self) -> None:
	cache_path = Path.cwd() / 'cache' / 'library.msgpack'
	with open(cache_path, 'rb') as f:
		library_cache = cast(dict, msgpack.unpackb(f.read()))

	layout = self.ui.libraryModScrollAreaWidgetContents.layout()
	clear_layout(self, layout)

	for key in library_cache.keys():
		nickname = library_cache[key]['options']['nickname']

		if nickname == '':
			nickname = key

		button = QPushButton(nickname)
		layout.addWidget(button)