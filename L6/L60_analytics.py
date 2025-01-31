# АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINERS
from L50_analytics  import C50_Analytics, C50_AnalyticsItem


class C60_AnalyticsItem(C50_AnalyticsItem):
	""" Элемент аналитики: Механика данных """

	def Name(self, text: str = None) -> str:
		""" Название """
		if text is None : return self.f_name.ToString(CONTAINERS.DISK).data
		else            :        self.f_name.FromString(CONTAINERS.DISK, text)

	def Include(self, items: list[str] = None) -> list[str]:
		""" Признаки+ """
		if items is None : return self.f_include.ToString(CONTAINERS.DISK).data
		else             :        self.f_include.FromString(CONTAINERS.DISK, items)

	def Exclude(self, items: list[str] = None) -> list[str]:
		""" Признаки- """
		if items is None : return self.f_exclude.ToString(CONTAINERS.DISK).data
		else             :        self.f_exclude.FromString(CONTAINERS.DISK, items)


class C60_Analytics(C50_Analytics):
	""" Аналитика: Механика данных """
	pass
