from PySide6.QtCore import QObject, QRunnable, Signal, Slot
from PySide6.QtWidgets import QLineEdit, QPushButton, QTabWidget, QToolButton


def clear_layout(self, layout):
	if layout is not None:
		while layout.count():
			item = layout.takeAt(0)
			widget = item.widget()
			if widget is not None:		
				widget.deleteLater()
			else:
				self.clear_layout(item.layout())

def connect_attributes(self, connect_qpushbutton: bool = True, connect_qtabwidget: bool = False, connect_qtoolbutton: bool = False, connect_qlineedit: bool = False):
	attributes = vars(self.ui)
	for attribute_name, attribute in attributes.items():
		if isinstance(attribute, QPushButton) and connect_qpushbutton:
			attribute.clicked.connect(self.button_action)
		if isinstance(attribute, QTabWidget) and connect_qtabwidget:
			attribute.currentChanged.connect(self.tab_action)
		if isinstance(attribute, QToolButton) and connect_qtoolbutton:
			attribute.clicked.connect(self.button_action)
		if isinstance(attribute, QLineEdit) and connect_qlineedit:
			attribute.textChanged.connect(self.line_action)
			
class Worker(QRunnable):

	def __init__(self, fn, *args, **kwargs):
		super(Worker, self).__init__()
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signal = WorkerSignal()

	@Slot()
	def run(self):
		try:
			self.fn(*self.args, **self.kwargs)
		finally:
			self.signal.emit_finished()

class WorkerSignal(QObject):
	finished = Signal()

	def emit_finished(self):
		self.finished.emit()