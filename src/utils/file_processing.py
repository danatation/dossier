from pathlib import Path
from src import log
import subprocess

from src.utils.game_config import parse_game_config
from src.utils.game_info import get_resolved_game_path
from src.unrpyc.utils import decompile_rpyc, Context, BadRpycException
from src import rpatool

import msgpack

context = Context()

def cache_library() -> None:
	cache_path = Path.cwd() / 'cache'
	cache_path.mkdir(exist_ok=True)
	library_dict = {}

	base_path = Path.cwd() / 'base'
	if sorted(base_path.glob('*')) == []:
		log.error('Please download DDLC from https://teamsalvato.itch.io/ddlc and extract the ZIP file to the "base" folder in order for Dossier to function.')
		return
	ddlc_config = parse_game_config(base_path)
	library_dict['base'] = ddlc_config

	mods_path = Path.cwd() / 'mods'
	for game in sorted(mods_path.glob('*')):
		game_config = parse_game_config(get_resolved_game_path(game))
		library_dict[game.name] = game_config

	with open(cache_path / 'library.msgpack', 'wb') as f:
		library_cache = msgpack.packb(library_dict)
		f.write(library_cache)

def compile_qt_files() -> None:
	qt_path = Path.cwd() / 'src' / 'qt'
	qt_files = sorted(qt_path.glob('*'))
	venv_bin_path = Path.cwd() / '.venv' / 'bin'

	for file in qt_files:
		if file.suffix == '.ui':
			subprocess.run([venv_bin_path / 'pyside6-uic', file, '-o', file.parent / f'{file.stem}_ui.py', '--from-imports'])
			log.debug(f'Compiled {file.name}')
		elif file.suffix == '.qrc':
			subprocess.run([venv_bin_path / 'pyside6-rcc', file, '-o', file.parent / f'{file.stem}_rc.py'])
			log.debug(f'Compiled {file.name}')

def extract_game_assets(game_path: Path) -> None:
	assets_path = game_path / 'assets'
	assets_path.mkdir(exist_ok=True)

	renpy_archives = sorted(game_path.rglob('*.rpa'))
	if not game_path.name == 'base':
		renpy_archives = [archive for archive in renpy_archives if 'images.rpa' not in str(archive) and 'fonts.rpa' not in str(archive) and 'audio.rpa' not in str(archive)]

	for archive_path in renpy_archives:
		archive = rpatool.RenPyArchive(file=archive_path)
		subdir_path = assets_path / archive_path.stem
		subdir_path.mkdir(exist_ok=True)
		archive_files = archive.list()
		for file in archive_files:
			data = archive.read(file)
			file_path = subdir_path / file
			file_path.parent.mkdir(parents=True, exist_ok=True)
			file_path.touch()
			with open(subdir_path / file, 'wb') as f:
				f.write(data)
			if file_path.suffix == '.rpyc':
				try:
					decompile_rpyc(file_path, context)
				except BadRpycException as err:
					log.error(f'Couldn\'t decompile {file_path.name}! Got the error: \n{err}')
				else:
					log.debug(f'Decompiled {file_path.name}')