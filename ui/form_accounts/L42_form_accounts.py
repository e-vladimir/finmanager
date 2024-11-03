# ФОРМА СЧЕТА: МОДЕЛЬ ДАННЫХ

from L20_PySide6       import C20_StandardItemModel
from L41_form_accounts import C41_FormAccounts
from L90_accounts      import C90_AccountsStruct, C90_AccountsGroup
from L90_workspace     import C90_Workspace


class C42_FormAccounts(C41_FormAccounts):
	""" Форма Счета: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_name  : str = ""
		self._processing_group : str = ""
		self._processing_ido   : str = ""

	def Init_10(self):
		super().Init_10()

		self.accounts_group  = C90_AccountsGroup()
		self.accounts_struct = C90_AccountsStruct()
		self.model_data      = C20_StandardItemModel()
		self.workspace       = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data.setModel(self.model_data)
