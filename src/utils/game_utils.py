from pathlib import Path
from .. import log
import shutil, time, subprocess, os

from src.utils.game_info import get_resolved_game_path, get_py_script_path, get_execution_path
from src.utils.game_config import parse_game_config, create_game_config

import tomlkit, patoolib
from tomlkit import document, nl, table, comment, parse

def extract_game(archive_path: Path) -> None:
	game_path = Path.cwd() / 'mods' / archive_path.stem
	
	if archive_path.exists() and not game_path.exists():
		patoolib.extract_archive(str(archive_path), outdir=str(game_path))
		setup_game(game_path)

def copy_game_files(game_path: Path, symlinking: bool=False) -> None:
	'''
	Copies the DDLC files to whatever mod you are trying to install
	'''

	ddlc_path = Path.cwd() / 'base'

	if game_path == ddlc_path:
		raise FileExistsError('you can\'t do that fucking idiot')

	ddlc_files = sorted(ddlc_path.rglob('*'))
	game_files = sorted(game_path.rglob('*'))

	for file in ddlc_files:
		target_path = get_resolved_game_path(game_path) / file.relative_to(ddlc_path)
		if target_path.exists():
			continue
		elif target_path.name == 'scripts.rpa' and not Path(get_resolved_game_path(game_path) / 'game' / 'the_lock.7z').exists():
			continue
		elif target_path.parts[-1] == 'saves':
			continue

		elif file.is_dir():
			target_path.mkdir()
		elif file.name == 'DDLC.py':
			shutil.copy(file, target_path)
		
		elif symlinking:
			target_path.symlink_to(file)
		else:
			shutil.copy(file, target_path)

def setup_game(game_path: Path) -> None:

	py_script = get_py_script_path(game_path)

	if not config_path.exists():
		create_game_config(game_path)

	# Ren'Py 7/8 games do not launch under Linux if they still have this folder
	if 'DDLC.py' not in str(py_script):
		exec_path = get_execution_path(game_path)
		exec_lib_path = exec_path / 'lib'
		
		if exec_lib_path.exists():
			shutil.rmtree(exec_lib_path)
			log.debug('Removed "lib/"')

	elf_path = exec_path / get_py_script_path(game_path).stem
	elf_path.chmod(0o755)
	log.debug(f'Gave game executable permissions (Linux safety catch)')

def launch_game(game_path: Path) -> None:
	
	exec_path = get_execution_path(game_path) / get_py_script_path(game_path).stem
	config_data = get_game_config(game_path)

	args = [exec_path]
	env = os.environ.copy()

	if get_py_script_path(game_path).name == 'DDLC.py':
		args.extend(['-EO', get_py_script_path(game_path)])
	if config_data['options']['renpy_save_dir'] == True:
		save_slot = config_data['options']['renpy_save_slot']
		if save_slot < 2:
			save_slot = ''
		save_dir = game_path / 'game' / f'saves{save_slot}'
		args.extend(['--savedir', save_dir])
	
	if config_data['options']['skip_splash_scr'] == True:
		env['RENPY_SKIP_SPLASHSCREEN'] = '1'
	if config_data['options']['skip_main_menu'] == True:
		env['RENPY_SKIP_MAIN_MENU'] = '1'

	subprocess.run(args, env=env, check=True)