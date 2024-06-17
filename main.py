import importlib
import sys

from PySide6.QtWidgets import QApplication

from src.utils import dossier, file_processing

if __name__ == '__main__':
	
	dossier.check_install()
	file_processing.compile_qt_files()

	mainwindow = importlib.import_module('src.utils.gui.mainwindow')
	app = QApplication(sys.argv)

	window = mainwindow.MainWindow()
	window.show()

	sys.exit(app.exec())