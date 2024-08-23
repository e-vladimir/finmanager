# ФОРМА ФИНСОСТАВ: МОДЕЛЬ ДАННЫХ

from L20_PySide6             import C20_StandardItemModel
from L41_form_fincomposition import C41_FormFincomposition
from L90_fincomposition      import C90_Fincomposition
from L90_workspace           import C90_Workspace


class C42_FormFincomposition(C41_FormFincomposition):
	""" Форма Финсостав: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._ido_processing  : str = ""
		self._name_processing : str = ""

	def Init_10(self):
		super().Init_10()

		self.model_data     = C20_StandardItemModel()

		self.fincomposition = C90_Fincomposition()
		self.workspace      = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data.setModel(self.model_data)
