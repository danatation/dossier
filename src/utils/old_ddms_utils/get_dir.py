'''
	Returns directories for installing mods, symlinking mods, etc.
	Also python files but that's between me and you ;D
'''
from pathlib import Path
import logging as log
log.basicConfig(level=log.NOTSET)

def get_ddms_dir() -> Path:
	log.debug(f' The root directory is at \"{Path.cwd()}\"')
	return Path.cwd()

def get_work_dir(folder_name: str) -> Path | None:
	work_dir = get_ddms_dir() / folder_name
	if work_dir.exists():
		log.debug(f" work_dir is \"{work_dir}\"")
		return work_dir
	else:
		log.error(f" \"{work_dir}\" does not exist!")
		return None

def get_mod_dir(mod_name: str) -> Path | None:
	mod_path = get_work_dir("mods") / mod_name
	if mod_path.exists():
		patterns = [
			"scripts.*",
			"script.rpy",
			"script.rpyc"
		]
		mod_scripts = [path for pattern in patterns for path in mod_path.rglob(pattern)]
		script_path = mod_scripts[0].parent
		if script_path.stem == "game":
			temp_path = script_path.parent
			if temp_path.glob("*.py"):
				mod_path = temp_path
			else:
				mod_path = script_path
		else:
			# mod_path = Path.cwd()
			print("Penis") # i don't remember what scenario this was for
	else:
		log.error(f' The mod folder doesn\'t exist!')
	return mod_path

def get_mod_script(mod_name: str) -> str:
	mod_path = get_mod_dir(mod_name)
	if mod_path.exists():
		py_scripts = sorted(mod_path.glob("*.py"))
		py_scr_names = [i.name for i in py_scripts]			
		if "DDLC.py" in py_scr_names:
			py_scr_names.remove("DDLC.py")
	try:
		return py_scr_names[0]
	except IndexError:
		return "DDLC.py"