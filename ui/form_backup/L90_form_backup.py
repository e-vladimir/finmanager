# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_backup import C80_FormBackup


class C90_FormBackup(C80_FormBackup):
	""" Форма Резервное копирование: Логика управления """

	def on_Open(self):
		""" Открытие формы """
		self.LoadModelData()
