# ФОРМА АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список элементов аналитики
		self.list_items.clicked.connect(self.on_AnalyticsItemSelected)
		self.list_items.doubleClicked.connect(self.on_RequestEditAnalyticsItemName)
		self.list_items.customContextMenuRequested.connect(self.on_RequestShowMenuItems)

		# Дерево параметров элемента аналитики
		self.tree_data_item.doubleClicked.connect(self.on_RequestProcessingTreeDataItem_DbClick)

		# Дерево данных Структура месяца
		self.tree_data_dm.doubleClicked.connect(self.on_ProcessingObjectSelected)

		# Меню Элементы аналитики
		self.action_items_create_item.triggered.connect(self.on_RequestCreateAnalyticsItem)
		self.action_items_delete_item.triggered.connect(self.on_RequestDeleteAnalyticsItem)
		self.action_items_edit_item_name.triggered.connect(self.on_RequestEditAnalyticsItemName)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.InitModelDataItems()
		self.ShowAnalyticsItems()
		self.AdjustListItems_Sort()

		self.InitModelDataItem()
		self.AdjustTreeDataItem_Size()
		self.AdjustTreeDataItem_Color()
		self.AdjustTreeDataItem_Expand()

		self.InitModelDataDm()
		self.LoadModelDataDm()
		self.AdjustTreeDataDm_Expand()
		self.AdjustTreeDataDm_Size()
		self.AdjustTreeDataDm_Color()
		self.AdjustTreeDataDm_Sort()

		self.InitModelDataDy()
		self.AdjustTreeDataDy_Size()
		self.AdjustTreeDataDy_Color()
		self.AdjustTreeDataDy_Expand()

		self.ShowTitle()

	# Элемент аналитики
	def on_AnalyticsItemSelected(self):
		""" Выбран элемент аналитики """
		self.ReadProcessingIdoFromListItems()
		self.LoadModelDataItem()

	def on_RequestCreateAnalyticsItem(self):
		""" Запрос на создание элемента аналитики """
		self.CreateAnalyticsItem()

		self.ShowAnalyticsItems()
		self.AdjustListItems_Sort()

	def on_RequestDeleteAnalyticsItem(self):
		""" Запрос на удаление элемента аналитики """
		self.DeleteAnalyticsItem()

		self.InitModelDataItems()
		self.ShowAnalyticsItems()

		self.InitModelDataItem()

	def on_RequestEditAnalyticsItemName(self):
		""" Запрос на редактирование названия элемента аналитики """
		self.ReadProcessingIdoFromListItems()
		self.EditAnalyticsItemName()
		self.LoadItemInModelDataItems()
		self.AdjustListItems_Sort()

	def on_RequestEditAnalyticsItemInclude(self):
		""" Запрос редактирования Признаки+ """
		self.ReadProcessingIdoFromListItems()
		self.EditAnalyticsItemInclude()
		self.LoadModelDataItem()

	def on_RequestEditAnalyticsItemExclude(self):
		""" Запрос редактирования Признаки- """
		self.ReadProcessingIdoFromListItems()
		self.EditAnalyticsItemExclude()
		self.LoadModelDataItem()

	# Дерево параметров элемент аналитики
	def on_RequestProcessingTreeDataItem_DbClick(self):
		""" Запрос на обработку двойного клика по дереву параметров элемента аналитики """
		self.ReadProcessingIdoFromTreeDataItem()
		self.ProcessingTreeDataItem_DbClick()

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self):
		""" Запрос на отображение меню Элементы аналитики """
		self.ReadProcessingIdoFromListItems()

		self.LoadModelDataItem()

		self.AdjustMenuItems_Text()
		self.AdjustMenuItems_Enable()

		self.ShowMenuItems()

	# Параметры аналитики
	def on_ProcessingObjectSelected(self):
		""" Выбран объект обработки """
		self.ReadProcessingObjectFromTreeDataDm()

		self.InitModelDataDy()
		self.LoadModelDataDy()
		self.AdjustTreeDataDy_Expand()
		self.AdjustTreeDataDy_Color()

		self.AdjustTabsMain_Text()
