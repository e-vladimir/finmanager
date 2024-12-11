# АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINERS
from L50_analytics  import C50_AnalyticsItem


class C60_AnalyticsItem(C50_AnalyticsItem):
	""" Фрагмент аналитики: Механика данных """

	# Параметры
	def Name(self, text: str = None) -> str:
		""" Наименование """
		if text is None: return self.f_name.ToString(CONTAINERS.DISK).data
		else           :        self.f_name.FromString(CONTAINERS.DISK, text)

	def LabelsInclude(self, labels: list[str] = None) -> list[str]:
		""" Метки включения """
		if labels is None: return self.f_labels_include.ToStrings(CONTAINERS.DISK).data
		else             :        self.f_labels_include.FromStrings(CONTAINERS.DISK, labels)

	def LabelsExclude(self, labels: list[str] = None) -> list[str]:
		""" Метки исключения """
		if labels is None: return self.f_labels_exclude.ToStrings(CONTAINERS.DISK).data
		else             :        self.f_labels_exclude.FromStrings(CONTAINERS.DISK, labels)
