# ФОРМА ФИНАНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ
from PySide6.QtCore import Qt
from PySide6.QtGui         import QCursor

from L60_form_finanalitics import C60_FormFinanalitics


class C70_FormFinanalitics(C60_FormFinanalitics):
	""" Форма Финаналитика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финаналитика - {self.workspace.DmDyToString()}")

	# Дерево параметров
	def AdjustTreeOptions_Expand(self):
		""" Дерево параметров: Настройка раскрытия """
		self.tree_options.expandAll()

	def AdjustTreeOptions_Color(self):
		""" Дерево параметров: Настройка цветов """
		self.model_options.setGroupsView(True, False, False)

	# Меню финаналитики
	def ShowMenuFinanalitics(self):
		""" Отобразить меню финаналитики """
		self.menu_finanalitics.exec(QCursor().pos())

	# Вкладка Анализ месяца
	def AdjustPageDm_Text(self):
		""" Вкладка месяц: Настройка текста """
		self.tabs_main.setTabText(1, f"Анализ {self.workspace.DmDyToString()}")

	# Вкладки
	def SwitchTabsMainToOptions(self):
		""" Переключение вкладки на Параметры """
		self.tabs_main.setCurrentIndex(0)

	# Таблица данных за месяц
	def AdjustTableDataDm_Size(self):
		""" Таблица данных за месяц: Настройка размера """
		self.table_data_dm.resizeColumnsToContents()

		sizes_optimal = [200, 100, 100, 100]
		for index_col, size_optimal in enumerate(sizes_optimal):
			col_size : int = self.table_data_dm.columnWidth(index_col)
			col_size       = max(col_size, size_optimal)

			self.table_data_dm.setColumnWidth(index_col, col_size)

	def AdjustTableDataDm_Align(self):
		""" Таблица данных за месяц: Настройка выравнивания """
		for index_row in range(self.model_data_dm.rowCount()):
			try:
				item_data = self.model_data_dm.item(index_row, 0)
				item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

				item_data = self.model_data_dm.item(index_row, 1)
				item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

				item_data = self.model_data_dm.item(index_row, 2)
				item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

				item_data = self.model_data_dm.item(index_row, 3)
				item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
			except: pass
