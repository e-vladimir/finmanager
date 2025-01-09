# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui      import QCursor, Qt

from L60_form_analytics import C60_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка """
		self.setWindowTitle(f"Аналитика - {self.workspace.DmDyToString()}")

	# Меню списка элементов аналитики
	def ShowMenuItems(self):
		""" Отображение меню элементов аналитики """
		self.menu_items.exec_(QCursor().pos())

	def AdjustMenuItems_Enable(self):
		""" Меню элементов аналитики: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_item_delete_item.setEnabled(flag_selected)

	def AdjustMenuItems_Text(self):
		""" Меню элементов аналитики: Настройка текста """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		self.submenu_items_item.setTitle(analytics_item.Name() or "Элемент аналитики")

	# Список элементов аналитики
	def AdjustListItems_Sort(self):
		""" Список элементов аналитики: Настройка сортировки """
		self.model_items.sort(0, Qt.SortOrder.AscendingOrder)
