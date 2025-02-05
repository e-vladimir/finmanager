# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ СОБЫТИЙ

from L42_form_processing import C42_FormProcessing


class C50_FormProcessing(C42_FormProcessing):
	""" Форма Обработка данных: Модель событий """

	# Обработка операций
	def on_OperationsChanged(self): pass
	def on_RequestEditOperationsInclude(self): pass
	def on_RequestEditOperationsExclude(self): pass
	def on_RequestEditOperationsDestination(self): pass
	def on_RequestEditOperationsDetail(self): pass
	def on_RequestEditOperationsObjectInt(self): pass
	def on_RequestEditOperationsObjectExt(self): pass
	def on_RequestEditOperationsColor(self): pass
	def on_RequestEditOperationsInterval(self): pass
	def on_RequestProcessingOperations(self): pass

	# Дерево данных Обработка операций
	def on_RequestProcessingTreeDataOperations_DbClick(self): pass

	# Меню Обработка операций
	def on_RequestShowMenuOperations(self): pass
