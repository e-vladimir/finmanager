# ФОРМА АНАЛИТИКА: ЛОГИКА ДАННЫХ

from L00_containers     import CONTAINERS
from L20_PySide6        import RequestText
from L70_form_analytics import C70_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C80_FormAnalytics(C70_FormAnalytics):
	""" Форма Аналитика: Логика данных """

	# Элементы аналитики
	def ShowAnalyticsItems(self):
		""" Отображение элементов аналитики """
		for self._processing_ido in self.analytics.Idos(): self.LoadItemAnalyticsInModelItems()

	# Элемент аналитики
	def CreateAnalyticsItem(self):
		""" Создание элемента аналитики """
		name : str | None = RequestText("Элемент аналитики", "Создание элемента аналитики")
		if     name is None                  : return

		name = name.strip()
		if not name: return
		if     name in self.analytics.Names(): return

		analytics_item = C90_AnalyticsItem()
		analytics_item.GenerateIdo()
		analytics_item.RegisterObject(CONTAINERS.DISK)

		analytics_item.Name(name)
