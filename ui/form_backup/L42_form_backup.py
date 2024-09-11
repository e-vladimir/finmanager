# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: МОДЕЛЬ ДАННЫХ

from L20_PySide6     import C20_StandardItemModel
from L41_form_backup import C41_FormBackup


class C42_FormBackup(C41_FormBackup):
	""" Форма Резервное копирование: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_filename : str = ""
		self._processing_name     : str = ""

	def Init_10(self):
		super().Init_10()

		self.model_data = C20_StandardItemModel()

	def Init_20(self):
		super().Init_20()

		self.list_data.setModel(self.model_data)
