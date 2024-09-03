# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from pathlib         import Path

from L00_fields      import FIELDS
from L20_PySide6     import C20_StandardItemModel
from L41_form_import import C41_FormImport
from L90_workspace   import C90_Workspace


class C42_FormImport(C41_FormImport):
	""" Форма Импорт данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._import_finactions_data     : list[list[str]]   = []
		self._import_finactions_header   : dict[int, FIELDS] = dict()
		self._import_finactions_filepath : Path              = Path()

		self._processing_column          : int               = -1
		self._processing_name            : str               = ""

	def Init_10(self):
		super().Init_10()

		self.model_import_finactions_data = C20_StandardItemModel()

		self.workspace                    = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.table_import_finactions_data.setModel(self.model_import_finactions_data)
