# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QHeaderView

from L60_form_anaytics import C60_FormAnalytics


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика: Механика управления """

	# Список элементов аналитики
	def AdjustListItems_Sort(self):
		""" Список элементов аналитики: Настройка сортировки """
		self.model_items.sort(0, Qt.SortOrder.AscendingOrder)

	# Дерево параметров элемента аналитики
	def AdjustTreeDataItem_Size(self):
		""" Дерево парамеров элемент аналитики: Настройка размеров """
		self.tree_data_item.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.tree_data_item.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

	def AdjustTreeDataItem_Expand(self):
		""" Дерево параметров элемент аналитики: Настройка вложенности """
		self.tree_data_item.expandAll()

	def AdjustTreeDataItem_Color(self):
		""" Дерево параметров элемент аналитики: Настройка цветовой схемы """
		self.model_item.adjustGroupView(True, True, True)
