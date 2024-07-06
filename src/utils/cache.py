from pathlib import Path

import msgpack

from src.utils.return_funcs import return_game_config, return_resolved_path


def cache_library() -> None:
	library = {}

	base_path = Path.cwd() / 'base'
	config = return_game_config(base_path)
	library['base'] = config

	mods_path = Path.cwd() / 'mods'
	mod_folders = sorted(mods_path.glob('*'))
	for path in mod_folders:
		resolved_path = return_resolved_path(path)
		config = return_game_config(resolved_path)
		library[path.name] = config

	msgpack_path = Path.cwd() / 'cache' / 'library.msgpack'
	with open(msgpack_path, 'wb') as f:
		msgpack.dump(library, f)