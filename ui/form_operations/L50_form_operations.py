# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: МОДЕЛЬ СОБЫТИЙ

from L42_form_operations import C42_FormOperations


class C50_FormOperations(C42_FormOperations):
	""" Форма Финансовые операции: Модель событий """

	# Дерево данных
	def on_RequestProcessingTreeDataDbClick(self): pass

	# Меню операций по счетам
	def on_RequestShowMenuOperations(self): pass

	# Финансовые операции
	def on_RequestCreateOperation(self): pass
	def on_RequestImportOperations(self): pass
	def on_RequestExportOperations(self): pass
	def on_RequestOpenProcessing(self): pass
	def on_RequestResetData(self): pass

	# Финансовая операция
	def on_RequestDeleteOperation(self): pass
	def on_RequestSetOperationAmount(self): pass
	def on_RequestSetOperationAccounts(self): pass
	def on_RequestSetOperationDestination(self): pass
	def on_RequestSetOperationDetail(self): pass
	def on_RequestSetOperationObjectInt(self): pass
	def on_RequestSetOperationObjectExt(self): pass
	def on_RequestSetOperationColorBlack(self): pass
	def on_RequestSetOperationColorGray(self): pass
	def on_RequestSetOperationColorRed(self): pass
	def on_RequestSetOperationColorBlue(self): pass
	def on_RequestSetOperationColorGreen(self): pass
	def on_RequestSplitOperation(self): pass
	def on_RequestCloneOperation(self): pass
