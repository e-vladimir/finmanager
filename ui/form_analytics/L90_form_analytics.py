# ФОРМА АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список элементов аналитики
		self.list_items.clicked.connect(self.on_AnalyticsItemSelected)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.InitModelDataItems()
		self.ShowItems()
		self.AdjustListItems_Sort()

		self.InitModelItem()
		self.AdjustTreeDataItem_Size()
		self.AdjustTreeDataItem_Color()
		self.AdjustTreeDataItem_Expand()

	# Элемент аналитики
	def on_AnalyticsItemSelected(self):
		""" Выбран элемент аналитики """
		self.ReadProcessingIdoFromListItems()
		self.LoadModelItem()
