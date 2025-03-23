# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 22 мар 2025

from L80_form_processing import C80_FormProcessing


class C90_FormProcessing(C80_FormProcessing):
	""" Форма Обработка данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных Обработка операций
		self.TreeDataOperations.doubleClicked.connect(self.on_TreeDataProcessingOperationsDoubleClicked)
		self.TreeDataOperations.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)

		# Меню Обработка операций
		self.ActionSetOperationsDescriptionInclude.triggered.connect(self.on_RequestSetOperationsDescriptionInclude)
		self.ActionSetOperationsDescriptionEqual.triggered.connect(self.on_RequestSetOperationsDescriptionEqual)
		self.ActionSetOperationsDescriptionReplace.triggered.connect(self.on_RequestSetOperationsDescriptionReplace)
		self.ActionSetOperationsDescriptionSet.triggered.connect(self.on_RequestSetOperationsDescriptionSet)
		self.ActionSetOperationsColorSet.triggered.connect(self.on_RequestSetOperationsColorSet)
		self.ActionProcessingOperations.triggered.connect(self.on_RequestProcessingOperations)

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.InitModelDataOperation()
		self.LoadModelDataOperations()

		self.AdjustTreeDataOperations_Expand()
		self.AdjustTreeDataOperations_Size()
		self.AdjustTreeDataOperations_Color()

	# Обработка операций
	def on_RequestSetOperationsDescriptionInclude(self):
		""" Запрос изменения параметра Описание содержит """
		self.SetOperationsDescriptionInclude()

	def on_RequestSetOperationsDescriptionEqual(self):
		""" Запрос изменения параметра Описание идентично """
		self.SetOperationsDescriptionEqual()

	def on_RequestSetOperationsDescriptionReplace(self):
		""" Запрос изменения параметра Замена фрагмента описания """
		self.SetOperationsDescriptionReplace()

	def on_RequestSetOperationsDescriptionSet(self):
		""" Запрос изменения параметра Установка описания """
		self.SetOperationsDescriptionSet()

	def on_RequestSetOperationsColorSet(self):
		""" Запрос изменения параметра Установка цвета """
		self.SetOperationsColorSet()

	def on_RequestProcessingOperations(self):
		""" Запрос обработки операций """
		self.ReadOperationsDescriptionInclude()
		self.ReadOperationsDescriptionReplace()
		self.ReadOperationsDescriptionSet()
		self.ReadOperationsColorSet()

		self.ProcessingOperations()

		self.Application.FormOperations.PartialUpdateData()

	def on_ProcessingOperationsChanged(self):
		""" Параметры обработки операций изменились """
		self.LoadModelDataOperations()

	# Дерево данных Обработка операций
	def on_TreeDataProcessingOperationsDoubleClicked(self):
		""" Двойной клик по дереву данных Обработка операций """
		self.ReadProcessingFieldFromTreeDataOperations()

		self.ControlProcessingField()

	# Меню Обработка операций
	def on_RequestShowMenuOperations(self):
		""" Запрос меню Обработка операций """
		self.ShowMenuOperations()
