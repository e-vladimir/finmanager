# АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L50_analytics          import C50_Analytics, C50_AnalyticsItem


class C60_AnalyticsItem(C50_AnalyticsItem):
	""" Элемент аналитики: Механика данных """

	def Name(self, text: str = None) -> str | None:
		""" Название """
		if text is None : return self.f_name.ToString(CONTAINERS.DISK).data
		else            :        self.f_name.FromString(CONTAINERS.DISK, text)

	def Include(self, items: list[str] = None) -> list[str] | None:
		""" Признаки+ """
		if items is None : return self.f_include.ToStrings(CONTAINERS.DISK).data
		else             :        self.f_include.FromStrings(CONTAINERS.DISK, items)

	def Exclude(self, items: list[str] = None) -> list[str] | None:
		""" Признаки- """
		if items is None : return self.f_exclude.ToStrings(CONTAINERS.DISK).data
		else             :        self.f_exclude.FromStrings(CONTAINERS.DISK, items)

	# Переключение
	def SwitchByName(self, name: str) -> bool:
		""" Переключение по названию """
		idc       : str       = self.Idc().data
		idp_name  : str       = self.f_name.Idp().data

		filter_items          = C30_FilterLinear1D(idc)
		filter_items.FilterIdpVlpByEqual(idp_name, name)
		filter_items.Capture(CONTAINERS.DISK)

		idos      : list[str] = filter_items.Idos().data
		if not idos: return False

		self.Ido(idos[0])

		return True


class C60_Analytics(C50_Analytics):
	""" Аналитика: Механика данных """
	pass
