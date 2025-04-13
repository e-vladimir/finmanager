# ФОРМА АНАЛИТИКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 11 апр 2025

from G10_datetime       import CalcDyDmByShiftDm

from L00_containers     import CONTAINERS
from L20_PySide6        import RequestConfirm, RequestItems, RequestText
from L20_form_analytics import T20_DynamicDyItem
from L70_form_analytics import C70_FormAnalytics
from L90_analytics      import C90_AnalyticsItem
from L90_operations     import C90_Operation


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


	# Данные аналитики
	def CaptureDataAnalytics(self):
		""" Захват данных аналитики данных """
		self._data_dynamic_dy.clear()

		operation = C90_Operation()
		dy, dm    = self.Workspace.DyDm()

		for _ in range(13):
			amount_income  : float = 0
			amount_outcome : float = 0

			for ido in self.Operations.Idos(dy, dm):
				operation.Ido(ido)

				flag_skip : bool      = True

				labels    : list[str] = operation.labels

				flag_skip &=     bool(self.processing_include) and (len(set(labels).intersection(self.processing_include)) == 0)
				flag_skip &= not(bool(self.processing_exclude) and (len(set(labels).intersection(self.processing_exclude)) >  0))

				if flag_skip: continue

				amount    : float     = operation.amount

				if amount > 0: amount_income  += amount
				else         : amount_outcome += amount

			self._data_dynamic_dy.append(T20_DynamicDyItem(dy             = dy,
							                               dm             = dm,
							                               amount_income  = int(amount_income),
							                               amount_outcome = int(amount_outcome)))

			dy, dm               = CalcDyDmByShiftDm(dy, dm, -1)
