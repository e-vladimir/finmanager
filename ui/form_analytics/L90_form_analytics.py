# ФОРМА АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика: Логика управления """

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.InitModelDataItems()
		self.ShowItems()
