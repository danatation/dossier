from src import log
from pathlib import Path	
import importlib, sys

from PySide6.QtWidgets import QApplication

from src.utils import dossier, file_processing, game_config, game_info, game_utils, spreadsheet
import src.utils.gui.mainwindow

if __name__ == '__main__':
	
	dossier.check_install()
	file_processing.compile_qt_files()

	mainwindow = importlib.import_module('src.utils.gui.mainwindow')
	app = QApplication(sys.argv)

	window = mainwindow.MainWindow()
	window.show()

	sys.exit(app.exec())