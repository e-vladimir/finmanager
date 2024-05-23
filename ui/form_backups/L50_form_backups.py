# ФОРМА РЕЗЕРВНЫЕ КОПИИ: МОДЕЛЬ СОБЫТИЙ

from L42_form_backups import C42_FormBackups


class C50_FormBackups(C42_FormBackups):
	""" Форма Резервные копии: Модель событий """

	# Меню резервных копий
	def on_RequestMenuBackups(self): pass

	def on_RequestCreateBackup(self): pass
	def on_RequestRestoreFromBackup(self): pass
	def on_RequestDeleteBackup(self): pass

	# Модель резервных копий
	def on_RequestShowBackups(self): pass
