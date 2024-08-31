# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МОДЕЛЬ ДАННЫХ

from L20_PySide6                import C20_StandardItemModel
from L41_form_finactions_record import C41_FormFinactionsRecord
from L90_finactions             import C90_FinactionsRecord
from L90_workspace              import C90_Workspace


class C42_FormFinactionsRecord(C41_FormFinactionsRecord):
	""" Форма Запись финдействий: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.model_data        = C20_StandardItemModel()

		self.finactions_record = C90_FinactionsRecord()
		self.workspace         = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.table_data.setModel(self.model_data)
