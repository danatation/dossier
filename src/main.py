from PySide6.QtWidgets import QApplication
from utils.compilers import *
from utils.dirs import *
from utils.mods import *
from utils.symlinks import *
from pathlib import Path
from gui import mainwindow_ui, ddms
import sys

if __name__ == '__main__':
	# ui_path = Path.cwd() / 'src' / 'gui' / 'mainwindow.ui'
	# compilers.compile_ui(ui_path, 'mainwindow_ui.py')
	# qrc_path = Path.cwd() / 'src' / 'resources' / 'icons.qrc'
	# compilers.compile_qrc(qrc_path, 'icons.py')
	# app = QApplication(sys.argv)
	# window = ddms.MainWindow()
	# window.show()
	# sys.exit(app.exec())
	
	run_mod('Exit Music Redux', skip_splash_scr=True, skip_menu=False)
	
	''' gui will come in later '''