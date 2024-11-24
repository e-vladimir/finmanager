# ФОРМА ПРАВИЛО ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from L41_form_rule import C41_FormRule
from L90_rules     import C90_ProcessingRule


class C42_FormRule(C41_FormRule):
	""" Форма Правило обработки данных: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.rule = C90_ProcessingRule()
