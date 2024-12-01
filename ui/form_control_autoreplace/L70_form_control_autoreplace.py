# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtWidgets            import QHeaderView

from L60_form_control_autoreplace import C60_FormControlAutoreplace


class C70_FormControlAutoreplace(C60_FormControlAutoreplace):
	""" Форма Управление автозаменой: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Управление автозаменой")

	# Таблица данных
	def AdjustTableData_Size(self):
		""" Таблица данных: Настройка размера """
		self.table_data.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_data.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.table_data.resizeRowsToContents()

	def AdjustTableData_Color(self):
		""" Таблица данных: Настройка цветов """
		pass
