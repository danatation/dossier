from pathlib import Path
from src.mods import Mod


def main():
	emr_path = Path.cwd() / 'mods' / 'Exit Music Redux 1.1'
	emr = Mod(rpath=emr_path, name='Exit Music: Redux')
	print(emr.apath)
	print(emr.find_codename())
	print(emr.find_exec_path())
	emr.run()


if __name__ == '__main__':
	main()