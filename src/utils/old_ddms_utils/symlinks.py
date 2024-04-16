'''
	Symlinks the DDLC base files to the desired mod instead of copying them to save storage
	Problems arise when moving the DDMS directory though since pathlib doesn't support relative symlinks
'''
from pathlib import Path
import logging as log
log.basicConfig(level=log.NOTSET)

def symlink_mod(mod_name: str) -> None:
	ddlc_path = get_work_dir("game")
	mod_path = get_mod_dir(mod_name)
	
	for path in ddlc_path.rglob("*"):
		ddlc_tuple, path_tuple = ddlc_path.parts, path.parts
		gen_tuple = path_tuple[len(ddlc_tuple):]
		gen_path = str("")
		for i in gen_tuple:
			gen_path += f"{i}/"
		target = mod_path / gen_path
		
		if not path.is_symlink() and not target.exists():
			if path.is_dir():
				target.mkdir()
				log.info(f" Directory \"{target}\" has been made")
			elif path.is_file() and not gen_tuple[-1] == "scripts.rpa" and not gen_tuple[-1] == get_mod_script(mod_name):
				target.symlink_to(path)
				log.info(f" Symlink \"{target}\" has been made")
			elif not gen_tuple[-1] == "scripts.rpa":
				shutil.copy(path, target)
				log.info(f" Python script \"{get_mod_script(mod_name)}\" has been copied")
			else:
				log.info(f" Skipping Ren'py archive \"{target}\" for Ren'py 6 mod support")
		else:
			log.warning(f" The target \"{target}\" either already exists or is a symlink")

def unsymlink_mod(mod_name: str) -> None:
	ddlc_path = get_work_dir("game")
	mod_path = get_mod_dir(mod_name)

	# Does NOT remove folders. It would make too much effort for it to be worth it

	for path in mod_path.rglob("*"):
		mod_tuple, path_tuple = mod_path.parts, path.parts
		gen_tuple = path_tuple[len(mod_tuple):]
		gen_path = str("")
		for i in gen_tuple:
			gen_path += f"{i}/"
		target = ddlc_path / gen_path
		resolved_link = path.resolve()
		if resolved_link == target and not target.is_symlink or not resolved_link.exists():
			log.info(f" target IS equal to resolved_link")
			path.unlink()
		else:
			log.info(f" {target} does not appear in DDLC")