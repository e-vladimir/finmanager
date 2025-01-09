# АНАЛИТИКА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L20_data_struct        import T20_StatisticItem
from L70_analytics          import C70_Analytics, C70_AnalyticsItem
from L90_operations         import C90_Operation


class C80_AnalyticsItem(C70_AnalyticsItem):
	""" Элемент аналитики: Логика данных """

	# Расчёты
	def ProcessingDm(self, dy: int, dm: int) -> T20_StatisticItem:
		""" Обработка месяца """
		result                    = T20_StatisticItem()

		operation                 = C90_Operation()
		idc           : str       = operation.Idc().data
		idp_dy        : str       = operation.f_dy.Idp().data
		idp_dm        : str       = operation.f_dm.Idp().data
		idp_amount    : str       = operation.f_amount.Idp().data
		idp_labels    : str       = operation.f_labels.Idp().data

		filter_data               = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		for label in self.Include(): filter_data.FilterIdpVlpByInclude(idp_labels, label)
		for label in self.Exclude(): filter_data.FilterIdpVlpByInclude(idp_labels, label, flag_invert=True)
		filter_data.Capture(CONTAINERS.DISK)

		amounts       : list[int] = filter_data.ToIntegers(idp_amount).data

		result.amount_income  = sum(filter(lambda amount: amount > 0, amounts))
		result.amount_outcome = sum(filter(lambda amount: amount < 0, amounts))

		return result


class C80_Analytics(C70_Analytics):
	""" Аналитика: Логика данных """

	# Элементы аналитики
	def Idos(self) -> list[str]:
		""" Список IDO с сортировкой по наименованию """
		item           = C80_AnalyticsItem()

		idc      : str = item.Idc().data
		idp_name : str = item.f_name.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_name).data

	def Names(self) -> list[str]:
		""" Список названий элементов аналитики """
		item           = C80_AnalyticsItem()

		idc      : str = item.Idc().data
		idp_name : str = item.f_name.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_name, True, True).data
