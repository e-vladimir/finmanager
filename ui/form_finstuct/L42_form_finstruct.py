# ФОРМА ФИНСТРУКТУРЫ: МОДЕЛЬ ДАННЫХ

from L20_PySide6        import C20_StandardItemModel
from L41_form_finstruct import C41_FormFinstruct
from L90_finstruct      import C90_Finstruct
from L90_workspace      import C90_Workspace


class C42_FormFinstruct(C41_FormFinstruct):
	""" Форма Финструктуры: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._oid_processing : str  = ""
		self._oid_memory     : str  = ""

		self._col_processing : int = -1

	def Init_10(self):
		super().Init_10()

		self.model_data = C20_StandardItemModel(None)

		self.finstruct  = C90_Finstruct()

		self.workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data.setModel(self.model_data)
