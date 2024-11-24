# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from L00_rules      import RULES
from L20_PySide6    import C20_StandardItemModel
from L41_form_rules import C41_FormRules
from L90_rules      import C90_ProcessingRules
from L90_workspace  import C90_Workspace


class C42_FormRules(C41_FormRules):
	""" Форма Правила обработки данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_column : int = -1
		self._processing_ido    : str   = ""
		self._processing_type   : RULES = RULES.UNKNOWN

	def Init_10(self):
		super().Init_10()

		self.model_data = C20_StandardItemModel()

		self.rules      = C90_ProcessingRules()
		self.workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.table_data.setModel(self.model_data)
