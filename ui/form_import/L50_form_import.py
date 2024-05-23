# ФОРМА ИМПОРТА ДАННЫХ: МОДЕЛЬ СОБЫТИЙ

from L42_form_import import C42_FormImport


class C50_FormImport(C42_FormImport):
	""" Форма импорта данных: Модель событий """

	def on_StartStopImport(self): pass

	def on_ImportStarted(self): pass
	def on_ImportFinished(self): pass

	def on_FindataRequestSelectFile(self): pass
	def on_FindataSelectedFile(self): pass

	def on_RequestShowStatistic(self): pass
