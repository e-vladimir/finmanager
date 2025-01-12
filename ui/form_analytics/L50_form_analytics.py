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
	def on_RequestEditName(self): pass

	def on_RequestEditVolumeTitle(self): pass
	def on_RequestEditVolumeValue(self): pass

	# Параметры
	def on_RequestEditInclude(self): pass
	def on_RequestEditExclude(self): pass

	# Дерево Параметры
	def on_RequestProcessingTreeOptionsDbClick(self): pass

	# Дерево Объёмная стоимость
	def on_RequestProcessingTreeVolumesDbClick(self): pass
