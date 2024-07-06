import importlib
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from src import log
from src.utils.dossier import check_install
from src.utils.game_funcs import launch_game

if __name__ == '__main__':

	check_install()
	
	# file_processing.compile_qt_files()

	mainwindow = importlib.import_module('src.utils.gui.mainwindow')
	app = QApplication(sys.argv)

	window = mainwindow.MainWindow()
	window.show()

	sys.exit(app.exec())
