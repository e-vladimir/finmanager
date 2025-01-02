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

	# Дерево структуры статистики
	def AdjustTreeStatisticStruct_Size(self):
		""" Дерево структуры статистики: Настройка размера """
		self.tree_statistic_struct.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.tree_statistic_struct.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
		self.tree_statistic_struct.header().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

		self.tree_statistic_struct.setColumnWidth(1, 100)
		self.tree_statistic_struct.setColumnWidth(2, 100)

	def AdjustTreeStatisticStruct_Sort(self):
		""" Дерево структуры статистики: Сортировка """
		self.tree_statistic_struct.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def ExpandTreeStatisticStruct(self):
		""" Раскрытие дерева структуры статистики """
		if self._processing_item is None: return

		self.tree_statistic_struct.expand(self._processing_item.index())

	# Вкладки
	def SwitchPagesToFirst(self):
		""" Включение первой вкладки """
		self.tabs_main.setCurrentIndex(0)
