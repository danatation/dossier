from pathlib import Path
import json, patoolib, platform, logging, subprocess, shutil, gspread
import pandas as pd
from utils import *
from gspread.utils import ValueRenderOption
logging.basicConfig(level=logging.NOTSET)

def get_work_dir(folder_name: str) -> Path:
	root_dir = get_root_dir()
	work_dir = root_dir / folder_name

	if work_dir.exists():
		logging.info(f" work_dir is \"{work_dir}\"")
		return work_dir
	else:
		logging.error(f" \"{work_dir}\" does not exist!")

def get_mod_dir(mod_name: str) -> Path:
	mod_path = get_work_dir("mods") / mod_name
	if mod_path.exists():
		patterns = [
			"scripts.*",
			"script.rpy",
			"script.rpyc"
		]
		mod_scripts = [path for pattern in patterns for path in Path(mod_path).rglob(pattern)]
		script_loc = mod_scripts[0].parent
		if script_loc.stem == "game":
			temp_path = script_loc.parent
			if temp_path.glob("*.py"):
				mod_path = temp_path
			else:
				mod_path = script_loc
		else:
			# mod_path = Path.cwd()
			print("Penis") # i don't remember what scenario this was for
	return mod_path

def get_spreadsheet() -> None:
	gc = gspread.service_account()
	spreadsheet = gc.open_by_key("1lgQD8o7qhdWmrwdJjbRv3u_bwdrXmpOzaixWFzLR8r4")
	worksheet = spreadsheet.get_worksheet(1)
	modlist = worksheet.get_all_values(value_render_option=ValueRenderOption.formula)
	url = "https://sheets.googleapis.com/v4/spreadsheets/" + "1lgQD8o7qhdWmrwdJjbRv3u_bwdrXmpOzaixWFzLR8r4" + "?fields=sheets&ranges=" + "Mod List"
	res = requests.get(url, headers={"Authorization": "Bearer " + access_token})
	obj = res.json()

	if 'merges' in obj['sheets'][0].keys():
		for e in obj['sheets'][0]['merges']:
			value = values[e['startRowIndex']][e['startColumnIndex']]
			rows = len(values)
			if rows < e['endRowIndex']:
				for i in range(0, e['endRowIndex'] - rows):
					values.append([''])
			for r in range(e['startRowIndex'], e['endRowIndex']):
				cols = len(values[r])
				if cols < e['endColumnIndex']:
					values[r].extend([''] * (e['endColumnIndex'] - cols))
				for c in range(e['startColumnIndex'], e['endColumnIndex']):
					values[r][c] = value
		
	with open(get_work_dir("downloads") / "modlist.json", "w") as json_file:
		json.dump(modlist, json_file)

def get_from_spreadsheet(mod_name: str, collumn: str) -> str:
	collumn_offset = {
		"mod_name": 0,
		"logo": 1,
		"downloadLink": 2,
		"downloadLinkAndroid": 3,
		"author": 4,
		"genre": 5,
		"focus": 6,
		"description": 7,
		"length": 8,
		"status": 9,
		"additionalNotes": 10,
		"releaseDate": 11
	}
	hyperlink_regex = r'=HYPERLINK\("(.*?)", ?"(.*?)"\)' # thanks github issues
	image_regex = r'=IMAGE\("(.*?)", ?"(.*?)"\)'

	modlist_file = get_work_dir("downloads") / "modlist.json"
	if not modlist_file.exists():
		logging.error(f" The DDLC Mod List Spreadsheet has not been found. Please download it again")
	modlist = pd.read_json(str(modlist_file))
	
	# searchResults = modlist[modlist.astype(str).apply(lambda row: mod_name in row, axis=1)]
	# print(searchResults)
	# print( modlist.loc[mod_name] )

