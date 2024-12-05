# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: ЛОГИКА ДАННЫХ

from L00_rules                    import RULES
from L70_form_control_description import C70_FormControlDescription


class C80_FormControlDescription(C70_FormControlDescription):
	""" Форма Управление описанием: Логика данных """

	# Правила автозамены описания
	def ShowRules(self):
		""" Отображение правил автозамены описания """
		for self._processing_ido in self.rules.IdosByType(RULES.REPLACE_DESCRIPTION): self.LoadRuleInModel()
