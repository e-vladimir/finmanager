# ФОРМА АНАЛИТИКА: ЛОГИКА ДАННЫХ

from G10_datetime       import CalcDyDmByShiftDm

from L00_containers     import CONTAINERS
from L00_months         import MONTHS_SHORT
from L20_PySide6        import RequestConfirm, RequestItems, RequestText
from L20_data_struct    import T20_StatisticItem
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

	def DeleteAnalyticsItem(self):
		""" Удаление элемента аналитики """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		if not RequestConfirm("Элементы аналитики", f"Удаление элемента аналитики:\n{analytics_item.Name()}"): return

		analytics_item.DeleteObject(CONTAINERS.DISK)

	def EditNameAnalyticsItem(self):
		""" Редактирование названия элемента аналитики """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		name : str | None = RequestText("Элемент аналитики", "Редактирование названия элемента аналитики", analytics_item.Name())
		if     name is None                  : return

		name = name.strip()
		if not name: return
		if     name in self.analytics.Names(): return

		analytics_item.Name(name)

	# Параметры
	def EditOptionsInclude(self):
		""" Редактирование признаков включения """
		analytics_item            = C90_AnalyticsItem(self._processing_ido)
		labels                    = RequestItems("Элемент аналитики",
		                                         "Параметры включения",
		                                         self.operations.Labels(),
		                                         analytics_item.Include())
		if labels is None: return

		analytics_item.Include(labels)

	def EditOptionsExclude(self):
		""" Редактирование признаков исключения """
		analytics_item            = C90_AnalyticsItem(self._processing_ido)
		labels                    = RequestItems("Элемент аналитики",
		                                         "Параметры исключения",
		                                         self.operations.Labels(),
		                                         analytics_item.Exclude())
		if labels is None: return

		analytics_item.Exclude(labels)

	# Динамика
	def CalcDynamic(self):
		""" Расчёт данных динамики """
		dy, dm              = self.workspace.DyDm()
		analytics_item      = C90_AnalyticsItem(self._processing_ido)

		statistics_items : list[T20_StatisticItem] = []

		for _ in range(12):
			statistics_item = analytics_item.CalcAmountsInDm(dy, dm)
			statistics_item.caption =f"{MONTHS_SHORT[dm]}\n{dy}"
			statistics_items.append(statistics_item)

			dy, dm = CalcDyDmByShiftDm(dy, dm, -1)

		self.dia_data_dynamic._statistics = list(reversed(statistics_items[:]))
		self.dia_data_dynamic.update()
