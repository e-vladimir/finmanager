# ФОРМА ФИНДЕЙСТВИЯ: МОДЕЛЬ СОБЫТИЙ

from L42_form_finactions import C42_FormFinactions


class C50_FormFinactions(C42_FormFinactions):
	""" Форма Финдействия: Модель событий """

	# Меню финдействий
	def on_RequestMenuFinactions(self): pass

	# Запись финдействий
	def on_RequestCreateFinactionsRecord(self): pass
	def on_RequestOpenFinactionsRecord(self): pass
	def on_RequestDeleteFinactionsRecord(self): pass
	def on_RequestSplitFinactionsRecord(self): pass
	def on_RequestEditNoteFinactionsRecord(self): pass

	# Дерево данных
	def on_RequestProcessingTreeDataDbClick(self): pass
