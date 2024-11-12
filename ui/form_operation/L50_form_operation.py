# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: МОДЕЛЬ СОБЫТИЙ

from L42_form_operation import C42_FormOperation


class C50_FormOperation(C42_FormOperation):
	""" Форма Финансовая операция: Модель событий """

	# Дерево данных
	def on_RequestProcessingTreeDataDbClick(self): pass

	# Финансовая операция
	def on_RequestSetDate(self)       : pass
	def on_RequestSetAmount(self)     : pass
	def on_RequestSetDescription(self): pass
	def on_RequestSetAccounts(self)   : pass
	def on_RequestSetLabels(self)     : pass
