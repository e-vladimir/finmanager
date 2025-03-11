# ФОРМА ОСНОВНАЯ: МОДЕЛЬ ДАННЫХ
# 12 фев 2025

from L41_form_main  import C41_FormMain
from L90_account    import C90_Accounts
from L90_operations import C90_Operations
from L90_workspace  import C90_Workspace


class C42_FormMain(C41_FormMain):
	""" Форма Основная: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.Accounts   = C90_Accounts()
		self.Operations = C90_Operations()
		self.Workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()
