# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: МОДЕЛЬ ДАННЫХ

from L20_PySide6        import C20_StandardItemModel
from L41_form_operation import C41_FormOperation
from L90_accounts       import C90_Accounts
from L90_operations     import C90_Operation
from L90_workspace      import C90_Workspace


class C42_FormOperation(C41_FormOperation):
	""" Форма Финансовая операция: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.model_data = C20_StandardItemModel()

		self.operation  = C90_Operation()
		self.accounts   = C90_Accounts()
		self.workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data.setModel(self.model_data)
