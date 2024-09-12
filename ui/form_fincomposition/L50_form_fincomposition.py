# ФОРМА ФИНСОСТАВ: МОДЕЛЬ СОБЫТИЙ

from L42_form_fincomposition import C42_FormFincomposition


class C50_FormFincomposition(C42_FormFincomposition):
	""" Форма Финсостав: Модель событий """

	# Меню финсостава
	def on_RequestShowMenuFincomposition(self): pass

	# Запись финсостава
	def on_RequestAppendFincompositionRecordToTop(self): pass

	def on_RequestAppendFincompositionRecord(self): pass
	def on_RequestRenameFincompositionRecord(self): pass
	def on_RequestDeleteFincompositionRecord(self): pass
	def on_RequestMoveUpFincompositionRecord(self): pass
	def on_RequestMemoryFincompositionRecord(self): pass
	def on_RequestPasteFincompositionRecord(self): pass

	def on_RequestResetFincomposition(self): pass
