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
