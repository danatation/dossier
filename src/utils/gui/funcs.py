from PySide6.QtWidgets import QPushButton, QTabWidget, QToolButton, QLineEdit

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