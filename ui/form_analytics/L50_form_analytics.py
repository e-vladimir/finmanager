# ФОРМА АНАЛИТИКА ДАННЫХ: МОДЕЛЬ СОБЫТИЙ
# 11 апр 2025

from L42_form_analytics import C42_FormAnalytics


class C50_FormAnalytics(C42_FormAnalytics):
	""" Форма Аналитика данных: Модель событий """

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self): pass


	# Меню Элемент аналитики
	def on_RequestShowMenuItem(self): pass


	# Элемент аналитики
	def on_RequestCreateItem(self): pass
	def on_RequestDeleteItem(self): pass
	def on_RequestEditItem(self): pass
	def on_RequestEditItemName(self): pass
	def on_RequestEditItemInclude(self): pass
	def on_RequestEditItemExclude(self): pass

	def on_ItemCreated(self): pass
	def on_ItemDeleted(self): pass
	def on_ItemSwitched(self): pass
	def on_ItemChanged(self): pass
