# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from pathlib         import Path

from L20_PySide6     import C20_StandardItemModel
from L41_form_import import C41_FormImport
from L90_operations  import C90_Operations
from L90_workspace   import C90_Workspace


class C42_FormImport(C41_FormImport):
	""" Форма Импорт данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._operations_data           : list        = []
		self._operations_header         : list        = []
		self._operations_fields         : list        = []
		self._operations_file           : Path | None = None
		self._operations_processing_row : int         = -1

	def Init_10(self):
		super().Init_10()

		self.model_operations = C20_StandardItemModel()

		self.operations       = C90_Operations()
		self.workspace        = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.table_operations_data.setModel(self.model_operations)
