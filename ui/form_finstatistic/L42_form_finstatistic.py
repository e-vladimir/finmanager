# ФОРМА ФИНСТАТИСТИКА: МОДЕЛЬ ДАННЫХ

from PySide6.QtCore        import QModelIndex

from L20_PySide6           import C20_StandardItemModel
from L41_form_finstatistic import C41_FormFinstatistic
from L90_findescription    import C90_Findescription
from L90_finstatistic      import C90_Finstatistic
from L90_workspace         import C90_Workspace


class C42_FormFinstatistic(C41_FormFinstatistic):
	""" Форма Финстатистика: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._oid_processing         : str       = ""
		self._oids_struct_processing : list[str] = []

		self._index_processing       : QModelIndex | None = None

	def Init_10(self):
		super().Init_10()

		self.model_finstatistic = C20_StandardItemModel(None)

		self.findescription     = C90_Findescription()
		self.finstatistic       = C90_Finstatistic()

		self.workspace          = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_finstatistic.setModel(self.model_finstatistic)
