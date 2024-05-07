from pathlib import Path
from typing import Union
import logging, hashlib, subprocess, platform, shutil, os, time, atexit, importlib, tomllib, asyncio

import tomlkit
from tomlkit import document, nl, table, comment
import patoolib

from utils.directories import get_mod_directory, get_work_directory

logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

def get_main_launch_script(game_dir: Path) -> Path:
	'''returns the path of the main launch .py script'''
	script_paths = sorted(game_dir.glob('*.py'))
	filtered_paths = [script for script in script_paths if script.name != 'DDLC.py']
	# if filtered_paths has at least 1 file than that means the mod is renpy 7/8
	if len(filtered_paths) > 0:
		return filtered_paths[0]
	elif len(script_paths) > 0:
		return script_paths[0]
	else:
		# only runs when symlinking a ren'py 6 mod
		# cheap way to not make it error out (there are no script files before symlinking)
		return get_work_directory('base') / 'DDLC.py'

def get_renpy_version(game_dir: Path) -> int:
	'''returns the renpy version by checking the amount of ren'py launch scripts in the game's directory'''
	game_scripts = sorted(game_dir.glob('*.py'))

	if len(game_scripts) > 1:
		# mods with a standalone script file will always be renpy7/8
		log.debug(f'The game is Ren\'py 7/8')
		return 78
	elif len(game_scripts) == 1:
		# SOME MODS (COUGH COUGH WINTERMUTE COUGH) update the main DDLC.py script file to be ren'py 7/8
		# so we're just going to checksum the script file to see if it's the original or not
		# heyyy this is older bulb i redownloaded wintermute and apparently they made it no longer like this
		# My efforts all went to nothing
		with open(game_scripts[0], 'rb') as f:
			md5_hash = hashlib.md5()

			# read the .py file in chunks because why not who fucking cares
			for chunk in iter(lambda: f.read(4096), b''):
				md5_hash.update(chunk)
	
		script_md5 = md5_hash.hexdigest()
		if script_md5 == '74fb8eb686fae8eef33e583da0ebed6e':
			log.debug(f'The game is Ren\'py 6')
			return 6
		else:
			log.debug(f'The game is Ren\'py 7/8 since its MD5 hash is {script_md5}')
			return 78
	else:
		log.info(f'mod is renpy6')

def get_execution_directory(game_dir: Path) -> Path:
	'''finds the appropiate ren'py execs inside lib''' 
	os = platform.system()
	arch = platform.machine()

	lib_paths = [
		f'py3-{os.lower()}-{arch}',
		f'py2-{os.lower()}-{arch}',
		f'{os.lower()}-{arch}'
	]

	if os != 'Darwin':
		lib_dir = game_dir / 'lib'
		for path in lib_paths:
			py_lib_dir = lib_dir / path
			if py_lib_dir.exists():
				return py_lib_dir
		else:
			log.error(f'The game directory couldn\'t be found!')
			return 1
	elif os == 'Darwin':
		# there's a high chance this doesn't even work lol
		lib_dir = game_dir / f'{get_main_launch_script(game_dir).stem}.app' / Contents / MacOS 
		if get_renpy_version(game_dir) == 6:
			return lib_dir / 'lib' / f'{os.lower()}-{arch}'
		else:
			return lib_dir

def parse_game_config(game_dir: Path) -> dict:
	config_path = game_dir / 'game' / 'dossier.toml'
	if not config_path.exists():
		from utils.game_utils import setup_game
		setup_game(game_dir)

	with open(config_path, 'r') as f:
		config_data = tomlkit.parse(f.read())

	overridable_config_options = ['different_save_dir', 'skip_splash_scr', 'skip_menu', 'discord_rpc']
	for option in overridable_config_options:
		if config_data['options'][option] == '':
			dossier_config_path = Path.cwd() / 'config.toml'
			with open(dossier_config_path, 'r') as f:
				dossier_config_path = tomlkit.parse(f.read())
				config_data['options'][option] = dossier_config_path['default_config_options'][option]
	return config_data
			
	# config_data = parse_game_config(mod_name)
	# config_value = config_data[config_category][config_key]

# def get_mod_config_value(mod_name: str, config_category: str, config_key: str) -> Union[str, int]: