# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ СОБЫТИЙ
# 01 апр 2025

from L42_form_export import C42_FormExport


class C50_FormExport(C42_FormExport):
	""" Форма экспорт данных: Модель событий """

	# Экспорт операций
	def on_RequestEditOperations(self): pass
	def on_RequestEditOperationsInterval(self): pass
	def on_RequestEditOperationsAccounts(self): pass
	def on_RequestEditOperationsDirectory(self): pass
	def on_RequestExportOperations(self): pass

	def on_OptionsOperationsChanged(self): pass


	# Меню экспорта операций
	def on_RequestShowMenuOperations(self): pass
