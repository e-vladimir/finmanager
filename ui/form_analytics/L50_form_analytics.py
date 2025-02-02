# ФОРМА АНАЛИТИКА: МОДЕЛЬ СОБЫТИЙ

from L42_form_analytics import C42_FormAnalytics


class C50_FormAnalytics(C42_FormAnalytics):
	""" Форма Аналитика: Модель событий """

	# Элемент аналитики
	def on_AnalyticsItemSelected(self): pass
	def on_RequestCreateAnalyticsItem(self): pass
	def on_RequestDeleteAnalyticsItem(self): pass
	def on_RequestEditAnalyticsItemName(self): pass
	def on_RequestEditAnalyticsItemInclude(self): pass
	def on_RequestEditAnalyticsItemExclude(self): pass

	# Параметры аналитики
	def on_ProcessingObjectSelected(self): pass

	# Дерево параметров элемента аналитики
	def on_RequestProcessingTreeDataItem_DbClick(self): pass

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self): pass
