# ФОРМА СТАТИСТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import Qt
from PySide6.QtWidgets  import QHeaderView

from L60_form_statistic import C60_FormStatistic


class C70_FormStatistic(C60_FormStatistic):
	""" Форма Статистика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Статистика - {self.workspace.DmDyToString()}")

	# Таблица статистики
	def AdjustTableStatistic_Size(self):
		""" Таблица статистики: Настройка размера """
		self.table_statistic.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

	def AdjustTableStatistic_Sort(self):
		""" Таблица статистики: Сортировка """
		self.table_statistic.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	# Дерево аналитики
	def AdjustTreeAnalytics_Size(self):
		""" Дерево аналитики: Настройка размера """
		self.tree_analytics.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.tree_analytics.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
		self.tree_analytics.header().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
		self.tree_analytics.header().setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
		self.tree_analytics.header().setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)

		self.tree_analytics.setColumnWidth(1, 200)
		self.tree_analytics.setColumnWidth(2, 200)
		self.tree_analytics.setColumnWidth(3, 100)
		self.tree_analytics.setColumnWidth(4, 100)

	def AdjustTreeAnalytics_Sort(self):
		""" Дерево аналитики: Сортировка """
		self.tree_analytics.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	# Вкладки
	def SwitchPagesToFirst(self):
		""" Включение первой вкладки """
		self.tabs_main.setCurrentIndex(0)
