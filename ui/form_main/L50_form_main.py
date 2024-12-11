# ФОРМА ОСНОВНАЯ: МОДЕЛЬ СОБЫТИЙ

from L42_form_main import C42_FormMain


class C50_FormMain(C42_FormMain):
	""" Форма Основная: Модель событий """

	# Переход в другие формы
	def on_RequestOpenFormArchives(self): pass
	def on_RequestOpenFormAccounts(self): pass
	def on_RequestOpenFormOperations(self): pass
	def on_RequestOpenFormStatistic(self): pass

	# Панель рабочего периода
	def on_RequestShiftDmToPrev(self): pass
	def on_RequestShiftDmToNext(self): pass
	def on_RequestSetDyDm(self): pass
