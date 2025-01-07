# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui      import QCursor
from PySide6.QtWidgets  import QHeaderView

from L60_form_analytics import C60_FormAnalytics


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка """
		self.setWindowTitle(f"Аналитика - {self.workspace.DmDyToString()}")

	# Меню Элементы аналитики
	def AdjustMenuItems_Enable(self):
		""" Меню Элементы аналитики: Настройка доступности """
		pass

	def AdjustMenuItems_Text(self):
		""" Меню Элементы аналитики: Настройка текста """
		pass

	def ShowMenuItems(self):
		""" Отображение меню Элементов аналитики """
		self.menu_items.exec_(QCursor().pos())

	# Таблица элементов аналитики
	def AdjustTableItems_Size(self):
		""" Таблица элементов аналитики: Настройка размера """
		self.table_items.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
