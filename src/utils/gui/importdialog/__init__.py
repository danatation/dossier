import importlib
from src import log
from pathlib import Path

from PySide6.QtWidgets import QDialog, QFileDialog, QDialogButtonBox

import patoolib, tomli

from ..funcs import connect_attributes
from src.utils.game_info import get_resolved_game_path
from src.utils.game_utils import setup_game, copy_game_files, extract_game
from src.utils.game_config import set_game_config_value

class Ui_Dialog(QDialog):
	def __init__(self):
		super().__init__()
		importdialog_ui = importlib.import_module('src.qt.importdialog_ui')
		self.ui = importdialog_ui.Ui_Dialog()
		self.ui.setupUi(self)
		self.setWindowTitle('Import')

		connect_attributes(self, connect_qtoolbutton=True, connect_qlineedit=True)
		self.ui.buttonBox.accepted.connect(self.button_action)
		self.accept_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
		self.accept_button.setEnabled(False)

		config_path = Path.cwd() / 'config.toml'
		with open(config_path, 'rb') as f:
			self.config = tomli.load(f)

		if self.config['settings']['symlink_ddlc_to_mods'] == True:
			log.info('YES')
			self.ui.symlinkRadio.setChecked(True)

	def button_action(self):
		sender = self.sender().objectName()

		if sender == 'locationToolButton':
			archive_path = QFileDialog.getOpenFileName(self)
			if patoolib.is_archive(archive_path[0]):
				self.ui.locationEdit.setText(archive_path[0])
		elif sender == 'buttonBox':
			archive_path = Path(self.ui.locationEdit.text())

			log.debug(f'Extracting archive... ({self.ui.locationEdit.text()})')

			outdir_path = Path.cwd() / 'mods' / archive_path.stem

			if outdir_path.exists():
				try:
					outdir_path.rmdir()
				except OSError:
					return
			extract_game(archive_path)

			log.debug(f'Setting the mod up...')

			game_path = get_resolved_game_path(outdir_path)
			setup_game(game_path)

			if self.ui.copyRadio.isChecked() == True:
				log.debug(f'Copying DDLC files...')
				copy_game_files(game_path)
			else:
				log.debug(f'Symlinking DDLC files...')
				copy_game_files(game_path, symlinking=True)

			name = self.ui.nameEdit.text()
			if not name == '':
				set_game_config_value(game_path, 'nickname', name)

	def line_action(self):
		sender = self.sender().objectName()

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