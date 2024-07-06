import platform
from pathlib import Path
from typing import cast

import tomlkit

from src.utils.config import make_dossier_config, make_game_config

def return_resolved_path(game_path: Path) -> Path:
	"""
	Returns the resolved path of a mod by getting every single Ren'py file and then filtering out the engine related ones.
	"""
	
	renpy_files = sorted(game_path.rglob('*.rp*'))
	game_files = []
		
	for file in renpy_files:
		if '.rpym' in file.suffix or '0' in file.stem or file.suffix == '.rpyb':
			# we need to filter out every single engine file and only get the good stuff (game data like images.rpa and scripts.rpa and all that)
			# .rpym, .rpymc, .rpyb and those weird files beginning in zeros are all boring engine files
			continue
		game_files.append(file)

	return game_files[0].parents[-1]
		
def return_py_script(game_path: Path) -> Path:
	"""
	Globs every single python script in the provided path and picks out the main one.
	This function is useful for seeing what the executable name is on Linux and for seeing what Ren'py version a mod is (if it returns DDLC.py then it's Ren'py 6).
	"""
	
	py_files = sorted(game_path.glob('*.py'))

	for path in py_files:
		# checking if the mod is ren'py 7/8
		if path.name != 'DDLC.py':
			# ren'py 6 mods only have DDLC.py, while newer ones have their own python script. this one has multiple so return the other one
			return path

	# due to the check failing, the mod is ren'py 6. return the only script it found
	return py_files[0]

def return_exec_path(game_path: Path) -> Path:
	"""
	Returns a mod's executable location.
	"""
	os = platform.system().lower()
	arch = platform.machine()

	exec_folders = [
		f'py3-{os}-{arch}',
		f'py2-{os}-{arch}',
		f'{os}-{arch}',
		f'{os}-i686' # ren'py 6 mods are always 32-bit on windows
	]

	lib_folder = game_path / 'lib'
	for name in exec_folders:
		exec_folder = lib_folder / name
		if exec_folder.exists():
			if os == 'linux':
				exec_name = return_py_script(game_path).stem
			elif os == 'windows':
				# HAAAAAAAAA YOU GUYS ARE LAMEEE
				exec_name = 'python.exe'
			else:
				# macos support coming Soon:tm:
				raise Exception('Your machine is not supported!')
			return exec_folder / exec_name
	raise FileNotFoundError('Could not find the game\'s executables!')

def return_game_config(game_path: Path) -> dict:
	dossier_config_path = Path.cwd() / 'dossier.toml'
	game_config_path = game_path / 'game' / 'dossier.toml'
	if not dossier_config_path.exists():
		make_dossier_config()
	if not game_config_path.exists():
		make_game_config(game_path)

	with open(dossier_config_path, 'rb') as f:
		dossier_config = cast(dict, tomlkit.load(f))
	with open(game_path / 'game' / 'dossier.toml', 'rb') as f:
		game_config = cast(dict, tomlkit.load(f))

	resolved_config = game_config

	for key in game_config['options']:
		if key in ('renpy_save_dir', 'skip_splash_scr', 'skip_main_menu', 'discord_rpc') and game_config['options'][key] == '':
			resolved_config['options'][key] = dossier_config['default_options'][key]
		else:
			resolved_config['options'][key] = game_config['options'][key]

	return resolved_config