# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from pathlib         import Path

from L00_options     import OPTIONS
from L20_PySide6     import C20_StandardItemModel
from L41_form_export import C41_FormExport
from L90_finactions  import C90_Finactions
from L90_finstruct   import C90_Finstruct
from L90_workspace   import C90_Workspace


class C42_FormExport(C41_FormExport):
	""" Форма Экспорт данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_row                     : int       = -1

		self._options_finactions_period_mode     : OPTIONS   = OPTIONS.MODE_DM
		self._options_finactions_period_dm       : int       = 0
		self._options_finactions_period_dy       : int       = 0
		self._options_finactions_finstruct_mode  : OPTIONS   = OPTIONS.MODE_ALL
		self._options_finactions_finstruct_names : list[str] = []
		self._options_finactions_folder          : Path      = Path()
		self._options_finactions_filenames       : list[str] = []

	def Init_10(self):
		super().Init_10()

		self.finactions       = C90_Finactions()
		self.finstruct        = C90_Finstruct()

		self.model_finactions = C20_StandardItemModel()

		self.workspace        = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

		self._options_finactions_period_dm      : int       = self.workspace.Dm()
		self._options_finactions_period_dy      : int       = self.workspace.Dy()

	def Init_20(self):
		super().Init_20()

		self.table_finactions_data.setModel(self.model_finactions)
