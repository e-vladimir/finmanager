# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ СОБЫТИЙ

from L42_form_export import C42_FormExport


class C50_FormExport(C42_FormExport):
	""" Форма Экспорт данных: Модель событий """

	# Дерево данных Финансовые операции
	def on_RequestProcessingTreeDataOperationsDbClick(self): pass

	# Меню Финансовые операции
	def on_RequestShowMenuOperations(self): pass

	# Экспорт Финансовых операций
	def on_RequestSetDateInOperations(self): pass
	def on_RequestSetAccountInOperations(self): pass
	def on_RequestSetPathInOperations(self): pass

	def on_RequestExportOperations(self): pass
