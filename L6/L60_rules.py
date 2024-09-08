# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_LOCAL
from L50_rules      import C50_ProcessingRulesRecord, C50_ProcessingRules


class C60_ProcessingRulesRecord(C50_ProcessingRulesRecord):
	""" Правило обработки данных: Механика данных """

	def Type(self, text: str = None) -> str:
		""" Тип правила """
		if text  is None: return self.f_type.ToString(CONTAINER_LOCAL).data
		else            :        self.f_type.FromString(CONTAINER_LOCAL, text)

	def OptionsInputAsString(self, text: str = None) -> str:
		""" Вход как строка """
		if text  is None: return self.f_options_input.ToString(CONTAINER_LOCAL).data
		else            :        self.f_options_input.FromString(CONTAINER_LOCAL, text)

	def OptionsInputAsStrings(self, texts: list[str] = None) -> list[str]:
		""" Вход как список строк """
		if texts is None: return sorted(self.f_options_input.ToStrings(CONTAINER_LOCAL).data)
		else            :        self.f_options_input.FromStrings(CONTAINER_LOCAL, texts)

	def OptionsOutputAsString(self, text: str = None) -> str:
		""" Выход как строка """
		if text  is None: return self.f_options_output.ToString(CONTAINER_LOCAL).data
		else            :        self.f_options_output.FromString(CONTAINER_LOCAL, text)

	def OptionsOutputAsStrings(self, texts: list[str] = None) -> list[str]:
		""" Выход как список строк """
		if texts is None: return sorted(self.f_options_output.ToStrings(CONTAINER_LOCAL).data)
		else            :        self.f_options_output.FromStrings(CONTAINER_LOCAL, texts)


class C60_ProcessingRules(C50_ProcessingRules):
	""" Правила обработки данных: Механика данных """
	pass
