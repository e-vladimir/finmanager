# ФОРМА АРХИВЫ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from L20_PySide6      import C20_StandardItemModel
from L41_form_backups import C41_FormArchives


class C42_FormArchives(C41_FormArchives):
	""" Форма Архив данных: Модель данных """

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
