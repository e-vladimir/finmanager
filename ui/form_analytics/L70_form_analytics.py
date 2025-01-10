# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from L60_form_analytics import C60_FormAnalytics


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
