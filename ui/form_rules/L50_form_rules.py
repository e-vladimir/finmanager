# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ СОБЫТИЙ

from L42_form_rules import C42_FormRules


class C50_FormRules(C42_FormRules):
	""" Форма Правила обработки данных: Модель событий """

	# Список типов правил
	def on_SwitchRulesType(self): pass

	# Меню правил обработки данных
	def on_RequestMenuRules(self): pass

	# Таблица данных
	def on_RequestProcessingDbClickTableData(self): pass

	# Правила обработки данных
	def on_RequestCreateRule(self): pass
	def on_RequestEditInputRule(self): pass
	def on_RequestEditOutputRule(self): pass
	def on_RequestDeleteRule(self): pass

	# Сброс данных
	def on_RequestResetRulesByType(self): pass
