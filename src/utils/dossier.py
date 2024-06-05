from pathlib import Path
import logging as log

from src.utils.game_config import create_dossier_config

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