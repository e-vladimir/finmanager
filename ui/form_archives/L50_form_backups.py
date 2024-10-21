# ФОРМА АРХИВЫ ДАННЫХ: МОДЕЛЬ СОБЫТИЙ

from L42_form_backups import C42_FormArchives


class C50_FormArchives(C42_FormArchives):
	""" Форма Архив данных: Модель событий """

	# Меню архива данных
	def on_RequestShowMenuArchives(self): pass

	def on_RequestCopyDataToArchive(self): pass
	def on_RequestCopyDataFromArchive(self): pass
	def on_RequestDeleteArchive(self): pass
