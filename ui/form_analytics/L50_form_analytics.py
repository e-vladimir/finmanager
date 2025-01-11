# ФОРМА АНАЛИТИКА: МОДЕЛЬ СОБЫТИЙ

from L42_form_analytics import C42_FormAnalytics


class C50_FormAnalytics(C42_FormAnalytics):
	""" Форма Аналитика: Модель событий """

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self): pass

	# Элемент аналитики
	def on_AnalyticsItemSelected(self): pass

	def on_RequestCreateAnalyticsItem(self): pass
	def on_RequestDeleteAnalyticsItem(self): pass
	def on_RequestEditNameAnalyticsItem(self): pass
