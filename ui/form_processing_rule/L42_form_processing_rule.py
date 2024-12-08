# ФОРМА ПРАВИЛО ОБРАБОТКИ: МОДЕЛЬ ДАННЫХ

from L41_form_processing_rule import C41_FormProcessingRule
from L90_rules                import C90_ProcessingRule
from L90_workspace            import C90_Workspace


class C42_FormProcessingRule(C41_FormProcessingRule):
	""" Форма Правило обработки: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.processing_rule = C90_ProcessingRule()

		self.workspace       = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()
