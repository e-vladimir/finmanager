# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МОДЕЛЬ СОБЫТИЙ

from L42_form_processing_operations import C42_FormProcessingOperations


class C50_FormProcessingOperations(C42_FormProcessingOperations):
	""" Форма Обработка операций: Модель событий """

	# Меню правил обработки
	def on_RequestShowMenuRules(self): pass

	# Тип правил обработки
	def on_RequestSwitchRulesToDescription(self): pass
	def on_RequestSwitchRulesToDestination(self): pass
	def on_RequestSwitchRulesToLabels(self): pass

	# Правила обработки
	def on_RequestCreateRule(self): pass
	def on_RequestApplyRules(self): pass

	# Правило обработки
	def on_RequestOpenRule(self): pass
	def on_RequestDeleteRule(self): pass
