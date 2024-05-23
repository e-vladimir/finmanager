# ФОРМА РЕЗЕРВНЫЕ КОПИИ: МОДЕЛЬ ДАННЫХ

from L20_PySide6      import C20_StandardItemModel
from L41_form_backups import C41_FormBackups


class C42_FormBackups(C41_FormBackups):
	""" Форма Резервные копии: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._filename_processing : str = ""

	def Init_10(self):
		super().Init_10()

		self.model_backups = C20_StandardItemModel(None)

	def Init_20(self):
		super().Init_20()

		self.lst_backups.setModel(self.model_backups)
