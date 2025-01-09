# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui      import QCursor, Qt

from L60_form_analytics import C60_FormAnalytics


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
		"""  """
		pass

	def AdjustMenuItems_Text(self):
		"""  """
		pass

	# Список элементов аналитики
	def AdjustListItems_Sort(self):
		""" Список элементов аналитики: Настройка сортировки """
		self.model_items.sort(0, Qt.SortOrder.AscendingOrder)
