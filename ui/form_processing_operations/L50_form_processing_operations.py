# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МОДЕЛЬ СОБЫТИЙ

from L42_form_processing_operations import C42_FormProcessingOperations


class C50_FormProcessingOperations(C42_FormProcessingOperations):
	""" Форма Обработка операций: Модель событий """

	# Субъект обработки
	def on_SubjectChanged(self): pass

	# Меню правил обработки
	def on_RequestShowMenuRules(self): pass

	# Правила обработки
	def on_RequestCreateRule(self): pass

	# Правило обработки
	def on_RequestOpenRule(self): pass
