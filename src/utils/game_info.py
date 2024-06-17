from pathlib import Path
from typing import Union
from src import log
import platform

import tomli

def get_py_script_path(game_path: Path) -> Path:
	'''
	Returns the Python script path that the game uses to launch itself
	Useful to know if the game is Ren'Py 6, and to know the Ren'Py project name
	'''

	if game_path.exists():
		scripts = sorted(game_path.rglob('*.py'))
	else:
		raise FileNotFoundError(f'The game path does not exist! ({game_path})')	
	py_scripts = []

	for script in scripts:
		pyo_path = script.parent / f'{script.stem}.pyo'
		if not pyo_path.exists() and not script.parent.stem == 'python-packages':
			py_scripts.append(script)

	for script in py_scripts:
		# Ren'Py 7/8 mods have multiple Python scripts. Skipping DDLC.py ensures we get our actual Ren'Py 7/8 script.
		if 'DDLC.py' in str(script) and len(py_scripts) > 1:
			continue
		else:
			log.debug(f'Returned Python script: "{script}"')
			return script

def get_resolved_game_path(game_path: Path) -> Path:
	'''
	Do i need to repeat myself
	'''

	renpy_scripts = sorted(game_path.rglob('*.rp*'))
	filtered_scripts = [script for script in renpy_scripts if '00' not in script.stem and 'rpym' not in script.suffix]

	try:
		least_nested_file = min(filtered_scripts, key=lambda x: len(x.parts))
	except ValueError:
		log.error(f'get_resolved_game_path() failed! ({game_path})')
		log.error(f'renpy_scripts: {renpy_scripts}')
		log.error(f'filtered_scripts: {filtered_scripts}')

	# Assuming the file is inside of game/, we return game/'s parent folder
	log.debug(f'Returned game path: "{least_nested_file.parents[1]}"')
	return least_nested_file.parents[1]

def get_execution_path(game_path: Path) -> Path:
	
	lib_path = game_path / 'lib'
	arch = platform.machine()
	os = platform.system()

	path_names = [
		f'py3-{os.lower()}-{arch}',
		f'py2-{os.lower()}-{arch}',
		f'{os.lower()}-{arch}',
		f'{os.lower()}-i686' # Required for Ren'Py 6 mods, as they are 32-bit (on Windows)
	]

	for name in path_names:
		exec_path = lib_path / name
		if exec_path.exists():
			log.debug(f'Machine is running "{name}"')
			return exec_path
	raise FileNotFoundError('Couldn\'t find executables!')