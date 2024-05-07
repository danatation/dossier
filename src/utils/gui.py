from pathlib import Path
import logging, hashlib, subprocess, platform, shutil, os, time, atexit, importlib

# from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QTabWidget
from PySide6.QtGui import QTextOption, QFontMetrics
from PySide6.QtCore import QRunnable, QThreadPool, Slot
from tomlkit import document, nl, table, comment
import patoolib
import asyncio

from utils.cache import read_library_cache, update_library_cache
from utils.game_utils import launch_mod, launch_base
from utils.game_info import get_mod_directory, get_work_directory

logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

def compile_ui_file(ui_path:Path, uic_name:str) -> None:
	compiler_path = Path.cwd() / '.venv' / 'bin' / 'pyside6-uic'
	ui_path = Path(ui_path)
	
	if compiler_path.exists() and ui_path.exists():
		uic_path = ui_path.parent / uic_name
		subprocess.run([compiler_path, ui_path, '-o', uic_path, '--from-imports'])
	else:
		if not compiler_path.exists():
			log.error(f'compiler_path: {compiler_path} does not exist!')
		if not ui_path.exists():
			log.error(f'ui_path: {ui_path} does not exist!')

def compile_qt_resources(qrc_path:Path, py_name:str) -> None:
	compiler_path = Path.cwd() / '.venv' / 'bin' / 'pyside6-rcc'
	qrc_path = Path(qrc_path)

	if compiler_path.exists() and qrc_path.exists():
		py_path = qrc_path.parent / py_name
		subprocess.run([compiler_path, qrc_path, '-o', py_path])
	else:
		if not compiler_path.exists():
			log.error(f'compiler_path: {compiler_path} does not exist!')
		if not qrc_path.exists():
			log.error(f'qrc_path: {qrc_path} does not exist!')

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.mainwindow_ui = importlib.import_module('qt.mainwindow_ui')
		self.ui = self.mainwindow_ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Dossier')

		# Initializing all of the buttons
		attributes = vars(self.ui)
		for attribute_name, attribute in attributes.items():
			if isinstance(attribute, QPushButton):
				attribute.clicked.connect(self.button_clicked)
			elif isinstance(attribute, QTabWidget):
				attribute.currentChanged.connect(self.tab_changed)

		self.library_cache = {} 
		self.selected_mod = None
		self.selected_mod_name = None
		self.threadpool = QThreadPool()
		
		asyncio.run(update_library_cache())
		asyncio.run(self.display_library())

	def button_clicked(self):
		sender = self.sender()

		if sender.objectName() == 'libraryImportButton':
			log.info(f'We will add importing later!')
		elif 'libraryModButton' in sender.objectName():
			self.mod_changed(sender)
		elif sender.objectName() == 'libraryModInfoPlay' and self.selected_mod != None:
			self.play_mod()
		elif sender.objectName() == 'libraryModInfoOptions':
			self.ui.libraryViewTabWidget.setCurrentIndex(2)
		else:
			log.info(f'Button {sender.objectName()} has no function assigned to it!')

	def tab_changed(self):
		sender = self.sender()

		current_tab = sender.currentWidget().objectName()

		if current_tab == 'libraryTab':
			asyncio.run(self.display_library())
		else:
			log.warn(f'Tab {current_tab} has no function assigned to it!')

	async def display_library(self):
		scroll_area = self.ui.libraryModScrollAreaWidgetContents.layout()
		self.clear_layout(scroll_area)

		self.selected_mod = None
		self.library_cache = read_library_cache()
		mod_names = self.library_cache.keys()

		i = -1
		for name in mod_names:
			i += 1
			nickname = self.library_cache[name]['options']['nickname']
			if nickname != '':
				name = nickname
			mod_button = QPushButton(name)
			mod_button.setFlat(True)
			mod_button.setCheckable(True)
			mod_button.setStyleSheet('QPushButton { text-align: left; padding: 4px; padding-left: 8px; }')
			mod_button.setObjectName(f'libraryModButton{i}')
			mod_button.clicked.connect(self.button_clicked)
			scroll_area.addWidget(mod_button)

		separator = QFrame()
		scroll_area.addWidget(separator)

	def clear_layout(self, layout):
		if layout is not None:
			while layout.count():
				item = layout.takeAt(0)
				widget = item.widget()
				if widget is not None:		
					widget.deleteLater()
				else:
					self.clear_layout(item.layout())

	def mod_changed(self, sender):
		if sender != self.selected_mod and self.selected_mod != None:
			self.selected_mod.setChecked(False)
		self.selected_mod = sender

		mod_index = int(sender.objectName().replace('libraryModButton', ''))
		mod_names = list(self.library_cache.keys())
		self.selected_mod_name = mod_names[mod_index]
		self.ui.libraryModInfoName.setText(self.selected_mod_name)

		nickname = self.library_cache[self.selected_mod_name]['options']['nickname']
		if nickname != '':
			self.ui.libraryModInfoName.setText(nickname) 

	def play_mod(self):
		worker = ModProcessWorker(self.selected_mod_name)
		self.threadpool.start(worker)

class ModProcessWorker(QRunnable):
	def __init__(self, mod_name):
		super(ModProcessWorker, self).__init__()
		self.args = mod_name
	
	@Slot()
	def run(self):
		if self.args == 'base':
			launch_base()
		else:
			launch_mod(self.args)