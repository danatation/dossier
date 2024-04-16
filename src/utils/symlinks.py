from pathlib import Path
from utils.dirs import *
from utils.mods import *
import logging as log
log.basicConfig(level=log.NOTSET)

def symlink_mod(mod_name: str, copy: bool=False) -> None:
	# symlink every file from the ddlc folder into the mod folder
	# do not overwrite anything
	# if the file is a directory, mkdir it 
	# if the file is a .py file, copy it (the python script does not like symlinks all that much)
	# if the file is called scripts.rpa, do not do anything (ren'py 6 compat)
	ddlc_dir = get_work_dir('base')	
	mod_dir = get_mod_dir(mod_name)
	ddlc_files = sorted(ddlc_dir.rglob('*'))
	
	for path in ddlc_files:
		path_parts, base_parts = path.parts, ddlc_dir.parts		
		common_path = path_parts[len(base_parts):]
		target_path = mod_dir / Path(*common_path)
		log.debug(f' path: {path}')
		log.debug(f' target_path: {target_path}')
		if not target_path.exists():
			if target_path.name == 'scripts.rpa':
				continue
			elif target_path.name == f'{get_launch_script(mod_name).name}':
				shutil.copy(path, target_path)
			elif path.is_dir():
				target_path.mkdir()
			else:
				target_path.symlink_to(path)

def delink_mod(mod_name: str) -> None:
	# does not work if ddlc files have been copied instead of linked
	# it also does not remove folders

	ddlc_dir = get_work_dir("game")
	mod_dir = get_mod_dir(mod_name)

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