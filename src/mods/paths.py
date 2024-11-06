from pathlib import Path


def find_relative_path(path: Path) -> Path | None:
	rp_files = sorted(path.rglob("*.rp*"))
	game_files = []

	for rp_file in rp_files:
		if '00' in rp_file.stem:  # generic engine file
			continue
		if rp_file.suffix == 'rpyb':  # cache files
			continue
		if 'rpym' in rp_file.suffix:  # .rpym files can be compiled (.rypmc)
			continue

		game_files.append(rp_file)

	try:
		return game_files[0].parents[1]
	except IndexError:
		return None



