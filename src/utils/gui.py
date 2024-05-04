from pathlib import Path
import logging, hashlib, subprocess, platform, shutil, os, time, atexit, importlib

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QTabWidget
from PySide6.QtGui import QTextOption, QFontMetrics
from tomlkit import document, nl, table, comment
import patoolib

from utils.directories import *
from utils.mod_info import *
from utils.mod_utils import *

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
		
	def button_clicked(self):
		sender = self.sender()

		if sender.objectName() == 'libraryImportButton':
			log.info(f'We will add importing later!')
		else:
			log.info(f'Button {sender.objectName()} has no function assigned to it!')

	def tab_changed(self):
		sender = self.sender()

		current_tab = sender.currentWidget().objectName()

		if current_tab == 'libraryTab':
			asyncio.run(self.update_library())
		else:
			log.warn(f'Tab {current_tab} has no function assigned to it!')

	async def update_library(self):
		mod_dir = get_work_directory('mods')
		mod_dirs = await list_directories(mod_dir)

		scroll_area = self.ui.libraryModScrollAreaWidgetContents.layout()
		self.clear_layout(scroll_area)
		
		mod_dir_tasks = []
		nickname_tasks = []

		for i in mod_dirs:
			nickname_task = asyncio.create_task(get_mod_config_value(i.name, 'options', 'nickname'))
			nickname_tasks.append(nickname_task)

			mod_button = QPushButton(i.name)
			
			mod_button.setFlat(True)
			mod_button.setCheckable(True)
			mod_button.setStyleSheet('QPushButton { text-align: left; padding: 4px; padding-left: 8px; }')
			
			scroll_area.addWidget(mod_button)

		results = await asyncio.gather(*nickname_tasks)

		for result in results:
			log.info(result)

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