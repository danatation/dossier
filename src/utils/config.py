import time
from pathlib import Path

from tomlkit import comment, document, dump, table


def make_dossier_config() -> None:
	doc = document()
	doc.add(comment('This file was autogenerated by Dossier. Edit with causion!'))
	doc.add(comment('https://github.com/drunkromanian/dossier'))

	options = table()
	options.add('symlink_base_files', False)
	options.add('renpy_save_dir', True)
	options.add('skip_splash_scr', False)
	options.add('skip_main_menu', False)
	options.add('discord_rpc', False)

	doc.add('default_options', options)

	config_path = Path.cwd() / 'dossier.toml'
	with open(config_path, 'w') as f:
		dump(doc, f)

def make_game_config(game_path: Path) -> None:
	doc = document()
	doc.add(comment('This file was autogenerated by Dossier. The options with "" are taken from Dossier\'s default settings. Edit with causion!'))
	doc.add(comment('https://github.com/drunkromanian/dossier'))

	info = table()
	info.add('date_added', time.time())
	info.add('last_played', 0)
	info.add('playtime', 0)
	doc.add('info', info)

	options = table()
	options.add('nickname', '')
	options.add('renpy_save_dir', '')
	options.add('renpy_save_slot', 1)
	options.add('custom_save_dir', '')
	options.add('skip_splash_scr', '')
	options.add('skip_main_menu', '')
	options.add('discord_rpc', '')
	doc.add('options', options)

	config_path = game_path / 'game' / 'dossier.toml'
	with open(config_path, 'w') as f:
		dump(doc, f)