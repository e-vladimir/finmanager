# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from pathlib           import Path

from G10_datetime      import CurrentDy, CurrentDm
from L00_struct_export import EXPORT_MODE_ACCOUNTS, EXPORT_MODE_DATE

from L20_PySide6       import C20_StandardItemModel
from L41_form_export   import C41_FormExport
from L90_accounts      import C90_Accounts
from L90_workspace     import C90_Workspace


class C42_FormExport(C41_FormExport):
	""" Форма Экспорт данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._operations_input_mode_date    : EXPORT_MODE_DATE     = EXPORT_MODE_DATE.ALL
		self._operations_input_dy           : int                  = CurrentDy()
		self._operations_input_dm           : int                  = CurrentDm()
		self._operations_input_mode_account : EXPORT_MODE_ACCOUNTS = EXPORT_MODE_ACCOUNTS.ALL
		self._operations_input_account      : str                  = ""

		self._operations_output_path        : Path                 = Path()
		self._operations_output_files       : list[str]            = []

		self._processing_ido                : str                  = ""

	def Init_10(self):
		super().Init_10()

		self.model_operations = C20_StandardItemModel()

		self.accounts         = C90_Accounts()
		self.workspace        = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data_operations.setModel(self.model_operations)
