from PySide6.QtWidgets import QApplication
from utils.compilers import *
from utils.dirs import *
from utils.mods import *
from utils.symlinks import *
from pathlib import Path
from gui import mainwindow_ui, ddms
import sys

# TODO move appdata/ folder inside of the mods game/ folder and rename it to ddms/
# TODO basic gui with mod importing and selection and playation
# incorporate the mod list and fix that weird bug with the merged cells
# implement the asset viewer with rpatool and unrpyc

if __name__ == '__main__':
	# ui_path = Path.cwd() / 'src' / 'gui' / 'mainwindow.ui'
	# compilers.compile_ui(ui_path, 'mainwindow_ui.py')
	# qrc_path = Path.cwd() / 'src' / 'resources' / 'icons.qrc'
	# compilers.compile_qrc(qrc_path, 'icons.py')
	# app = QApplication(sys.argv)
	# window = ddms.MainWindow()
	# window.show()
	# sys.exit(app.exec())	
	
	# setup_mod('Impossible')
	run_mod('Impossible')

	''' gui will come in later '''