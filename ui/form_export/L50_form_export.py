# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ СОБЫТИЙ

from L42_form_export import C42_FormExport


class C50_FormExport(C42_FormExport):
	""" Форма Экспорт данных: Модель событий """

	# Меню экспорта финдействий
	def on_RequestShowMenuExportFinactions(self): pass

	# Параметры экспорта финдействий
	def on_RequestSetOptionsFinactionsPeriodMode(self): pass
	def on_RequestSetOptionsFinactionsPeriodDm(self): pass
	def on_RequestSetOptionsFinactionsPeriodDy(self): pass
	def on_RequestSetOptionsFinactionsFinstructMode(self): pass
	def on_RequestSetOptionsFinactionsFinstructName(self): pass
	def on_RequestSetOptionsFinactionsFolder(self): pass

	# Таблица данных финдействий
	def on_RequestProcessingDbClickTableFinactionsData(self): pass

	# Экспорт финдействий
	def on_RequestProcessingExportFinactions(self): pass
