# ФОРМА ПРАВИЛО ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from L00_rules     import RULES
from L70_form_rule import C70_FormRule


class C80_FormRule(C70_FormRule):
	""" Форма Правило обработки данных: Логика данных """

	# Правило обработки данных
	def SaveRule(self):
		""" Запись данных """
		match self.rule.Type():
			case RULES.REPLACE_TEXT        :
				self.rule.InputAsStrings(self.edit_input.toPlainText().split('\n'))
				self.rule.OutputAsString(self.edit_output.toPlainText())

			case RULES.DETECT_LABEL_BY_TEXT:
				self.rule.InputAsStrings(self.edit_input.toPlainText().split('\n'))
				self.rule.OutputAsStrings(self.edit_output.toPlainText().split('\n'))
