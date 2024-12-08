# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: ЛОГИКА ДАННЫХ

from L00_form_processing_operations import SUBJECTS
from L00_rules                      import RULES

from L70_form_processing_operations import C70_FormProcessingOperations


class C80_FormProcessingOperations(C70_FormProcessingOperations):
	""" Форма Обработка операций: Логика данных """

	# Правила обработки
	def ShowRules(self):
		""" Отображение правил обработки """
		match self._processing_subject:
			case SUBJECTS.DESCRIPTION:
				for self._processing_ido in self.rules.IdosByType(RULES.REPLACE_DESCRIPTION): self.LoadRuleToModel()

			case SUBJECTS.DESTINATION:
				for self._processing_ido in self.rules.IdosByType(RULES.MATCH_DESTINATION)  : self.LoadRuleToModel()

			case SUBJECTS.LABELS     :
				for self._processing_ido in self.rules.IdosByType(RULES.DETECT_LABEL)       : self.LoadRuleToModel()
