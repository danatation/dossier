import logging, asyncio
from pathlib import Path

import tomlkit
import msgpack

from utils.directories import get_work_directory, list_directories, get_mod_directory
from utils.game_info import parse_game_config

logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

async def async_parse_game_config(game_dir: Path):
	'''parse_game_config() but asynchronous'''
	
	return parse_game_config(game_dir)

async def update_library_cache() -> None:
	'''condenses your mods and config files into a dictionary for msgpack to make into a convienent little cache thing'''

	mod_dirs = await list_directories(get_work_directory('mods'))
	cache_dict = {}
	cache_dict['base'] = await async_parse_game_config(get_work_directory('base'))

	for mod in mod_dirs:
		config_dict = await async_parse_game_config(get_mod_directory(mod))
		cache_dict[mod.name] = config_dict

	cache_path = get_work_directory('cache') / 'library.msgpack'
	
	with open(cache_path, 'wb') as f:
		msgpack_data = msgpack.packb(cache_dict)
		f.write(msgpack_data)

def read_library_cache() -> dict:
	'''unpacks library cache'''

	cache_path = get_work_directory('cache') / 'library.msgpack'

	with open(cache_path, 'rb') as f:
		binary_data = f.read()
		return msgpack.unpackb(binary_data)