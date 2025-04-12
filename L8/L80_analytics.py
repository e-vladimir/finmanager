# АНАЛИТИКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 12 апр 2025

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L70_analytics          import C70_Analytics, C70_AnalyticsItem


class C80_AnalyticsItem(C70_AnalyticsItem):
	""" Элемент аналитики данных: Логика данных """
	pass


class C80_Analytics(C70_Analytics):
	""" Аналитика данных: Логика данных """

	# Выборки данных
	@classmethod
	def Names(cls) -> list[str]:
		""" Список названий элементов аналитики """
		analytics_item = C80_AnalyticsItem()
		idc      : str = analytics_item.Idc().data
		idp_name : str = analytics_item.FName.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_name, True, True).data

	@classmethod
	def Idos(cls) -> list[str]:
		""" Список IDO элементов аналитики """
		analytics_item = C80_AnalyticsItem()
		idc      : str = analytics_item.Idc().data
		idp_name : str = analytics_item.FName.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_name).data
