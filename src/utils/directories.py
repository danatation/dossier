from pathlib import Path
import logging, hashlib, subprocess, platform, shutil, os, time, atexit, importlib

from tomlkit import document, nl, table, comment
import aiofiles.os
import aiofiles
import aiopath
import patoolib


logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

def get_work_directory(folder_name: str) -> Path:
	'''What could this possibly do'''
	ddms_dir = Path.cwd() / folder_name
	return ddms_dir if ddms_dir.exists() else 1

def get_mod_directory(mod_name: str) -> Path:
	'''tries to find mod script file and then determines the root of the mod'''
	mod_dir = get_work_directory('mods') / mod_name

	if mod_dir.exists():
		all_script_files = sorted(mod_dir.rglob('*.rp*'))

		# remove everything that pops up in renpy/
		# then pick the least nested file
		for script_file in all_script_files:
			if '00' in script_file.stem:
				all_script_files.remove(script_file)
			
			if 'rpym' in script_file.suffix:
				all_script_files.remove(script_file)
		script = min(all_script_files, key=lambda x: len(x.parts))

		# set the cwd to be outside of the script file(s)
		if script.parts[-2] == 'game':
			log.info(f'mod_dir: {script.parents[1]}')
			return script.parents[1]
		# create game/ and paste everything in it
		else:
			Path(script.parent / 'game').mkdir(exist_ok=True)
			game_files = sorted(Path(script.parent).glob('*'))
			parent_dir = script.parts[-2]
			for file in game_files:
				parts_list = list(file.parts)
				# pasting a folder into itself is not very wise
				if parts_list[-1] == 'game':
					continue
				dir_index = len(parts_list) - 1 - file.parts[::-1].index(parent_dir)
				parts_list.insert(dir_index + 1, 'game')
				target_dir = Path(*parts_list)
				file.replace(target_dir)
			return script.parent

async def list_directories(path: Path) -> list:
	dirs = []
	entries = await aiofiles.os.listdir(path)
	for entry in entries:
		entry_path = path / entry
		if await aiofiles.os.path.isdir(entry_path):
			dirs.append(entry_path)
	return dirs

async def async_symlink(source, target) -> None:
	if not await target.exists():
		await target.symlink_to(source)

async def async_copy(source, target) -> None:
	async with aiofiles.open(source, 'rb') as src, aiofiles.open(target, 'wb') as tgt:
		await tgt.write(await src.read())

async def async_mkdir(target) -> None:
	await target.mkdir(parents=True, exist_ok=True)

async def symlink_mod(mod_name: str, copy: bool = False) -> None:
	'''
	symlinks every file from the ddlc folder into the mod folder without overwriting anything
	code has been made asynchronous with chatgpt i am very sorry it looks hideous
	'''

	# TODO change this chatgpt ass code

	from utils.game_info import get_main_launch_script
	
	ddlc_dir = aiopath.AsyncPath(get_work_directory('base'))    
	mod_dir = aiopath.AsyncPath(get_mod_directory(mod_name))
	ddlc_files = []
	async for path in ddlc_dir.rglob('*'):
		ddlc_files.append(path)

	for path in ddlc_files:
		path_parts, base_parts = path.parts, ddlc_dir.parts        
		common_path = path_parts[len(base_parts):]
		target_path = mod_dir / aiopath.AsyncPath(*common_path)
		log.debug(f'path: {path}')
		log.debug(f'target_path: {target_path}')

		if not await target_path.exists():
			# Handle specific file exclusions
			if target_path.name == 'scripts.rpa' and not (await (get_mod_directory(mod_name) / 'game' / 'the_lock.7z').exists()):
				continue
			if target_path.name == 'dossier.toml':
				continue
			if target_path.parts[-1] == 'saves':
				continue
			elif target_path.name == f'{get_main_launch_script(mod_name).name}':
				await async_copy(path, target_path)
			elif await path.is_dir():
				await async_mkdir(target_path)
			elif copy:
				await async_copy(path, target_path)
			else:
				await async_symlink(path, target_path)


def delink_mod(mod_name: str) -> None:
	# TODO rewrite this 
	# TODO please rewrite this
	# does not work if ddlc files have been copied instead of linked
	# it also does not remove folders

	ddlc_dir = get_work_directory("game")
	mod_dir = get_mod_directory(mod_name)

	for path in mod_dir.rglob("*"):
		mod_tuple, path_tuple = mod_path.parts, path.parts
		gen_tuple = path_tuple[len(mod_tuple):]
		gen_dir = str("")
		for i in gen_tuple:
			gen_dir += f"{i}/"
		target = ddlc_dir / gen_dir
		resolved_link = path.resolve()
		if resolved_link == target and not target.is_symlink or not resolved_link.exists():
			log.info(f" target IS equal to resolved_link")
			path.unlink()
		else:
			log.info(f" {target} does not appear in DDLC")