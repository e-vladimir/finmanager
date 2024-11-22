# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L00_rules import RULES
from L80_rules import C80_ProcessingRule, C80_ProcessingRules


class C90_ProcessingRule(C80_ProcessingRule):
	""" Правило обработки данных: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Выполнена регистрация объекта """
		self.Type(RULES.UNKNOWN)

		self.InputAsString("")
		self.OutputAsString("")


class C90_ProcessingRules(C80_ProcessingRules):
	""" Правила обработки данных: Логика управления """
	pass
