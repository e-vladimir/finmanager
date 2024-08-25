# ФОРМА ОСНОВНАЯ: МОДЕЛЬ СОБЫТИЙ

from L42_form_main import C42_FormMain


class C50_FormMain(C42_FormMain):
	""" Форма основная: Модель событий """

	# Панель финпериода
	def on_RequestNextDm(self): pass
	def on_RequestPrevDm(self): pass
	def on_RequestSetDyDm(self): pass

	# Переход в другие формы
	def on_RequestOpenFincomposition(self): pass
	def on_RequestOpenFinstruct(self): pass
