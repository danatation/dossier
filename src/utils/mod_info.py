from pathlib import Path
from typing import Union
import logging, hashlib, subprocess, platform, shutil, os, time, atexit, importlib, tomllib, asyncio

import tomlkit
from tomlkit import document, nl, table, comment
import patoolib

from utils.directories import *

logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

def get_main_launch_script(mod_name: str) -> Path:
	'''returns the path of the main launch .py script'''
	mod_dir = get_mod_directory(mod_name)
	script_paths = sorted(mod_dir.glob('*.py'))
	filtered_paths = [script for script in script_paths if script.name != 'DDLC.py']
	# if filtered_paths has at least 1 file than that means the mod is renpy 7/8
	if len(filtered_paths) > 0:
		return filtered_paths[0]
	elif len(script_paths) > 0:
		return script_paths[0]
	else:
		# only runs when symlinking a ren'py 6 mod
		# cheap way to not make it error out (there are no script files before symlinking)
		return get_work_dir('base') / 'DDLC.py'

def get_renpy_version(mod_name: str) -> int:
	'''returns the renpy version by checking the amount of ren'py launch scripts in the mod's directory'''
	mod_dir = get_mod_directory(mod_name)
	game_scripts = sorted(mod_dir.glob('*.py'))

	if len(game_scripts) > 1:
		# mods with a standalone script file will always be renpy7/8
		log.debug(f'mod is renpy7/8')
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
			log.debug(f'mod is renpy6')
			return 6
		else:
			log.debug(f'mod is renpy7/8, md5 hash is: {script_md5}')
			return 78
	else:
		log.info(f'mod is renpy6')

def get_execution_directory(mod_name: str) -> Path:
	'''finds the appropiate ren'py execs inside lib''' 
	mod_dir = get_mod_directory(mod_name)
	os = platform.system()
	arch = platform.machine()

	lib_paths = [
		f'py3-{os.lower()}-{arch}',
		f'py2-{os.lower()}-{arch}',
		f'{os.lower()}-{arch}'
	]

	if os != 'Darwin':
		lib_dir = mod_dir / 'lib'
		for path in lib_paths:
			py_lib_dir = lib_dir / path
			if py_lib_dir.exists():
				return py_lib_dir
		else:
			log.error(f'mod_dir couldn\'t be found!')
			return 1
	elif os == 'Darwin':
		# there's a high chance this doesn't even work lol
		lib_dir = mod_dir / f'{get_main_launch_script(mod_name).stem}.app' / Contents / MacOS 
		if get_renpy_version() == 6:
			return lib_dir / 'lib' / f'{os.lower()}-{arch}'
		else:
			return lib_dir

async def get_mod_config_value(mod_name: str, config_category: str, config_key: str) -> Union[str, int]:
	config_path = get_mod_directory(mod_name) / 'game' / 'dossier.toml'
	with open(config_path, 'r') as f:
		config_data = tomlkit.parse(f.read())

	return config_data[config_category][config_key]