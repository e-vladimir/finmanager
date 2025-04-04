# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 01 апр 2025

from pathlib         import Path

from G10_datetime    import CurrentDy, CurrentDm

from L00_form_export import ACCOUNTS, EXPORT_FIELDS, INTERVALS
from L20_PySide6     import C20_StandardItemModel
from L41_form_export import C41_FormExport
from L90_account     import C90_Accounts
from L90_workspace   import C90_Workspace


class C42_FormExport(C41_FormExport):
	""" Форма экспорт данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._operations_interval_mode    : INTERVALS     = INTERVALS.DY
		self._operations_interval_dy      : int           = CurrentDy()
		self._operations_interval_dm      : int           = CurrentDm()

		self._operations_accounts_mode    : ACCOUNTS      = ACCOUNTS.ALL
		self._operations_accounts_group   : str           = ""
		self._operations_accounts_account : str           = ""

		self._operations_directory        : Path          = Path("./")

		self._processing_field            : EXPORT_FIELDS = EXPORT_FIELDS.NONE

	def Init_10(self):
		super().Init_10()

		self.ModelDataOperations = C20_StandardItemModel()

		self.Accounts            = C90_Accounts()
		self.Workspace           = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.TreeDataOperations.setModel(self.ModelDataOperations)
