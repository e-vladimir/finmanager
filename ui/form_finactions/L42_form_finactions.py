# ФОРМА ФИНДЕЙСТВИЯ: МОДЕЛЬ ДАННЫХ

from L00_colors          import COLORS
from L20_PySide6         import C20_StandardItemModel
from L41_form_finactions import C41_FormFinactions
from L90_finactions      import C90_Finactions
from L90_finstruct       import C90_Finstruct
from L90_workspace       import C90_Workspace


class C42_FormFinactions(C41_FormFinactions):
	""" Форма Финдействия: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_dd     : int           = 0
		self._processing_ido    : str           = ""
		self._processing_idos   : list[str]     = []
		self._processing_column : int           = -1
		self._processing_color  : COLORS | None = None

	def Init_10(self):
		super().Init_10()

		self.model_data = C20_StandardItemModel()

		self.finstruct  = C90_Finstruct()
		self.finactions = C90_Finactions()
		self.workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data.setModel(self.model_data)