def install_mod(archive_path: str=None, archive_name: str=None, name: str=None, delete_archive=False) -> None:
	global mod_folder, mod_name
	if archive_path:
		archive_path = Path(archive_path)

	try:
		archive_path.exists()
	except AttributeError:
		if not archive_path:
			logging.debug(" archive_path has not been selected. Moving onto archive_name")
		else:
			logging.warning(" archive_path does not exist!")
	else:
		mod_folder = get_work_dir("mods") / archive_path.stem
		if name:
			mod_folder = get_work_dir("mods") / name
			mod_name = name
		else:
			mod_folder = get_work_dir("mods") / archive_path.stem
			mod_name = archive_path.stem
		logging.info(f" mod_folder is \"{mod_folder}\"")
		logging.info(f" mod_name is \"{mod_name}\"")
	
	if archive_name:
			download_dir = get_work_dir("downloads")
			archive_path = download_dir / archive_name
			logging.info(f" archive_path is \"{archive_path}\"")
			
			if archive_path.exists():
				if name:
					mod_folder = get_work_dir("mods") / name
					mod_name = name
				else:
					mod_folder = get_work_dir("mods") / archive_path.stem
					mod_name = archive_path.stem
				logging.info(f" mod_folder is \"{mod_folder}\"")
				logging.info(f" mod_name is \"{mod_name}\"")
			else:
				logging.warning(" archive_path does not exist!")

	if not mod_folder.exists():
		patoolib.extract_archive(str(archive_path), outdir=str(mod_folder))
		if delete_archive:
			archive_path.unlink()
			logging.debug(f" {mod_name}'s archive has been removed")
	else:
		logging.error(f" {mod_name} already exists!")

def get_mod_script(mod_name: str) -> str:
	mod_path = get_mod_dir(mod_name)
	if mod_path.exists():
		py_scripts = sorted(mod_path.glob("*.py"))
		py_scr_names = [i.name for i in py_scripts]			
		if "DDLC.py" in py_scr_names:
			py_scr_names.remove("DDLC.py")
	try:
		return py_scr_names[0] #.split(".", -1)[0]
	except IndexError:
		return "DDLC.py"

def swap_mod(mod_name: str) -> None:
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
				logging.info(f" Directory \"{target}\" has been made")
			elif path.is_file() and not gen_tuple[-1] == "scripts.rpa" and not gen_tuple[-1] == get_mod_script(mod_name):
				target.symlink_to(path)
				logging.info(f" Symlink \"{target}\" has been made")
			elif not gen_tuple[-1] == "scripts.rpa":
				shutil.copy(path, target)
				logging.info(f" Python script \"{get_mod_script(mod_name)}\" has been copied")
			else:
				logging.info(f" Skipping Ren'py archive \"{target}\" for Ren'py 6 mod support")
		else:
			logging.warning(f" The target \"{target}\" either already exists or is a symlink")

def unswap_mod(mod_name: str) -> None:
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
			logging.info(f" target IS equal to resolved_link")
			path.unlink()
		else:
			logging.info(f" {target} does not appear in DDLC")
			
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
		logging.error(" Operating System could not be determined!")
	if platform.machine() == "x86_64":
		os += "x86_64"
	elif platform.machine() == "i686":
		os += "i686"
	else:
		logging.error(" Architecture could not be determined!")
	logging.debug(f" \"os\" has been set to \"{os}\"")

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
	# swap_mod(mod_name)
	if "i686" in os:
		logging.warning(" Literally no mod supports this. You're on your own. Sorry!")
	elif "windows" in os:
		mod_exec = mod_lib_dir / "pythonw.exe"
	else:
		mod_exec = mod_lib_dir / py_name
		try:
			mod_exec.chmod(mod_exec.stat().st_mode | 0o111)
		except FileNotFoundError:
			# Assuming that the DDMS directory has moved
			unswap_mod(mod_name)
			swap_mod(mod_name)

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
		subprocess.run([mod_exec, "-EO", f"{mod_path}/DDLC.py", "--savedir"])
	else:
		subprocess.run([mod_exec, "--savedir", str(save_folder)], check=True)