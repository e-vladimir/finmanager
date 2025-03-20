# ФОРМА КОПИИ АРХИВА ДАННЫХ: МОДЕЛЬ СОБЫТИЙ
# 18 мар 2025

from L42_form_backups import C42_FormBackups


class C50_FormBackups(C42_FormBackups):
	""" Форма Копии архива данных: Модель событий """

	# Меню Копии архива данных
	def on_RequestShowMenuBackups(self): pass

	# Копия архива данных
	def on_RequestCreateBackup(self): pass
	def on_RequestRestoreFromBackup(self): pass
	def on_RequestDeleteBackup(self): pass
