# ФОРМА ФИНСОСТАВ: МОДЕЛЬ СОБЫТИЙ

from L42_form_fincomposition import C42_FormFincomposition


class C50_FormFincomposition(C42_FormFincomposition):
	""" Форма Финсостав: Модель событий """

	# Меню финсостава
	def on_RequestMenuFincomposition(self): pass

	# Запись финсостава
	def on_RequestCreateTopFincompositionRecord(self): pass
	def on_RequestCreateFincompositionRecord(self): pass
