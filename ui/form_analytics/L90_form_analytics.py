# ФОРМА АНАЛИТИКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 11 апр 2025

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список элементов аналитики
		self.ListDataItems.customContextMenuRequested.connect(self.on_RequestShowMenuItems)
		self.ListDataItems.clicked.connect(self.on_ItemSwitched)
		self.ListDataItems.doubleClicked.connect(self.on_RequestEditItemName)

		# Дерево параметров элемента аналитики
		self.TreeDataItem.customContextMenuRequested.connect(self.on_RequestShowMenuItem)
		self.TreeDataItem.doubleClicked.connect(self.on_RequestEditItem)

		# Меню элементов аналитики
		self.ActionCreateItem.triggered.connect(self.on_RequestCreateItem)
		self.ActionDeleteItem.triggered.connect(self.on_RequestDeleteItem)
		self.ActionEditItemName.triggered.connect(self.on_RequestEditItemName)

		# Меню элемента аналитики
		self.ActionEditItemInclude.triggered.connect(self.on_RequestEditItemInclude)
		self.ActionEditItemExclude.triggered.connect(self.on_RequestEditItemExclude)

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.SwitchTabsMainToAnalytics()

		self.ShowTitle()

		self.InitModelDataItems()
		self.LoadAnalyticsItems()
		self.AdjustListItems_Sort()

		self.ReadProcessingIdoFromListDataItems()
		self.ReadProcessingFieldFromTreeDataItem()

		self.InitModelDataItem()
		self.LoadModelDataItem()
		self.AdjustTreeDataItem_Color()
		self.AdjustTreeDataItem_Size()
		self.AdjustTreeDataItem_Expand()

		self.ReadOperations()
		self.ReadDataDynamicDy()

		self.InitModelDataAnalytics()
		self.LoadDataDynamicDyInModel()
		self.LoadDataDynamicDmInModel()
		self.LoadDataOperationsInModel()
		self.LoadDataDistributionInModel()
		self.AdjustTreeDataAnalytics_Expand()
		self.AdjustTreeDataAnalytics_Color()
		self.AdjustTreeDataAnalytics_Size()


	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self):
		""" Запрос отображения меню элементов аналитики """
		self.ReadProcessingIdoFromListDataItems()

		self.AdjustMenuItems()
		self.AdjustMenuItems_Text()
		self.AdjustMenuItems_Enable()

		self.ShowMenuItems()


	# Меню Элемент аналитики
	def on_RequestShowMenuItem(self):
		""" Запрос отображения меню элемента аналитики """
		self.ReadProcessingIdoFromListDataItems()

		self.AdjustMenuItems_Text()

		self.AdjustMenuItem()
		self.AdjustMenuItem_Text()
		self.AdjustMenuItem_Enable()

		self.ShowMenuItem()


	# Элемент аналитики
	def on_RequestCreateItem(self):
		""" Запрос создания элемента аналитики """
		self.CreateItem()

	def on_RequestDeleteItem(self):
		""" Запрос удаления элемента аналитики """
		self.DeleteItem()

	def on_RequestEditItem(self):
		""" Запрос редактирования элемента аналитики """
		self.ReadProcessingFieldFromTreeDataItem()

		self.EditItem()

	def on_RequestEditItemName(self):
		""" Запрос редактирования названия элемента аналитики """
		self.EditItemName()

	def on_RequestEditItemInclude(self):
		""" Запрос редактирования параметра Признаки+ """
		self.EditItemInclude()

	def on_RequestEditItemExclude(self):
		""" Запрос редактирования параметра Признаки- """
		self.EditItemExclude()

	def on_ItemCreated(self):
		""" Создан элемент аналитики """
		self.LoadAnalyticsItemInModel()

		self.AdjustListItems_Sort()

	def on_ItemDeleted(self):
		""" Элемент аналитики удалён """
		self.ClearModelDataItems()
		self.ReadProcessingIdoFromListDataItems()

		self.on_ItemSwitched()

	def on_ItemSwitched(self):
		""" Выбран элемент аналитики """
		self.ReadProcessingIdoFromListDataItems()

		self.LoadModelDataItem()

	def on_ItemChanged(self):
		""" Элемент аналитики изменился """
		self.LoadAnalyticsItemInModel()
		self.AdjustListItems_Sort()

		self.LoadModelDataItem()
