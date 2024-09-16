# ФОРМА ФИНСТАТИСТИКА: МОДЕЛЬ ДАННЫХ

from L20_PySide6            import C20_StandardItemModel
from L41_form_finstatistics import C41_FormFinstatistics
from L90_finstatistics      import C90_Finstatistics
from L90_finstructs         import C90_Finstruct
from L90_workspace          import C90_Workspace


class C42_FormFinstatistics(C41_FormFinstatistics):
	""" Форма Финстатистика: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.finstruct     = C90_Finstruct()
		self.finstatistics = C90_Finstatistics()

		self.workspace     = C90_Workspace()

		self.model_data    = C20_StandardItemModel()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.table_data.setModel(self.model_data)
