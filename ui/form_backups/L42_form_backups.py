# ФОРМА АРХИВ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from L20_PySide6      import C20_StandardItemModel
from L41_form_backups import C41_FormBackups


class C42_FormBackups(C41_FormBackups):
	""" Форма Архив данных: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.model_data = C20_StandardItemModel()

	def Init_20(self):
		super().Init_20()

		self.list_data.setModel(self.model_data)
