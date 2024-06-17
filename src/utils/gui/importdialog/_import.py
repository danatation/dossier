from pathlib import Path

import patoolib
from PySide6.QtWidgets import QProgressBar

from src import log
from src.utils.game_config import set_game_config_value
from src.utils.game_info import get_resolved_game_path
from src.utils.game_utils import copy_game_files, extract_game, setup_game


def import_mod(self):
	self.ui.buttonBox.setEnabled(False)
	progress_bar = QProgressBar()
	progress_bar.setRange(0, 100)
	layout = self.ui.importLayout.layout()
	layout.addWidget(progress_bar)
	
	archive_path = Path(self.ui.locationEdit.text())

	if not patoolib.is_archive(archive_path):
		log.error(f'"{archive_path.name}" is not an archive!')
		return

	outdir_path = Path.cwd() / 'mods' / archive_path.stem

	if outdir_path.exists():
		try:
			outdir_path.rmdir()
		except OSError:
			return
	log.debug('Passed outdir_path.exists() check!')

	log.debug('Extracting archive...')
	extract_game(archive_path)
	log.debug('Extracted archive!')

	game_path = get_resolved_game_path(outdir_path)

	if self.ui.copyRadio.isChecked() == True:
		copy_game_files(game_path)		
	else:
		copy_game_files(game_path, symlinking=True)
	log.debug('copy_games_files() done!')

	log.debug('Setting up mod...')
	setup_game(game_path)
	log.debug('Set up mod!')

	name = self.ui.nameEdit.text()

	if not name == '':
		set_game_config_value(game_path, 'nickname', name)