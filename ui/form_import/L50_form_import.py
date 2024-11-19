# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ СОБЫТИЙ

from L42_form_import import C42_FormImport


class C50_FormImport(C42_FormImport):
	""" Форма Импорт данных: Модель событий """

	# Меню импорта финансовых операций
	def on_RequestShowMenuOperations(self): pass

	def on_RequestOpenFileInOperations(self): pass
	def on_RequestSwitchDataInOperation(self): pass
	def on_RequestImportOperation(self): pass

	def on_RequestSetFieldInOperations(self): pass

	# Таблица данных импорта финансовых операций
	def on_RequestProcessingTableOperationsDbClick(self): pass
