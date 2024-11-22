# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L00_rules              import RULES
from L70_rules              import C70_ProcessingRule, C70_ProcessingRules


class C80_ProcessingRule(C70_ProcessingRule):
	""" Правило обработки данных: Логика данных """
	pass


class C80_ProcessingRules(C70_ProcessingRules):
	""" Правила обработки данных: Логика данных """

	# Тип правил обработки данных
	def IdosByType(self, rules_type: RULES, sort_by_output: bool = False) -> list[str]:
		""" Список IDO правил по типу правил обработки данных """
		rule       = C80_ProcessingRule()
		idc        = rule.Idc().data
		idp_type   = rule.f_type.Idp().data
		idp_input  = rule.f_input.Idp().data
		idp_output = rule.f_output.Idp().data

		filter_data = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_type, rules_type.value)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_output if sort_by_output else idp_input).data
