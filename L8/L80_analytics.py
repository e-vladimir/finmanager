# АНАЛИТИКА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L70_analytics          import C70_AnalyticsItem, C70_Analytics


class C80_AnalyticsItem(C70_AnalyticsItem):
	""" Элемент аналитики: Логика данных """
	pass


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
