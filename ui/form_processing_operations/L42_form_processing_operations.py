# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МОДЕЛЬ ДАННЫХ

from L00_form_processing_operations import SUBJECTS
from L20_PySide6                    import C20_StandardItemModel
from L41_form_processing_operations import C41_FormProcessingOperations
from L90_rules                      import C90_ProcessingRules
from L90_workspace                  import C90_Workspace


class C42_FormProcessingOperations(C41_FormProcessingOperations):
	""" Форма Обработка операций: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_subject : SUBJECTS | None = None
		self._processing_ido     : str             = ""

	def Init_10(self):
		super().Init_10()

		self.model_rules = C20_StandardItemModel()
		self.model_tools = C20_StandardItemModel()

		self.rules       = C90_ProcessingRules()
		self.workspace   = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.table_rules.setModel(self.model_rules)
		self.table_tools.setModel(self.model_tools)
