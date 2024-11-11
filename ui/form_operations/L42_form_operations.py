# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: МОДЕЛЬ ДАННЫХ

from L20_PySide6         import C20_StandardItemModel
from L41_form_operations import C41_FormOperations
from L90_accounts        import C90_Accounts
from L90_operations      import C90_Operations
from L90_workspace       import C90_Workspace


class C42_FormOperations(C41_FormOperations):
	""" Форма Финансовые операции: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_ido    : str = ""
		self._processing_dd     : int = 1
		self._processing_column : int = 0

	def Init_10(self):
		super().Init_10()

		self.accounts   = C90_Accounts()
		self.operations = C90_Operations()
		self.model_data = C20_StandardItemModel()
		self.workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data.setModel(self.model_data)
