# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui      import QCursor

from L60_form_analytics import C60_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Аналитика - {self.workspace.DmDyToString()}")

	# Вкладки
	def SwitchTabsToOptions(self):
		""" Переключение на вкладку Параметры """
		self.tabs_data.setCurrentIndex(0)

	# Меню Элементы аналитики
	def AdjustMenuItems_Text(self):
		""" Меню Элементы аналитики: Настройка текста """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		self.submenu_items_item.setTitle(analytics_item.Name() or "Элемент аналитики")

	def AdjustMenuItems_Enable(self):
		""" Меню Элементы аналитики: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_items_delete_item.setEnabled(flag_selected)

	def ShowMenuItems(self):
		""" Меню Элементы аналитики: Отображение """
		self.menu_items.exec_(QCursor().pos())
