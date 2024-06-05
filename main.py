from src.utils import dossier
from src.utils import game_config
from src.utils import game_info
from src.utils import game_utils
from src.utils import cache
from src.utils import game_assets
from src.utils import spreadsheet

from pathlib import Path	

dossier.check_install()

game_assets.extract_game_assets(Path.cwd() / 'base')
