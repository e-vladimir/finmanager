# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ СОБЫТИЙ
# 14 мар 2025

from L42_form_import import C42_FormImport


class C50_FormImport(C42_FormImport):
	""" Форма Импорт данных: Модель событий """

	# Меню Импорт операций
	def on_RequestShowMenuOperations(self): pass

	# Импорт операций
	def on_RequestLoadOperationsFromFile(self): pass
	def on_RequestEditOperationsField(self): pass
	def on_RequestImportOperations(self): pass

	def on_OperationsDataLoaded(self): pass
	def on_OperationsStructChanged(self): pass
	def on_Imported(self): pass
