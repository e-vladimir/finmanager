# ФОРМА АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица Элементов аналитики
		self.table_items.customContextMenuRequested.connect(self.on_RequestMenuItems)

		# Меню Элементы аналитики
		self.action_items_create_item.triggered.connect(self.on_RequestCreateItemAnalytics)

	# Форма
	def on_Open(self):
		""" Отрытие формы """
		self.ShowTitle()

		self.InitModelItems()
		self.ShowAnalyticsItems()

		self.AdjustTableItems_Size()

	# Меню Элементы управления
	def on_RequestMenuItems(self):
		""" Запрос отображения меню элементов аналитики """
		self.AdjustMenuItems_Text()
		self.AdjustMenuItems_Enable()

		self.ShowMenuItems()

	# Элементы аналитики
	def on_RequestCreateItemAnalytics(self):
		""" Создание элемента аналитики """
		self.CreateItemAnalytics()

		self.ShowAnalyticsItems()
