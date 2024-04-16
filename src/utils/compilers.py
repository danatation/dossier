from pathlib import Path
import logging as log
import subprocess
log.basicConfig(level=log.NOTSET)

''' Compiles the Qt Designer .ui file on startup to make my life slightly easier '''

def compile_ui(ui_path:Path, uic_name:str) -> None:
	compiler_path = Path.home() / '.local' / 'bin' / 'pyside6-uic'
	ui_path = Path(ui_path)
	
	if compiler_path.exists() and ui_path.exists():
		uic_path = ui_path.parent / uic_name
		subprocess.run([compiler_path, ui_path, '-o', uic_path, '--from-imports'])
	else:
		if not compiler_path.exists():
			log.error(f' compiler_path: {compiler_path} does not exist!')
		if not ui_path.exists():
			log.error(f' ui_path: {ui_path} does not exist!')

def compile_qrc(qrc_path:Path, py_name:str) -> None:
	compiler_path = Path.home() / '.local' / 'bin' / 'pyside6-rcc'
	qrc_path = Path(qrc_path)

	if compiler_path.exists() and qrc_path.exists():
		py_path = qrc_path.parent / py_name
		subprocess.run([compiler_path, qrc_path, '-o', py_path])
	else:
		if not compiler_path.exists():
			log.error(f' compiler_path: {compiler_path} does not exist!')
		if not qrc_path.exists():
			log.error(f' qrc_path: {qrc_path} does not exist!')