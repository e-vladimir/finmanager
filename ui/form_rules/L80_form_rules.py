# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from L70_form_rules import C70_FormRules


class C80_FormRules(C70_FormRules):
	""" Форма Правила обработки данных: Логика данных """

	# Правила обработки данных
	def ShowRules(self):
		""" Загрузка правил обработки данных """
		for self._processing_ido in self.rules.IdosByType(self._processing_type): self.LoadRule()
