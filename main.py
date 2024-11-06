import os
import sys
import signal
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine


def main():
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()

	signal.signal(signal.SIGINT, signal.SIG_DFL)

	if not os.environ.get('QT_QUICK_CONTROLS_STYLE'):
		os.environ['QT_QUICK_CONTROLS_STYLE'] = 'org.kde.desktop'

	url = QUrl(f'file://{Path.cwd()}/src/qml/main.qml')
	engine.load(url)

	if len(engine.rootObjects()) == 0:
		quit()

	app.exec()


if __name__ == '__main__':
	main()
