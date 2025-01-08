# ФОРМА АНАЛИТИКА: ЛОГИКА ДАННЫХ

from L70_form_analytics import C70_FormAnalytics


class C80_FormAnalytics(C70_FormAnalytics):
	""" Форма Аналитика: Логика данных """

	# Элементы аналитики
	def ShowAnalyticsItems(self):
		""" Отображение элементов аналитики """
		for self._processing_ido in self.analytics.Idos(): self.LoadAnalyticsItemInModel()
