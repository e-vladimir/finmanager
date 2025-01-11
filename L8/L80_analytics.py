# АНАЛИТИКА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L20_data_struct        import T20_StatisticItem
from L90_operations         import C90_Operation
from L70_analytics          import C70_AnalyticsItem, C70_Analytics


class C80_AnalyticsItem(C70_AnalyticsItem):
	""" Элемент аналитики: Логика данных """

	def CaptureIdos(self, dy: int = None, dm: int = None) -> list[str]:
		""" Захват списка IDO в указанном месяце """
		result  : list[str] = []

		include : set[str]  = set(self.Include())
		exclude : set[str]  = set(self.Exclude())

		operation           = C90_Operation()
		idc     : str       = operation.Idc().data
		idp_dy  : str       = operation.f_dy.Idp().data
		idp_dm  : str       = operation.f_dm.Idp().data

		filter_data         = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		for ido in filter_data.Idos().data:
			operation.Ido(ido)

			labels : set[str] = set(operation.Labels())

			if     labels.intersection(exclude): continue
			if not labels.intersection(include): continue

			result.append(ido)

		return result

	def CalcAmountsInDm(self, dy: int, dm: int) -> T20_StatisticItem:
		""" Расчёт объёмов в месяце """
		amounts : list[float] = list(map(lambda ido: C90_Operation(ido).Amount(), self.CaptureIdos(dy, dm)))

		result                = T20_StatisticItem()
		result.amount_income  = sum(filter(lambda amount: amount > 0, amounts))
		result.amount_outcome = sum(filter(lambda amount: amount < 0, amounts))

		return result


class C80_Analytics(C70_Analytics):
	""" Аналитика: Логика данных """

	# Элементы аналитики
	def Idos(self) -> list[str]:
		""" Список IDO элементов аналитики """
		analytics_item = C80_AnalyticsItem()
		idc      : str = analytics_item.Idc().data
		idp_name : str = analytics_item.f_name.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_name).data

	def Names(self) -> list[str]:
		""" Список названий элементов аналитики """
		analytics_item = C80_AnalyticsItem()
		idc      : str = analytics_item.Idc().data
		idp_name : str = analytics_item.f_name.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_name, True, True).data
