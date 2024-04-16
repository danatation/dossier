from pathlib import Path
import logging as log, hashlib, patoolib
import subprocess, platform, shutil, os
from utils.dirs import *
log.basicConfig(level=log.NOTSET)

def get_renpy_version(mod_name: str) -> int:
	'''return code 6 is ren'py 6
	return code 78 is either ren'py 7 or 8'''
	mod_dir = get_mod_dir(mod_name)
	game_scripts = sorted(mod_dir.glob('*.py'))

	if len(game_scripts) > 1:
		# mods with a standalone script file will always be renpy7/8
		log.debug(f' mod is renpy7/8')
		return 78
	elif len(game_scripts) == 1:
		# SOME MODS (COUGH COUGH WINTERMUTE COUGH) update the main DDLC.py script file to be ren'py 7/8
		# so we're just going to checksum the script file to see if it's the original or not
		with open(game_scripts[0], 'rb') as f:
			md5_hash = hashlib.md5()

			# read the .py file in chunks because why not who fucking cares
			for chunk in iter(lambda: f.read(4096), b''):
				md5_hash.update(chunk)
	
		script_md5 = md5_hash.hexdigest()
		if script_md5 == '74fb8eb686fae8eef33e583da0ebed6e':
			log.debug(f' mod is renpy6')
			return 6
		else:
			log.debug(f' mod is renpy7/8, md5 hash is: {script_md5}')
			return 78
	else:
		log.info(f' mod is renpy6')

def get_launch_script(mod_name: str) -> Path:
	'''returns the path of the main launch .py script'''
	mod_dir = get_mod_dir(mod_name)
	script_paths = sorted(mod_dir.glob('*.py'))
	filtered_paths = [script for script in script_paths if script.name != 'DDLC.py']
	# if filtered_paths has at least 1 file than that means the mod is renpy 7/8
	if len(filtered_paths) > 0:
		return filtered_paths[0]
	else:
		return script_paths[0]

def find_exec_dir(mod_name: str) -> Path:
	'''finds the appropiate ren'py execs inside lib''' 
	mod_dir = get_mod_dir(mod_name)
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
			log.error(f' mod_dir couldn\'t be found!')
			return 1
	elif os == 'Darwin':
		# there's a high chance this doesn't even work lol
		lib_dir = mod_dir / f'{get_launch_script(mod_name).stem}.app' / Contents / MacOS 
		if get_renpy_version() == 6:
			return lib_dir / 'lib' / f'{os.lower()}-{arch}'
		else:
			return lib_dir

def install_mod(mod_path: Path, mod_name: str=None, force_install: bool=False) -> None:
	'''Installs the mod idk what you want from me'''
	if mod_name == None:
		mod_name = mod_path.stem

	forbidden_patterns = [
		'<', '>', ':', '"', '/', '\\', '|', '?', '*',
		'CON', 'PRN', 'AUX', 'NUL', 
		'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
		'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
	]

	# removes sinful patterns
	# is also made out of magic (chatgpt)
	mod_name = "".join([pattern for pattern in list(mod_name) if not pattern in forbidden_patterns])

	if Path(mod_path).exists():
		log.info(f' it is archive')
		mod_dir = get_work_dir('mods') / mod_name
		if mod_dir.exists() and force_install == False:
			log.error(f' mod already exists')
			return 1
		else:
			mod_dir.mkdir(exist_ok=True)
			patoolib.extract_archive(mod_path, outdir=mod_dir)
			setup_mod(mod_name)
	else:
		log.info(f' it is not archive :(')


def setup_mod(mod_name: str) -> None:
	'''sets up various extra folders and files'''
	
	# removes lib/ folder for ren'py 7/8 compat
	if get_renpy_version(mod_name) == 78:
		exec_dir = find_exec_dir(mod_name)
		lib_dir = exec_dir / 'lib'
		if lib_dir.exists():
			shutil.rmtree(lib_dir)
	
	# makes folder in appdata/ with save dir and more
	appdata_dir = get_work_dir('appdata') / mod_name
	appdata_dir.mkdir(exist_ok=True)
	save_dir = appdata_dir / 'saves'
	save_dir.mkdir(exist_ok=True)
	config_path = appdata_dir / 'config.json'
	if not config_path.exists():
		config_path.touch()

def run_mod(mod_name: str, change_save_dir: bool=True, skip_splash_scr: bool=False, skip_menu: bool=False) -> None:
	'''runs the mod with the wanted parameters'''

	exec_dir = find_exec_dir(mod_name)
	exec_name = get_launch_script(mod_name).stem
	exec_path = exec_dir / exec_name
	exec_path.chmod(exec_path.stat().st_mode | 0o111)
	log.info(f' exec: {exec_path}')
	
	args = [str(exec_path)]
	env = os.environ.copy()
	if get_renpy_version(mod_name) == 6:
		args.extend(['-EO', get_launch_script(mod_name)])
	if change_save_dir:
		appdata_dir = get_work_dir('appdata') / mod_name
		save_dir = appdata_dir / 'saves'
		save_parameter = '--savedir'
		args.extend([save_parameter, str(save_dir)])
	if skip_splash_scr:
		env['RENPY_SKIP_SPLASHSCREEN'] = '1'
	if skip_menu:
		env['RENPY_SKIP_MAIN_MENU'] = '1'

	subprocess.run(args, env=env, check=True)