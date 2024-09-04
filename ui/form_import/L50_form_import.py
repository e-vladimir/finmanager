# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ СОБЫТИЙ

from L42_form_import import C42_FormImport


class C50_FormImport(C42_FormImport):
	""" Форма Импорт данных: Модель событий """

	# Меню импорта финдействий
	def on_RequestShowMenuImportFinactions(self): pass

	# Импорт финдействий
	def on_RequestOpenImportFinactionsFile(self): pass
	def on_RequestExecImportFinactions(self): pass

	# Таблица данных импорта финдействий
	def on_RequestSetFieldImportFinactions(self): pass
	def on_RequestResetFieldImportFinactions(self): pass
