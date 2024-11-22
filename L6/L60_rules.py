# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINERS
from L00_rules      import RULES
from L50_rules      import C50_ProcessingRule, C50_ProcessingRules


class C60_ProcessingRule(C50_ProcessingRule):
	""" Правило обработки данных: Механика данных """

	# Параметры
	def Type(self, value: RULES = None) -> RULES:
		""" Тип правила """
		if value is None  : return RULES(self.f_type.ToString(CONTAINERS.DISK).data)
		else              :              self.f_type.FromString(CONTAINERS.DISK, value.value)

	def InputAsString(self, text: str = None) -> str:
		""" Вход как строка """
		if text is None   : return self.f_input.ToString(CONTAINERS.DISK).data
		else              :        self.f_input.FromString(CONTAINERS.DISK, text)

	def InputAsStrings(self, strings: list[str] = None) -> list[str]:
		""" Вход как список строк """
		if strings is None: return self.f_input.ToStrings(CONTAINERS.DISK).data
		else              :        self.f_input.FromStrings(CONTAINERS.DISK, strings)

	def OutputAsString(self, text: str = None) -> str:
		""" Выход как строка """
		if text is None   : return self.f_output.ToString(CONTAINERS.DISK).data
		else              :        self.f_output.FromString(CONTAINERS.DISK, text)

	def OutputAsStrings(self, strings: list[str] = None) -> list[str]:
		""" Выход как список строк """
		if strings is None: return self.f_output.ToStrings(CONTAINERS.DISK).data
		else              :        self.f_output.FromStrings(CONTAINERS.DISK, strings)


class C60_ProcessingRules(C50_ProcessingRules):
	""" Правила обработки данных: Механика данных """
	pass
