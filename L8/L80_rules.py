# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ
# 30 мар 2025

from G30_cactus_datafilters import C30_FilterLinear1D
from L00_containers         import CONTAINERS
from L00_rules              import RULES
from L70_rules              import C70_ProcessingRule, C70_ProcessingRules


class C80_ProcessingRule(C70_ProcessingRule):
	""" Правило обработки данных: Логика данных """
	pass


class C80_ProcessingRules(C70_ProcessingRules):
	""" Правила обработки данных: Логика данных """

	# Выборка данных
	@classmethod
	def Idos(cls, rules_type: RULES) -> list[str]:
		""" Список IDO """
		rule       = C80_ProcessingRule()
		idc        = rule.Idc().data
		idp_type   = rule.FRulesType.Idp().data
		idp_input  = rule.FInput.Idp().data
		idp_output = rule.FOutput.Idp().data
		idp_block  = rule.FBlock.Idp().data

		filter_data = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_type, rules_type)
		filter_data.Capture(CONTAINERS.DISK)

		match rules_type:
			case RULES.NONE               : return filter_data.Idos().data
			case RULES.REPLACE_DESCRIPTION: return filter_data.Idos(idp_output).data

			case _                        : return filter_data.Idos().data
