# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINERS
from L00_rules      import RULES

from L50_rules      import C50_ProcessingRule, C50_ProcessingRules


class C60_ProcessingRule(C50_ProcessingRule):
	""" Правило обработки данных: Механика данных """

	# Параметры
	def RuleType(self, rule_type: RULES = None) -> RULES:
		""" Тип правила """
		if rule_type is None: return RULES(self.f_rule_type.ToString(CONTAINERS.DISK).data)
		else                :              self.f_rule_type.FromString(CONTAINERS.DISK, rule_type.value)

	def InputAsString(self, text: str = None) -> str:
		""" Вход как строка """
		if text is None: return self.f_input.ToString(CONTAINERS.DISK).data
		else           :        self.f_input.FromString(CONTAINERS.DISK, text)

	def InputAsStrings(self, items: list[str] = None) -> list[str]:
		""" Вход как список строк """
		if items is None: return list(sorted(self.f_input.ToStrings(CONTAINERS.DISK).data))
		else            :                    self.f_input.FromStrings(CONTAINERS.DISK, sorted(items))

	def OutputAsString(self, text: str = None) -> str:
		""" Выход как строка """
		if text is None: return self.f_output.ToString(CONTAINERS.DISK).data
		else           :        self.f_output.FromString(CONTAINERS.DISK, text)

	def OutputAsStrings(self, items: list[str] = None) -> list[str]:
		""" Выход как список строк """
		if items is None: return list(sorted(self.f_output.ToStrings(CONTAINERS.DISK).data))
		else            :                    self.f_output.FromStrings(CONTAINERS.DISK, sorted(items))


class C60_ProcessingRules(C50_ProcessingRules):
	""" Правила обработки данных: Механика данных """
	pass
