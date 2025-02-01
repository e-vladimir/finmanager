# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import Qt
from PySide6.QtGui      import QCursor
from PySide6.QtWidgets  import QHeaderView

from L00_form_analytics import ANALYTICS
from L60_form_anaytics  import C60_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


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

	def ProcessingTreeDataItem_DbClick(self):
		""" Обработка двойного клика по дереву параметров элемента аналитики """
		match self._processing_ido:
			case ANALYTICS.INCLUDE: self.on_RequestEditAnalyticsItemInclude()
			case ANALYTICS.EXCLUDE: self.on_RequestEditAnalyticsItemExclude()

	# Меню Элементы аналитики
	def AdjustMenuItems_Enable(self):
		""" Настройка доступности меню Элементы аналитики """
		flag_selected = bool(self._processing_ido)

		self.action_items_edit_item_name.setEnabled(flag_selected)
		self.action_items_delete_item.setEnabled(flag_selected)

	def AdjustMenuItems_Text(self):
		""" Настройка текстов меню Элементы аналитики """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		self.submenu_items_item.setTitle(analytics_item.Name() or "Элемент аналитики")

	def ShowMenuItems(self):
		""" Отображение меню Элементы аналитики """
		self.menu_items_items.exec_(QCursor().pos())
