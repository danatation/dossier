from pathlib import Path
import sys, importlib

from PySide6.QtWidgets import QApplication

from utils.gui import compile_ui_file, compile_qt_resources

if __name__ == '__main__':

	testing = True
	if testing:
		ui_path = Path.cwd() / 'src' / 'qt' / 'mainwindow.ui'
		compile_ui_file(ui_path, 'mainwindow_ui.py')
		qrc_path = Path.cwd() / 'src' / 'qt' / 'icons.qrc'
		compile_qt_resources(qrc_path, 'icon_rc.py')

	dossier_gui = importlib.import_module('utils.gui')
	app = QApplication(sys.argv)
	window = dossier_gui.MainWindow()
	window.show()
	sys.exit(app.exec())	