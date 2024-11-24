# ФОРМА ПРАВИЛО ОБРАБОТКИ ДАННЫХ: МЕХАНИКА ДАННЫХ

from L50_form_rule import C50_FormRule


class C60_FormRule(C50_FormRule):
	""" Форма Правило обработки данных: Механика данных """

	# Параметры
	def ReadIdoRuleFromWorkspace(self):
		""" Чтение IDO правила обработки данных из workspace """
		self.rule.Ido(self.workspace.IdoRule())
