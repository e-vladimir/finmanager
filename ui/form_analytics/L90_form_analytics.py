# ФОРМА АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица Элементы аналитики
		self.table_items.customContextMenuRequested.connect(self.on_RequestShowMenuItems)
		self.table_items.doubleClicked.connect(self.on_RequestProcessingTableItemsDbClick)

		# Меню Элементы аналитики
		self.action_items_create_item.triggered.connect(self.on_RequestCreateAnalyticsItem)
		self.action_items_item_edit_name.triggered.connect(self.on_RequestEditNameAnalyticsItem)
		self.action_items_item_delete.triggered.connect(self.on_RequestDeleteAnalyticsItem)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.InitModelItems()
		self.ShowAnalyticsItems()

		self.AdjustTableItems_Size()
		self.AdjustTableItems_Sort()

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self):
		""" Запрос отображения меню Элементы аналитики """
		self.ReadProcessingIdoFromTableItems()

		self.AdjustMenuItems_Enable()
		self.AdjustMenuItems_Text()

		self.ShowMenuItems()

	# Таблица Элементы аналитики
	def on_RequestProcessingTableItemsDbClick(self):
		""" Запрос двойной обработки клика по таблице Элементы аналитики """
		self.ReadProcessingIdoFromTableItems()
		self.ReadProcessingColumnFromTableItems()

		self.ProcessingTableItems_DbClick()

	# Элемент аналитики
	def on_RequestCreateAnalyticsItem(self):
		""" Запрос создания элемента аналитики """
		self.CreateAnalyticsItem()

		self.ShowAnalyticsItems()

		self.AdjustTableItems_Sort()
		self.AdjustTableItems_Size()

	def on_RequestDeleteAnalyticsItem(self):
		""" Запрос удаления элемента аналитики """
		self.DeleteAnalyticsItem()

		self.InitModelItems()
		self.ShowAnalyticsItems()

		self.AdjustTableItems_Size()

	def on_RequestEditNameAnalyticsItem(self):
		""" Запрос редактирования названия элемента аналитики """
		self.EditNameAnalyticsItem()

		self.LoadAnalyticsItemInModel()
		self.AdjustTableItems_Sort()
