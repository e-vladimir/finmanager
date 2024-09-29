# ФОРМА ФИНАНАЛИТИКА: МОДЕЛЬ ДАННЫХ

from L20_PySide6           import C20_StandardItemModel
from L41_form_finanalitics import C41_FormFinanalitics
from L90_finanalitics      import C90_Finanalitics
from L90_workspace         import C90_Workspace


class C42_FormFinanalitics(C41_FormFinanalitics):
	""" Форма Финаналитика: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_label : str = ""

	def Init_01(self):
		super().Init_01()

		self.finanalitics  = C90_Finanalitics()

		self.workspace     = C90_Workspace()

		self.model_options = C20_StandardItemModel()
		self.model_data_dm = C20_StandardItemModel()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_options.setModel(self.model_options)
		self.table_data_dm.setModel(self.model_data_dm)
