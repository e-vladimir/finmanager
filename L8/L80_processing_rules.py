# ПРАВИЛА ОБРАБОТКИ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL

from L70_processing_rules   import C70_RecordProcessingRules, C70_ProcessingRules


class C80_RecordProcessingRules(C70_RecordProcessingRules):
	""" Правило обработки: Логика данных """

	# Обработка данных
	def ExecReplaceText(self, data_input: str) -> str:
		""" Выполнение замены текстовых фрагментов """
		result        : str = data_input
		option_output : str = self.OptionsOutputAsString()

		for option_input in self.OptionsInputAsStrings(): result = result.replace(option_input, option_output)

		return result

	def ExecDetectFindescription(self, data_input: str) -> str:
		""" Выполнение определения финсостава по текстовых фрагментам """
		option_output : str = self.OptionsOutputAsString()

		for option_input in self.OptionsInputAsStrings():
			if option_input.lower() in data_input.lower(): return option_output

		return ""


class C80_ProcessingRules(C70_ProcessingRules):
	""" Правила обработки: Логика данных """

	# Выборки данных
	def IdosByType(self, processing_type: str = "") -> list[str]:
		""" Список OID записей правил с учётом типа обработки """
		filter_findata = C30_FilterLinear1D(self._idc)

		if processing_type: filter_findata.FilterIdpVlpByEqual(self._idp_type, processing_type)

		filter_findata.Capture(CONTAINER_LOCAL)

		return filter_findata.Idos(self._idp_options_output).data
