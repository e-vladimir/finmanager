# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from pathlib         import Path

from L20_PySide6     import C20_StandardItemModel
from L41_form_import import C41_FormImport
from L90_workspace   import C90_Workspace


class C42_FormImport(C41_FormImport):
	""" Форма Импорт данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._operations_data    : list        = []
		self._operations_header  : list        = []
		self._operations_options : list        = []

		self._operations_file    : Path | None = None

	def Init_10(self):
		super().Init_10()

		self.model_operations = C20_StandardItemModel()

		self.workspace        = C90_Workspace()

	def Init_20(self):
		super().Init_20()

		self.table_operations_data.setModel(self.model_operations)
