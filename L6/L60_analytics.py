# АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINERS
from L50_analytics  import C50_AnalyticsItem, C50_Analytics


class C60_AnalyticsItem(C50_AnalyticsItem):
	""" Элемент аналитики: Механика данных """

	def Name(self, text: str = None) -> str:
		""" Название """
		if text is None : return self.f_name.ToString(CONTAINERS.DISK).data
		else            :        self.f_name.FromString(CONTAINERS.DISK, text)


class C60_Analytics(C50_Analytics):
	""" Аналитика: Механика данных """
	pass
