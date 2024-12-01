# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: ЛОГИКА ДАННЫХ

from L00_rules                    import RULES
from L70_form_control_autoreplace import C70_FormControlAutoreplace


class C80_FormControlAutoreplace(C70_FormControlAutoreplace):
	""" Форма Управление автозаменой: Логика данных """

	# Правила автозамены
	def ShowRules(self):
		""" Отображение правил """
		for self._processing_ido in self.rules.IdosByType(RULES.REPLACE_TEXT, True): self.LoadRuleAutoreplace()
