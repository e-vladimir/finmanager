# ФОРМА АНАЛИТИКА: ЛОГИКА ДАННЫХ

from L00_containers     import CONTAINERS
from L20_PySide6 import RequestConfirm, RequestItems, RequestMultipleText, RequestText
from L70_form_analytics import C70_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C80_FormAnalytics(C70_FormAnalytics):
	""" Форма Аналитика: Логика данных """

	# Элементы аналитики
	def ShowAnalyticsItems(self):
		""" Отображение элементов аналитики """
		for self._processing_ido in self.analytics.Idos(): self.LoadAnalyticsItemInModel()

	# Элемент аналитики
	def CreateAnalyticsItem(self):
		""" Создание элемента аналитики """
		name : str | None = RequestText("Элемент аналитики", "Создание элемента аналитики", "")

		if     name is None                  : return
		if     name in self.analytics.Names(): return
		if not name.strip()                  : return

		analytics_item = C90_AnalyticsItem()
		analytics_item.GenerateIdo()
		analytics_item.RegisterObject(CONTAINERS.DISK)

		analytics_item.Name(name)

	def DeleteAnalyticsItem(self):
		""" Удаление элемента аналитики """
		if not self._processing_ido: return

		analytics_item = C90_AnalyticsItem(self._processing_ido)

		if not RequestConfirm("Элементы аналитики", f"Удаление: {analytics_item.Name()}"): return

		analytics_item.DeleteObject(CONTAINERS.DISK)

	def EditNameAnalyticsItem(self):
		""" Редактирование наименования элемента аналитики """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		name : str | None = RequestText("Элемент аналитики", "Редактирование названия", analytics_item.Name())
		if name is None: return

		analytics_item.Name(name)

	def EditIncludeAnalyticsItem(self):
		""" Редактирование признаков включения """
		analytics_item           = C90_AnalyticsItem(self._processing_ido)

		items : list[str] | None = RequestMultipleText("Элемент аналитики", f"{analytics_item.Name()}\n\nКритерии включения (+)", analytics_item.Include())
		if items is None: return

		analytics_item.Include(items)

	def ExpandIncludeAnalyticsItem(self):
		""" Расширение признаков включения """
		analytics_item            = C90_AnalyticsItem(self._processing_ido)

		labels : list[str] | None = self.operations.Labels()
		labels                    = RequestItems("Элемент аналитики", f"{analytics_item.Name()}\n\nРасширение критериев включения (+)", labels, analytics_item.Include())
		if labels is None: return

		analytics_item.Include(list(set(analytics_item.Include()).union(set(labels))))

	def EditExcludeAnalyticsItem(self):
		""" Редактирование признаков отключения """
		analytics_item           = C90_AnalyticsItem(self._processing_ido)

		items : list[str] | None = RequestMultipleText("Элемент аналитики", f"{analytics_item.Name()}\n\nКритерии исключения (-)", analytics_item.Exclude())
		if items is None: return

		analytics_item.Exclude(items)

	def ExpandExcludeAnalyticsItem(self):
		""" Расширение признаков исключения """
		analytics_item            = C90_AnalyticsItem(self._processing_ido)

		labels : list[str] | None = self.operations.Labels()
		labels                    = RequestItems("Элемент аналитики", f"{analytics_item.Name()}\n\nРасширение критериев исключения (-)", labels, analytics_item.Exclude())
		if labels is None: return

		analytics_item.Exclude(list(set(analytics_item.Exclude()).union(set(labels))))
