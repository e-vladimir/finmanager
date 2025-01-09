# ФОРМА АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список элементов аналитики
		self.list_items.clicked.connect(self.on_AnalyticsItemSelected)
		self.list_items.customContextMenuRequested.connect(self.on_RequestShowMenuItems)

		# Меню элементов аналитики
		self.action_items_create_item.triggered.connect(self.on_RequestCreateAnalyticsItem)
		self.action_item_delete_item.triggered.connect(self.on_RequestDeleteAnalyticsItem)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelItems()
		self.ShowAnalyticsItems()

		self.InitModelData()

	# Элемент аналитики
	def on_AnalyticsItemSelected(self):
		""" Выбран элемент аналитики """
		self.ReadProcessingIdoFromListItems()
		self.LoadAnalyticsItemInModelData()

	def on_RequestCreateAnalyticsItem(self):
		""" Запрос создания элемента аналитики """
		self.CreateAnalyticsItem()

		self.ShowAnalyticsItems()

		self.AdjustListItems_Sort()

	def on_RequestDeleteAnalyticsItem(self):
		""" Запрос удаления элемента аналитики """
		self.DeleteAnalyticItem()

		self.InitModelItems()
		self.ShowAnalyticsItems()

	# Меню элементов аналитики
	def on_RequestShowMenuItems(self):
		""" Запрос отображения меню элементов аналитики """
		self.ReadProcessingIdoFromListItems()

		self.AdjustMenuItems_Text()
		self.AdjustMenuItems_Enable()

		self.ShowMenuItems()
