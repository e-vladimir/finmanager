# ФОРМА КОПИИ АРХИВА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 18 мар 2025

from L20_PySide6      import C20_StandardItemModel
from L41_form_backups import C41_FormBackups


class C42_FormBackups(C41_FormBackups):
	""" Форма Копии архива данных: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.ModelData = C20_StandardItemModel()

	def Init_20(self):
		super().Init_20()

		self.ListData.setModel(self.ModelData)
