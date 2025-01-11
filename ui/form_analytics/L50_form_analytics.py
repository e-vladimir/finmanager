# ФОРМА АНАЛИТИКА: МОДЕЛЬ СОБЫТИЙ

from L42_form_analytics import C42_FormAnalytics


class C50_FormAnalytics(C42_FormAnalytics):
	""" Форма Аналитика: Модель событий """

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self): pass

	# Меню Параметры
	def on_RequestShowMenuOptions(self): pass

	# Элемент аналитики
	def on_AnalyticsItemSelected(self): pass

	def on_RequestCreateAnalyticsItem(self): pass
	def on_RequestDeleteAnalyticsItem(self): pass
	def on_RequestEditNameAnalyticsItem(self): pass

	# Параметры
	def on_RequestEditOptionsInclude(self): pass
	def on_RequestEditOptionsExclude(self): pass

	# Дерево Параметры
	def on_RequestProcessingTreeOptionsDbClick(self): pass
