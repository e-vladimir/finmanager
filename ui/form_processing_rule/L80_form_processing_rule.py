# ФОРМА ПРАВИЛО ОБРАБОТКИ: ЛОГИКА ДАННЫХ

from L00_rules                import RULES
from L70_form_processing_rule import C70_FormProcessingRule


class C80_FormProcessingRule(C70_FormProcessingRule):
	""" Форма Правило обработки: Логика данных """

	# Правило обработки
	def SaveProcessingRule(self):
		""" Запись правила обработки """
		match self.processing_rule.RuleType():
			case RULES.REPLACE_DESCRIPTION:
				self.processing_rule.InputAsStrings(self.edit_input_multiple.toPlainText().split('\n'))
				self.processing_rule.OutputAsString(self.edit_output_single.text())

			case RULES.MATCH_DESTINATION:
				self.processing_rule.InputAsStrings(self.edit_input_multiple.toPlainText().split('\n'))
				self.processing_rule.OutputAsString(self.edit_output_single.text())

			case RULES.DETECT_LABEL:
				self.processing_rule.InputAsStrings(self.edit_input_multiple.toPlainText().split('\n'))
				self.processing_rule.OutputAsStrings(self.edit_output_multiple.toPlainText().split('\n'))
