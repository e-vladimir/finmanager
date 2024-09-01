# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МОДЕЛЬ ДАННЫХ

from L20_PySide6                import C20_StandardItemModel
from L41_form_finactions_record import C41_FormFinactionsRecord
from L90_finactions             import C90_FinactionsRecord
from L90_finstruct              import C90_Finstruct
from L90_workspace              import C90_Workspace


class C42_FormFinactionsRecord(C41_FormFinactionsRecord):
	""" Форма Запись финдействий: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_name : str = ""
		self._processing_ido  : str = ""

	def Init_10(self):
		super().Init_10()

		self.model_finstruct   = C20_StandardItemModel()

		self.finstruct         = C90_Finstruct()
		self.finactions_record = C90_FinactionsRecord()
		self.workspace         = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_finstruct.setModel(self.model_finstruct)
