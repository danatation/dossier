from pathlib import Path
from .. import log

from src.utils.game_config import parse_game_config
from src.utils.game_info import get_resolved_game_path

import msgpack

def cache_library() -> None:
	cache_path = Path.cwd() / 'cache'
	cache_path.mkdir(exist_ok=True)
	library_dict = {}

	ddlc_config = parse_game_config(Path.cwd() / 'base')
	library_dict['base'] = ddlc_config['info']['nickname']

	mods_path = Path.cwd() / 'mods'
	for game in sorted(mods_path.glob('*')):
		game_config = parse_game_config(get_resolved_game_path(game))
		library_dict[game.name] = game_config['info']['nickname']

	log.debug(f'library_dict: "{library_dict}')

	with open(cache_path / 'library.msgpack', 'wb') as f:
		library_cache = msgpack.packb(library_dict)
		f.write(library_cache)

def parse_cache(cache_type: str) -> dict:
	cache_path = Path.cwd() / 'cache'
	msgpack_path = cache_path / f'{cache_type}.msgpack'

	if msgpack_path.exists():
		with open(msgpack_path, 'rb') as f:
			binary_data = f.read()
			return msgpack.unpackb(binary_data)
