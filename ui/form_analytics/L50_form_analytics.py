# ФОРМА АНАЛИТИКА: МОДЕЛЬ СОБЫТИЙ

from L42_form_analytics import C42_FormAnalytics


class C50_FormAnalytics(C42_FormAnalytics):
	""" Форма Аналитика: Модель событий """

	# Таблица Элементы аналитики
	def on_RequestProcessingTableItemsDbClick(self): pass

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self): pass

	# Элемент аналитики
	def on_RequestCreateAnalyticsItem(self): pass
	def on_RequestDeleteAnalyticsItem(self): pass

	def on_RequestEditNameAnalyticsItem(self): pass
	def on_RequestEditIncludeAnalyticsItem(self): pass
	def on_RequestExpandIncludeAnalyticsItem(self): pass
	def on_RequestEditExcludeAnalyticsItem(self): pass
	def on_RequestExpandExcludeAnalyticsItem(self): pass
