# ФОРМА СТАТИСТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_statistic import C80_FormStatistic


class C90_FormStatistic(C80_FormStatistic):
	""" Форма Статистика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево структуры статистики
		self.tree_statistic_struct.doubleClicked.connect(self.on_RequestExpandStatistic)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.SwitchPagesToFirst()

		self.ShowTitle()

		self.InitModelStatistic()
		self.LoadStatisticInModelStatistic()
		self.AdjustTableStatistic_Size()
		self.AdjustTableStatistic_Sort()

		self.InitModelStatisticStruct()
		self.ReadProcessingItemFromTreeStatisticStruct()
		self.ReadProcessingLabelsFromCurrentItem()
		self.LoadModelStatisticStruct()
		self.AdjustTreeStatisticStruct_Size()
		self.AdjustTreeStatisticStruct_Sort()

		self.InitModelAnalytics()
		self.ShowAnalytics()
		self.AdjustTreeAnalytics_Size()
		self.AdjustTreeAnalytics_Sort()

	# Дерево структуры статистики
	def on_RequestExpandStatistic(self):
		""" Запрос на раскрытие статистики """
		self.ReadProcessingItemFromTreeStatisticStruct()
		self.ReadProcessingLabelsFromCurrentItem()

		self.LoadModelStatisticStruct()

		self.ExpandTreeStatisticStruct()
