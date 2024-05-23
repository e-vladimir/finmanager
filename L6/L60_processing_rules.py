# ПРАВИЛА ОБРАБОТКИ: МЕХАНИКА ДАНННЫХ

from L00_containers       import CONTAINER_LOCAL

from L50_processing_rules import C50_RecordProcessingRules, C50_ProcessingRules


class C60_RecordProcessingRules(C50_RecordProcessingRules):
	""" Правило обработки: Механика данных """

	# Тип
	def Type(self, text: str = None) -> str:
		""" Тип """
		if text is None: return self.f_type.ToString(CONTAINER_LOCAL).text
		else           :        self.f_type.FromString(CONTAINER_LOCAL, text)

	# Параметры
	def OptionsInputAsString(self, text: str = None) -> str:
		""" Параметры (строка) """
		if text is None: return self.f_options_input.ToString(CONTAINER_LOCAL).text
		else           :        self.f_options_input.FromString(CONTAINER_LOCAL, text)

	def OptionsInputAsStrings(self, strings : list[str] = None) -> list[str]:
		""" Параметры (список строк) """
		if strings is None: return self.f_options_input.ToStrings(CONTAINER_LOCAL).items
		else              :        self.f_options_input.FromStrings(CONTAINER_LOCAL, sorted(strings))

	# Данные
	def OptionsOutputAsString(self, text: str = None) -> str:
		""" Данные (строка) """
		if text is None: return self.f_options_output.ToString(CONTAINER_LOCAL).text
		else           :        self.f_options_output.FromString(CONTAINER_LOCAL, text)

	def OptionsOutputAsStrings(self, strings : list[str] = None) -> list[str]:
		""" Данные (список строк) """
		if strings is None: return self.f_options_output.ToStrings(CONTAINER_LOCAL).items
		else              :        self.f_options_output.FromStrings(CONTAINER_LOCAL, sorted(strings))


class C60_ProcessingRules(C50_ProcessingRules):
	""" Правила обработки: Механика данных """

	pass
