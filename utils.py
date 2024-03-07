from funcs import *

def get_root_dir() -> Path:
	if platform.system() == "Linux":
		rootDir = Path.home() / ".local/share/doki-doki-mod-swapper/"
		logging.debug(f" rootDir is \"{rootDir}\"")
		if rootDir.is_symlink():
			rootDir = rootDir.readlink()
			logging.debug(f" rootDir is a symlink and is \"{rootDir}\"")
		return rootDir

