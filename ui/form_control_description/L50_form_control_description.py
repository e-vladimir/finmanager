# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: МОДЕЛЬ СОБЫТИЙ

from L42_form_control_description import C42_FormControlDescription


class C50_FormControlDescription(C42_FormControlDescription):
	""" Форма Управление описанием: Модель событий """

	# Меню автозамены описания
	def on_RequestShowMenuRules(self): pass

	# Таблица правил
	def on_RequestProcessingTableRules_DbClick(self): pass

	# Правила автозамены правил
	def on_RequestApplyRules(self): pass

	# Правило автозамены описания
	def on_RequestCreateRule(self): pass
	def on_RequestDeleteRule(self): pass
	def on_RequestEditInput(self): pass
	def on_RequestEditOutput(self): pass
