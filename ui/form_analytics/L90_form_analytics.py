# ФОРМА АНАЛИТИКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 27 апр 2025

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.TreeData.customContextMenuRequested.connect(self.on_RequestShowMenuStruct)
		self.TreeData.doubleClicked.connect(self.on_TreeDataDbClicked)


		# Меню структуры данных
		self.ActionCreateTopDestination.triggered.connect(self.on_RequestCreateTopDestination)
		self.ActionResetDestinations.triggered.connect(self.on_RequestResetDestinations)

		self.ActionCreateDestination.triggered.connect(self.on_RequestCreateDestination)
		self.ActionCreateSubDestination.triggered.connect(self.on_RequestCreateSubDestination)
		self.ActionEditDestinationName.triggered.connect(self.on_RequestEditDestinationName)
		self.ActionDeleteDestination.triggered.connect(self.on_RequestDeleteDestination)


	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.ShowTitle()

		self.InitModelData()
		self.LoadDistributionInModel()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataSort()
		self.AdjustTreeDataSize()
		self.AdjustTreeDataColor()


	# Меню структуры аналитики
	def on_RequestShowMenuStruct(self):
		""" Запрос отображению меню структуры аналитики """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingParentFromTreeData()
		self.ReadProcessingGroupFromTreeData()

		self.AdjustMenuStruct()
		self.AdjustMenuStructEnable()
		self.AdjustMenuStructText()

		self.ShowMenuStruct()


	# Структура аналитики
	def on_RequestResetDestinations(self):
		""" Запрос сброса элементов аналитики """
		self.ResetDestinations()

	def on_StructChanged(self):
		""" Структура данных изменилась """
		self.ResetDistributionInModel()
		self.LoadDistributionInModel()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataSort()
		self.AdjustTreeDataSize()
		self.AdjustTreeDataColor()


	# Элемент структуры аналитики
	def on_RequestCreateTopDestination(self):
		""" Запрос на создание общего назначения """
		self.processing_parent = ""

		self.CreateDestination()

	def on_RequestCreateDestination(self):
		""" Запрос создания назначения """
		self.CreateDestination()

	def on_RequestCreateSubDestination(self):
		""" Запрос на уточнение назначения """
		self.processing_parent = self.processing_ido
		self.processing_ido    = ""

		self.CreateDestination()

	def on_RequestEditDestinationName(self):
		""" Запрос редактирования названия назначения """
		self.EditDestinationName()

	def on_RequestDeleteDestination(self):
		""" Запрос удаления назначения """
		self.DeleteDestination()

	def on_DestinationCreated(self):
		""" Создан элемент аналитики """
		self.LoadDistributionInModel()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataSort()
		self.AdjustTreeDataSize()
		self.AdjustTreeDataColor()

	def on_DestinationChanged(self):
		""" Изменился элемент аналитики """
		self.LoadDistributionInModel()
		self.AdjustTreeDataSort()


	# Дерево данных
	def on_TreeDataDbClicked(self):
		""" Двойной клик по дереву данных """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingParentFromTreeData()
		self.ReadProcessingGroupFromTreeData()

		self.ProcessingTreeDataDbClick()
