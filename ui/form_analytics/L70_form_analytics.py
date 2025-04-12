# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 11 апр 2025

from PySide6.QtCore     import Qt

from L60_form_analytics import C60_FormAnalytics


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Аналитика данных - {self.Workspace.DmDyToString()}")


	# Список элементов аналитики
	def AdjustListItems_Sort(self):
		""" Настройка сортировки списка элементов аналитики """
		self.ModelDataItems.sort(0, Qt.SortOrder.AscendingOrder)
