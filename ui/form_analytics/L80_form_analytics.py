# ФОРМА АНАЛИТИКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 11 апр 2025

from L70_form_analytics import C70_FormAnalytics


class C80_FormAnalytics(C70_FormAnalytics):
	""" Форма Аналитика данных: Логика данных """

	# Список элементов аналитики
	def LoadAnalyticsItems(self):
		""" Загрузка элементов аналитики в модель данных """
		for self.processing_ido in self.Analytics.Idos(): self.LoadAnalyticsItemInModel()
