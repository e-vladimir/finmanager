# ФОРМА АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список Элементы аналитики
		self.list_items.customContextMenuRequested.connect(self.on_RequestShowMenuItems)

		# Меню Элементы аналитики
		self.action_items_create_item.triggered.connect(self.on_RequestCreateAnalyticsItem)
		self.action_items_delete_item.triggered.connect(self.on_RequestDeleteAnalyticsItem)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()
		self.SwitchTabsToOptions()

		self.InitModelItems()
		self.InitModelDataOptions()
		self.InitModelDataVolumes()

		self.ShowAnalyticsItems()

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self):
		""" Запрос вызова меню Элементы аналитики """
		self.ReadProcessingIdoFromListItems()

		self.AdjustMenuItems_Text()
		self.AdjustMenuItems_Enable()

		self.ShowMenuItems()

	# Элемент аналитики
	def on_RequestCreateAnalyticsItem(self):
		""" Запрос на создание элемента аналитики """
		self.CreateAnalyticsItem()

		self.ShowAnalyticsItems()

	def on_RequestDeleteAnalyticsItem(self):
		""" Запрос на удаление элемента аналитики """
		self.DeleteAnalyticsItem()

		self.InitModelItems()
		self.ShowAnalyticsItems()
