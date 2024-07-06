def clear_layout(self, layout):
	if layout is not None:
		while layout.count():
			item = layout.takeAt(0)
			widget = item.widget()
			if widget is not None:		
				widget.deleteLater()
			else:
				self.clear_layout(item.layout())