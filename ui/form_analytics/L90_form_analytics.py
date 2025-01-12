# ФОРМА АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список Элементы аналитики
		self.list_items.customContextMenuRequested.connect(self.on_RequestShowMenuItems)
		self.list_items.doubleClicked.connect(self.on_RequestEditName)
		self.list_items.clicked.connect(self.on_AnalyticsItemSelected)

		# Меню Элементы аналитики
		self.action_items_create_item.triggered.connect(self.on_RequestCreateAnalyticsItem)
		self.action_items_item_edit_name.triggered.connect(self.on_RequestEditName)
		self.action_items_item_delete.triggered.connect(self.on_RequestDeleteAnalyticsItem)

		# Дерево Параметры
		self.tree_data_options.customContextMenuRequested.connect(self.on_RequestShowMenuOptions)
		self.tree_data_options.doubleClicked.connect(self.on_RequestProcessingTreeOptionsDbClick)

		# Дерево Объёмная стоимость
		self.tree_data_volume.doubleClicked.connect(self.on_RequestProcessingTreeVolumesDbClick)

		# Меню Параметры
		self.action_options_edit_include.triggered.connect(self.on_RequestEditInclude)
		self.action_options_edit_exclude.triggered.connect(self.on_RequestEditExclude)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()
		self.SwitchTabsToOptions()

		self.InitModelItems()
		self.ShowAnalyticsItems()

		self.InitModelDataOptions()
		self.AdjustTreeOptions_Expand()
		self.AdjustTreeOptions_Size()
		self.AdjustTreeOptions_Color()

		self.InitDynamic()

		self.InitModelDataVolumes()
		self.AdjustTreeVolumes_Expand()
		self.AdjustTreeVolumes_Size()
		self.AdjustTreeVolumes_Color()

	# Меню Элементы аналитики
	def on_RequestShowMenuItems(self):
		""" Запрос вызова меню Элементы аналитики """
		self.ReadProcessingIdoFromListItems()

		self.AdjustMenuItems_Text()
		self.AdjustMenuItems_Enable()

		self.ShowMenuItems()

	# Меню Параметры
	def on_RequestShowMenuOptions(self):
		""" Запрос вызова меню Параметры """
		self.ReadProcessingIdoFromListItems()

		self.AdjustMenuOptions_Text()
		self.AdjustMenuOptions_Enable()

		self.ShowMenuOptions()

	# Элемент аналитики
	def on_AnalyticsItemSelected(self):
		""" Выбран элемент аналитики """
		self.ReadProcessingIdoFromListItems()

		self.LoadModelDataOptions()

		self.CalcDynamic()

		self.InitModelDataVolumes()
		self.LoadModelDataVolumes()

		self.AdjustTreeVolumes_Expand()
		self.AdjustTreeVolumes_Size()
		self.AdjustTreeVolumes_Color()

	def on_RequestCreateAnalyticsItem(self):
		""" Запрос на создание элемента аналитики """
		self.CreateAnalyticsItem()

		self.ShowAnalyticsItems()

		self.AdjustListItems_Sort()

	def on_RequestDeleteAnalyticsItem(self):
		""" Запрос на удаление элемента аналитики """
		self.DeleteAnalyticsItem()

		self.InitModelItems()
		self.ShowAnalyticsItems()

	def on_RequestEditName(self):
		""" Запрос на редактирование названия элемента аналитики """
		self.ReadProcessingIdoFromListItems()

		self.EditName()

		self.LoadItemAnalyticsInModelItems()

		self.AdjustListItems_Sort()

	def on_RequestEditVolumeTitle(self):
		""" Запрос на редактирование названия ед.изм. """
		self.ReadProcessingIdoFromListItems()

		self.EditVolumeTitle()
		self.LoadModelDataVolumes()

	def on_RequestEditVolumeValue(self):
		""" Запрос на редактирование объёма ед.изм. """
		self.ReadProcessingIdoFromListItems()

		self.EditVolumeValue()
		self.LoadModelDataVolumes()

	# Параметры
	def on_RequestEditInclude(self):
		""" Запрос редактирования признаков включения """
		self.ReadProcessingIdoFromListItems()

		self.EditInclude()

		self.LoadModelDataOptions()

	def on_RequestEditExclude(self):
		""" Запрос редактирования признаков исключения """
		self.ReadProcessingIdoFromListItems()

		self.EditExclude()

		self.LoadModelDataOptions()

	# Дерево Параметры
	def on_RequestProcessingTreeOptionsDbClick(self):
		""" Запрос на обработку двойного клика по дереву параметров """
		self.ReadProcessingIdoFromTreeOptions()

		self.ProcessingTreeOptions_DbClick()

	# Дерево Объёмная стоимость
	def on_RequestProcessingTreeVolumesDbClick(self):
		""" Запрос на обработку двойного клика по дереву Объёмная стоимость """
		self.ReadProcessingIdoFromTreeVolumes()

		self.ProcessingTreeVolumes_DbClick()
