# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L00_rules              import RULES
from L70_rules              import C70_ProcessingRules, C70_ProcessingRulesRecord


class C80_ProcessingRulesRecord(C70_ProcessingRulesRecord):
	""" Правило обработки данных: Логика данных """
	pass


class C80_ProcessingRules(C70_ProcessingRules):
	""" Правила обработки данных: Логика данных """

	# Выборки данных
	def IdosByType(self, rules_type: RULES) -> list[str]:
		""" Список IDO указанного типа правил """
		record      = C80_ProcessingRulesRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.FilterIdpVlpByEqual(record.f_type.Idp().data, rules_type)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.Idos().data
