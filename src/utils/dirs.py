from pathlib import Path
import logging as log
log.basicConfig(level=log.NOTSET)

def check_dossier_tree(ddms_dir: str) -> int:
	# look in base/ and quit if there's nothing in there 
	base_dir = Path.cwd() / 'base'
	base_files = sorted(base_dir.glob('*'))
	if not base_files:
		return 1

def get_work_dir(folder_name: str) -> Path:
	ddms_dir = Path.cwd() / folder_name
	return ddms_dir if ddms_dir.exists() else 1

def get_mod_dir(mod_name: str) -> Path:
	# tries to find mod script file and then determines the root of the mod

	mod_dir = get_work_dir('mods') / mod_name

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
			log.info(f' mod_dir: {script.parents[1]}')
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

