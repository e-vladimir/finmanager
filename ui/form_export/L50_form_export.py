# ФОРМА ЭКСПОРТА: МОДЕЛЬ СОБЫТИЙ

from L42_form_export import C42_FormExport


class C50_FormExport(C42_FormExport):
	""" Форма экспорта: Модель событий """

	# Панель финданных
	def on_RequestReadFindataDyDm(self): pass
	def on_FindataDyDmChanged(self): pass

	def on_RequestReadFindataFinstruct(self): pass

	def on_RequestSetFindataDirectory(self): pass

	def on_FindataOptionsChanged(self): pass

	# Панель статистики
	def on_RequestStartStopExport(self): pass

	# Экспорт
	def on_ExportStarted(self): pass
	def on_ExportProcessing(self): pass
	def on_ExportFinished(self): pass
