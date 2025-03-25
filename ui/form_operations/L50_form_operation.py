# ФОРМА ОПЕРАЦИИ: МОДЕЛЬ СОБЫТИЙ
# 11 мар 2025

from L42_form_operation import C42_FormOperation


class C50_FormOperation(C42_FormOperation):
	""" Форма Операции: Модель событий """

	# Меню операций
	def on_RequestMenuOperation(self): pass

	# Дерево данных
	def on_TreeDataDoubleClicked(self): pass

	# Операции
	def on_RequestOpenFormImport(self): pass
	def on_RequestResetOperations(self): pass

	def on_OperationsReset(self): pass

	# Операция
	def on_RequestCreateOperation(self): pass
	def on_RequestDeleteOperation(self): pass
	def on_RequestEditOperationAmount(self): pass
	def on_RequestEditOperationAccounts(self): pass
	def on_RequestEditOperationDescriptions(self): pass
	def on_RequestEditOperationLabels(self): pass
	def on_RequestSetOperationColorToBlack(self): pass
	def on_RequestSetOperationColorToGray(self): pass
	def on_RequestSetOperationColorToGreen(self): pass
	def on_RequestSetOperationColorToBlue(self): pass
	def on_RequestSetOperationColorToRed(self): pass
	def on_RequestSplitOperation(self): pass
	def on_RequestCopyOperation(self): pass

	def on_OperationCreated(self): pass
	def on_OperationDeleted(self): pass
	def on_OperationChanged(self): pass

	# Обработка данных
	def on_RequestOpenProcessing(self): pass
