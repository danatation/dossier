import json, patoolib, platform, subprocess, shutil, gspread, sys, time
import pandas as pd
from gspread.utils import ValueRenderOption
from pathlib import Path
import logging as log
log.basicConfig(level=log.NOTSET)

def install_mod(archive_path: Path=None, archive_name: str=None, name: str=None, delete_archive: bool=False, skip_filtering: bool=False) -> None:
	# TODO add delete_archive
	# The world would be a better place if Windows would just fuycking let me use these
	# AHEM this just filters the folder name so that the os doesn't freak out
	forbidden_characters: list = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
	forbidden_names: list = [
		'CON', 'PRN', 'AUX', 'NUL',
		'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 	
		'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9', 
	]
	forbidden_patterns: list = forbidden_characters + forbidden_names
	filtered_name: str = ""
	# FUCK YOU BILL GATES
	# You can opt out of the filtering (if you don't have Windows)
	if platform.system() == "Windows":
		skip_filtering = False 
	# FUCK YOU LINUS AND STEVE BUT WAY LESS
	elif not platform.system() == "Windows" and skip_filtering == True:
		forbidden_patterns: list = ["/"] 
	if name:
		filtered_name = "".join([character for character in list(name) if not character in forbidden_patterns])
	
	# Set the path of the archive and check to see if it even exists
	try:
		archive_path = get_work_dir("downloads") / archive_name
	except TypeError:
		log.debug(f' The archive name has not been provided. Moving on')
	else:
		if not archive_path.exists():
			sys.exit(f' The archive "{archive_path}" does not exist! Giving up')
	
	# If no name is provided then make one up using the archive name
	if filtered_name == "":
		filtered_name = "".join([character for character in list(archive_path.stem) if not character in forbidden_patterns])

	# Extract that thang
	mod_path: Path = get_work_dir("mods") / filtered_name
	if mod_path.exists():
		sys.exit(f' "{mod_path}" already exists!')
	else:
		patoolib.extract_archive(str(archive_path), outdir=str(mod_path))

	# Setting up appdata for that thang
	appdata_path: Path = get_work_dir("appdata") / filtered_name
	Path.mkdir(appdata_path, exist_ok=True)
	Path.mkdir(appdata_path / "savedir", exist_ok=True)
	with open(str(appdata_path / "info.json"), 'w') as f:
		f.write('{}')
	set_mod_info(filtered_name, name=name)

def set_mod_info(mod_name: str, name: str=None) -> None:
	mod_info: Path = get_work_dir("appdata") / mod_name / "info.json"
	with open(str(mod_info), 'r') as f:
	# If info.json is empty, add the mod and creation date to it
		if f.read() == "{}":
			if not name:
				name = mod_name
			append_to_json = {
				"modName": name,
				"dateAdded": time.time()
			}
			with open(str(mod_info)) as f:
				data = json.load(f)
				data.update(append_to_json)
			with open(str(mod_info), 'w') as f:
				json.dump(data, f, sort_keys=True, indent=4)
			
def run_mod(mod_name: str, unique_save_folder: bool=True, skip_splash_screen: bool=False, skip_main_menu: bool=False) -> None:
	renpy6, renpy78 = True, False
	global mod_lib_dir

	# This determines the Ren'py version
	mod_path = get_mod_dir(mod_name)
	if mod_path.exists():
		py_scripts = sorted(mod_path.glob("*.py"))
		py_scr_names = [i.name for i in py_scripts]			
		if "DDLC.py" in py_scr_names:
			py_scr_names.remove("DDLC.py")
			if not py_scr_names == []:
				py_name, pyExt = py_scr_names[0].split(".")
				renpy6 = False
				renpy78 = True
			else:
				py_name = "DDLC"
		
	# This determines what operating system you have
	if platform.system() == "Linux" or "Darwin":
		os = "linux-"
	elif platform.system() == "Windows":
		os = "windows-"
	else:
		log.error(" Operating System could not be determined!")
	if platform.machine() == "x86_64":
		os += "x86_64"
	elif platform.machine() == "i686":
		os += "i686"
	else:
		log.error(" Architecture could not be determined!")
	log.debug(f" \"os\" has been set to \"{os}\"")

	# This determines what folder the executable is in
	if renpy6:
		if Path(mod_path / f"lib/{os}/").exists():
			mod_lib_dir = mod_path / f"lib/{os}/"
	if renpy78:
		if Path(mod_path / f"lib/py2-{os}/").exists():
			mod_lib_dir = mod_path / f"lib/py2-{os}/"
		elif Path(mod_path / f"lib/{os}/").exists():
			mod_lib_dir = mod_path / f"lib/{os}/"
			if Path(mod_path / f"lib/{os}/lib/").exists():
				shutil.rmtree(mod_lib_dir / "lib/")
			# The game will literally not launch if we don't do this
		if Path(mod_path / f"lib/py3-{os}/").exists():
			mod_lib_dir = mod_path / f"lib/py3-{os}/"

	# This runs that bitch
	if "i686" in os:
		log.warning(" Literally no mod supports this. You're on your own. Sorry!")
	elif "windows" in os:
		mod_exec = mod_lib_dir / "pythonw.exe"
	else:
		mod_exec = mod_lib_dir / py_name
		try:
			mod_exec.chmod(mod_exec.stat().st_mode | 0o111)
		except FileNotFoundError:
			# Assuming that the DDMS directory has moved
			unsymlink_mod(mod_name)
			symlink_mod(mod_name)

	if unique_save_folder:
		save_folder = get_work_dir("appdata") / mod_name # Path("/home/bulb/Games/Doki Doki Mod Swapper/appdata/Exit Music Redux 1.1")
		# save_folder.mkdir(exist_ok=True)
	else:
		save_folder = str("")
	if skip_splash_screen:
		splash_screen = "RENPY_SKIP_splash_screen=1"
	else:
		splash_screen = str()
	if skip_main_menu:
		main_menu = "RENPY_SKIP_MAIN_MENU=1"
	else:
		main_menu = str("")

	if renpy6:
		subprocess.run([mod_exec, "-EO", f"{mod_path}/DDLC.py", "--savedir", str(save_folder)], check=True)
	else:
		subprocess.run([mod_exec, "--savedir", str(save_folder)], check=True)

if __name__ == "__main__":
	install_mod(archive_name="Exit Music Redux 1.1.zip", name="Exit Music: Redux")