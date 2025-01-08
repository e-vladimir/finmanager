# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import Qt
from PySide6.QtWidgets  import QHeaderView

from L60_form_analytics import C60_FormAnalytics


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка """
		self.setWindowTitle(f"Аналитика - {self.workspace.DmDyToString()}")

	# Таблица элементов аналитики
	def AdjustTableItems_Size(self):
		""" Таблица элементов аналитики: Настройка размера """
		self.table_items.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_items.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
		self.table_items.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

		self.table_items.setColumnWidth(1, 200)
		self.table_items.setColumnWidth(2, 200)

	def AdjustTableItems_Sort(self):
		""" Таблица элементов аналитики: Сортировка """
		self.table_items.sortByColumn(0, Qt.SortOrder.AscendingOrder)
