from pathlib import Path
from .. import log
import sys

from src import rpatool
from src.unrpyc.utils import decompile_rpyc
	 
def extract_game_assets(game_path: Path) -> None:
	assets_path = game_path / 'game' / 'assets' 
	assets_path.mkdir(exist_ok=True)

	renpy_archives = sorted(game_path.rglob('*.rpa'))
	if not game_path.name == 'base':
		renpy_archives = [archive for archive in renpy_archives if 'images.rpa' not in str(archive) and 'fonts.rpa' not in str(archive) and 'audio.rpa' not in str(archive)]

	for archive_path in renpy_archives:
		archive = rpatool.RenPyArchive(file=archive_path)
		subdir_path = assets_path / archive_path.stem
		subdir_path.mkdir(exist_ok=True)
		archive_files = archive.list()
		for file in archive_files:
			data = archive.read(file)
			file_path = subdir_path / file
			file_path.parent.mkdir(parents=True, exist_ok=True)
			file_path.touch()
			with open(subdir_path / file, 'wb') as f:
				f.write(data)
			if file_path.suffix == '.rpyc':
				log.debug(f'file_name: {file_path.name}')
				try:
					decompile_rpyc(file_path)
				except Exception:
					log.warn(f'Couldn\'t decompile. Skipping...')
				else:
					log.debug(f'Succesfully decompiled {file_path.stem}!')