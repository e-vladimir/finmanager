# ФОРМА АНАЛИТИКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 11 апр 2025

from L00_containers     import CONTAINERS
from L20_PySide6        import RequestConfirm, RequestItems, RequestText
from L70_form_analytics import C70_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C80_FormAnalytics(C70_FormAnalytics):
	""" Форма Аналитика данных: Логика данных """

	# Список элементов аналитики
	def LoadAnalyticsItems(self):
		""" Загрузка элементов аналитики в модель данных """
		for self.processing_ido in self.Analytics.Idos(): self.LoadAnalyticsItemInModel()


	# Элемент аналитики
	def CreateItem(self):
		""" Создание элемента аналитики """
		name : str | None   = RequestText(f"Управление элементами аналитики",
		                                  f"Создание элемента аналитики\n\nНазвание:")
		if name is None                  : return
		if name in self.Analytics.Names(): return

		analytics_item      = C90_AnalyticsItem()
		analytics_item.GenerateIdo()
		analytics_item.RegisterObject(CONTAINERS.DISK)

		analytics_item.name = name

		self.processing_ido = analytics_item.Ido().data

		self.on_ItemCreated()

	def DeleteItem(self):
		""" Удаление элемента аналитики """
		analytics_item = C90_AnalyticsItem(self.processing_ido)

		if not RequestConfirm(f"Управление элементами аналитики",
		                      f"Удаление {analytics_item.name}"): return

		analytics_item.DeleteObject(CONTAINERS.DISK)

		self.on_ItemDeleted()

	def EditItemName(self):
		""" Редактирование названия элемента аналитики """
		analytics_item = C90_AnalyticsItem(self.processing_ido)

		name : str | None   = RequestText(f"Управление элементами аналитики",
		                                  f"Управление элементом аналитики\n\nНазвание:",
		                                   analytics_item.name)
		if name is None                  : return
		if name in self.Analytics.Names(): return

		analytics_item.name = name

		self.on_ItemChanged()

	def EditItemInclude(self):
		""" Редактирование данных Признаки+ """
		analytics_item = C90_AnalyticsItem(self.processing_ido)

		labels : list[str] | None = RequestItems("Управление элементом аналитики",
		                                         "Признаки+:",
		                                         self.Operations.Labels(),
		                                         analytics_item.include)
		if labels is None: return

		analytics_item.include = labels

		self.on_ItemChanged()

	def EditItemExclude(self):
		""" Редактирование данных Признаки- """
		analytics_item = C90_AnalyticsItem(self.processing_ido)

		labels : list[str] | None = RequestItems("Управление элементом аналитики",
		                                         "Признаки-:",
		                                         self.Operations.Labels(),
		                                         analytics_item.exclude)
		if labels is None: return

		analytics_item.exclude = labels

		self.on_ItemChanged()
