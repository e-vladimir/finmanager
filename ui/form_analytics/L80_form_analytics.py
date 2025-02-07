# ФОРМА АНАЛИТИКА: ЛОГИКА ДАННЫХ

from L00_containers     import CONTAINERS
from L20_PySide6        import RequestConfirm, RequestItems, RequestText, RequestValue
from L70_form_analytics import C70_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C80_FormAnalytics(C70_FormAnalytics):
	""" Форма Аналитика: Логика данных """

	# Элементы аналитики
	def ShowAnalyticsItems(self):
		""" Отображение списка элементов аналитики """
		for self._processing_ido in self.analytics.Idos(): self.LoadItemInModelDataItems()

	# Элемент аналитики
	def CreateAnalyticsItem(self):
		""" Создание элемента аналитики """
		name : str | None = RequestText("Элементы аналитики", "Создание элемента аналитики.\n\nНазвание:")
		if name is None                  : return
		if name in self.analytics.Names(): return

		analytic_item     = C90_AnalyticsItem()
		analytic_item.GenerateIdo()
		analytic_item.RegisterObject(CONTAINERS.DISK)

		analytic_item.Name(name)

	def DeleteAnalyticsItem(self):
		""" Удаление элемента аналитики """
		if not self._processing_ido: return

		analytics_item = C90_AnalyticsItem(self._processing_ido)

		if not RequestConfirm("Элементы аналитики",
		                      f"Удаление элемента аналитики {analytics_item.Name()}"): return

		analytics_item.DeleteObject(CONTAINERS.DISK)

	def EditAnalyticsItemInclude(self):
		""" Редактирование признаков+ элемента аналитики """
		if not self._processing_ido: return

		analytics_item             = C90_AnalyticsItem(self._processing_ido)

		labels  : set[str]         = (set(self.operations.Destinations()).union(self.operations.Details())
		                                                                 .union(self.operations.ObjectsInt())
		                                                                 .union(self.operations.ObjectsExt())
 		                              )

		include : list[str] | None = RequestItems( "Элемент аналитики",
		                                          f"{analytics_item.Name()}\n\nПризнаки+:",
		                                          sorted(labels),
		                                          analytics_item.Include()
		                                          )
		if not include: return

		analytics_item.Include(include)

	def EditAnalyticsItemExclude(self):
		""" Редактирование признаков- элемента аналитики """
		if not self._processing_ido: return

		analytics_item             = C90_AnalyticsItem(self._processing_ido)

		labels  : set[str]         = (set(self.operations.Destinations()).union(self.operations.Details())
		                                                                 .union(self.operations.ObjectsInt())
		                                                                 .union(self.operations.ObjectsExt())
 		                              )

		exclude : list[str] | None = RequestItems( "Элемент аналитики",
		                                          f"{analytics_item.Name()}\n\nПризнаки-:",
		                                          sorted(labels),
		                                          analytics_item.Include()
		                                          )
		if not exclude: return

		analytics_item.Exclude(exclude)

	def EditAnalyticsItemName(self):
		""" Редактирование названия элемента аналитики """
		if not self._processing_ido: return

		analytics_item    = C90_AnalyticsItem(self._processing_ido)

		name : str | None = RequestText("Элемент аналитики",
		                                f"{analytics_item.Name()}",
		                                analytics_item.Name())
		if name is None                  : return
		if name in self.analytics.Names(): return

		analytics_item.Name(name)

	def EditAnalyticsItemMeasurementUnit(self):
		""" Редактирование названия единицы объёмного измерения """
		if not self._processing_ido: return

		analytics_item    = C90_AnalyticsItem(self._processing_ido)

		unit : str | None = RequestText("Элемент аналитики",
		                                f"{analytics_item.Name()}\n\nЕдиницы объёмного измерения:",
		                                analytics_item.MeasurementUnit())
		if unit is None                  : return

		analytics_item.MeasurementUnit(unit)

	def EditAnalyticsItemMeasurementValue(self):
		""" Редактирование названия объёма измерения """
		if not self._processing_ido: return

		analytics_item     = C90_AnalyticsItem(self._processing_ido)

		value : int | None = RequestValue("Элемент аналитики",
		                                  f"{analytics_item.Name()}\n\nОбъём измерения:",
		                                  analytics_item.MeasurementValue(),
		                                  -99999999,
		                                   99999999)
		if value is None                  : return

		analytics_item.MeasurementValue(value)
