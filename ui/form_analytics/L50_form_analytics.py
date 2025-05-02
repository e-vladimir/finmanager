# ФОРМА АНАЛИТИКА ДАННЫХ: МОДЕЛЬ СОБЫТИЙ
# 27 апр 2025

from L42_form_analytics import C42_FormAnalytics


class C50_FormAnalytics(C42_FormAnalytics):
	""" Форма Аналитика данных: Модель событий """

	# Меню структуры аналитики
	def on_RequestShowMenuStruct(self): pass


	# Структура аналитики
	def on_RequestResetDestinations(self): pass

	def on_StructChanged(self): pass


	# Элемент структуры аналитики
	def on_RequestCreateTopDestination(self): pass
	def on_RequestCreateDestination(self): pass
	def on_RequestCreateSubDestination(self): pass
	def on_RequestEditDestinationName(self): pass
	def on_RequestDeleteDestination(self): pass

	def on_DestinationCreated(self): pass
	def on_DestinationChanged(self): pass


	# Дерево данных
	def on_TreeDataDbClicked(self): pass
