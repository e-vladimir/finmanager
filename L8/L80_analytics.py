# АНАЛИТИКА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L20_struct_statistic   import T20_StructStatistic
from L70_analytics          import C70_Analytics, C70_AnalyticsItem
from L90_operations         import C90_Operation, C90_Operations


class C80_AnalyticsItem(C70_AnalyticsItem):
	""" Элемент аналитики: Логика данных """

	# Захват данных
	def CaptureAmountInDm(self, dy: int, dm: int) -> T20_StructStatistic:
		""" Захват данных для указанного месяца """
		amounts : list[float] = list()

		for ido in C90_Operations.OperationsIdosInDyDmDd(dy, dm):
			operation = C90_Operation(ido)

			labels : set[str] = {operation.Destination(),
			                     operation.ObjectInt(),
			                     operation.ObjectExt()
			                     }

			if not labels.intersection(self.Include()): continue
			if     labels.intersection(self.Exclude()): continue

			amounts.append(operation.Amount())

		return T20_StructStatistic(self.Name(),
		                           int(sum(filter(lambda amount: amount > 0, amounts))),
		                           int(sum(filter(lambda amount: amount < 0, amounts)))
		                           )


class C80_Analytics(C70_Analytics):
	""" Аналитика: Логика данных """

	# Выборки данных
	def Names(self) -> list[str]:
		""" Список названий элементов аналитики """
		analytics_item = C80_AnalyticsItem()
		idc      : str = analytics_item.Idc().data
		idp_name : str = analytics_item.f_name.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_name, True, True).data

	def Idos(self) -> list[str]:
		""" Список IDO элементов аналитики """
		analytics_item = C80_AnalyticsItem()
		idc      : str = analytics_item.Idc().data
		idp_name : str = analytics_item.f_name.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_name).data
