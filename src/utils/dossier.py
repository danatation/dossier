from pathlib import Path

import tomlkit


def check_install() -> None:
	base_folder = Path.cwd() / 'base'

	if not base_folder.exists() or not base_folder.is_dir() or not sorted(base_folder.glob('*')):
		setup_dossier()

	config_path = Path.cwd() / 'dossier.toml'
	with open(config_path, 'rb') as f:
		config = tomlkit.load(f)
	# TODO make it check if the config file is valid or not
	if len(config) < 1:
		setup_dossier()

def setup_dossier() -> None:
	...