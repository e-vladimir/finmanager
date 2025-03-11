# ФОРМА СЧЕТА: МОДЕЛЬ ДАННЫХ
# 14 фев 2025

from L20_PySide6       import C20_StandardItemModel
from L41_form_accounts import C41_FormAccounts
from L90_account       import C90_Accounts
from L90_report        import C90_Report
from L90_workspace     import C90_Workspace


class C42_FormAccounts(C41_FormAccounts):
	""" Форма Счета: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_ido   : str = ""
		self._processing_idp   : str = ""
		self._processing_group : str = ""

	def Init_10(self):
		super().Init_10()

		self.ModelData = C20_StandardItemModel()

		self.Accounts  = C90_Accounts()
		self.Report    = C90_Report()
		self.Workspace = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.TreeData.setModel(self.ModelData)
