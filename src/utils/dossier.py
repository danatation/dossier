from pathlib import Path
import logging as log

import tomlkit
from tomlkit import document, comment, table, dump

def check_install() -> None:
	mods_folder = Path.cwd() / 'mods'
	base_folder = Path.cwd() / 'base'
	config_path = Path.cwd() / 'config.toml'

	if not mods_folder.exists() or not base_folder.exists() or not config_path.exists():
		log.info('Setting up Dossier\'s environment...')
		
		mods_folder.mkdir(exist_ok=True)
		base_folder.mkdir(exist_ok=True)
		cache_folder.mkdir(exist_ok=True)
		log.debug('Created "mods/" and "base/"')

		if not config_path.exists():
			create_dossier_config()

	if sorted(base_folder.glob('*')) == []:
		log.error('Please download DDLC from https://teamsalvato.itch.io/ddlc and extract the ZIP file to the "base" folder in order for Dossier to function!')
		quit()

def create_dossier_config() -> None:
	doc = document()
	doc.add(comment('The main config file for Dossier. Edit with caution!'))
	settings = table()
	settings.add('symlink_ddlc_to_mods', False)
	doc.add('settings', settings)
	default_options = table()
	default_options.add('renpy_save_dir', False)
	default_options.add('skip_splash_scr', False)
	default_options.add('skip_main_menu', False)
	default_options.add('discord_rpc', False)
	doc.add('default_options', default_options)

	config_path = Path.cwd() / 'config.toml'
	with open(config_path, 'w') as f:
		tomlkit.dump(doc, f)	
	log.debug('Created "config.toml"')