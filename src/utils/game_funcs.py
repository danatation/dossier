import subprocess
import time
from os import environ
from pathlib import Path
from multiprocessing import Process

import discordrpc
import psutil

from src import log
from src.utils.return_funcs import (return_exec_path, return_game_config,
                                    return_py_script)


def launch_game(game_path: Path) -> None:
	game_config = return_game_config(game_path)
	options = game_config['options']
	env = environ.copy()
	save_path = None

	args = [str(return_exec_path(game_path))]
	py_script = return_py_script(game_path)
	if py_script.name == 'DDLC.py':
		args.extend(['-EO', str(py_script)])

	if options['renpy_save_slot'] > 1:
		save_slot = options['renpy_save_slot']
	else:
		save_slot = ''

	if options['renpy_save_dir']:
		save_path = game_path / 'game' / f'saves{save_slot}'

	custom_save_path = options['custom_save_dir']
	if custom_save_path:
		save_path = custom_save_path

	if save_path:
		args.extend(['--savedir', str(save_path)])

	if options['skip_splash_scr']:
		env['RENPY_SKIP_SPLASHSCREEN'] = '1'

	if options['skip_main_menu']:
		env['RENPY_SKIP_MAIN_MENU'] = '1'

	if options['discord_rpc']:
		# TODO this is easier to do in pyside
		...

	subprocess.run(args, env=env)

def start_rpc() -> None:
	rpc = discordrpc.RPC(app_id=1252869123042447412)

	rpc.set_activity(
		# state='Running',
		details=f'Playing game',
		ts_start=int(time.time()),
		large_image='big_icon',
		large_text='Dossier'
	)

	rpc.run()