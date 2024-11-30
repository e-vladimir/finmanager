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
	def on_RequestControlAutoreplace(self): pass
	def on_RequestReplaceText(self): pass
	def on_RequestResetData(self): pass
	def on_RequestImportOperations(self): pass
	def on_RequestExportOperations(self): pass

	# Пакет операций
	def on_RequestUncheckedAllPackOperations(self): pass
	def on_RequestExpandPackOperations(self): pass
	def on_RequestCollapsePackOperations(self): pass
	def on_RequestDeletePackOperation(self): pass

	# Финансовая операция
	def on_RequestOpenOperation(self): pass
	def on_RequestDeleteOperation(self): pass
	def on_RequestSetOperationColorBlack(self): pass
	def on_RequestSetOperationColorGray(self): pass
	def on_RequestSetOperationColorRed(self): pass
	def on_RequestSetOperationColorBlue(self): pass
	def on_RequestSetOperationColorGreen(self): pass
	def on_RequestSetOperationDescription(self): pass
	def on_RequestSetOperationLabels(self): pass
	def on_RequestSplitOperation(self): pass
