import importlib
from pathlib import Path

import patoolib
import tomli
from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFileDialog

from ..funcs import Worker, connect_attributes
from ._import import import_mod


class Ui_Dialog(QDialog):
	def __init__(self):
		super().__init__()
		importdialog_ui = importlib.import_module('src.qt.importdialog_ui')
		self.ui = importdialog_ui.Ui_Dialog()
		self.ui.setupUi(self)
		self.setWindowTitle('Import')

		connect_attributes(self, connect_qtoolbutton=True, connect_qlineedit=True)
		self.accept_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
		self.accept_button.setEnabled(False)
		self.threadpool = QThreadPool()
		self.is_importing = False	

		config_path = Path.cwd() / 'config.toml'
		with open(config_path, 'rb') as f:
			self.config = tomli.load(f)

		if self.config['settings']['symlink_ddlc_to_mods'] == True:
			self.ui.symlinkRadio.setChecked(True)

	def button_action(self):
		sender = self.sender().objectName()

		if sender == 'locationToolButton':
			archive_path = QFileDialog.getOpenFileName(self)
			if patoolib.is_archive(archive_path[0]):
				self.ui.locationEdit.setText(archive_path[0])

	def line_action(self):
		archive_path = Path(self.ui.locationEdit.text())
		
		if not archive_path.is_dir() and archive_path.exists():
			archive_name = archive_path.stem
			self.ui.nameEdit.setPlaceholderText(archive_name)
			self.accept_button.setEnabled(True)
		else:
			self.ui.nameEdit.setPlaceholderText('')
			self.accept_button.setEnabled(False)

		if self.ui.nameEdit.text() == 'base':
			self.accept_button.setEnabled(False)

	def accept(self):
		worker = Worker(import_mod, self)
		worker.signal.finished.connect(lambda: super(Ui_Dialog, self).accept())
		self.threadpool.start(worker)