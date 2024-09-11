# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: МОДЕЛЬ СОБЫТИЙ

from L42_form_backup import C42_FormBackup


class C50_FormBackup(C42_FormBackup):
	""" Форма Резервное копирование: Модель событий """

	# Меню резервных копий
	def on_RequestMenuBackup(self): pass

	# Резервное копирование
	def on_RequestCreateBackup(self): pass

	# Резервная копия
	def on_RequestRestoreBackup(self): pass
	def on_RequestDeleteBackup(self): pass
