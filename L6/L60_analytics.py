# АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINERS
from L50_analytics  import C50_AnalyticsItem, C50_Analytics


class C60_AnalyticsItem(C50_AnalyticsItem):
	""" Элемент аналитики: Механика данных """

	def Name(self, text: str = None) -> str:
		""" Название """
		if text is None : return self.f_name.ToString(CONTAINERS.DISK).data
		else            :        self.f_name.FromString(CONTAINERS.DISK, text)

	def Include(self, labels: list[str]) -> list[str]:
		""" Признаки включения """
		if labels is None:
			data : list[str] = self.f_include.ToStrings(CONTAINERS.DISK).data
			return list(sorted(data))
		else             :
			data : set[str] = set(labels)
			if '' in data: data.remove('')
			self.f_include.FromStrings(CONTAINERS.DISK, sorted(data))

	def Exclude(self, labels: list[str]) -> list[str]:
		""" Признаки исключения """
		if labels is None:
			data : list[str] = self.f_exclude.ToStrings(CONTAINERS.DISK).data
			return list(sorted(data))
		else             :
			data : set[str] = set(labels)
			if '' in data: data.remove('')
			self.f_exclude.FromStrings(CONTAINERS.DISK, sorted(data))


class C60_Analytics(C50_Analytics):
	""" Аналитика: Механика данных """
	pass
