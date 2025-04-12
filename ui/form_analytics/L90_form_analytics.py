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

		# Меню элементов аналитики
		self.ActionCreateItem.triggered.connect(self.on_RequestCreateItem)
		self.ActionDeleteItem.triggered.connect(self.on_RequestDeleteItem)
		self.ActionEditItemName.triggered.connect(self.on_RequestEditItemName)


	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.SwitchTabsMainToItems()

		self.ShowTitle()

		self.InitModelDataItems()
		self.LoadAnalyticsItems()
		self.AdjustListItems_Sort()

		self.InitModelDataItem()
		self.LoadModelDataItem()
		self.AdjustTreeDataItem_Color()
		self.AdjustTreeDataItem_Size()
		self.AdjustTreeDataItem_Expand()


	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self):
		""" Запрос отображения меню элементов аналитики """
		self.ReadProcessingIdoFromListDataItems()

		self.AdjustMenuItems()
		self.AdjustMenuItems_Text()
		self.AdjustMenuItems_Enable()

		self.ShowMenuItems()


	# Элемент аналитики
	def on_RequestCreateItem(self):
		""" Запрос создания элемента аналитики """
		self.CreateItem()

	def on_RequestDeleteItem(self):
		""" Запрос удаления элемента аналитики """
		self.DeleteItem()

	def on_RequestEditItemName(self):
		""" Запрос редактирования названия элемента аналитики """
		self.EditItemName()

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
