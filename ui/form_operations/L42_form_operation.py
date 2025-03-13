# ФОРМА ОПЕРАЦИИ: МОДЕЛЬ ДАННЫХ
# 11 мар 2025

from L20_PySide6        import C20_StandardItemModel
from L41_form_operation import C41_FormOperation
from L90_account        import C90_Accounts
from L90_operations     import C90_Operations
from L90_workspace      import C90_Workspace


class C42_FormOperation(C41_FormOperation):
	""" Форма Операции: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_ido : str = ""
		self._processing_idp : str = ""
		self._processing_dd  : int = 0

	def Init_10(self):
		super().Init_10()

		self.ModelData  = C20_StandardItemModel()

		self.Accounts   = C90_Accounts()
		self.Operations = C90_Operations()
		self.Workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.TreeData.setModel(self.ModelData)
